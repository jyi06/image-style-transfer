# Image Style Transfer · 图片风格迁移

> 把任意图片转换成 **50 种精修风格**之一 —— 国风水墨、古典油画、浮世绘、赛博朋克、吉卜力、黑白胶片、文学杂志跨页、装饰艺术、孔版印刷、教堂花窗…… 以及另外 40 种。

[English →](README.md)

**仓库镜像：** [GitHub](https://github.com/jyi06/image-style-transfer) · [Gitee](https://gitee.com/jyi106/image-style-transfer) —— 国内建议用 Gitee 镜像，克隆更快，下面的示例图也能正常打开。

基于开放的 **Agent Skills** 标准构建，同一份 skill 可直接运行在 **Codex、ChatGPT、Claude Code、Cursor、GitHub Copilot、Gemini CLI、VS Code** 等任何能读取 `SKILL.md` 的宿主里。

---

## 效果示例

同一张输入图，套用 50 种风格中的 7 种。下面每一张都只用了库里对应的那一条提示词模板，**没有针对性手工调参**。

![左为原图，右为 #26 JOJO](docs/gallery/before-after.png)

![同一张输入图的 7 种风格：国风水墨、JOJO、时装大片、黑白胶片、印象派厚涂、表现主义厚涂人像、文学杂志版式](docs/gallery/showcase.png)

| 图块 | 风格 | 提示词在做什么 |
|------|------|----------------|
| #7 | 国风水墨 | 写意笔法、墨分五色、大片留白；斗篷化为泼墨 |
| #26 | JOJO | 赛璐璐平涂、硬边色块、粗重的荒木线排线 |
| #3 | 时装大片 | 硬调主光、杂志封面级对比、高定造型 |
| #18 | 黑白胶片 | 银盐印相、深黑场、不留任何色彩 |
| #31 | 印象派厚涂 | 碎笔触、可见厚颜料、边缘消解 |
| #32 | 表现主义厚涂人像 | 形体扭曲、生猛笔触、色彩夸张 |
| #37 | 文学杂志版式 | 构成主义几何、正圆裁切、克制诗排版 |

---

## 它和网上那些提示词有什么区别

大多数"风格迁移提示词"就一句话——"画成油画"。这个库不一样，每一条都是**经过实测打磨的完整提示词**，包含四个真正起作用的要素：

- **精确术语锚点**：`impasto`（厚涂）、`chiaroscuro`（明暗对照）、`wet-on-wet`（湿画法）、`Ben-Day dots`（本戴点）、`Araki line`（荒木线）。术语比形容词有效得多。
- **点名参照物**：具体到某位画家、某部电影或某个品牌（"莫奈"、"葛饰北斋"、"银翼杀手"、"Kinfolk"），引导力远强于"好看"。
- **每种风格各自的推荐强度**：图生图最重要的旋钮就是强度，而胶片颗粒和像素风需要的值完全不同——库里逐条给了推荐值。
- **已知翻车点**：每条都写明什么会出错。比如人像**绝不能**用葛饰北斋，那会把人脸变成"照片 + 波浪贴纸"的拼贴感。

除了提示词库，这个 skill 还带了一套**局部精修工作流**，专门解决所有人都会卡住的那一步：整张图 95% 都对了，就一个细节不对，而重跑整图会把其他部分全毁掉。正确做法是——裁出局部补丁 → 单独重绘 → 羽化贴回，**蒙版外像素逐像素不变**。文档里附了实测的前后数值。

## 50 种风格一览

| 编号 | 分类 | 风格 |
|---|------|------|
| 1–4 | 文艺 · 杂志 | 文艺杂志（Kinfolk）、日系清新、时装大片、极简北欧 |
| 5–10 | 绘画 · 手作 | 油画、水彩、国风水墨、铅笔素描、浮世绘、马克笔插画 |
| 11–16 | 潮流 · 数字 | 赛博朋克、蒸汽波、像素风、3D 卡通盲盒、黏土定格、波普 |
| 17–21 | 复古 · 胶片 | 电影胶片、黑白胶片、港风复古、美式复古海报、拍立得 |
| 22–26 | 动漫 · 插画 | 日系动漫、吉卜力、欧美漫画、绘本童话、JOJO（赛璐璐 + 荒木线） |
| 27–32 | 特殊材质 · 色调 | 剪纸拼贴、积木、霓虹玻璃、莫兰迪、印象派厚涂、表现主义厚涂人像 |
| 33–37 | 编辑设计 · 纸刊 | 微缩风景明信片、拾景纸刊、水彩手账、抽象记忆面板、现代文学艺术杂志 |
| 38–43 | 印刷 · 平面 · 装饰 | 装饰艺术、新艺术运动、包豪斯海报、孔版印刷、木刻版画、钢版雕刻 |
| 44–48 | 艺术流派 · 观念 | 点彩派、超现实主义、欧普艺术、湿壁画、教堂花窗 |
| 49–50 | 材质 · 手作 | 手工刺绣、大理石雕塑 |

完整提示词与参数见 [`skills/image-style-transfer/references/style-library.md`](skills/image-style-transfer/references/style-library.md)。

> **编号规则：只追加，不插入。** 编号是公开接口——用户会直接说「做 26 和 37」。新风格一律取末尾的下一个空号，这样**所有发出去的编号永远有效**；中途插入会让后面全部错位。

## 安装

### Codex

Codex 会扫描 `.agents/skills`（仓库级，一路向上到仓库根）和 `~/.agents/skills`（用户级）。

```bash
# GitHub
git clone https://github.com/jyi06/image-style-transfer.git
# 国内建议改用 Gitee 镜像（把上面一行注释掉，启用下面这行）
# git clone https://gitee.com/jyi106/image-style-transfer.git
cd image-style-transfer

# 用户级安装（所有仓库可用）
mkdir -p ~/.agents/skills
ln -s "$PWD/skills/image-style-transfer" ~/.agents/skills/image-style-transfer
```

> 注意：**不是** `.codex/skills/` —— Codex 不扫描那个路径。软链接会被跟随，所以你可以直接在 checkout 里继续改。

之后在 Codex 里用 `/skills` 或 `$image-style-transfer` 调用，也可以直接描述任务让它自动匹配。

### Claude Code

```bash
mkdir -p ~/.claude/skills
ln -s "$PWD/skills/image-style-transfer" ~/.claude/skills/image-style-transfer
```

### 仓库级（任意宿主）

把 skill 提交进仓库，整个团队都能用：

```bash
mkdir -p .agents/skills
cp -r path/to/image-style-transfer/skills/image-style-transfer .agents/skills/
```

## 给它接一个图像生成能力

这个 skill 负责决定**要什么**；模型由宿主提供。两种方式：

**1. MCP 图像工具（推荐）**：如果你的 agent 已经接了图像生成/编辑的 MCP server，直接让它用即可，无需额外配置。

**2. 内置脚本**：`scripts/generate.py` 零依赖（仅标准库），对接任何 OpenAI 兼容的 `/v1/images/edits` 接口：

```bash
export OPENAI_API_KEY=sk-...
# 使用兼容网关时可选：
# export OPENAI_BASE_URL=https://your-gateway.example.com/v1
# export IMAGE_MODEL=gpt-image-1

python3 skills/image-style-transfer/scripts/generate.py \
  --image photo.jpg \
  --prompt "中国水墨画风格，写意笔法，……" \
  --out generated-images/ink.png \
  --match-aspect
```

如果网关支持显式的强度参数，用 `--extra` 传：

```bash
python3 .../generate.py --image photo.jpg --prompt "..." --out out.png --extra strength=0.6
```

skill 会把自己的强度建议（`0.35–0.9`）映射到你所用平台的参数名上——`input_fidelity`、`image_strength`、`denoising_strength`、`--iw` 等等。

## 用法

装好之后直接和 agent 对话：

> 把这张照片做成一幅中国水墨画。

> 把这张人像做成九十年代港片剧照的感觉。

> 我发一张图，把风格菜单给我看看。

> 这张做水彩，再做一个像素风。

如果只发图、不说风格，skill 会先给出**最匹配该图类型的 4 个风格**，并附上完整清单。你可以回编号、回风格名，或者说"都要"。

## 仓库结构

```
image-style-transfer/
├── plugin.json                              # 便携清单（agent-plugins.org schema）
├── README.md / README.zh-CN.md
├── LICENSE
└── skills/
    └── image-style-transfer/
        ├── SKILL.md                         # 工作流
        ├── agents/openai.yaml               # Codex 侧元数据与依赖声明
        ├── references/
        │   ├── style-library.md             # 50 条提示词模板
        │   └── style-menu.md                # 选择菜单 + 按图类型智能推荐
        └── scripts/
            └── generate.py                  # 可选·零依赖图生图脚本
```

## 参与贡献

风格库是设计成可持续增长的。新增风格时，**三处编号必须同步更新**：`SKILL.md`（总览表）、`style-library.md`（条目本体）、`style-menu.md`（菜单），以及总数。

如果你发现了新的翻车点，请写进 `SKILL.md` 的 *Notes* 里，并带上你实测到的具体现象。重点不是"重新训练模型"，而是"**这里会坏，坏成什么样，怎么绕过去**"。

## 发布

作者署名为 **can1123**，仓库位于 `github.com/jyi06/image-style-transfer`，配置已全部填好，**无需再改任何占位符**。

如果要换成别的账号发布，改 `plugin.json` 里的 `author`、`homepage`、`repository`，以及 `extensions.com.openai.interface` 里的几个 URL，再改 `LICENSE` 的著作权行即可。

```bash
git init && git add -A && git commit -m "Initial release"
git branch -M main
git remote add origin https://github.com/jyi06/image-style-transfer.git
git push -u origin main
```

可选：提交到 OpenAI 的插件目录，或做成团队 marketplace 目录供本地安装。

## 许可

MIT —— 见 [LICENSE](LICENSE)。
