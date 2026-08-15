"""训练曲线绘图辅助：从 SB3 Monitor 日志读取并绘制回报曲线。"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from stable_baselines3.common.monitor import load_results
from stable_baselines3.common.results_plotter import ts2xy


def load_monitor_rewards(log_dir: str | Path) -> tuple[np.ndarray, np.ndarray]:
    """读取 Monitor 日志，返回 (timesteps, episode_rewards)。"""
    df = load_results(str(log_dir))
    return ts2xy(df, "timesteps")


def plot_learning_curve(
    log_dirs: dict[str, str | Path],
    window: int = 20,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """对比多组实验的学习曲线（滑动平均）。

    Parameters
    ----------
    log_dirs : {实验名: Monitor 日志目录}
    window : 滑动平均窗口（episode 数）
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 5))
    for label, log_dir in log_dirs.items():
        x, y = load_monitor_rewards(log_dir)
        if len(y) >= window:
            y_smooth = pd.Series(y).rolling(window, min_periods=1).mean().to_numpy()
        else:
            y_smooth = y
        ax.plot(x, y_smooth, label=label)
    ax.set_xlabel("Timesteps")
    ax.set_ylabel("Episode reward (smoothed)")
    ax.legend()
    ax.grid(alpha=0.3)
    return ax
