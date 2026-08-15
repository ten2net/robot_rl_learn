"""自定义 Gymnasium 环境示例。

`DroneHoverEnv` 是一个简化的一维无人机定高环境：
状态 = [高度误差, 垂直速度]，动作 = 归一化推力。
它在 M1-M2 的 notebook 中用于练习「如何写一个规范的自定义环境」。
"""

from __future__ import annotations

import gymnasium as gym
import numpy as np
from gymnasium import spaces


class DroneHoverEnv(gym.Env):
    """一维无人机定高悬停环境（教学简化版）。

    - 观测: [高度误差 (m), 垂直速度 (m/s)]
    - 动作: 推力归一化到 [-1, 1]，映射到 [0, 2g] 的加速度
    - 奖励: 高度误差与速度惩罚，悬停在目标高度奖励最大
    - 终止: 高度超出安全范围
    """

    metadata = {"render_modes": []}

    def __init__(
        self,
        target_height: float = 1.0,
        max_steps: int = 500,
        dt: float = 0.02,
        seed: int | None = None,
    ) -> None:
        super().__init__()
        self.target_height = target_height
        self.max_steps = max_steps
        self.dt = dt
        self.gravity = 9.81

        high = np.array([5.0, 10.0], dtype=np.float32)
        self.observation_space = spaces.Box(-high, high, dtype=np.float32)
        self.action_space = spaces.Box(-1.0, 1.0, shape=(1,), dtype=np.float32)

        self._rng = np.random.default_rng(seed)
        self._height = 0.0
        self._velocity = 0.0
        self._steps = 0

    def reset(
        self, *, seed: int | None = None, options: dict | None = None
    ) -> tuple[np.ndarray, dict]:
        super().reset(seed=seed)
        if seed is not None:
            self._rng = np.random.default_rng(seed)
        self._height = float(self._rng.uniform(0.0, 2.0))
        self._velocity = float(self._rng.uniform(-0.5, 0.5))
        self._steps = 0
        return self._get_obs(), {}

    def step(self, action: np.ndarray) -> tuple[np.ndarray, float, bool, bool, dict]:
        thrust = float(np.clip(action[0], -1.0, 1.0))
        accel = (thrust + 1.0) * self.gravity - self.gravity  # [-g, g] 映射
        self._velocity += accel * self.dt
        self._height += self._velocity * self.dt
        self._steps += 1

        height_err = self._height - self.target_height
        reward = -(
            height_err**2 + 0.1 * self._velocity**2 + 0.01 * thrust**2
        )

        terminated = abs(height_err) > 3.0
        truncated = self._steps >= self.max_steps
        return self._get_obs(), float(reward), terminated, truncated, {}

    def _get_obs(self) -> np.ndarray:
        return np.array(
            [self._height - self.target_height, self._velocity], dtype=np.float32
        )
