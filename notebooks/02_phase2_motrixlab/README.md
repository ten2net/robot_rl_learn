# 阶段二（W13–W18）：MotrixLab —— 国产 Sim2Real 能力

> 阶段目标：理解 GPU/CPU 并行仿真与 Sim2Real 核心技术（域随机化、观测噪声、系统辨识），
> 在国产 MotrixSim/MotrixLab 框架上复现四足/机械臂 RL 训练流程。
> 周次与编号对应 `docs/learning_path.md`；安装方法见 `docs/phase2_motrixlab.md`。

## Notebook 索引

| 周 | Notebook | 主题 | 本机可执行性 |
|----|----------|------|--------------|
| W13 | [01_motrixsim_intro.ipynb](01_motrixsim_intro.ipynb) | MotrixSim 物理引擎入门：SceneModel/SceneData、数值积分稳定性、并行仿真为什么快 | 概念演示（numpy）可执行；MotrixSim 示例 cell 未执行（附预期输出） |
| W14 | [02_motrixlab_workflow.ipynb](02_motrixlab_workflow.ipynb) | MotrixLab 框架：motrix_envs/motrix_rl 分层、view/train/play 三件套、读懂四足任务设计 | SB3 同构流程可执行；MotrixLab 命令 cell 未执行 |
| W15 | [03_domain_randomization.ipynb](03_domain_randomization.ipynb) | Sim2Real I：域随机化原理、CartPole 鲁棒性热力图实验、MotrixSim override API | 全部实验可执行；override API cell 未执行 |
| W16 | [04_obs_noise_latency.ipynb](04_obs_noise_latency.ipynb) | Sim2Real II：观测噪声（白噪声/偏置/量化）与动作延迟的注入、退化曲线与加固训练 | 全部可执行 |
| W17 | [05_sysid_eval.ipynb](05_sysid_eval.ipynb) | Sim2Real III：系统辨识（网格搜索+残差诊断）与分层评估协议设计 | 全部可执行 |
| W18 | [06_project_transfer.ipynb](06_project_transfer.ipynb) | 阶段项目：训练→加固→分层评估→报告的端到端流水线（含评分 rubric） | 路径 B（SB3）可执行；路径 A（MotrixLab）cell 未执行 |

## 使用说明

- 所有 notebook 默认 kernel 为本项目 `.venv`（`uv run jupyter lab` 启动）。
- 标注「⚠️ 运行前提」的 code cell 依赖 MotrixSim/MotrixLab，在本机**保持未执行状态**，
  每个此类 cell 前的 markdown 均给出了预期输出描述；完成 `docs/phase2_motrixlab.md`
  的安装后可手动执行。
- 训练产物（策略权重、报告图）写入项目根目录 `runs/`（已由 `common/paths.py` 管理并 gitignore）。
- 建议顺序完成；W15–W17 的实验代码在 W18 项目中被原样复用。

## 核心资源

- [MotrixLab GitHub](https://github.com/Motphys/MotrixLab) 与 [MotrixLab 文档](https://motrixlab.readthedocs.io/)
- [MotrixSim 文档](https://motrixsim.readthedocs.io/zh-cn/latest/)
- [谋先飞 × Xbotics 机器人强化学习与仿真实训营](https://github.com/Xbotics-Embodied-AI-club/Motphys-Xbotics-Robot-Rl-Sim-Training-Camp)
