"""阶段一公共代码的单元测试。运行: uv run pytest"""

import numpy as np
from stable_baselines3.common.env_checker import check_env

from robot_rl_learn.phase1_sb3.envs import DroneHoverEnv


def test_drone_hover_env_passes_gym_checker():
    """自定义环境必须通过 SB3 官方的规范检查。"""
    env = DroneHoverEnv(seed=42)
    check_env(env, warn=True)


def test_drone_hover_env_step_shapes():
    env = DroneHoverEnv(seed=0)
    obs, _ = env.reset()
    assert obs.shape == (2,)
    obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
    assert obs.shape == (2,)
    assert isinstance(reward, float)
    assert isinstance(terminated, bool) and isinstance(truncated, bool)
    assert isinstance(info, dict)


def test_drone_hover_env_truncates_at_max_steps():
    env = DroneHoverEnv(max_steps=5, seed=0)
    env.reset()
    truncated = False
    for _ in range(5):
        _, _, terminated, truncated, _ = env.step(np.array([0.0], dtype=np.float32))
        if terminated:
            break
    assert truncated or terminated
