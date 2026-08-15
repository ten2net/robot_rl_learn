# 阶段四环境安装指南：Isaac Sim / Isaac Lab / OpenUSD

> 适用范围：W31–W38（`notebooks/04_phase4_isaac/`）。
> 官方来源（命令以官方文档为准，本文是带注释的摘录与排错补充）：
> [Isaac Lab pip 安装文档](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html)、
> [Isaac Sim 文档](https://docs.isaacsim.omniverse.nvidia.com/)、[OpenUSD](https://openusd.org/)。

## 0. 硬件与系统要求

| 项 | 要求 |
|----|------|
| GPU | NVIDIA RTX 系列（建议 8 GB 显存以上；4096 环境并行建议 16 GB+） |
| 驱动 | 最新 NVIDIA 驱动（支持 CUDA 12.x），`nvidia-smi` 能正常输出 |
| 系统 | Ubuntu 22.04 / 24.04（或 Windows 11）；**GLIBC ≥ 2.35**（`ldd --version` 检查） |
| 磁盘 | 至少 30–50 GB 空闲（Isaac Sim pip 包 + 扩展缓存 + 资产） |
| Python | Isaac Sim 5.x → **3.11**；Isaac Sim 4.x → 3.10（版本不匹配会直接报错） |

> ⚠️ **不要装进本项目的 `.venv`**：本项目 Python 版本范围（>=3.10,<3.13）与 Isaac Sim 5.x
> 锁定的 3.11 并不总是匹配，且 isaacsim 依赖庞大。按官方建议建**独立环境**。
> 本项目 `.venv` 只用于 notebook 讲解与纯 Python 部分（W31 的 USDA 文本、W34/W35 的可执行 cell）。

## 1. 安装 usd-core（W31，纯 CPU，可选但推荐）

OpenUSD 的 Python API（`pxr` 模块）以纯 wheel 分发，不需要 GPU：

```bash
# 装进项目 .venv（notebook 的 kernel 环境）
uv pip install usd-core

# 验证
uv run python -c "from pxr import Usd; print('pxr OK')"
```

装好后 `01_openusd_intro.ipynb` 中带「needs-pxr」标注的 cell 即可运行。

## 2. 安装 Isaac Sim（W32 起，需 GPU）

以下步骤在**有 NVIDIA GPU 的机器**上执行。官方同时支持 conda / venv / uv，这里用 uv：

```bash
# ① 建独立环境（Python 3.11；--seed 顺带装 pip，Isaac Lab 安装需要）
uv venv --python 3.11 --seed env_isaaclab
source env_isaaclab/bin/activate

# ② 升级 pip
pip install --upgrade pip

# ③ 安装 Isaac Sim（约数 GB，耐心；注意 --extra-index-url 指向 NVIDIA 源）
pip install "isaacsim[all,extscache]==5.1.0" --extra-index-url https://pypi.nvidia.com

# ④ 安装与 Isaac Sim 5.x 匹配的 CUDA 版 PyTorch（Linux/Windows x86_64）
pip install -U torch==2.7.0 torchvision==0.22.0 --index-url https://download.pytorch.org/whl/cu128
```

> 若使用 uv 建的环境，后续命令里把 `pip` 换成 `uv pip` 亦可。

### 验证 Isaac Sim

```bash
isaacsim            # 启动仿真器主程序
```

- **首次运行**：会从 registry 拉取扩展缓存，**可长达 10 分钟**，属正常现象；
- 首次运行会提示接受 NVIDIA Omniverse EULA，输入 `Yes`；
- 无显示器的服务器上验证可改用后续 Isaac Lab 的 `--headless` 脚本。

## 3. 安装 Isaac Lab

```bash
# ① 克隆源码（建议放在 Isaac 专用工作区，不必放进本仓库）
git clone https://github.com/isaac-sim/IsaacLab.git --branch main
cd IsaacLab

# ② Linux 依赖（robomimic 需要）
sudo apt install cmake build-essential

# ③ 安装全部扩展 + RL 框架（rl_games / rsl_rl / sb3 / skrl / robomimic）
./isaaclab.sh --install          # 或只装 rsl_rl：./isaaclab.sh --install rsl_rl
```

### 验证 Isaac Lab

```bash
# 启动空场景（有显示器会弹出黑色视口；Ctrl+C 退出）
./isaaclab.sh -p scripts/tutorials/00_sim/create_empty.py

# 列出全部内置任务
./isaaclab.sh -p scripts/environments/list_envs.py

# 跑一个真正的训练：Ant，4096 环境，无渲染
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Ant-v0 --num_envs=4096 --headless
```

`list_envs.py` 打出任务表、`train.py` 开始滚动打印 iteration/fps，即安装成功。

## 4. 与本项目的配合方式

- Jupyter：项目 notebook 的默认 kernel 是 `.venv`（`uv run jupyter lab`）。
  **Isaac cell 不在本机执行**（notebook 中已标注）；在有 GPU 的机器上，可用
  `env_isaaclab` 注册独立 kernel：
  `python -m ipykernel install --user --name env_isaaclab --display-name "Isaac Lab (3.11)"`
  （需先在 `env_isaaclab` 中 `pip install ipykernel`）。
- 资产/训练产物：Isaac Lab 的日志写在其仓库 `logs/` 下；本项目的 `runs/`、
  `checkpoints/` 仍用于存放你自己的实验记录与导出模型（遵守 AGENTS.md 约定）。

## 5. 常见问题（troubleshooting）

| 症状 | 原因与解法 |
|------|-----------|
| `ModuleNotFoundError: No module named 'isaacsim'` | 没激活 `env_isaaclab`，或在错误的 shell/终端里运行；`which python` 检查 |
| 安装 isaacsim 时依赖冲突 | Python 版本不是 3.11（5.x）/ 3.10（4.x）；重建环境 |
| 启动报 GLIBC 相关错误 | 系统 GLIBC < 2.35（如 Ubuntu 20.04）；换 22.04+ 或改用官方二进制安装方式 |
| 首次启动「卡」在加载 | 首次拉取扩展缓存（约 10 分钟），不是卡死；看日志确认有进度 |
| 服务器无显示、启动即崩 | 训练/脚本一律加 `--headless` |
| Vulkan / GPU 相关报错 | 驱动过旧，`nvidia-smi` 确认驱动版本后升级 |
| `pip` 找不到（uv 环境） | `uv venv` 不带 pip；用 `--seed` 重建或用 `uv pip` 代替 |
| 磁盘爆满 | isaacsim 包 + 扩展缓存很大；可清理 `~/.cache/ov` 与 pip 缓存 |

## 6. 版本速查

| 组件 | 本文采用版本 | 备注 |
|------|--------------|------|
| Isaac Sim | 5.1.0 | `pip install "isaacsim[all,extscache]==5.1.0" --extra-index-url https://pypi.nvidia.com` |
| PyTorch | 2.7.0 + cu128 | Isaac Sim 5.x 官方配套 |
| Isaac Lab | main 分支 | 与 Isaac Sim 5.x 对应；老项目注意版本匹配 |
| Python | 3.11（Isaac 环境）/ 3.10–3.12（项目 .venv） | 两者分开 |
| usd-core | 最新稳定版 | 纯 CPU，装项目 .venv |

> 版本号会随官方更新变化，安装前请再对照
> [Isaac Lab 官方安装页](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html)。
