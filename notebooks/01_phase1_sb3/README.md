# 阶段一前半（W01–W06）：RL 基础与 SB3 算法入门

本目录收录 12 个月自学工程**阶段一（Stable Baselines3 算法基础）前半段**的 6 个教学 notebook，
与 `docs/learning_path.md` 的 W01–W06 一一对应。所有 notebook 均已用
`jupyter nbconvert --execute` 在项目 `.venv`（CPU）中实际执行过，输出即预期效果。

## 先修要求

- 自动化/控制专业本科数学：线性代数、基础概率（条件期望）、常微分方程直觉；
- 初级 Python：函数、类、numpy 基本操作；PyTorch 在 W04 前自学到会写 `nn.Module` 即可；
- 环境：项目根目录 `uv sync` 后 `uv run jupyter lab` 启动，kernel 选 `.venv` 中的 Python。

## Notebook 索引

| 周 | Notebook | 主题 | 核心实验 |
|----|----------|------|----------|
| W01 | `01_rl_foundations.ipynb` | MDP、回报、Bellman 方程 | 手算+编程求解 4×4 GridWorld（策略评估/价值迭代） |
| W02 | `02_gymnasium_custom_env.ipynb` | Gymnasium API 与自定义环境 | `check_env` 验证 `DroneHoverEnv`，PPO 首训 |
| W03 | `03_tabular_qlearning.ipynb` | 表格法 Q-Learning / SARSA | FrozenLake 上 numpy 从零实现两算法并对比 |
| W04 | `04_dqn.ipynb` | DQN 与函数逼近 | 手写 mini-DQN，经验回放/目标网络 2×2 消融 |
| W05 | `05_ppo.ipynb` | 策略梯度与近端优化 | SB3 PPO 超参解读，`clip_range` 对比实验 |
| W06 | `06_sac_td3.ipynb` | 连续控制 SAC 与 TD3 | Pendulum 对比 SAC/TD3；MountainCarContinuous 稀疏奖励 |

## 学习建议

- 按周次顺序学习；W01 是全阶段的数学地基，不要跳过。
- 每本 notebook 末尾的「✏️ 练习」必须亲手写代码完成（参考答案在折叠块中，做完再点开）。
- 训练产物统一写入 `runs/`（由 `common/paths.py` 管理），已在 `.gitignore` 中。
- 每周结束按学习方法约定在 `journal/` 写 200 字小结。

## 常见问题

- **训练比预期慢**：所有实验都按 CPU 几分钟内设计（1e4–5e4 步）；若明显更慢，检查是否误用了 GPU 版 torch 之外的异常环境。
- **想复现「满分」效果**：正文为控制时间用了较少步数，把 `total_timesteps` 加大 5–10 倍即可获得教科书级曲线。
