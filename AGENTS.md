# AGENTS.md — 项目约定

## 项目定位

12 个月机器人 RL/IL 自学工程。主线见 `docs/learning_path.md`：
SB3（M1–M4）→ MotrixLab（M5–M6）→ ROS2 Jazzy（M7–M9）→ Isaac Lab/OpenUSD（M10–M12）。

## 工程规范

- 依赖管理只用 **uv**：改依赖编辑 `pyproject.toml` 后 `uv sync`；不要手动 pip install 到 .venv。
- Python 版本：`>=3.10,<3.13`。
- 可复用代码放 `src/robot_rl_learn/`，notebook 里只做实验与教学讲解；
  src 中的公共代码必须有 `tests/` 里的单元测试。
- 训练产物一律写入 `runs/`、`logs/`、`checkpoints/`（见 `common/paths.py`），已 gitignore。
- 提交前运行：`uv run pytest`、`uv run ruff check .`。

## Notebook 编写约定

- 目录：`notebooks/0X_<phase>/NN_<topic>.ipynb`，编号与 `docs/learning_path.md` 的周次表对应。
- 每个 notebook 结构：**学习目标 → 讲解+可运行示例 → ✏️ 练习（带分值/难度）→
  折叠的参考答案 → 延伸阅读**。
- 练习题的参考答案放在 `<details>` HTML 折叠块中，避免学习者直接看到。
- 默认 kernel 是项目的 `.venv`（`uv run jupyter lab` 启动即选中）。
- 本机有 GPU 且多任务并行：阶段一可执行 notebook 的首个 code cell 统一加
  `CUDA_VISIBLE_DEVICES=""`（在 import torch 之前）与 `OMP_NUM_THREADS=4` /
  `torch.set_num_threads(4)`，避免 CUDA 设备混用与 OMP 线程争抢。
- 运行 pytest 时使用 `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run pytest`
  （系统里 /opt/ros 的 pytest 插件会干扰）。
- 阶段二/三/四的 notebook 若依赖本机没有的框架（MotrixLab/ROS2/Isaac），
  代码 cell 需注明运行前提，不能在本机执行的 cell 保持未执行状态并提供预期输出截图描述。

## 文档约定

- 各阶段环境安装指南：`docs/phaseN_*.md`；修改依赖或安装方式后同步更新。
- 学习路线周次表在 `docs/learning_path.md`，新增/调整 notebook 时必须同步更新该表。
