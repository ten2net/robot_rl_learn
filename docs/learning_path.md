# 12 个月学习路线总纲

> 主线：**Stable Baselines3 打算法基础 → MotrixLab 建立国产 Sim2Real 能力 →
> ROS2 Jazzy 掌握机器人中间件 → Isaac Lab/OpenUSD 选修前沿**
>
> 节奏假设：每周 6–10 小时，共 48 周；每周 1 个 notebook + 1 组练习。
> 能力对标：机器人 RL/IL 方向**中级工程师**——能独立完成
> 「建模环境 → 训练策略 → Sim2Real 加固 → 接入 ROS2 系统」全流程。

---

## 阶段一（M1–M4）：Stable Baselines3 算法基础

目标：理解 RL 数学框架，熟练使用 SB3 训练/调参/评估，掌握行为克隆与 GAIL，
形成「notebook 实验 + src 复用 + pytest 验证」的工程习惯。

| 周 | 主题 | Notebook | 练习重点 |
|----|------|----------|----------|
| W01 | RL 问题建模：MDP/回报/价值函数 | `01_rl_foundations.ipynb` | 手算 GridWorld 的 Bellman 方程；区分 on/off-policy |
| W02 | Gymnasium API 与自定义环境 | `02_gymnasium_custom_env.ipynb` | 用 `check_env` 验证自写 `DroneHoverEnv`；设计奖励函数 |
| W03 | 表格法：Q-Learning / SARSA | `03_tabular_qlearning.ipynb` | 在 FrozenLake 上对比两种算法；调 ε-greedy 衰减 |
| W04 | DQN 与函数逼近 | `04_dqn.ipynb` | CartPole 上训练 DQN；消融经验回放/目标网络 |
| W05 | PPO：策略梯度与近端优化 | `05_ppo.ipynb` | 读 SB3 的 PPO 超参；调 `n_steps/clip_range/entropy_coef` |
| W06 | 连续控制：SAC 与 TD3 | `06_sac_td3.ipynb` | Pendulum/MountainCarContinuous 对比 SAC vs TD3；画学习曲线 |
| W07 | 训练工程化：向量化环境/回调/日志 | `07_training_engineering.ipynb` | 用 EvalCallback+Checkpoint；TensorBoard 分析失败训练 |
| W08 | 超参调优与 RL Baselines3 Zoo | `08_hparams_zoo.ipynb` | 用 Optuna 调 PPO；复现 Zoo 的官方超参 |
| W09 | 模仿学习 I：行为克隆 BC | `09_behavior_cloning.ipynb` | 从 PPO 专家采数据 → BC；分析协变量偏移 |
| W10 | 模仿学习 II：DAgger 与 GAIL | `10_dagger_gail.ipynb` | DAgger 修 BC 的分布偏移；GAIL vs BC 对比 |
| W11 | 阶段项目：自定义无人机悬停训练 | `11_project_drone_hover.ipynb` | 端到端：环境→训练→评估→消融报告 |
| W12 | 阶段复盘 + 补漏 | （无 notebook） | 整理实验报告；重做错题 |

**核心资源**

