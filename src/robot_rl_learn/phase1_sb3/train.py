"""SB3 训练/评估辅助函数。

封装 notebooks 中反复出现的样板代码：向量化环境、评估、检查点回调。
"""

from __future__ import annotations

from pathlib import Path

import gymnasium as gym
from stable_baselines3 import PPO, SAC, TD3
from stable_baselines3.common.base_class import BaseAlgorithm
from stable_baselines3.common.callbacks import CheckpointCallback, EvalCallback
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import VecEnv

ALGO_REGISTRY: dict[str, type[BaseAlgorithm]] = {
    "PPO": PPO,
    "SAC": SAC,
    "TD3": TD3,
}


def make_envs(env_id: str, n_envs: int = 4, seed: int = 0) -> VecEnv:
    """创建带 Monitor 的向量化训练环境。"""
    return make_vec_env(env_id, n_envs=n_envs, seed=seed, wrapper_class=Monitor)


def train(
    algo: str,
    env_id: str,
    total_timesteps: int = 100_000,
    n_envs: int = 4,
    seed: int = 0,
    log_dir: str | Path = "runs",
    eval_freq: int = 10_000,
    **algo_kwargs,
) -> BaseAlgorithm:
    """训练一个 SB3 算法，带评估回调与检查点保存。

    Parameters
    ----------
    algo : {"PPO", "SAC", "TD3"}
    env_id : Gymnasium 环境 id（含通过 register() 注册的自定义环境）
    algo_kwargs : 透传给算法构造函数的额外超参数
    """
    algo_cls = ALGO_REGISTRY[algo.upper()]
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    train_env = make_envs(env_id, n_envs=n_envs, seed=seed)
    eval_env = Monitor(gym.make(env_id))

    callbacks = [
        EvalCallback(
            eval_env,
            best_model_save_path=str(log_dir / "best"),
            log_path=str(log_dir / "eval"),
            eval_freq=max(eval_freq // n_envs, 1),
            deterministic=True,
        ),
        CheckpointCallback(
            save_freq=max(eval_freq // n_envs, 1),
            save_path=str(log_dir / "checkpoints"),
        ),
    ]

    model = algo_cls(
        "MlpPolicy",
        train_env,
        seed=seed,
        tensorboard_log=str(log_dir / "tensorboard"),
        **algo_kwargs,
    )
    model.learn(total_timesteps=total_timesteps, callback=callbacks)
    model.save(log_dir / "final_model")
    return model


def evaluate(model: BaseAlgorithm, env_id: str, n_episodes: int = 10) -> tuple[float, float]:
    """确定性评估，返回 (平均回报, 标准差)。"""
    env = make_vec_env(env_id, n_envs=1)
    mean, std = evaluate_policy(model, env, n_eval_episodes=n_episodes, deterministic=True)
    return float(mean), float(std)
