# 阶段三（W21–W28）：ROS2 Jazzy 机器人中间件

> 主线：从「算法工程师」补齐「系统工程师」能力——节点通信、TF2、URDF、
> Gazebo 仿真、ros2_control、Nav2，最终把阶段一/二训出的策略包成 ROS2 节点跑起来。
> 周次与练习对应关系见 `docs/learning_path.md`；环境安装见 `docs/phase3_ros2.md`。

## ⚠️ 运行前提

ROS2 Jazzy 只支持 **Ubuntu 24.04 + apt 安装**（不能 pip），本目录的
`ros2`/`rclpy`/`gz` 相关内容以「讲解 + 命令块 + 代码模板 + 预期输出」呈现，
**需复制到有 ROS2 的机器上执行**；每个 notebook 中的纯 Python 概念演示
（transforms3d、XML 解析、numpy 模拟）已在本项目环境中真实执行。
依赖：`uv sync --extra ros`（仅 transforms3d）。

## Notebook 索引

| 周 | Notebook | 内容 | 练习重点 |
|----|----------|------|----------|
| W21 | `01_ros2_concepts.ipynb` | DDS 与 QoS 直觉；节点/话题/服务/动作/参数/Launch 五大机制；turtlesim CLI 实验 | 接口普查；场景选型决策表；QoS 模拟器扩展 |
| W22 | `02_rclpy_pubsub.ipynb` | rclpy 节点骨架、回调驱动模型、参数、Launch、Executor 调度 | 温度监控对；可调速 talker；三节点 launch；异步服务客户端 |
| W23 | `03_tf2_urdf.ipynb` | 旋转表示与四元数（transforms3d 实算）；齐次变换链；TF2 树；URDF/Xacro 手写 | 四元数体检；手算 vs 矩阵；2R 机械臂 URDF；TF 广播+监听节点 |
| W24 | `04_gazebo_sim.ipynb` | Gazebo Harmonic 架构与 Jazzy 配对；SDF vs URDF；ros_gz 桥接；传感器插件；仿真时钟 | 物理步长对齐检查；小车+lidar 进 Gazebo；QoS 故障排查报告 |
| W25 | `05_ros2_control.ipynb` | ControllerManager 架构；`<ros2_control>` 标签；控制器链与 spawner；差速运动学（实算） | mock 硬件全流程；打滑下里程计漂移蒙特卡洛；Gazebo 完整控制链 |
| W26 | `06_nav2.ipynb` | Nav2 架构；代价地图膨胀层（实算+可视化）；AMCL vs SLAM；关键参数解剖 | 手写距离变换；膨胀参数实验；SLAM 建图交付；调参实验报告 |
| W27 | `07_rl_policy_node.ipynb` | 训练→部署契约；PolicyCore 分层设计（实算闭环）；完整 rclpy 策略节点模板；watchdog 安全机制 | 契约测试；契约漂移对照实验；部署 DroneHoverEnv PPO 策略；watchdog 分级 |
| W28 | `08_project_nav.ipynb` | 阶段综合项目：系统集成架构、一键 launch、SPL 评估协议（实算）、故障排查清单 | 项目计划书；M0–M2 控制链；M3 导航基线；M4–M5 RL 增强对比评估 |

## 学习建议

1. **先概念后环境**：W21–W23 的纯 Python 部分在本机即可完成；
   没有 Ubuntu 24.04 机器时，用 Docker（`osrf/ros:jazzy-desktop`）集中完成
   标注「需要 ROS2 环境」的练习（见 `docs/phase3_ros2.md` 方案 B）。
2. **沿数据流排错**：阶段三的核心技能不是写代码，而是
   `ros2 topic/node/tf2_echo` 沿数据流逐段验证——每个 notebook 都给了排查口诀。
3. **错题本**：把 QoS 不匹配、`use_sim_time` 漏设、TF 断树等坑记入
   `journal/troubleshooting.md`。