- 教材：Sutton & Barto《Reinforcement Learning: An Introduction》(2nd, 2018)，[免费 PDF](http://incompleteideas.net/book/the-book-2nd.html)
- 中文教材：[《动手学强化学习》张伟楠等](https://hrl.boyuai.com/)（配套代码友好）
- 课程：[David Silver UCL RL 课程](https://www.davidstarsilver.uk/teaching/)、[Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course)
- 文档：[Stable Baselines3 文档](https://stable-baselines3.readthedocs.io/)、[Gymnasium 文档](https://gymnasium.farama.org/)、[RL Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo)
- 代码参考：[CleanRL](https://github.com/vwxyzjn/cleanrl)（单文件算法实现，适合精读）
- 论文：DQN ([Mnih 2015](https://arxiv.org/abs/1312.5602))、PPO ([Schulman 2017](https://arxiv.org/abs/1707.06347))、SAC ([Haarnoja 2018](https://arxiv.org/abs/1801.01290))、TD3 ([Fujimoto 2018](https://arxiv.org/abs/1802.09477))、DAgger ([Ross 2011](https://arxiv.org/abs/1011.0686))、GAIL ([Ho & Ermon 2016](https://arxiv.org/abs/1606.03476))

---

## 阶段二（M5–M6）：MotrixLab —— 国产 Sim2Real 能力

目标：理解 GPU 并行仿真与 Sim2Real 的核心技术（域随机化、观测噪声、系统辨识），
在国产 MotrixSim/MotrixLab 框架上复现四足/机械臂 RL 训练流程。

| 周 | 主题 | Notebook | 练习重点 |
|----|------|----------|----------|
| W13 | MotrixSim 物理引擎入门 | `01_motrixsim_intro.ipynb` | 加载机器人模型；理解并行仿真 API |
| W14 | MotrixLab 框架：环境注册与训练 | `02_motrixlab_workflow.ipynb` | 跑通官方示例任务；读懂配置体系 |
| W15 | Sim2Real I：域随机化 | `03_domain_randomization.ipynb` | 给质量/摩擦/推力加随机化；评估鲁棒性 |
| W16 | Sim2Real II：观测噪声与动作延迟 | `04_obs_noise_latency.ipynb` | 注入传感器噪声；对比策略退化曲线 |
| W17 | Sim2Real III：系统辨识与评估方法 | `05_sysid_eval.ipynb` | 设计 Real→Sim 标定实验；写评估协议 |
| W18 | 阶段项目：MotrixLab 上的迁移训练 | `06_project_transfer.ipynb` | 端到端：训练→加固→鲁棒性报告 |
| W19–W20 | 机动周：补阶段一欠账 / 提前学 ROS2 | — | — |

**核心资源**

- 官方：[MotrixLab 文档](https://motrixlab.readthedocs.io/) 与 [GitHub: Motphys/MotrixLab](https://github.com/Motphys/MotrixLab)、[MotrixSim 文档](https://motrixsim.readthedocs.io/zh-cn/latest/)
- 实训：[谋先飞×Xbotics 机器人强化学习与仿真实训营（GitHub）](https://github.com/Xbotics-Embodied-AI-club/Motphys-Xbotics-Robot-Rl-Sim-Training-Camp)
- 论文：Domain Randomization ([Tobin 2017](https://arxiv.org/abs/1703.06907))、Sim-to-Real 综述 ([Zhao 2020](https://arxiv.org/abs/2009.13303))、ETH 四足分钟级训练 ([Rudin 2022](https://arxiv.org/abs/2201.08117))、Walk These Ways ([Margolis 2022](https://arxiv.org/abs/2211.03238))
- 对比阅读：Isaac Gym/Lab 的 leg 任务设计思路（为阶段四铺垫）

---

## 阶段三（M7–M9）：ROS2 Jazzy 机器人中间件

目标：从「算法工程师」补齐「系统工程师」能力：节点通信、TF2 坐标变换、
URDF 建模、ros2_control 控制链、Nav2 导航栈，最终把阶段一/二训出的策略
包成 ROS2 节点在 Gazebo 仿真机器人上跑起来。

| 周 | 主题 | Notebook | 练习重点 |
|----|------|----------|----------|
| W21 | ROS2 核心概念与工具链 | `01_ros2_concepts.ipynb` | 节点/话题/服务/动作动手实验 |
| W22 | Python 节点编程（rclpy） | `02_rclpy_pubsub.ipynb` | 写发布/订阅、参数、Launch 文件 |
| W23 | TF2 坐标变换与机器人描述 | `03_tf2_urdf.ipynb` | 手写 URDF；广播/监听 TF |
| W24 | Gazebo Harmonic 仿真 | `04_gazebo_sim.ipynb` | 在 Gazebo 中加载 URDF；接仿真传感器 |
| W25 | ros2_control 控制框架 | `05_ros2_control.ipynb` | 配置控制器管理器；写自定义控制器 |
| W26 | Nav2 导航栈 | `06_nav2.ipynb` | 配置 AMCL+规划器；调代价地图参数 |
| W27 | RL 策略 × ROS2：策略节点封装 | `07_rl_policy_node.ipynb` | 把 SB3/MotrixLab 策略包成订阅观测/发布动作的节点 |
| W28 | 阶段项目：仿真无人机自主导航 | `08_project_nav.ipynb` | 端到端系统集成 + 演示录屏 |
| W29–W30 | 机动周 | — | — |

**核心资源**

- 官方：[ROS2 Jazzy 文档与教程](https://docs.ros.org/en/jazzy/)、[ros2_control 文档](https://control.ros.org/jazzy/)、[Nav2 文档](https://docs.nav2.org/)、[MoveIt2 教程](https://moveit.picknik.ai/main/index.html)、[Gazebo 文档](https://gazebosim.org/docs/harmonic)
- 中文：[鱼香 ROS《ROS2 机器人开发：从入门到实践》](https://fishros.com/d2lros2/)
- 视频：Articulated Robotics（YouTube，ROS2 + 真实机器人全流程）
- 论文/书：《A Concise Introduction to Robot Programming with ROS2》(F. Martín Rico, 2022)

---

## 阶段四（M10–M12，选修前沿）：Isaac Lab / OpenUSD + Capstone

目标：接触 GPU 大规模并行仿真与 USD 场景描述的前沿栈，
理解「工业级具身智能训练流水线」，并完成毕业项目。

| 周 | 主题 | Notebook | 练习重点 |
|----|------|----------|----------|
| W31 | OpenUSD 基础：场景图与组合 | `01_openusd_intro.ipynb` | 用 pxr API 读写 USD 场景；理解 Layer/Prim |
| W32 | Isaac Sim / Isaac Lab 概览 | `02_isaac_lab_intro.ipynb` | 跑通官方示例环境；理解 Manager-based 设计 |
| W33 | Isaac Lab 自定义 RL 任务 | `03_isaac_custom_task.ipynb` | 移植阶段二的任务到 Isaac Lab |
| W34 | 大规模并行训练与评估 | `04_isaac_massive_parallel.ipynb` | 对比 16 vs 4096 环境的吞吐；rsl_rl 调参 |
| W35–W38 | **Capstone 毕业项目**（三选一） | `05_capstone.ipynb` | 见下 |
| W39–W40 | 项目答辩材料：报告+演示视频 | — | — |

**Capstone 选题（三选一）**

1. **无人机穿越**：Isaac Lab 或 MotrixLab 中训练穿越障碍的四旋翼策略，
   加域随机化，导出 ROS2 策略节点在 Gazebo 中复现。
2. **四足导航**：MotrixLab 训行走策略 + Nav2 规划，打通「导航→运控」分层架构。
3. **抓取模仿学习**：采集遥操作/脚本示教数据，BC/ACT 训练机械臂抓取策略，
   在 Isaac Lab 评估成功率。

**核心资源**

- 官方：[Isaac Lab 文档](https://isaac-sim.github.io/IsaacLab/)、[Isaac Sim 文档](https://docs.isaacsim.omniverse.nvidia.com/)、[OpenUSD 官方](https://openusd.org/)
- 代码：[rsl_rl](https://github.com/leggedrobotics/rsl_rl)、[skrl](https://github.com/Toni-SM/skrl)
- 论文：Isaac Gym ([Makoviychuk 2021](https://arxiv.org/abs/2108.10470))、Diffusion Policy ([Chi 2023](https://arxiv.org/abs/2303.04137))、ACT/Aloha ([Zhao 2023](https://arxiv.org/abs/2304.13705))、RT-2 ([Brohan 2023](https://arxiv.org/abs/2307.15818))

---

## 学习方法约定

1. **输出倒逼输入**：每周末写 200 字小结（学到了什么/卡在哪/下周计划），放在 `journal/`。
2. **练习不跳步**：`✏️ 练习` 必须亲手写代码，参考答案仅用于对答案。
3. **错题本**：把每个阶段的报错与解法记入 `journal/troubleshooting.md`，这是中级工程师最值钱的资产。
4. **读论文节奏**：阶段一每月 1 篇经典算法论文；阶段二起每月 2 篇应用论文，用「问题-方法-实验-局限」四段式做笔记。
