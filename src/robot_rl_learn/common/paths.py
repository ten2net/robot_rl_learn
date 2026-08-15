"""项目路径管理：统一存放训练产物，保持仓库整洁。"""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

LOGS_DIR = PROJECT_ROOT / "logs"
RUNS_DIR = PROJECT_ROOT / "runs"
CHECKPOINTS_DIR = PROJECT_ROOT / "checkpoints"

for _d in (LOGS_DIR, RUNS_DIR, CHECKPOINTS_DIR):
    _d.mkdir(parents=True, exist_ok=True)


def make_run_dir(name: str) -> Path:
    """创建一次实验的运行目录（runs/<name>/），已存在则直接返回。"""
    run_dir = RUNS_DIR / name
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir
