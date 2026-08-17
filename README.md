# robot_rl_learn — 机器人强化学习/模仿学习 12 个月自学工程

面向自动化控制专业本科生的工程化自学项目：以 Jupyter 课程为主线，
按照 **由浅入深、由软到硬、由仿真到系统** 的路径，用 12 个月把能力训练到
「机器人 RL/IL 方向中级工程师」水平。

## 学习路线

| 阶段 | 月份 | 主题 | 目标 |
|------|------|------|------|
| 〇（学前） | 4 周 | **Python 工程与科学计算基础** | 补齐语言/NumPy/SciPy/Plotly/Streamlit 功底 |
| 一 | M1–M4 | **Stable Baselines3 算法基础** | 吃透 RL 数学基础与主流算法，能独立实现/调参/评估 |
| 二 | M5–M6 | **MotrixLab 国产 Sim2Real** | 在国产仿真器上做域随机化与 Sim2Real 迁移训练 |
| 三 | M7–M9 | **ROS2 Jazzy 机器人中间件** | 掌握节点/话题/TF2/ros2_control/Nav2，打通仿真到系统 |
| 四 | M10–M12 | **Isaac Lab / OpenUSD（选修前沿）+ 毕业项目** | 接触 GPU 并行仿真前沿，完成一个端到端 Capstone |

详细周计划见 [`docs/learning_path.md`](docs/learning_path.md)；
各阶段环境安装见 `docs/phase*_*.md`。

## 快速开始

```bash
# 1. 安装 uv（如未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 安装依赖（uv 自动创建 .venv 并锁定版本）
uv sync

# 3. 启动 JupyterLab；Python 基础较弱请从 notebooks/00_basic/ 开始，
#    否则直接从 notebooks/01_phase1_sb3/ 开始
uv run jupyter lab

# 4. 运行测试 / 代码检查
uv run pytest
uv run ruff check .
```

> 阶段三（ROS2 Jazzy）需要 Ubuntu 24.04 + apt 安装 ROS2，无法 pip 安装；
> 阶段四（Isaac Lab）需要 NVIDIA GPU。详见对应阶段文档。

## 项目结构

```
robot_rl_learn/
├── pyproject.toml          # uv 工程定义（依赖/分组/工具配置）
├── src/robot_rl_learn/     # 可复用公共代码（notebook 中 import 使用）
│   ├── common/             # 路径管理等跨阶段工具
│   └── phase1_sb3/         # 阶段一：自定义环境、训练/评估/绘图辅助
├── notebooks/              # 课程主体，按阶段分目录
│   ├── 00_basic/           # 学前：Python 工程与科学计算基础（B01-B08）
│   ├── 01_phase1_sb3/      # M1-M4：RL 基础 + SB3 + 模仿学习
│   ├── 02_phase2_motrixlab/# M5-M6：MotrixSim/MotrixLab + Sim2Real
│   ├── 03_phase3_ros2/     # M7-M9：ROS2 Jazzy
│   └── 04_phase4_isaac/    # M10-M12：Isaac Lab/OpenUSD + Capstone
├── docs/                   # 学习路线、各阶段安装指南、资源清单
├── tests/                  # src/ 的单元测试（uv run pytest）
├── runs/  logs/  checkpoints/   # 训练产物（已 gitignore）
└── AGENTS.md               # 给 AI 助手/协作者的项目约定
```

## 使用建议

- **每周 1 个 notebook**：每个 notebook 约 1–3 小时，含「讲解 → 示例 → 练习题 → 参考答案」。
- **练习先行**：先自己做练习（`### ✏️ 练习` 标记），再点开折叠的参考答案对比。
- **代码进 src**：当 notebook 里的代码第二次被复用时，把它移入 `src/` 并写测试——这是工程化习惯的训练。
- **记录实验**：所有训练产物自动落在 `runs/`，用 TensorBoard 对比（`uv run tensorboard --logdir runs`）。

## 环境要求

| 阶段 | 硬件 | 系统 |
|------|------|------|
| M1–M4 | CPU 即可，有 GPU 更快 | Linux / macOS / WSL2 |
| M5–M6 | 建议 NVIDIA GPU | Linux（Windows 见 MotrixSim 文档） |
| M7–M9 | CPU 即可 | **Ubuntu 24.04**（ROS2 Jazzy 官方支持） |
| M10–M12 | **NVIDIA GPU（≥8GB 显存，RTX 系列）** | Ubuntu 22.04/24.04 |
