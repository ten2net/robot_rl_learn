# 阶段四（W31–W35+）：Isaac Lab / OpenUSD 选修前沿 + Capstone

> 前置阅读：`docs/learning_path.md` 阶段四表格；环境安装见 `docs/phase4_isaac.md`。
> 本阶段除特别标注外，代码 cell 均需要 **NVIDIA GPU + Isaac Sim/Isaac Lab**，
> 在无 GPU 的机器上保持未执行（每个 cell 已注明运行前提与预期输出）。

| # | Notebook | 周次 | 主题 | 本地可运行？ |
|---|----------|------|------|--------------|
| 01 | `01_openusd_intro.ipynb` | W31 | OpenUSD 基础：Stage/Layer/Prim/Attribute、USDA 文本格式、组合机制（Sublayers/References/Variants/Inherits） | 部分（USDA 文本 cell 可跑；pxr cell 需 `uv pip install usd-core`） |
| 02 | `02_isaac_lab_intro.ipynb` | W32 | Isaac Sim / Isaac Lab 概览：架构、GPU 加速原理、Manager-based vs Direct、官方示例 | 否（全部需 GPU） |
| 03 | `03_isaac_custom_task.ipynb` | W33 | Isaac Lab 自定义 RL 任务：Manager-based CartPole 改造 + Direct 四旋翼悬停骨架 | 否（模板代码，落地到有 GPU 的 Isaac Lab 环境运行） |
| 04 | `04_isaac_massive_parallel.ipynb` | W34 | 大规模并行训练：Amdahl 定律、吞吐对比实验、rsl_rl PPO 超参、评估与导出 | 部分（Amdahl/吞吐示意图 cell 可跑，需项目环境 matplotlib） |
| 05 | `05_capstone.ipynb` | W35–W38 | Capstone 毕业项目指南：三选题（无人机穿越/四足导航/抓取 IL）的里程碑、指标、验收标准与报告模板 | 部分（Wilson 置信区间 cell 可跑，纯标准库） |

## 学习顺序与建议

1. 先读 `docs/phase4_isaac.md` 完成（或规划）环境安装——没有 GPU 也可以学，
   W31 的 USD 部分和 W34/W35 的可执行 cell 都不依赖 GPU；
2. W31→W34 每周一个 notebook，练习参考答案在折叠块中，先自己做再对答案；
3. W35 之前确定 Capstone 选题并写 `journal/capstone_plan.md`（见 `05_capstone.ipynb` 练习 1）；
4. 每周小结与排错日志记入 `journal/`（见 `docs/learning_path.md` 学习方法约定）。
