# 阶段〇（学前基础）：Python 工程与科学计算

> 对应 `docs/learning_path.md` 的「阶段〇（学前 4 周）」表格（B00–B08）。
> 用自动化专业熟悉的例子（信号、电路、弹簧、单摆、PID、阶跃响应）学习 Python 科学生态，
> 为后续 SB3 → MotrixLab → ROS2 → Isaac 主线扫清语言与工具障碍。

## 先修要求

- **零基础可学**：会打开终端、会基本打字即可；
- 数学上默认学过微积分与线性代数（自动化本科二年级水平），能看懂 $\dot{y}=f(t,y)$ 这种记号；
- 环境：项目根目录已 `uv sync`；启动 notebook 用 `uv run jupyter lab`（kernel 自动选中 `.venv`）。

## Notebook 索引与每周建议

建议节奏：每周 2 个 notebook，每个 2–4 小时（含练习），共 4 周。
**练习先独立做、再点开折叠的参考答案**；交付前用「Restart Kernel and Run All Cells」从头跑通。

| 周 | Notebook | 主题 | 你将做出什么 |
|----|----------|------|-------------|
| B00 | `00_shell_commands.ipynb` | 命令行速成（Windows CMD / Linux bash 对照） | 终端认路、文件操作、查日志、跑脚本、环境变量与代理、进程管理 |
| B01 | `01_python_basics.ipynb` | uv/Jupyter 环境、变量/类型/控制流/函数、列表切片 | 手写欧拉法仿真一阶环节并测调节时间 |
| B02 | `02_data_structures.ipynb` | list/tuple/dict/set、推导式、文件读写、异常、模块化 | 仿真结果存 CSV、参数存 JSON、自写 `.py` 模块 |
| B03 | `03_numpy.ipynb` | ndarray、广播、向量化实测、统计与线代、随机种子 | timeit 实测向量化加速；`eigvals` 判稳定性 |
| B04 | `04_pandas_matplotlib.ipynb` | DataFrame 分析流水线、规范出图 | 温度传感器数据分析 + 报告级双子图（存 PNG） |
| B05 | `05_scipy_simulation.ipynb` | **重点课**：solve_ivp 求 ODE、插值、拟合 | 一阶环节/RLC/弹簧阻尼/单摆仿真；curve_fit 辨识参数 |
| B06 | `06_plotly.ipynb` | 交互折线/子图/3D 曲面/动画滑块、HTML 导出 | 根轨迹风格极点图、正弦相位动画 |
| B07 | `07_streamlit.ipynb` | Streamlit 心智模型、widget、session_state | 生成 PID 调参面板 app.py + headless 冒烟测试 |
| B08 | `08_project_control_sim.ipynb` | 综合项目：控制系统仿真工作台 | P/PI/PID 对比 + 指标表 + 报告图 + 部署指引 + 自评量表 |

## 与后续阶段的衔接

- **B01–B02（语法与文件）** → 阶段一 W07 训练工程化：读 SB3 的超参 dict、管理日志与检查点；
- **B03（NumPy 向量化/随机种子）** → 阶段一所有算法课：批量采样、可复现对比实验；
  阶段二/四 GPU 并行仿真的「批量环境」思想同源；
- **B04（pandas/matplotlib 流水线）** → 每次训练后的学习曲线分析与实验报告出图；
- **B05（solve_ivp 数值模拟）** → 理解物理仿真器在做什么（Isaac/MuJoCo 之前的关键一课）；
  W02 自定义 Gymnasium 环境的动力学积分就是同一套写法；
- **B06–B07（plotly/streamlit）** → 给训练/仿真结果做交互式调参面板与演示页面；
- **B08（端到端小项目）** → 直接预演主线「建模 → 实验 → 指标 → 报告 → 部署」的完整工作流。

## 产物说明

notebook 运行产物（CSV/PNG/HTML/app.py/临时模块）统一写入 `runs/00_basic/`（已 gitignore），
删除后重跑 notebook 即可重新生成。
