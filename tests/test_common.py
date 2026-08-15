"""公共工具测试。"""

from robot_rl_learn.common.paths import CHECKPOINTS_DIR, LOGS_DIR, RUNS_DIR, make_run_dir


def test_artifact_dirs_exist():
    for d in (LOGS_DIR, RUNS_DIR, CHECKPOINTS_DIR):
        assert d.is_dir()


def test_make_run_dir(tmp_path):
    d = make_run_dir("pytest_smoke")
    assert d.is_dir()
    assert d == RUNS_DIR / "pytest_smoke"
    d.rmdir()  # 清理
