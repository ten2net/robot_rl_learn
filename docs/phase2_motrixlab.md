# 阶段二环境安装指南：MotrixSim / MotrixLab

> 对应 `docs/learning_path.md` 的阶段二（W13–W20）。
> 两份工具的关系：**MotrixSim** 是物理仿真引擎（Python 包，可直接装进本工程）；
> **MotrixLab** 是基于 MotrixSim 的 RL 训练框架（独立 Git 仓库，建议单独目录安装）。
> 信息来源：官方文档与 GitHub README（链接见文末），最后核对日期 2026-08。

---

## 1. MotrixSim（物理引擎）

### 1.1 安装

官方安装命令（[安装 Python SDK](https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/installation.html)）：

```bash
# 方式一：pip
pip install motrixsim

# 方式二：uv（本项目依赖管理工具）
uv add motrixsim
```

本工程的 `pyproject.toml` 已声明 `motrix` extra（`motrixsim>=0.1`），理论上一键安装：

```bash
uv sync --extra motrix
```

> **已知问题（排障提示）**：若 `uv sync` 报依赖解析冲突（`imitation` 与 `gymnasium>=1.0`
> 的版本约束冲突，属本工程 pyproject 的既有问题），可绕开全量同步，直接向现有
> 虚拟环境补装：
>
> ```bash
> uv pip install motrixsim        # 装入本工程 .venv，不改 pyproject
> ```
>
> 如需 USD 模型支持，安装可选 extra：`uv pip install "motrixsim[usd]"`。

### 1.2 验证安装

```bash
uv pip list | grep motrixsim
uv run python -c "import motrixsim; print(motrixsim.__version__)"
```

### 1.3 跑通 Hello MotrixSim

按官方[快速入门](https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/hello_motrixsim.html)，
最小示例只需四行核心代码（加载模型 → 创建数据 → step 循环 → 渲染同步）：

```python
import motrixsim as mx

model = mx.load_model("assets/boston_dynamics_spot/scene.xml")
with mx.render.RenderApp("warn") as render:
    render.launch(model)
    data = mx.SceneData(model)
    while True:
        model.step(data)
        render.sync(data)
```

示例模型（Spot 机器狗）从官方文档仓库获取：

```bash
git clone --depth 1 https://github.com/Motphys/motrixsim-docs.git temp-docs
mkdir -p assets
cp -r temp-docs/examples/assets/boston_dynamics_spot assets/
rm -rf temp-docs
```

**预期结果**：渲染窗口中 Spot 在重力作用下自然站立并保持平衡。

### 1.4 平台注意事项

- 支持 Windows / Linux / macOS；**macOS (Apple Silicon)** 上使用渲染器的示例需用
  `uv run mxpython <script.py>` 启动（纯物理仿真脚本不受此限）。
- 无显卡也可学习本阶段：MotrixSim 的 CPU 版本基于 Rust 开发，支持大规模 CPU 并行；
  GPU 并行为可选加速。
- 不想本地安装也可以先用官方**网页仿真器**（拖拽 MJCF 模型文件夹即可仿真），
  见 MotrixSim 文档「网页仿真器」章节。

---

## 2. MotrixLab（RL 训练框架）

### 2.1 安装（独立目录）

MotrixLab 是自带 uv 工程的独立仓库，**不要**装进本工程的 `.venv`，推荐：

```bash
mkdir -p ~/workspace && cd ~/workspace
git clone https://github.com/Motphys/MotrixLab
cd MotrixLab
git lfs pull                          # 拉取模型资产等大文件（需先安装 git-lfs）

# 全量安装（SKRL 的 JAX+PyTorch 双后端 + RSLRL）
uv sync --all-packages --all-extras

# 或按需精简安装（三选一）：
uv sync --all-packages --extra skrl-jax     # SKRL + JAX 后端（仅 Linux）
uv sync --all-packages --extra skrl-torch   # SKRL + PyTorch 后端
uv sync --all-packages --extra rslrl        # RSLRL（仅 PyTorch）
```

> Ubuntu 上若没有 git-lfs：`sudo apt install git-lfs && git lfs install`。

### 2.2 验证安装（三件套）

```bash
# ① 环境预览：随机动作演示，验证仿真与渲染链路（应弹出倒立摆窗口）
uv run scripts/view.py --env cartpole

# ② 训练：默认 SKRL 框架，自动选择训练后端
uv run scripts/train.py --env cartpole

# ③ 查看训练曲线
uv run tensorboard --logdir runs/cartpole

# ④ 部署测试训练好的策略
uv run scripts/play.py --env cartpole
```

**预期结果**：训练中终端滚动打印迭代日志，`runs/cartpole/` 下生成检查点与
TensorBoard 日志；`play.py` 窗口中倒立摆能长时间保持平衡。

常用参数（[官方文档](https://motrixlab.readthedocs.io/zh-cn/latest/user_guide/tutorial/training_and_result.html)）：
`--env`（默认 cartpole）、`--rllib skrl|rslrl`、`--sim-backend np`、
`--train-backend jax|torch`、`--num-envs`（默认 2048）、`--render`
（训练中按空格键切换渲染开关）。学习率等算法超参不在命令行，需改配置数据类。

### 2.3 建议的首批任务

| 顺序 | 环境 ID | 内容 |
|------|---------|------|
| 1 | `cartpole` | 链路验证（分钟级） |
| 2 | `dm-quadruped-walk` | 四足平地行走（0.5 m/s，W14/W18 主讲任务） |
| 3 | `dm-quadruped-run` / `-escape` / `-fetch` | 同族进阶任务，任选 |

---

## 3. 常见问题（FAQ）

- **`git lfs pull` 报错或没有 git-lfs**：先安装 git-lfs（`sudo apt install git-lfs`），
  并在仓库内执行过一次 `git lfs install`；否则模型资产只是指针文件，加载会失败。
- **`uv run` 在 MotrixLab 目录下解析缓慢**：首次 `uv sync` 会下载 JAX/PyTorch 等大依赖，
  耐心等待；之后运行有缓存。
- **无显示环境（远程服务器）**：不要加 `--render` / 不运行 `view.py`/`play.py` 的渲染窗口，
  训练与 TensorBoard 均不依赖显示；渲染相关问题见 MotrixSim 文档「环境准备」FAQ。
- **USD 模型加载失败**：需安装 `motrixsim[usd]` 可选依赖（见 1.2）。

## 4. 参考链接（均已核对）

- MotrixLab GitHub：<https://github.com/Motphys/MotrixLab>
- MotrixLab 文档：<https://motrixlab.readthedocs.io/>
  （快速入门 / 训练执行和结果分析 / 四足机器人任务）
- MotrixSim 文档：<https://motrixsim.readthedocs.io/zh-cn/latest/>
  （安装 / 快速入门 / 模型 / 数据 / 参数随机化）
- MotrixSim PyPI：<https://pypi.org/project/motrixsim/>
- 谋先飞 × Xbotics 实训营：<https://github.com/Xbotics-Embodied-AI-club/Motphys-Xbotics-Robot-Rl-Sim-Training-Camp>
