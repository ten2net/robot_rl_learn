# 阶段三环境安装指南：ROS2 Jazzy + Gazebo Harmonic

> 适用周次：W21–W28（`notebooks/03_phase3_ros2/`）。
> 关键事实：**ROS2 Jazzy 官方支持平台是 Ubuntu 24.04 LTS，通过 apt 安装，
> 不能 pip 安装到项目 .venv**。项目 `pyproject.toml` 的 `ros` extra 只含
> `transforms3d`（供纯 Python 演示用），与 ROS2 本体无关。

## 一、先决定你的方案

| 方案 | 适用 | 说明 |
|------|------|------|
| **A. Ubuntu 24.04 原生安装** | 有 Ubuntu 24.04 机器/双系统 | 最佳体验，推荐 |
| **B. Docker 镜像** | 其它 Linux/macOS/Windows(WSL2) | `osrf/ros:jazzy-desktop`，GUI 需额外配置 X11 |
| **C. 仅本机学习** | 暂时没有可用环境 | 完成各 notebook 的纯 Python 部分 + 读模板，ROS 实操留到机动周 |

本机（开发机）没有 ROS2 环境属预期情况——notebook 中的 `ros2`/`gz` 命令
都写成可复制的命令块并附预期输出，不会在本机执行。

## 二、方案 A：Ubuntu 24.04 安装 ROS2 Jazzy

以下命令与 [官方安装文档](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)
一致（安装方式：ros-apt-source）。

```bash
# 1) 系统 locale（必须是 UTF-8）
sudo apt update && sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# 2) 启用 universe 仓库
sudo apt install -y software-properties-common
sudo add-apt-repository universe

# 3) 添加 ROS2 apt 源（ros-apt-source 方式，自动管理密钥）
sudo apt install -y curl
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-$VERSION_CODENAME})_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb

# 4) 安装 ROS2 Jazzy 桌面版（含 RViz、rqt、demo 包）与开发工具
sudo apt update
sudo apt install -y ros-jazzy-desktop ros-dev-tools

# 5) 每个新终端都要 source（建议写入 ~/.bashrc）
source /opt/ros/jazzy/setup.bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc

# 6) 验证
ros2 run demo_nodes_py talker        # 另开终端 ros2 run demo_nodes_py listener
```

## 三、阶段三课程包清单（按周安装）

```bash
# W21 概念与 CLI
sudo apt install -y ros-jazzy-turtlesim ros-jazzy-rqt-graph

# W23 TF2 / URDF / Xacro
sudo apt install -y ros-jazzy-tf2-tools ros-jazzy-robot-state-publisher \
  ros-jazzy-joint-state-publisher-gui ros-jazzy-xacro liburdfdom-tools

# W24 Gazebo Harmonic 集成（Jazzy 官方配对 Harmonic，一条命令自动带齐）
sudo apt install -y ros-jazzy-ros-gz

# W25 ros2_control
sudo apt install -y ros-jazzy-ros2-control ros-jazzy-ros2-controllers \
  ros-jazzy-gz-ros2-control

# W26 Nav2 + SLAM
sudo apt install -y ros-jazzy-navigation2 ros-jazzy-nav2-bringup \
  ros-jazzy-slam-toolbox ros-jazzy-turtlebot3-gazebo
```

## 四、方案 B：Docker（无 Ubuntu 24.04 时）

```bash
# 需已安装 Docker；镜像约 2.5 GB
docker pull osrf/ros:jazzy-desktop

# 无 GUI 的基础用法（CLI 实验足够）
docker run -it --rm --net=host osrf/ros:jazzy-desktop
# 容器内：ros2 run demo_nodes_py talker

# GUI（Linux 主机，X11 转发 RViz/Gazebo）
xhost +local:docker
docker run -it --rm --net=host -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix osrf/ros:jazzy-desktop
```

Gazebo Harmonic 不在 `osrf/ros:jazzy-desktop` 基础镜像里，容器内需
`apt update && apt install -y ros-jazzy-ros-gz`（同方案 A 第三节）。

## 五、本机纯 Python 部分

notebook 中的 transforms3d / XML / numpy 演示只依赖项目环境：

```bash
uv sync --extra ros        # 追加 transforms3d 到 .venv
```

> ⚠️ 已知问题：当前 `pyproject.toml` 的依赖解析存在冲突
>（`imitation>=1.0` 要求 `gymnasium<1.0`，而项目要求 `gymnasium>=1.0`），
> `uv sync` 可能失败。这是项目级待修复项；临时方案可用
> `uv run --no-project --with transforms3d --with numpy -- python ...`
> 单独运行演示代码，不影响 ROS2 环境本身。

## 六、验证清单

在 ROS2 机器上依次执行，全部通过即环境就绪：

```bash
ros2 --version                                   # 打印 jazzy
ros2 run turtlesim turtlesim_node                # W21
ros2 run tf2_ros tf2_echo a b                    # W23（报 LookupException 属正常，说明工具可用）
gz sim --version                                 # W24：gz-sim 8.x（Harmonic）
ros2 pkg list | grep -E "ros_gz|ros2_control|nav2_bringup"   # W24-W26
```

## 参考链接（已核实）

- [ROS2 Jazzy 官方安装文档](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)
- [ROS2 Jazzy 文档主页](https://docs.ros.org/en/jazzy/)
- [Gazebo ↔ ROS 版本配对（Jazzy=Harmonic）](https://gazebosim.org/docs/harmonic/ros_installation)
- [ros2_control 文档（Jazzy）](https://control.ros.org/jazzy/index.html)
- [Nav2 Getting Started](https://docs.nav2.org/getting_started/index.html)
