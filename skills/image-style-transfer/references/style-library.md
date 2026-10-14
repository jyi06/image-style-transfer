# 风格提示词库（Style Prompt Library） — 共 80 个风格

本文件是 image-style-transfer 的核心资产。每个风格给出**可直接使用的提示词模板**、
**推荐输入保真度（input_fidelity）** 与 **适用场景**。

> **v5 更新（2026-10-14）**：新增 **30 个风格（编号 51–80）**，形成四个新分节——
> **十一、东亚传统（51–57）**、**十二、西方艺术史经典（58–65）**、
> **十三、摄影与影像工艺（66–73）**、**十四、当代插画与数字（74–80）**。
> 原「十一、风格推导公式」「十二、术语校准来源」顺延为 **十五 / 十六**。
> ⚠️ **1–50 的编号一个都没动**（新条目一律**追加在末尾**）：编号是用户与旧文档引用的事实接口，
> 中途插入会让所有后续编号错位。**今后扩充也请照此办理 —— 只追加，不插入。**
> 分类分布（共 80）：文艺杂志 4 ｜ 绘画手作 6 ｜ 潮流数字 6 ｜ 复古胶片 5 ｜ 动漫插画 5 ｜
> 特殊材质·色调·表现主义 6 ｜ 编辑设计·纸刊与海报 5 ｜ 印刷平面·装饰 6 ｜ 艺术流派·观念 5 ｜ 材质手作 2 ｜
> **东亚传统 7** ｜ **西方艺术史经典 8** ｜ **摄影与影像工艺 8** ｜ **当代插画与数字 7**。
>
> **v4 更新（2026-10-14）**：新增 **13 个风格（编号 38–50）**，形成三个新分节——
> **八、印刷·平面·装饰艺术（38–43）**、**九、艺术流派·观念（44–48）**、**十、材质与手作（49–50）**。
> 分类分布（当时共 50）：文艺杂志 4 ｜ 绘画手作 6 ｜ 潮流数字 6 ｜ 复古胶片 5 ｜ 动漫插画 5 ｜
> 特殊材质·色调·表现主义 6 ｜ 编辑设计·纸刊与海报 5 ｜ 印刷平面·装饰 6 ｜ 艺术流派·观念 5 ｜ 材质手作 2。
>
> **v3 更新（2026-10-12）**：风格库重排为**连续编号 1–37**（此前 #26 JOJO 与 #32 表现主义厚涂
> 因后续新增而编号错位，现按分类位置归位），并统一了编号 ↔ 分类 ↔ `style-menu.md` 菜单三处的对应关系。
> 分类分布：文艺杂志 4 ｜ 绘画手作 6（含 JOJO）｜ 潮流数字 6 ｜ 复古胶片 5 ｜ 动漫插画 4 ｜
> 特殊材质·色调·表现主义 6 ｜ 编辑设计·纸刊与海报 6（含现代文学艺术杂志）。
>
> **v2 更新（2026-10-11）**：已用 GitHub 开放提示词资源（艺术流派术语库 180+ 条、艺术技法表 140+ 条、
> 色彩/情绪词表、风格提示词块）对全部条目做了**术语校准与参照物补强**。
> 核心改进：给每个风格加上 **① 精确英文术语锚点**、**② 标志性参照物**（点名比形容词有效得多）、
> **③ 材质/笔触/光影的具体描述**、**④ 常见失败模式的规避**。来源见文末「九、术语校准来源」。

## 使用规则

1. 先按用户给的风格名在下方检索匹配条目（大小写、中英文皆可匹配）。
2. 命中则取该条目的「提示词模板」，再按 SKILL.md 的「提示词组装公式」套入用户原图主体。
3. 未命中（用户要的风格不在库中）则按「风格推导公式」现场生成，并追加到本文件末尾（保持库可增长）。
4. `input_fidelity` 是 ImageGen 图生图参数，值越高越贴近原图。**风格迁移推荐 0.55–0.75**，
   想要"面目全非式改画"可降到 0.35–0.5，只想加滤镜感可升到 0.8–0.9。
5. **通用负向约束**（每条风格模板后统一追加）：
   `保持主体身份与构图；不要文字水印，不要额外肢体，不要变形，不要糊脸`

---

## 一、文艺 · 杂志风

### 1. 文艺杂志风（Vintage Editorial / Kinfolk）
- **关键词**：editorial photography, Kinfolk, Cereal magazine, muted oatmeal palette, film grain, soft haze, negative space, low contrast, art direction
- **术语锚点**：negative space（留白）｜low-key contrast（低对比）｜film grain（胶片颗粒）
- **参照物**：Kinfolk／Cereal Magazine 内页；中画幅胶片生活方式摄影
- **提示词模板（强化版）**：`文艺杂志内页摄影风格，Kinfolk／Cereal 式极简生活美学，整体重塑为低饱和燕麦米色调，柔和漫射的自然光，轻微朦胧光晕与柔焦，明显胶片颗粒与细腻噪点，低对比度高级灰，主体偏侧并留出大面积留白，宁静克制的叙事感，皮肤质感自然通透，暖灰与浅驼色为主色，画面清淡透气，仿佛时尚生活方式杂志的跨页内页，印刷质感与纸张肌理，构图讲究，艺术指导感强`
- **推荐 input_fidelity**：0.5（要含蓄的"滤镜感"用 0.7；要明显的"改画感"用 0.45–0.55）
- **适合**：人像、静物、街景
- **加强要点**：把色调写死（燕麦／米白／暖灰）、追加"整体重塑色调""明显胶片颗粒""低对比度"，并把 input_fidelity 降到 0.5

### 2. 日系清新杂志风（Japanese Fresh Editorial）
- **关键词**：Japanese photobook, high-key, airy, soft pastel, cyan-blue cast, clean composition, morning light, minimal
- **术语锚点**：high-key（高调）｜cyan cast（青调）｜airiness（空气感）
- **参照物**：日系写真集（photobook）；川内伦子／川岛小鸟式日常纪实
- **提示词模板**：`日系写真集风格，高调通透的画面，柔和均匀的晨光，淡雅青蓝与奶白色调，极轻的胶片颗粒，构图干净留白，清新自然的空气感，像一本日系生活写真杂志的内页`
- **推荐 input_fidelity**：0.7
- **适合**：人像、食物、日常风景

### 3. 时装大片（High Fashion Editorial）
- **关键词**：high fashion editorial, Vogue, dramatic lighting, high contrast, glossy skin, bold silhouette, studio lighting, couture
- **术语锚点**：chiaroscuro（明暗对照）｜tenebrism（暗色调主义）｜glossy skin（通透皮肤光）
- **参照物**：Vogue／Harper's Bazaar 封面；Peter Lindbergh 式硬光
- **提示词模板**：`高端时装杂志大片风格，戏剧化的侧逆光与明暗对照，高对比度，皮肤质感细腻有光泽，服装的材质与剪裁清晰，背景简约而有质感，色彩高级克制，主体气场强烈，专业影棚布光，大片级修图质感`
- **推荐 input_fidelity**：0.65
- **适合**：人物、服饰
- **避免**：不要平光、不要廉价影楼感

### 4. 极简北欧风（Minimal Nordic）
- **关键词**：Scandinavian minimal, muted beige, soft shadow, clean, negative space, matte, hygge
- **术语锚点**：negative space（留白）｜matte finish（哑光）｜diffused light（漫射光）
- **参照物**：北欧家居设计杂志封面
- **提示词模板**：`北欧极简主义风格，莫兰迪米白与暖灰调，柔和漫射光，干净的大面积留白，克制的构图，哑光质感，安静高级，像家居设计杂志的封面`
- **推荐 input_fidelity**：0.72
- **适合**：静物、室内、产品

---

## 二、绘画 · 手作

### 5. 油画风（Oil Painting）
- **关键词**：oil painting, impasto, scumbling, glazing, chiaroscuro, canvas weave, alla prima, rich color blend
- **术语锚点**：**impasto（厚涂）**｜**chiaroscuro（明暗对照）**｜scumbling（干笔擦）｜glazing（透明罩染）｜alla prima（一次性完成）
- **参照物**：伦勃朗式明暗；印象派（Impressionism）色彩
- **提示词模板**：`古典油画风格，厚涂（impasto）笔触，可见的颜料堆叠与刮刀痕，透明罩染与干笔擦的肌理，明暗对照（chiaroscuro）的暖调光影，画布纹理清晰，笔触松弛而有力，像美术馆里的布面油画`
- **推荐 input_fidelity**：0.6（想要"照片感消失"降到 0.4；极致油画语言用 0.22，见条目 32）
- **适合**：人像、风景、静物

### 6. 水彩风（Watercolor）
- **关键词**：watercolor, wet-on-wet, wet-on-dry, translucent washes, bleeding edges, granulation, cold-press paper
- **术语锚点**：**wet-on-wet（湿画法）**｜color wash（水色罩染）｜bleeding edge（自然扩散边）｜granulation（颜料沉积）｜cold-press paper（冷压水彩纸）
- **提示词模板**：`水彩画风格，湿画法晕染（wet-on-wet），透明的水色叠加，边缘自然扩散与颜料沉积，冷压水彩纸的颗粒肌理，留白透气，色彩清淡通透，笔触轻盈`
- **推荐 input_fidelity**：0.6
- **适合**：风景、花卉、人像
- **避免**：不要油画厚涂感、不要塑料光泽

### 7. 国风水墨（Chinese Ink Wash）
- **关键词**：ink wash painting, sumi-e, xieyi, liubai, haboku, rice paper, varying ink density, calligraphic line
- **术语锚点**：**xieyi（写意）**｜sumi-e（墨绘）｜haboku（破墨）｜飞白（flying white）｜留白（liubai）
- **参照物**：水墨写意传统（墨分五色）
- **提示词模板**：`中国水墨画风格，写意笔法，墨分五色——浓、淡、干、湿、焦的变化，枯笔飞白，宣纸渗化质感，大量留白，意境悠远，线条有书法韵味，仅以少量朱红点染`
- **推荐 input_fidelity**：0.6
- **适合**：山水、花鸟、人物
- **避免**：不要彩色写实、不要西式透视

### 8. 铅笔素描（Pencil Sketch）
- **关键词**：pencil sketch, graphite, hatching, cross-hatching, contour drawing, monochrome, sketchbook
- **术语锚点**：**hatching／cross-hatching（排线／交叉排线）**｜contour drawing（轮廓线）｜graphite（石墨）
- **提示词模板**：`铅笔素描风格，石墨（graphite）质感，排线与交叉排线塑造体积，边缘线明确，纸张颗粒感，黑白灰层次分明，手绘速写本气息`
- **推荐 input_fidelity**：0.65
- **适合**：人物、动物、建筑

### 9. 浮世绘（Ukiyo-e）
- **关键词**：ukiyo-e, Japanese woodblock print, nishiki-e, flat color, bold outlines, decorative pattern, carved impression
- **术语锚点**：**ukiyo-e（浮世绘）**｜nishiki-e（锦绘）｜shin-hanga（新版画）｜sosaku-hanga（创作版画）
- **参照物（按题材选，选错会翻车）**：
  - **人像 → 喜多川歌麿（美人画 bijin-ga）、东洲斋写乐（役者绘，夸张锐利）** ← 人像必须用这组
  - 风景/波浪 → 葛饰北斋（富岳三十六景、神奈川冲浪里）、歌川广重
  - ⚠️ **不要把葛饰北斋用在人像上**：他是风景/波浪向的画家，会把人像带成"照片 + 波纹贴纸"的拼贴感，而人物本体仍是照片质感（2026-10-11 实测踩坑，用户当场否决）
- **提示词模板（人像版）**：`日本浮世绘美人画（bijin-ga）风格，喜多川歌麿式的平面化女性形象，脸型拉长、眉目以单线概括，颈部有"三本线"（三道平行细线）与华丽发簪纹样，平涂色块与粗壮有力的轮廓线，装饰性纹样（青海波纹、云纹、雷纹、友禅和服纹），靛蓝、朱红与藤黄配色，可见木版雕刻的印痕与套色偏移，和纸纤维质感，平面装饰感强，完全放弃体积与光影；保持人物发型轮廓、笑容与构图不变`
- **提示词模板（风景版）**：`日本浮世绘木版画风格，葛饰北斋式的构图张力，平涂色块与粗壮有力的轮廓线，装饰性纹样（波纹、云纹、雷纹），靛蓝、朱红与藤黄配色，可见木版雕刻的印痕与套色偏移，平面装饰感强`
- **推荐 input_fidelity**：**人像 0.42–0.48**（0.55 实测偏照片，脸太"实"）｜风景 0.55
- **适合**：风景、人物、动物
- **避免**：不要写实光影、不要 3D 立体感、不要照片质感、不要"照片 + 纹样贴纸"的拼贴感

### 10. 马克笔插画（Marker Illustration）
- **关键词**：marker illustration, alcohol marker, copic, bold flat color, clean ink outline, color bleed, graphic
- **术语锚点**：alcohol marker（酒精马克笔）｜flat color（平涂）｜ink outline（勾线）
- **提示词模板**：`马克笔插画风格，酒精马克笔（Copic 式）平涂，色彩饱和明快，清晰的黑色勾线与块面分明，叠色处自然渗色，手账插画质感，干净利落`
- **推荐 input_fidelity**：0.6
- **适合**：人物、静物、场景

---

## 三、潮流 · 数字

### 11. 赛博朋克（Cyberpunk）
- **关键词**：cyberpunk, neon lights, teal and magenta, rain-soaked, holographic, volumetric fog, futuristic city
- **术语锚点**：**cyberpunk（赛博朋克流派）**｜neon（霓虹）｜volumetric fog（体积雾）｜holographic（全息）
- **参照物**：**《银翼杀手》**式雨夜霓虹
- **提示词模板**：`赛博朋克风格，霓虹青紫双色光，湿润街道的反光，全息广告牌与密集招牌，体积雾与光晕，高对比强光，未来都市的科技冷峻感，银翼杀手式的雨夜氛围`
- **推荐 input_fidelity**：0.5
- **适合**：人像、街头、建筑

### 12. 蒸汽波（Vaporwave）
- **关键词**：vaporwave, synthwave, retro-futurism, pastel pink and cyan, grid horizon, chrome, VHS
- **术语锚点**：**vaporwave（蒸汽波）**｜synthwave｜retro-futurism（复古未来主义）｜chrome（镀铬）
- **提示词模板**：`蒸汽波风格，粉紫与青色渐变，八十年代复古未来主义，网格地平线与落日，镀铬（chrome）质感，VHS 录像带的轻微失真，怀旧的数字美学`
- **推荐 input_fidelity**：0.5
- **适合**：风景、静物、人物

### 13. 像素风（Pixel Art）
- **关键词**：pixel art, 16-bit, limited palette, crisp pixels, dithering, isometric, retro game sprite
- **术语锚点**：**pixel art（像素艺术）**｜dithering（抖动渐隐）｜limited palette（有限调色板）｜isometric（等距）
- **提示词模板**：`像素艺术风格，16 位复古游戏画面，有限调色板，像素颗粒清晰锐利，抖动渐隐（dithering），等距视角，复古游戏精灵图质感`
- **推荐 input_fidelity**：0.4
- **适合**：人物、场景、物品
- **避免**：不要平滑渐变、不要抗锯齿

### 14. 3D 卡通 / 盲盒（3D Cartoon）
- **关键词**：3D render, Pixar style, blind box toy, soft studio light, glossy plastic, subsurface scattering
- **术语锚点**：**subsurface scattering（次表面散射）**｜glossy plastic（光滑塑料）｜soft studio light（柔和影棚光）
- **参照物**：皮克斯质感、Blender 潮流手办
- **提示词模板**：`3D 卡通渲染风格，皮克斯质感，盲盒潮玩造型，柔和的影棚布光与次表面散射的透亮皮肤，光滑的塑料／树脂材质，圆润可爱，背景干净，超清渲染`
- **推荐 input_fidelity**：0.55
- **适合**：人物、宠物、物品

### 15. 黏土定格（Claymation）
- **关键词**：claymation, plasticine, stop-motion, fingerprint texture, miniature set, practical lighting
- **术语锚点**：**claymation（黏土定格）**｜plasticine（橡皮泥）｜stop-motion（定格动画）
- **参照物**：阿德曼（Aardman）定格动画
- **提示词模板**：`黏土定格动画风格，橡皮泥手工质感，可见指纹与塑形痕迹，微缩实景布景，柔和的定格影棚光，质朴可爱，暖色调`
- **推荐 input_fidelity**：0.55
- **适合**：人物、动物、静物

### 16. 波普艺术（Pop Art）
- **关键词**：pop art, Ben-Day dots, halftone, screen print, bold primary colors, Warhol, Lichtenstein
- **术语锚点**：**Ben-Day dots（本戴点）**｜halftone（网点）｜screen print（丝网印）
- **参照物**：**安迪·沃霍尔**、利希滕斯坦
- **提示词模板**：`波普艺术风格，本戴点（Ben-Day dots）网点印刷质感，高饱和原色平涂，粗黑轮廓，重复排列的色块，安迪·沃霍尔式的丝网印平面海报感`
- **推荐 input_fidelity**：0.5
- **适合**：人像、产品、图形

---

## 四、复古 · 胶片

### 17. 电影胶片感（Cinematic Film）
- **关键词**：cinematic, anamorphic, film grain, teal and orange, shallow depth of field, moody
- **术语锚点**：**anamorphic（变形宽银幕）**｜teal & orange（青橙调）｜shallow DOF（浅景深）｜film grain（胶片颗粒）
- **参照物**：35mm 电影剧照；柯达胶片色
- **提示词模板**：`电影感胶片风格，变形宽银幕（anamorphic）构图与横向光斑，青橙色调，浅景深虚化，细腻的胶片颗粒与轻微光晕，戏剧化光影，像 35mm 电影剧照`
- **推荐 input_fidelity**：0.72
- **适合**：人像、街景、风景

### 18. 黑白胶片（Black & White Film）
- **关键词**：black and white, monochrome, silver gelatin, high contrast, film grain, dramatic shadow
- **术语锚点**：**silver gelatin print（银盐印相）**｜monochrome（单色）｜deep blacks（深黑场）｜tenebrism
- **参照物**：经典纪实黑白摄影（银盐胶片）
- **提示词模板**：`黑白胶片摄影风格，银盐（silver gelatin）质感，丰富的高光与阴影层次，细腻的颗粒与深黑场，戏剧化明暗对比，经典纪实摄影的永恒感`
- **推荐 input_fidelity**：0.78
- **适合**：人像、建筑、街头

### 19. 港风复古（HK Retro）
- **关键词**：Hong Kong retro, 90s film, neon reflection, tungsten warm, nostalgic cinema
- **术语锚点**：**tungsten（钨丝灯色温）**｜neon reflection（霓虹反光）｜underexposure（欠曝）
- **参照物**：**王家卫**式九十年代港片
- **提示词模板**：`九十年代香港复古电影风格，王家卫式的钨丝灯暖黄与霓虹冷光交织，湿润街面反光，轻微欠曝与胶片颗粒，怀旧港片的暧昧氛围`
- **推荐 input_fidelity**：0.65
- **适合**：人像、街头

### 20. 美式复古海报（Vintage American Poster）
- **关键词**：vintage poster, 1950s advertising, mid-century, screen print, halftone, aged paper, limited palette
- **术语锚点**：**mid-century modern（中世纪现代）**｜screen print（丝网印）｜halftone（网点）｜aged paper（做旧纸）
- **提示词模板**：`美式复古海报风格，五十年代广告插画，丝网印刷的平面色块与网点，做旧泛黄的纸张质感，米黄与砖红主色，边缘轻微磨损，画面留出标题排版区`
- **推荐 input_fidelity**：0.55
- **适合**：人像、产品、场景

### 21. 拍立得（Polaroid）
- **关键词**：polaroid, instant film, soft focus, washed highlights, color shift, white border, flash
- **术语锚点**：**instant film（即时成像）**｜washed highlights（高光溢出）｜color shift（偏色）｜flash direct（闪光直打）
- **提示词模板**：`宝丽来拍立得风格，柔焦与轻微过曝的高光，偏色的复古色调，白色相纸边框，即时成像的褪色感，闪光灯直打的生活抓拍气息`
- **推荐 input_fidelity**：0.78
- **适合**：人像、日常、静物

---

## 五、动漫 · 插画
### 22. 日系动漫（Anime）
- **关键词**：anime, cel shading, clean lineart, vibrant, big eyes, key visual, Japanese animation
- **术语锚点**：**cel shading（赛璐璐上色）**｜lineart（线稿）｜key visual（关键帧）｜rim light（轮廓光）
- **参照物**：新海诚式通透光线；wlop／rossdraws（厚涂向）
- **提示词模板**：`日系动漫风格，赛璐璐（cel）上色与干净利落的线稿，色彩明亮饱和，精致的高光与逆光光晕，眼睛大而有神，背景细腻，动画关键帧（key visual）质感，新海诚式的通透光线`
- **推荐 input_fidelity**：0.5
- **适合**：人物、场景

### 23. 吉卜力风（Studio Ghibli）
- **关键词**：Studio Ghibli, hand-painted background, gouache, warm nostalgic, lush nature, soft cel
- **术语锚点**：**gouache（水粉）**｜hand-painted background（手绘背景）｜soft cel（柔和赛璐璐）
- **参照物**：**吉卜力工作室**、宫崎骏
- **提示词模板**：`吉卜力动画风格，手绘水粉（gouache）背景，温暖怀旧的光线，葱郁细腻的自然草木，柔和的人物上色，宁静治愈的氛围`
- **推荐 input_fidelity**：0.5
- **适合**：风景、人物、场景

### 24. 欧美漫画（Comic Book）
- **关键词**：comic book, ink outline, cross-hatching, halftone, dynamic panel, Marvel/DC
- **术语锚点**：**halftone（网点）**｜cross-hatching（交叉排线）｜dynamic perspective（夸张透视）
- **提示词模板**：`欧美漫画风格，粗黑墨线与交叉排线的阴影，高对比网点（halftone）上色，夸张的透视与分镜张力，美漫封面质感`
- **推荐 input_fidelity**：0.5
- **适合**：人物、动作场景

### 25. 绘本童话（Storybook Illustration）
- **关键词**：storybook, children's book, gouache, watercolor, soft palette, whimsical, paper grain
- **术语锚点**：**gouache（水粉）**｜whimsical（童趣）｜paper grain（纸纹）
- **提示词模板**：`绘本童话插画风格，柔和粉彩与水彩／水粉混合，童趣的造型比例，温暖的柔光，纸张肌理，像一本精装童书的跨页`
- **推荐 input_fidelity**：0.6
- **适合**：人物、动物、场景

### 26. JOJO 动漫风（Araki Anime / David Production 赛璐璐）★ 用户指定
- **来源**：2026-10-11 用户先点单「JOJO 类的写实风」，实测两版后**要求改为与动漫（#22 日系动漫）相同的渲染语言**，遂改写为赛璐璐版；术语取自 GitHub 开放提示词库（`moyin-creator`／`qcut` 的 `2D JOJO风` 预设、`Nano-Banana-AI-Studio` 的 `cartoonStyle='jojo'` 规则、A1111 styles 的 `jojo cover art` 条目）
- **关键词**：JoJo's Bizarre Adventure anime, Hirohiko Araki, David Production, cel shading, bold lineart, Araki line, heavy hatching, JoJo pose, vibrant unnatural palette, menacing onomatopoeia
- **术语锚点**：**cel shading（赛璐璐上色）**｜**Araki line（荒木线：密集平行与交叉的排线阴影）**｜**JoJo pose（乔乔立：脊柱后仰、四肢外旋的夸张英雄姿态）**｜**menacing onomatopoeia（「ゴゴゴ」威压拟声词）**｜**key visual（动画关键帧）**｜**David Production**（动画版制作方）
- **参照物（三重）**：① **David Production 的 TV 动画版**（黄金之风／石之海／星尘斗士）② A1111 的 `jojo cover art` 条目（点名各部封面：vento aureo／stone ocean／steel ball run／jojolion）③ 荒木飞吕彦原画
- **⚠️ 与 #22 日系动漫的关系（关键）**：**两者共用同一套渲染语言（赛璐璐平涂 + 干净墨线），但造型语言相反**——
  - **#22 日系动漫**：柔和可爱（大眼、圆润、低对比、治愈）
  - **#26 JOJO 动漫风**：锐利张扬（高颧骨、刀刻下颌、厚唇、浓密睫毛、粗黑棱角眉 + 密集荒木线 + 极端撞色）
  - 所以**不要照抄 #22 的提示词**，只在"上色方式"上对齐，在"造型结构"上必须保持荒木的锐度
- **提示词模板**：`JOJO 的奇妙冒险动画风格（David Production 制作），荒木飞吕彦（Hirohiko Araki）的人物造型语言：赛璐璐（cel）平涂上色，干净但粗壮有力的墨线稿；面部密布荒木线（Araki line）——在阴影侧、颧骨下方、下颌、脖颈、发根用密集平行与交叉的排线；面部结构夸张锐利——高颧骨、锋利如刀刻的下颌线、饱满厚唇且唇线明确、浓密睫毛、深邃眼窝、粗黑有棱角的眉毛；强烈的非自然撞色（钴紫、祖母绿、金、品红、青蓝）；服装为华丽繁复的时装（巴洛克纹样、金属扣件、刺绣），用平涂分色与硬边阴影呈现；背景为戏剧性的放射光线、翻涌云气与几何装饰；整体是明亮通透的动画关键帧（key visual）质感`
- **配色档**（2026-10-11 首增 · 用户反馈「颜色太鲜艳」→ **2026-10-13 用户指定：默认用 A 档**）：
  - **A 档 · 标准 JOJO（原味）★ 用户指定默认**：强烈非自然撞色（钴紫、祖母绿、金、品红、青蓝）—— JOJO 辨识度最高，张扬热闹。**生成时默认直接用此档，不必再询问用户**
  - **B 档 · 克制配色（备选 · 仅在用户明确要求时使用）**：以**清透青蓝 + 米白**为主调，仅在徽章、领带、阴影与大色块交界处用**少量暖赭／暗金**点缀；**剔除钴紫／品红／祖母绿的高饱和撞色**；整体色调统一、安静、像精细调色后的动画电影关键帧。提示词追加：`配色克制和谐，以清透的青蓝与米白为主调，仅用少量暖赭与暗金作点缀，摒弃高饱和的紫、品红与祖母绿撞色，整体色调统一而安静，像精心调色后的动画电影关键帧`
  - **默认档 = A 档**：直接用模板里的「强烈的非自然撞色（钴紫、祖母绿、金、品红、青蓝）」，不做任何替换。
  - **切到 B 档（仅在用户明确要求时）**：把模板里的「强烈的非自然撞色（钴紫、祖母绿、金、品红、青蓝）」整句**替换**为上面 B 档那句。
  - **A 档加强（可选）**：实测 A 档容易被原图底色锚定、撞色铺不满；若要更炸，追加 `背景与水体本身也使用钴紫、品红与祖母绿的高饱和撞色，不要保留原图的青蓝色调`。
- **推荐 input_fidelity**：**0.5**（与 #22 一致；赛璐璐是**整幅画法替换**，不需要压得很低）
- **可选强化**：加入 `「ゴゴゴ」式威压拟声词文字` 会立刻强化 JOJO 身份，但**这是文字**——需单独向用户确认是否要（默认不加）
- **留档：写实版参数**（2026-10-11 实测过两版，如需回到写实方向可直接取用）：
  - `0.5` + 写实光影词 = 只改光影色彩，**看不到排线、面部仍是照片**，JOJO 身份弱
  - `0.35` + 把「荒木线必须见效」与「面部结构必须夸张化」写成**硬性要求** = **JOJO 身份立住**，但**相似度明显下降**
  - 结论：写实方向受限于"在照片上叠一层风格"，天花板低；**赛璐璐是整幅画法替换，效果更彻底**
- **构图提示**：JOJO 的签名是全身 JoJo pose + 夸张时装版型，**半身胸像施展不开** —— 想要最强效果，用**全身照**
- **适合**：人像、全身动作、街拍
- **避免**：不要照片质感、不要真人写实摄影、不要 3D 渲染、**不要萌系圆润大眼与 Q 版可爱化**（那是 #22 的领域）、不要低饱和与柔和粉彩、不要细弱线条、不要平滑无排线、不要柔光小清新；不要文字水印（除明确要求拟声词）

---

## 六、特殊材质 · 色调 · 表现主义

### 27. 剪纸拼贴（Paper Cutout）
- **关键词**：paper cutout, collage, layered paper, hard shadow, torn edge, handmade
- **术语锚点**：**collage（拼贴）**｜layered paper（分层纸）｜hard shadow（硬投影）｜torn edge（撕纸边）
- **提示词模板**：`剪纸拼贴风格，分层的彩色纸片叠加，清晰的剪纸轮廓与硬投影，撕纸毛边，手工拼贴的立体层次感，配色明快`
- **推荐 input_fidelity**：0.5
- **适合**：风景、人物、静物

### 28. 积木风（Lego / Building Blocks）
- **关键词**：Lego, building blocks, plastic brick, studs, isometric, toy world
- **术语锚点**：**plastic brick（塑料积木）**｜studs（凸点）｜isometric（等距）
- **提示词模板**：`积木玩具风格，乐高式塑料积木搭建，可见凸点（studs）与拼装缝隙，圆角塑料质感，玩具微缩世界，明亮均匀的布光`
- **推荐 input_fidelity**：0.4
- **适合**：人物、场景、物品

### 29. 霓虹玻璃（Neon Glass）
- **关键词**：neon, stained glass, refraction, caustics, luminous, volumetric light
- **术语锚点**：**refraction（折射）**｜caustics（焦散）｜volumetric light（体积光）
- **提示词模板**：`霓虹玻璃风格，半透明玻璃的折射与色散，霓虹管发光，体积光与光晕，暗底衬托出通透的高饱和色，未来感材质`
- **推荐 input_fidelity**：0.55
- **适合**：静物、人像、建筑

### 30. 莫兰迪色调（Morandi Tone）
- **关键词**：Morandi palette, desaturated, dusty pastel, matte, quiet, still life aesthetic
- **术语锚点**：**desaturated（低饱和）**｜dusty pastel（灰调粉彩）｜matte（哑光）
- **参照物**：乔治·莫兰迪静物画
- **提示词模板**：`莫兰迪色调风格，低饱和的灰调粉彩，柔和的漫射光，哑光质感，安静克制的静物美学，色彩之间彼此渗透，高级而温柔`
- **推荐 input_fidelity**：0.8
- **适合**：静物、人像、室内

### 31. 印象派厚涂（Impressionist Impasto）
- **关键词**：Impressionism, broken brushwork, dappled light, plein air, vibrant atmospheric color, Monet
- **术语锚点**：**broken brushwork（碎笔触）**｜dappled light（斑驳光斑）｜en plein air（外光写生）
- **参照物**：**莫奈（Monet）**户外写生
- **提示词模板**：`印象派风格，短促跳动的碎笔触（broken brushwork），斑驳跳跃的光斑，空气中弥漫的光色变化，外光写生（en plein air）的明快透气，莫奈式的户外写生`
- **推荐 input_fidelity**：0.55
- **适合**：风景、花园、河畔

### 32. 表现主义厚涂人像（Expressionist Impasto Portrait）★ 用户定稿
- **来源**：2026-10-11 实测调参得出（用户以「原图感太强、油画感不够」为起点，三轮迭代定稿）
- **关键词**：expressionist impasto, semi-abstract, reinvent not trace, simplified flat planes, palette-knife slabs, raised pigment ridges, fauve colour, anti-photograph
- **术语锚点**：**Expressionism（表现主义）**｜**Fauvism／fauve（野兽派／野兽派色彩）**｜impasto｜palette-knife slab（刮刀色板）｜flat plane（平涂块面）
- **核心心法（三条，缺一不可）**：
  1. **画家重新发明场景，而不是描照片** —— 明确舍弃照片的小特征、质感与完成度
  2. **形体简化为大面积平涂色块**，允许解剖被缩写与轻微变形（"笔触比解剖准确更重要"）
  3. **反照片铁律**：参考图只提供身份/姿态/配色/构图，其摄影细节不得在结果任何位置存活
- **硬性约束 · 天空笔触（2026-10-11 补充，用户反馈「天空褶皱不自然」）**：天空的厚涂必须**顺着天空自身的流动方向平缓推演** —— 舒展的长弧扫笔、层叠的水平色带、连贯而有方向感的颜料脊；**明确禁止**皱褶状、疙瘩状、结痂状、揉搓状、揉纸状的不自然色块堆积（这是本风格最易翻车处）
- **硬性约束 · 眼部焦点（2026-10-11 补充，用户反馈「眼部特写不细致」）**：眼睛是全画**最精细的焦点**，必须比面部任何其他区域更细 —— 虹膜与瞳孔的圆形轮廓明确、有清晰的高光点，眼睑、睫毛与眼周结构被细致刻画，眼神明亮有神；**绝不允许**眼睛糊成色块、失去焦点或与周围笔触同粗
- **提示词模板**：`一幅夸张的表现主义厚涂油画，出自大胆的现代画家之手——不是照片，不是给照片加油画滤镜。参考照片只提供身份、姿态与配色：画家重新发明这个场景，刻意舍弃摄影细节与完成度。整幅由粗犷可见的笔触构成：宽大的刮刀扫痕、凸起的颜料脊、刮擦出的平面与奔放的书写性笔触，画面处处是实打实的厚涂颜料堆积。形体被简化与夸张：形状概括为大面积平涂色块，弧线被推成粗犷的体块，次要细节直接消失，部分区域崩塌为纯粹的色块与色带；解剖可被缩写与轻微变形——画家的笔触比解剖准确更重要——但构图、姿态与整体剪影仍可辨认。反照片铁律：任何位置都不得残留摄影细节——无摄影级皮肤纹理、无毛孔、无镜头锐度、无单根发丝、无布料织纹、无虚化；即使最精细的段落也必须是可见的颜料。面部是全画最精细的区域，但仍由粗犷简化的色块构成：受光面是几块干净的暖色平面，阴影面是几块冷色平面；眼神保持灵动、笑容保留，但皮肤是平涂的色块与笔触，绝不是摄影质感；眼睛是全画最精细的焦点——虹膜与瞳孔的圆形轮廓明确、有清晰的高光点，眼睑、睫毛与眼周结构被细致刻画，眼神明亮有神，绝不糊成色块或失去焦点。头发是赭石、熟褐与红棕的整片扫笔；外套由宽笔触与刮刀刮出的青色与浅蓝色平面构成，明暗分界清晰。环境最抽象、最厚：天空变成一片电光蓝的厚涂色域，其笔触顺着天空的流动方向平缓推演——舒展的长弧扫笔与层叠的水平色带，颜料脊连贯而有方向感，绝不能形成皱褶状、疙瘩状、结痂状、揉搓状的不自然色块堆积；建筑立面简化为几条竖向刀痕，深色橱窗成为几块厚重的深色颜料板，路面是厚涂的暖色板块。色彩推向超自然的饱和——电光蓝、米白、赭石与熟褐、浅青、深藏青、暗栗——明快透气。层级明确：面部最精细 → 头发与衣物宽放 → 环境最抽象最厚。负面：不要摄影写实、不要照片加滤镜感、不要平滑油画滤镜、不要通篇同样大小的细笔触、不要浑浊脏色、不要浮雕雕塑感、不要黏土、不要蜡像、不要石膏、不要 3D 浅浮雕、不要颜料糊掉、不要丢笑容、不要文字水印`
- **推荐 input_fidelity**：**0.22**（用户定稿版：油画感强、形体夸张但人物仍可辨）｜**0.14**（更极端的抽象，天空仅剩几笔大扫痕）｜0.40（仍偏写实，不推荐）
- **强化次序（重要）**：`input_fidelity` 是这个风格的**唯一有效旋钮**。实测阶梯：`medium`=照片感 → `0.40/0.28`=明显油画但形体太老实 → `0.22`=半抽象 ✓ → `0.14`=夸张抽象
- **适合**：人像（首选）、街景、宠物
- **注意**：面部始终是全画最"实"的区域（为保身份可辨）。若要连脸也抽象化，需删掉"面部最精细/笑容保留"约束，但人物相似度会明显下降

---

## 七、编辑设计 · 纸刊与海报（重构版式型）

### 33. 厚涂油画·微缩风景明信片（Impasto Oil Micro-Landscape Poster）
- **来源**：社区流行的「Photo-to-zine-postcard / Impasto Oil Diptych」风格
- **关键词**：impasto oil painting, diptych poster, 50/50 split, miniature landscape, palette knife marks, sculptural volume, warm white negative space, editorial typography
- **术语锚点**：**impasto（厚涂）**｜palette knife（刮刀）｜miniature diorama（微缩景）｜negative space（留白）
- **提示词模板**：`把这张照片改造成一张竖版 3:4 的高级设计海报，画面严格上下各占 50%。上半部分保留原始照片，保持主体的身份、结构、姿态与真实质感，仅做轻微的画册级调色；下半部分提取主体最具辨识度的轮廓、姿态与叙事关系，重构成三维厚涂油画的微缩风景——不要照抄照片，而要重塑为精致、立体、有手工感的微缩世界，保留主体核心特征。构图为大面积留白 + 居中或略偏的对角主轴，置于米白色肌理艺术纸上，一条由原图主题色衍生的半透明厚涂色带托举主体（化作水面、地面、小径或光带），主体与色带通过倒影、涟漪、延展笔触自然融合。笔触强调厚涂油画、微缩实体感与透光感，可见颜料堆叠、刮刀痕、凸起颜料脊、不均匀边缘、纸张肌理与手工塑形，在水面、云、色带与高光处加重油彩。色彩从原照片最明亮、最有生命力的颜色中提取并重新调和，使用清透天蓝、湖蓝、浅绿、暖黄、珊瑚橙与蜜桃粉，冷暖对比和谐，大量暖白作呼吸空间，明亮而柔和，加入金色阳光与暖橙点缀，整体阳光、清新、治愈。背景极简通透，只有云、阳光、薄雾与空气感。文字为极简几何无衬线体英文短标题与少量小字注释，自然融入留白或色块。整体是高级收藏级编辑海报，上实拍下油画，明亮、宁静、有触感、当代。负面：不要拼贴、不要不等分割、不要浑浊廉价色、不要扁平插画、不要动漫、不要下半部分照抄照片、不要塑料感 CGI、不要贴纸感、不要过多文字、不要杂乱、不要水印与 logo`
- **推荐 input_fidelity**：0.5（该风格会**重构版式**，需要大改；仅想保留原构图时删去"上下各占 50%"相关句子）
- **适合**：风景、人像、宠物、建筑
- **注意**：属于「重构版式」型风格，输出与输入构图差异极大，出图前需让用户有预期

### 34. 拾景纸刊 · 实景拼贴（Gathered Scenes Zine v1.9）
- **来源**：Zeejay0/gathered-scenes-zine-skill（签名：**真景不改、同位简译、源色渐隐、艳色引路、颗粒消融**）
- **关键词**：flat-scanned paper poster, photographic anchor unchanged, registered illustration, guide color, torn fibre paper edge, grain dissolve
- **术语锚点**：photographic anchor（摄影锚点）｜registered illustration（同位简译）｜guide color（引导色）｜grain dissolve（颗粒消融）
- **结构（三层，必须清晰区分）**：① **摄影锚点** —— 原照片在保留区域内**完全不变**，保持真实摄影质感与细节；② **同位简译插画** —— 在纸上与原场景**同位置**的稀疏印刷式简译，用少量大形状概括体积与结构，色彩从原图派生并向纸张逐渐褪去；③ **引导色** —— 一条取自原图的高饱和线或紧凑色块，引导视线
- **提示词模板**：`把照片做成一张平铺扫描感的纸刊海报，保留三层且彼此清晰区分：① 摄影锚点——原照片在保留区域内完全不变，保持真实摄影质感与细节；② 同位简译插画——在纸上与原场景同位置的稀疏印刷式简译，用少量大形状概括体积与结构，色彩从原图派生并逐渐向纸张褪去；③ 引导色——一条取自原图的高饱和线或紧凑色块引导视线。手撕纤维纸边自然延伸，颗粒消融让插画与纸张融合，大面积留白，整体安静克制`
- **推荐 input_fidelity**：0.8（必须保住原图区域）
- **适合**：竖图、旅行照、主体关系清楚的场景
- **限制**：要求"原图区域像素级不变"，纯图生图只能近似，精准需后期合成
- **变体 · 影像蒸馏（Scene Distillation Zine v1.3）**：**不保留原照片**。只提取语义核心、情绪张力与视觉隐喻，用纸张、插画、色彩与自由文字重做一件**新的纸上作品**。提示词把上面第①层删掉，改为"把照片视为语义证据而非视觉图层，重新创作一张独立成立的艺术海报"。

### 35. 清新怀旧水彩手账（Soft Watercolor Journal）
- **关键词**：soft watercolor illustration, wet-on-wet wash, warm paper texture, pastel, journal layout, vertical serif title, dotted divider, nostalgic and fresh
- **术语锚点**：**wet-on-wet（湿画法）**｜journal layout（手账版式）｜dotted divider（点状分隔线）
- **提示词模板**：`整幅重绘为清新怀旧的水彩插画，湿画法晕染通透，水色叠加自然扩散，留白透气，暖白纸肌理明显；画风柔和治愈，配色为湖蓝、米白、浅草绿与少量砖红点缀；画面右侧留出竖向留白栏，以克制的衬线体写英文短标题与编号（如 "Reading by Windows / NO. 08"），配一条点状分隔线；整体像一页水彩日记 / 旅行手账`
- **推荐 input_fidelity**：0.45（整幅要重绘为水彩）
- **适合**：人像、静物、室内、旅行

### 36. 抽象编辑 · 记忆面板（Photo Abstract Editorial）
- **来源**：ZzzLc0405/photo-abstract-editorial
- **术语锚点**：abstract color field（抽象色域）｜minimal brushwork（极简笔触）｜editorial serif（编辑衬线体）
- **结构**：竖向编辑作品 = 上方**保留原照片**（不重画、不扩展、不修饰、不加滤镜） + 下方**象牙白抽象记忆面板**（用最少笔触重建照片的空间关系、结构节奏与色彩关系） + **2–5 词英文诗意标题**（仅置于面板，克制编辑衬线体）
- **硬约束**：人物只能用「不规则连续的短竖笔触」或「微锥形色块」表示，**绝不出现头、四肢、脸、衣物**；每个笔触都必须能追溯到原图的一个真实视觉事实；面板背景为平整连续的中性象牙白，**无渐变、无纸纹、无噪点、无阴影、无晕影**；照片与面板直接相接，无边框、无阴影、无拼贴、无样机效果
- **比例**：竖图 照片 55–68% / 面板 32–45%；横图 照片 38–52% / 面板 48–62%；近方形 48–58% / 42–52%；**不机械对半**
- **提示词模板**：`保留上传照片为原始影像（不重画、不扩展、不修饰、不加滤镜），置于画面上方；在下方象牙白面板上，仅根据照片本身的空间关系、结构节奏与色彩关系，用最少的笔触重建一个抽象记忆面板——色块、弧线、连续短竖笔触、层叠色带；每个笔触都要能追溯到原图的真实视觉事实；人物只用不规则的连续短竖笔触或微锥形色块表示，绝不画头、四肢、脸或衣物；提取原图的低饱和配色，大面积留白，避免装饰性与对称；在面板上以克制的编辑衬线体写一个 2–5 词的原创英文标题；照片区与面板直接相接，无边框、无阴影、无拼贴、无样机效果`
- **推荐 input_fidelity**：不适用（结构重排型）；照片区要求保真，纯图生图只能近似
- **适合**：人像、建筑、风景

### 37. 现代文学艺术杂志（Literary Modernism Editorial）★ 用户指定
- **来源**：2026-10-11 用户反馈「文艺杂志风太复古，我不仅仅要色调的改变，加点现代文学艺术的新东西」—— 遂新建本条目，作为 #1（Kinfolk 复古克制）的**当代对立面**
- **定位（关键）**：这**不是色调迁移风格**，而是**重构版式型** —— 保留主体为可辨识的摄影元素，但整页引入**现代主义文学与艺术的视觉语言**，让画面变成一页当代文学／艺术杂志的跨页
- **关键词**：literary magazine spread, modernist editorial design, constructivism, Bauhaus geometry, concrete poetry typography, collage, conceptual juxtaposition, asymmetric grid, serigraphy
- **术语锚点**：**Constructivism（构成主义）**｜**Bauhaus（包豪斯）**｜**concrete poetry（具体诗）**｜**asymmetric grid（非对称网格）**｜**serigraphy／screen print（丝网印）**｜**conceptual juxtaposition（概念性并置）**
- **三大现代文学艺术元素（必加，这正是与 #1 的本质差别）**：
  1. **构成主义／包豪斯几何**：细直线、正圆、矩形色块与对角线分割，几何元素与照片**交叠咬合**而非并列
  2. **现代诗排版**：以**小号衬线体或等宽字体**错落排布几行诗性短句（可竖排、可断行、可只留半个词），像一页具体诗；**文字是构图的一部分**，不是说明文字
  3. **概念性并置**：把主体的某个元素**抽离并放大**为抽象符号（一滴水、一张票根、一段光斑），与主体形成超现实对话
- **参照物**：**埃尔·利西茨基《用红色楔子击打白色》** ／ 包豪斯刊物与莫霍利-纳吉的构成 ／ 当代独立文学杂志（Granta、The Paris Review 当代封面）／ 汉斯·阿尔普的拼贴
- **配色**：象牙白／米白纸底 + 黑白 + **一抹高饱和强调色**（克莱因蓝或朱红，**仅一处，点到为止**）；丝网印的平涂质感与轻微套色偏移
- **构图**：非对称网格 + 大面积留白；照片以**几何裁切**嵌入（直角、正圆窗口或斜切），与几何色块咬合
- **提示词模板**：`把这张照片重构成一页当代文学艺术杂志的跨页版式（现代主义编辑设计）：保留主体为可辨识的摄影元素，以几何裁切（直角、正圆窗口或斜切）嵌入版面；整页引入现代主义艺术语言——构成主义与包豪斯的几何元素（细直线、正圆、矩形色块、对角线分割），几何形状与照片交叠咬合而非并列；以克制的现代诗排版错落排布几行诗性短句（小号衬线体或等宽字体，可竖排、可断行、可只留半个词），文字作为构图的一部分自然融入留白；把主体的一个元素抽离放大为抽象符号（一滴水、一张票根或一段光斑），与主体形成概念性的超现实并置；非对称网格与大面积留白，画面安静而有智性；配色为象牙白纸底加黑白，仅用一抹克莱因蓝或朱红作强调；丝网印的平涂质感与轻微套色偏移，纸张肌理清晰；整体是当代独立文学杂志的编辑设计，现代、克制、有观念性；保持人物五官特征与笑容可辨；不要复古怀旧色调，不要泛黄做旧，不要田园小清新，不要浓艳多彩，不要廉价滤镜感，不要文字水印，不要额外肢体，不要变形`
- **推荐 input_fidelity**：**0.45**（需要模型敢于重构版式并加入几何与文字；属"结构调整较大"的一档）｜0.6（更保照片，几何与排版会显得像贴纸）
- **与 #1 文艺杂志风的分工**：**#1 = 复古克制的色调迁移（Kinfolk）**；**#37 = 当代观念的版式重构（构成主义 + 现代诗 + 拼贴）** —— 用户嫌 #1 太复古时直接切 #37
- **适合**：人像、街景、静物、建筑
- **避免**：不要复古怀旧、不要泛黄做旧、不要柔光小清新、不要浓艳撞色、不要廉价滤镜感、不要对称呆板的居中排版

---

## 八、印刷 · 平面 · 装饰艺术

> v4 新增（38–43）。共同点：**用"印刷／雕刻的工艺语言"重做画面**，而不是换一种绘画笔触。
> 这类风格的辨识度来自**工艺痕迹**（套印偏移、凿痕、排线），提示词里必须把这些痕迹写实。

### 38. 装饰艺术（Art Deco）
- **关键词**：Art Deco, gilded geometry, stepped form, symmetry, machine-age, polished metal, lacquer, Chrysler Building
- **术语锚点**：**gilded geometry（镀金几何）**｜stepped form（阶梯式收分）｜axial symmetry（中轴对称）｜lacquer（漆面）｜sunburst（放射日纹）
- **参照物**：克莱斯勒大厦／帝国大厦的装饰语汇；塔玛拉·德·兰碧卡（Tamara de Lempicka）的人物画
- **提示词模板**：`装饰艺术（Art Deco）风格，镀金几何纹样（gilded geometry）与阶梯式收分造型，严格的中轴对称构图，黑、金与祖母绿配色，抛光金属与漆面的光泽，放射日纹（sunburst）与扇形装饰，机械时代的装饰语汇，平整的装饰性块面，整体像一张上世纪二十年代的装饰艺术海报；保持主体五官、姿态与构图不变`
- **推荐 input_fidelity**：0.6
- **适合**：人像、建筑、产品
- **避免**：不要巴洛克式繁复曲线、不要柔和粉彩、不要卡通化、不要 3D 渲染感

### 39. 新艺术运动（Art Nouveau）
- **关键词**：Art Nouveau, whiplash curve, sinuous line, ornamental border, Alphonse Mucha, muted pastel, decorative panel
- **术语锚点**：**whiplash curve（鞭形曲线）**｜sinuous line（蜿蜒线）｜ornamental border（装饰边框）｜decorative panel（装饰画板）
- **参照物**：**阿尔丰斯·穆夏（Alphonse Mucha）**、奥布里·比亚兹莱；吉马尔设计的巴黎地铁入口
- **提示词模板**：`新艺术运动（Art Nouveau）风格，穆夏式的装饰画板构图，蜿蜒的鞭形曲线（whiplash curve）与植物卷草纹样环绕主体，粗细分明的装饰性轮廓线，米黄、灰绿与暗金的柔和配色，平涂色块上加微妙的水彩渐变，画面上方或下方留出对称的装饰边框与留白区；保持主体五官与姿态可辨`
- **推荐 input_fidelity**：0.6
- **适合**：人像、花卉、海报
- **避免**：不要硬朗几何、不要赛博霓虹、不要照片写实、不要现代扁平化

### 40. 包豪斯海报（Bauhaus Poster）
- **关键词**：Bauhaus, geometric abstraction, primary colour triad, grid system, photomontage, Moholy-Nagy, functionalism
- **术语锚点**：**geometric abstraction（几何抽象）**｜primary colour triad（原色三色）｜grid system（网格系统）｜photomontage（摄影拼贴）
- **参照物**：莫霍利-纳吉与赫伯特·拜耶的包豪斯刊物；德绍包豪斯时期的展览海报
- **提示词模板**：`包豪斯（Bauhaus）平面海报风格，几何抽象与网格系统（grid system），红黄蓝原色与黑灰，粗壮的无衬线字体沿斜轴排布，主体以摄影局部拼贴（photomontage）的方式嵌入几何色块，正圆、矩形与 45° 对角线分割画面，纸张平印质感，理性、功能主义、现代主义；保持主体五官可辨`
- **推荐 input_fidelity**：0.5
- **适合**：人像、产品、建筑
- **避免**：不要装饰性曲线、不要泛黄做旧、不要柔和渐变、不要廉价复古滤镜
- **与 #37 的分工**：**#40 = 纯平面设计语言（原色几何 + 网格）**；**#37 = 文学杂志观念版式（构成主义 + 现代诗 + 一抹强调色）**。要"纯海报"选 40，要"有文字与观念"选 37

### 41. 孔版印刷（Risograph）
- **关键词**：risograph, spot ink, overprint, misregistration, fluorescent pink, duotone, textured paper, grainy ink
- **术语锚点**：**spot ink（专色油墨）**｜overprint（叠印）｜misregistration（套印偏移）｜duotone（双色印刷）
- **参照物**：Risograph 印刷的独立杂志、演出海报与小报
- **提示词模板**：`孔版印刷（Risograph）风格，仅用两三种专色油墨（荧光粉、亮蓝、黑）依次套印叠加，可见明显的套印偏移与错位，油墨颗粒粗粝、实地有细微斑驳与不均匀，纸张纤维与轻微透印，高对比平涂、几乎没有渐变，像一张独立出版社的 Risograph 演出海报；保持主体五官与构图不变`
- **推荐 input_fidelity**：0.5
- **适合**：人像、图形、海报
- **避免**：不要四色全彩、不要光滑渐变、不要 3D 质感、不要精确对齐（错位正是特征）

### 42. 木刻版画（Woodcut）
- **关键词**：woodcut, relief print, gouge marks, carved line, black and white, hatching, limited ink
- **术语锚点**：**relief print（凸版）**｜gouge mark（凿痕）｜carved line（刻线）｜linocut（麻胶版）
- **参照物**：凯绥·柯勒惠支的木刻；德国表现主义版画
- **提示词模板**：`木刻版画（woodcut）风格，凸版印刷的雕刻语言，粗犷有力的刻线与凿痕（gouge mark），刀口转折明确、保留木纹与刻痕的粗糙手感，以密集排线塑造明暗，黑处为浓墨、白处为纸的留白，仅用黑白或极少的套色，边缘凌厉、无灰阶渐变；保持主体五官与姿态可辨`
- **推荐 input_fidelity**：0.55
- **适合**：人像、动物、风景
- **避免**：不要写实光影、不要柔和平滑、不要彩色渐变
- **与 #9 浮世绘的区别**：#9 是**日本**套色木版（平涂色块 + 装饰纹样），#42 是**单色凸版的雕刻线条**（靠刻线造体积），不要混用参照物

### 43. 钢版雕刻（Intaglio Engraving / 纸币雕版线）
- **关键词**：intaglio engraving, fine line, cross-hatched hatching, banknote engraving, guilloche, currency portrait, steel plate
- **术语锚点**：**intaglio（凹版）**｜**cross-hatched hatching（交叉细排线）**｜**guilloche（扭索饰纹）**｜line engraving（线刻）
- **参照物**：纸币与邮票上的**钢版雕刻人像**；旧证券、护照上的雕版线
- **提示词模板**：`钢版雕刻（intaglio engraving）风格，纸币人像式的极细线刻（fine line engraving），全部明暗与体积由密到可见的平行与交叉细线（cross-hatched hatching）构成，线条纤细均匀、方向随形体流转，单色墨印在棉纸上，背景加入扭索饰纹（guilloche）与同心细线环，边缘有雕版压痕；保持主体五官与姿态准确可辨`
- **推荐 input_fidelity**：**0.75**（线条要密而准，太低会把五官刻糊）
- **适合**：人像、建筑、纹章类题材
- **避免**：不要色块、不要粗黑轮廓、不要写实皮肤质感

---

## 九、艺术流派 · 观念

> v4 新增（44–48）。这一类靠**艺术史中的某个"观念"**取胜，而不是靠材质。
> 提示词里除了术语，**必须点出该流派的核心机制**（点彩的视觉混合、超现实的错置、欧普的视觉振动）。

### 44. 点彩派（Pointillism / Divisionism）
- **关键词**：pointillism, divisionism, Seurat, optical colour mixing, complementary contrast, en plein air
- **术语锚点**：**pointillism（点彩）**｜**divisionism（分色主义）**｜optical mixing（视觉混合）｜complementary contrast（补色对比）
- **参照物**：**乔治·修拉（Georges Seurat）**《大碗岛的星期天下午》；保罗·西涅克
- **提示词模板**：`点彩派（pointillism / divisionism）风格，整幅由小而均匀的纯色圆点密集并置构成，不预先调色、依靠视觉混合（optical mixing）产生色彩，暖冷互补色点相邻堆叠形成光感与体积，外光写生下明快跳跃的空气感，近看是无数色点、远看形体清晰，像修拉式的点彩油画；保持主体轮廓、五官与构图不变`
- **推荐 input_fidelity**：0.5
- **适合**：风景、人物、水岸
- **避免**：不要平滑笔触、不要厚涂刮刀痕、不要清晰单一的黑边线
- **与 #31 印象派厚涂的区别**：#31 是**碎笔触（短线块）**，#44 是**纯色圆点**；两者都属印象派谱系，但笔触单位不同

### 45. 超现实主义（Surrealism）
- **关键词**：surrealism, Dali, Magritte, impossible juxtaposition, dream logic, hyperreal texture, uncanny scale
- **术语锚点**：**surrealism（超现实主义）**｜**impossible juxtaposition（不可能并置）**｜dream logic（梦境逻辑）｜uncanny scale（异常比例）
- **参照物**：**达利（Dalí）**、**马格利特（Magritte）**
- **提示词模板**：`超现实主义（Surrealism）风格，达利与马格利特式的梦境逻辑（dream logic）：主体以照相级的写实质感（hyperreal texture）呈现，却被置于不可能的并置（impossible juxtaposition）之中——悬浮、错置或异常比例（uncanny scale），背景为无垠空旷的荒原或绝对静默的室内，柔和却带方向性的戏剧光，长时间曝光般的绝对静止，画面安静而令人不安；保持主体五官特征与姿态不变`
- **推荐 input_fidelity**：0.6
- **适合**：人像、静物、建筑
- **避免**：不要卡通化、不要赛博霓虹、不要随手拼贴的廉价感、不要恐怖惊悚向

### 46. 欧普艺术（Op Art）
- **关键词**：Op Art, optical illusion, Bridget Riley, moiré, high-contrast black and white, vibrating line, geometric repetition
- **术语锚点**：**Op Art（欧普艺术）**｜**moiré（摩尔纹）**｜optical vibration（视觉振动）｜geometric repetition（几何重复）
- **参照物**：**布里奇特·赖利（Bridget Riley）**、维克托·瓦萨雷里
- **提示词模板**：`欧普艺术（Op Art）风格，布里奇特·赖利式的视觉振动（optical vibration）：高对比的黑白或极少色相的细密几何条纹与波浪线重复排列，透过疏密与曲率的变化在平面上制造起伏、扭曲与摩尔纹（moiré），主体被这些条纹重新包裹与塑形，画面严格平面、无光影，注视久了产生眩晕感；保持主体轮廓与姿态可辨`
- **推荐 input_fidelity**：0.45
- **适合**：人像、图形、建筑
- **避免**：不要立体光影、不要柔和渐变、不要涂鸦式随意、不要彩色多色相

### 47. 湿壁画（Fresco）
- **关键词**：fresco, buon fresco, plaster ground, cracked surface, earth pigments, matte, Renaissance wall
- **术语锚点**：**buon fresco（湿壁画）**｜plaster ground（灰泥底）｜earth pigment（矿物土色）｜craquelure（龟裂）
- **参照物**：乔托、拉斐尔签字厅壁画；庞贝壁画
- **提示词模板**：`湿壁画（fresco）风格，在石灰灰泥（plaster ground）上作画，使用矿物土色颜料——赭石、土红、橄榄绿与灰蓝，完全哑光，色彩因渗入灰泥而略显粉化柔和，墙面有斑驳的龟裂（craquelure）、剥落与岁月污渍，笔触宽而肯定、不做细腻过渡，仿佛教堂或宫殿里的一面古老墙壁；保持主体五官与姿态可辨`
- **推荐 input_fidelity**：0.6
- **适合**：人像、古典／宗教题材、风景
- **避免**：不要油画光泽、不要现代高饱和、不要无瑕的数码平滑、不要做旧滤镜式的假泛黄

### 48. 教堂花窗（Stained Glass）
- **关键词**：stained glass, leaded glass, backlit, jewel tones, black lead lines, gothic window, luminous
- **术语锚点**：**leaded glass（铅条镶嵌玻璃）**｜backlight（背光穿透）｜jewel tone（宝石色）｜grisaille（灰色单彩玻璃）
- **参照物**：沙特尔大教堂、巴黎圣母院的玫瑰花窗
- **提示词模板**：`教堂彩绘花窗（stained glass）风格，主体由一块块彩色玻璃（leaded glass）拼合而成，粗黑的铅条勾勒每一块的轮廓与内部结构，强烈的背光穿透玻璃，宝石般的钴蓝、血红、琥珀与祖母绿发出通透的光，玻璃内部可见气泡、流纹与厚薄不均造成的深浅变化，整体嵌在石砌的哥特式窗框之中；保持主体轮廓、五官位置与构图不变`
- **推荐 input_fidelity**：0.55
- **适合**：人像、宗教题材、建筑
- **避免**：不要写实光影、不要霓虹管发光质感、不要平滑渐变
- **与 #29 霓虹玻璃的区别**：#29 是**现代霓虹管 + 玻璃折射**（通透、冷、未来感）；#48 是**铅条分割的彩色玻璃拼块**（有黑线骨架、暖、宗教感）

---

## 十、材质与手作

> v4 新增（49–50）。核心是**把画面换成一种真实的物理材料**，成败取决于"材料的微观痕迹"是否写实。

### 49. 手工刺绣（Embroidery）
- **关键词**：embroidery, satin stitch, counted thread, visible weave, raised texture, silk floss, hand-stitched
- **术语锚点**：**satin stitch（缎面绣）**｜**counted thread（数纱绣）**｜silk floss（丝光线）｜raised texture（浮雕质感）
- **参照物**：中式苏绣；法式高定刺绣（Lesage 工坊）
- **提示词模板**：`手工刺绣（embroidery）风格，整幅由丝线绣成——缎面绣（satin stitch）的平行线走向铺满色块，数纱绣（counted thread）的短针构成细部，丝线有清晰的捻向与柔和光泽，光线下形成细微的明暗起伏与浮雕质感（raised texture），底布为可见经纬的亚麻或丝绸，针脚边缘留有自然的线头与轻微不平整；保持主体五官、姿态与构图可辨`
- **推荐 input_fidelity**：0.5
- **适合**：人像、花卉、静物
- **避免**：不要平滑印刷感、不要写实摄影质感、不要塑料或金属光泽、不要针织毛衣感（那是粗针织物，不是刺绣）

### 50. 大理石雕塑（Marble Sculpture）
- **关键词**：marble sculpture, carved stone, chisel marks, Carrara marble, subsurface scattering, museum lighting, monochrome white
- **术语锚点**：**Carrara marble（卡拉拉大理石）**｜chisel mark（凿痕）｜subsurface scattering（次表面散射）｜drapery fold（衣褶）
- **参照物**：米开朗基罗、贝尼尼的巴洛克大理石像
- **提示词模板**：`大理石雕塑（marble sculpture）风格，主体被雕刻成一尊卡拉拉（Carrara）白色大理石的立体雕像，石面经打磨而温润，边缘与转折处留有细密的凿痕（chisel mark），皮肤与衣物呈现石头特有的半透散射（subsurface scattering）与柔和过渡，衣物褶皱被固化为厚重的石褶（drapery fold），美术馆式的顶部柔光配深色背景衬托，整体洁白、庄重、永恒；保持主体姿态、五官结构与构图不变`
- **推荐 input_fidelity**：0.6
- **适合**：人像、半身像、动物
- **避免**：不要彩色、不要彩绘雕塑、不要塑料或 3D 打印质感、不要石膏的粉白死板感

---

## 十一、东亚传统

> v5 新增（51–57）。共同点：**用东亚传统书画／器物的"媒介语言"重做画面**——纸、绢、矿彩、单色墨线、釉下青花、金线。
> 辨识度来自三件事：**① 单色或极克制的色域 ② 明确的"载体"（绢本、宣纸、瓷胎、墙面、棉布）③ 装饰性的平面秩序**。
> ⚠️ 提示词里**必须把"载体"写出来**（绢本设色 / 宣纸 / 瓷胎 / 泥壁），否则模型只会给一层"中国风滤镜"。

### 51. 工笔重彩（Gongbi）
- **关键词**：gongbi, fine-line brushwork, mineral pigment, silk ground, meticulous, layered flat colour, iron-wire line
- **术语锚点**：**gongbi（工笔）**｜fine-line brushwork（细线勾勒）｜mineral pigment（矿物颜料：石青／石绿／朱砂／蛤白）｜silk ground（绢本）｜**iron-wire line（铁线描）**
- **参照物**：唐宋院体工笔（《簪花仕女图》《捣练图》《韩熙载夜宴图》）；于非闇、陈之佛的现代工笔
- **提示词模板**：`中国工笔画（gongbi）风格，绢本设色，以细而匀的墨线勾勒轮廓（细线勾勒、铁线描），轮廓内用石青、石绿、朱砂、蛤白等矿物颜料层层积染（三矾九染）而成，色块平整明净、边缘利落，几乎不见笔触；衣纹以流畅的游丝描组织，发丝与眉眼刻画精细、根根分明；背景为纯色绢地或极简的折枝花石，大量留白；整体工整、雅致、设色明快而不艳；保持主体五官、姿态与构图不变`
- **推荐 input_fidelity**：0.55
- **适合**：人像、花卉、禽鸟
- **避免**：不要写意飞白、不要油画笔触与厚涂、不要写实摄影质感、不要西式透视与强投影

### 52. 青绿山水（Blue-Green Landscape）
- **关键词**：blue-green landscape, qinglu shanshui, mineral azurite and malachite, gold outline, silk ground, decorative mountain forms
- **术语锚点**：**qinglu shanshui（青绿山水）**｜mineral azurite & malachite（石青／石绿）｜**gold outline（泥金勾线）**｜decorative stylised mountain（装饰化山形）
- **参照物**：王希孟《千里江山图》；展子虔《游春图》；《江山秋色图》
- **提示词模板**：`中国青绿山水画风格，以石青、石绿等矿物颜料敷色，绢本设色；山形被概括为装饰性的层叠体块，山石轮廓与结构线以泥金勾提（gold outline），山顶与坡脚的石青由浓到淡自然过渡（赭石打底、青绿罩染）；云气以留白与淡粉渲染表现，水面留白或施极淡的花青；色彩明丽厚重、沉着而不俗；保持主体位置与整体构图可辨`
- **推荐 input_fidelity**：0.5
- **适合**：风景、建筑、人物（作为点景）
- **避免**：不要水墨写意、不要西式光影与透视、不要照片质感、不要油画的厚涂肌理

### 53. 白描（Baimiao）
- **关键词**：baimiao, outline drawing, single-colour ink line, no shading, iron-wire line, silkworm-thread line, calligraphic rhythm
- **术语锚点**：**baimiao（白描）**｜**iron-wire line（铁线描）**｜**silkworm-thread line（游丝描）**｜no shading（不施墨色）
- **参照物**：李公麟白描；《八十七神仙卷》；陈洪绶的人物线描；《朝元仙仗图》
- **提示词模板**：`中国白描（baimiao）风格，仅以单色墨线勾勒物象，完全不用明暗与色块；线条为铁线描／游丝描一路，粗细有致、起收有顿挫，行笔有书法般的节律与呼吸感；衣纹的转折与叠压交代清楚，密处不闷、疏处不空；背景留白，仅在必要处以极淡的墨色略作点染；保持主体五官、姿态与构图准确可辨`
- **推荐 input_fidelity**：**0.7**（全靠线条承载形体，压太低五官会走形）
- **适合**：人像、衣纹、花鸟
- **避免**：不要任何色块与明暗、不要交叉排线（那是 #8 素描／#24 美漫）、不要石墨的粗颗粒、不要照片质感

### 54. 敦煌壁画（Dunhuang Mural）
- **关键词**：Dunhuang mural, cave painting, mineral pigment, oxidised colour, flying apsara, decorative border band, weathered wall
- **术语锚点**：mineral pigment（矿物颜料：石青／石绿／土红／铅丹）｜**oxidised／darkened flesh（变色发黑的肤色）**｜decorative border band（装饰边饰）｜**flying apsara（飞天）**
- **参照物**：莫高窟第 220、285、320 窟；榆林窟；克孜尔石窟
- **提示词模板**：`敦煌壁画风格，矿彩重彩绘制在粗粝的泥壁之上：土红、石青、石绿与蛤白平涂，线条为遒劲的墨线或土红线，形体略带稚拙的装饰性夸张；部分颜色因千年氧化而变黑变暗（尤其是人体的肤色），壁面遍布剥落、裂纹与烟熏的斑驳痕迹；画面四周环绕联珠纹、卷草纹或忍冬纹的装饰边饰；人物有飘带翻卷、动势飞扬的飞天感；保持主体五官与姿态可辨`
- **推荐 input_fidelity**：0.5
- **适合**：人像、群像、装饰题材
- **避免**：不要平滑无瑕的数字感、不要现代高饱和实色、不要西式明暗造型、**不要干净崭新的壁画**（风化与剥落是本体特征之一）

### 55. 青花瓷（Blue-and-White Porcelain）
- **关键词**：blue-and-white porcelain, underglaze cobalt, qinghua, ceramic glaze, Ming style, banded border, crackle
- **术语锚点**：**underglaze cobalt（釉下钴蓝）**｜glaze（釉面）｜**crackle／craquelure（开片冰裂）**｜banded border（弦纹边饰）｜窑变晕散（kiln drift）
- **参照物**：元青花（萧何月下追韩信梅瓶）；明永宣青花；克拉克瓷
- **提示词模板**：`青花瓷（blue-and-white porcelain）风格，画面以釉下钴蓝单色绘制在洁白的瓷胎上：蓝料浓处发深沉的黑蓝、淡处呈清透的灰蓝，全画只有白底与蓝料两色；笔触为勾线与分水相结合的瓷绘语言，浓淡层次分明、有分水的自然积边；主体外围绕以弦纹、缠枝莲、回纹或云肩式开光的边饰带；釉面有温润的反光与细密的开片冰裂（crackle），边缘可见窑变的轻微晕散；保持主体轮廓、五官与构图不变`
- **推荐 input_fidelity**：0.5
- **适合**：静物、花鸟、人像（作为器物纹样）
- **避免**：不要多色、不要油画笔触、不要纸质肌理、不要现代摄影的镜面高光

### 56. 唐卡（Thangka）
- **关键词**：thangka, Tibetan Buddhist scroll painting, mineral pigment, gold line, flat symbolic composition, brocade mount, mandala
- **术语锚点**：mineral pigment（矿物颜料）｜**gold line（金线勾勒）**｜flat symbolic composition（平面象征性构图）｜brocade mount（锦缎装裱）｜mandala（坛城图式）
- **参照物**：西藏与热贡唐卡；坛城（mandala）；藏传佛教卷轴画
- **提示词模板**：`藏传佛教唐卡（thangka）风格，矿物颜料绘于棉布（棉布画心）之上：石青、石绿、朱红、金与蛤白高度饱和而庄重；人物轮廓与衣纹以金线勾提（gold line），形体端正对称、比例程式化，平面化处理、不设透视与投影；背光、莲座、卷草与祥云等象征性元素环绕主体，构图严密对称、装饰性极强；四周为锦缎装裱式的边框；保持主体五官位置与整体姿态可辨`
- **推荐 input_fidelity**：0.5
- **适合**：人像、宗教题材、装饰画
- **避免**：不要写实光影、不要随手涂鸦感、不要现代矢量扁平的简化、不要低饱和灰调

### 57. 金石拓片（Stele Rubbing）
- **关键词**：stele rubbing, ink rubbing, stone carving, uneven inking, paper pressed into grooves, weathered stone, epigraphy
- **术语锚点**：**ink rubbing（拓本）**｜relief carving（阳文／阴文刻）｜uneven inking（拓墨不匀）｜paper into the groove（纸入凹槽）｜碑刻崩口（chipped edge）
- **参照物**：汉碑与北朝造像记的拓本；秦砖汉瓦拓片；汉画像砖拓片
- **提示词模板**：`金石拓片（stele rubbing）风格，画面如同从一块风化石碑上拓下：宣纸被压入凹刻的线条之中，凸起处着墨、凹处留白，墨色浓淡不匀、有斑驳的飞白与漏拓；石面的裂纹、剥落与风化痕迹一并留在纸上，边缘为不规则的纸边；字口与线条因石刻而方硬有力、转折处略见崩口；整体为纯黑与纸白的单色，古拙、厚重、有金石气；保持主体轮廓与五官可辨`
- **推荐 input_fidelity**：0.55
- **适合**：人像、纹样、文字类题材
- **避免**：不要柔和渐变、不要彩色、**不要木刻的刀痕感（那是 #42 木刻版画）**、不要均匀干净的印刷效果

---

## 十二、西方艺术史经典

> v5 新增（58–65）。这一类从**西方艺术史的某个具体时期／流派**取语言。
> 与第八节（印刷工艺）、第九节（观念流派）的分工：这里拼的是**造型与色彩体系**，
> 提示词要点出**该时期特有的形体处理方式与用光方式**，而不是只写一个流派名。

### 58. 拜占庭马赛克（Byzantine Mosaic）
- **关键词**：Byzantine mosaic, tessera, gold ground, hieratic frontal pose, smalti, Ravenna, icon
- **术语锚点**：**tessera（马赛克镶嵌小块）**｜**gold ground（金底）**｜hieratic frontal（正面端坐的圣像程式）｜smalti（玻璃马赛克料）｜灰缝（grout line）
- **参照物**：拉文纳圣维塔莱教堂《查士丁尼与侍从》；圣索菲亚大教堂；克里特圣像画
- **提示词模板**：`拜占庭马赛克（Byzantine mosaic）风格，整幅由无数细小的方形马赛克小块（tessera）拼成，块与块之间留有灰缝、角度略有偏斜因而表面起伏闪烁；背景为整片耀眼的金底（gold ground）；人物呈正面对称端坐的圣像程式（hieratic frontal），五官大而沉静、目光平视，衣褶被归纳为程式化的折线；色彩为金、深蓝、翠绿、朱红与白，庄重肃穆、超越时间；保持主体五官位置与姿态可辨`
- **推荐 input_fidelity**：0.5
- **适合**：人像、宗教题材、装饰
- **避免**：不要写实光影、不要 3D 渲染、不要平滑渐变、不要现代摄影质感

### 59. 中世纪手抄本（Illuminated Manuscript）
- **关键词**：illuminated manuscript, gold leaf, vellum, decorated initial, marginalia, tempera, gothic
- **术语锚点**：**gold leaf（金箔贴饰）**｜vellum（羊皮纸）｜**decorated initial（装饰首字母）**｜marginalia（页边装饰）｜historiated initial（故事首字母）
- **参照物**：《凯尔斯书》；林堡兄弟《贝里公爵的豪华时祷书》；《温切斯特圣经》
- **提示词模板**：`中世纪泥金装饰手抄本（illuminated manuscript）风格，画在泛黄的羊皮纸（vellum）上；主体被置于一个华丽的装饰首字母或藤蔓式边框之内，边框由金箔贴饰（gold leaf）、红蓝矿物颜料与细密的藤蔓卷叶纹组成；人物造型平面化、比例稚拙、姿态程式化，以蛋彩（tempera）平涂并用金线勾提；纸面可见虫蛀、水渍与磨损，页边点缀小花与小走兽的页边装饰（marginalia）；保持主体五官与姿态可辨`
- **推荐 input_fidelity**：0.5
- **适合**：人像、纹章、装饰画
- **避免**：不要写实透视、不要现代扁平插画、不要数码渐变、不要靠滤镜硬做的假泛黄

### 60. 维米尔式室内光（Vermeer Interior Light）
- **关键词**：Vermeer, Dutch Golden Age, north light, quiet interior, ultramarine and ochre, camera obscura softness, domestic stillness
- **术语锚点**：**north light（北向窗光）**｜ultramarine（群青）｜ochre（赭黄）｜camera obscura softness（暗箱式的柔焦）｜quiet interior（静默室内）
- **参照物**：**约翰内斯·维米尔（Johannes Vermeer）**《戴珍珠耳环的少女》《倒牛奶的女仆》；彼得·德·霍赫
- **提示词模板**：`荷兰黄金时代的室内油画风格，维米尔式的左向柔和窗光（north light）从画面一侧斜射进来，在墙面与人物上形成细腻的明暗过渡与淡淡的柔焦（暗箱式的柔焦）；色彩为温润的赭黄、土红与沉稳的群青（ultramarine），颜料有细微的颗粒与珍珠般的柔光；空间安静、时间仿佛静止，人物姿态含蓄内敛，背景为简洁的室内墙面与少量静物；保持主体五官特征、姿态与构图不变`
- **推荐 input_fidelity**：0.55
- **适合**：人像、室内、静物
- **避免**：不要戏剧化的硬光与深黑背景（那是 #61 巴洛克）、不要高饱和、不要现代摄影的锐利、不要厚涂刮刀痕

### 61. 巴洛克（Baroque）
- **关键词**：Baroque, Caravaggio, tenebrism, dramatic diagonals, theatrical light, rich drapery, chiaroscuro
- **术语锚点**：**tenebrism（暗色调主义）**｜**chiaroscuro（明暗对照）**｜diagonal composition（对角构图）｜theatrical gesture（戏剧化姿态）
- **参照物**：**卡拉瓦乔（Caravaggio）**、鲁本斯、伦勃朗、贝尼尼
- **提示词模板**：`巴洛克（Baroque）油画风格，卡拉瓦乔式的暗色调主义（tenebrism）：全画沉浸在深重的暗部之中，一束强烈的戏剧光从侧上方斜射，把主体从漆黑里"切"出来；背景几乎全黑，明暗交界极其锐利；构图沿对角线展开，姿态富有舞台感与动势；衣着为厚重华丽的织物，褶皱丰盈，色彩浓郁（深红、金褐、墨绿、铅白），笔触奔放；保持主体五官特征与整体姿态可辨`
- **推荐 input_fidelity**：0.55
- **适合**：人像、群像、静物
- **避免**：不要平光、不要明亮通透的均匀照明（那是 #60 维米尔）、不要低饱和灰调、不要现代照片的干净背景
- **与 #5 油画风的分工**：#5 是**通识的古典油画技法**（厚涂 + 罩染），不锁定时代；**#61 特指巴洛克的舞台式用光与对角动势**——暗部更重、光更硬。要"美术馆里的油画"用 **5**，要"戏剧性的深黑对比"用 **61**

### 62. 洛可可（Rococo）
- **关键词**：Rococo, pastel palette, fête galante, rocaille, asymmetric ornament, silky fabric, light-hearted
- **术语锚点**：**fête galante（雅宴画）**｜pastel palette（粉彩调）｜**rocaille（贝壳涡卷装饰）**｜asymmetric ornament（非对称装饰）
- **参照物**：**华托（Watteau）**、**布歇（Boucher）**、弗拉戈纳尔；凡尔赛的小特里亚农宫
- **提示词模板**：`洛可可（Rococo）风格，柔美轻盈的粉彩调（pastel palette）——粉红、淡蓝、薄荷绿、奶油白与浅金；光线明亮而漫射，画面轻松愉悦、带贵族式的闲适；人物衣着为丝绸与缎带，褶皱柔软流转、有细密的反光；背景点缀贝壳涡卷（rocaille）与缠枝纹样的非对称装饰，可浅淡地融入画面边缘；笔触轻柔、色彩清透；保持主体五官特征与姿态不变`
- **推荐 input_fidelity**：0.55
- **适合**：人像、风景、静物
- **避免**：不要深黑暗部、不要硬光、不要高饱和原色、不要粗犷的厚涂笔触

### 63. 立体主义（Cubism）
- **关键词**：Cubism, geometric fragmentation, simultaneous viewpoints, analytic cubism, faceted planes, ochre and grey
- **术语锚点**：**analytic cubism（分析立体主义）**｜**faceted plane（切面）**｜**simultaneous viewpoint（多视点并置）**｜papier collé（拼贴）
- **参照物**：**毕加索（Picasso）**与**布拉克（Braque）**的 1910–1913 时期；胡安·格里斯
- **提示词模板**：`立体主义（Cubism）风格，主体被拆解为无数几何切面（faceted plane），同时从多个视点并置呈现（simultaneous viewpoint）——正脸与侧脸、正面与俯视在同一画面里交叠；轮廓被打散又重新咬合，形体在画面上摊平、悬浮、相互穿插；色彩极度克制，只用赭石、灰、褐、橄榄绿与黑，几乎不表现体积与光源；保留画布的粗织肌理与断续的笔触；保持主体的关键身份特征（发色、服装、姿态）可辨`
- **推荐 input_fidelity**：0.4
- **适合**：人像、静物、乐器
- **避免**：不要写实光影、不要柔和渐变、不要单一视点、不要明快高饱和

### 64. 抽象表现主义 · 行动绘画（Action Painting）
- **关键词**：Abstract Expressionism, action painting, Jackson Pollock, drip and splatter, all-over composition, gestural
- **术语锚点**：**action painting（行动绘画）**｜**drip technique（滴洒法）**｜**all-over composition（满幅构图）**｜gestural mark（书写性笔痕）
- **参照物**：**杰克逊·波洛克（Jackson Pollock）**、威廉·德·库宁、弗朗茨·克莱因
- **提示词模板**：`抽象表现主义的行动绘画（action painting）风格，颜料以滴洒、泼溅、甩掷的方式（drip）落在平铺的画布上，形成层层交叠、粗细不一的线条与色斑；全画为满幅构图（all-over）、没有焦点与留白，笔触充满速度与身体的动势；色彩以黑、白、铝银、赭红与深蓝为主，颜料有厚薄与光泽差；主体的轮廓只以隐约的色块暗示，人形从纷乱的颜料中浮现又被吞没；保持主体的姿态与整体剪影可辨`
- **推荐 input_fidelity**：0.35
- **适合**：人像（抽象化）、场景、情绪表达
- **避免**：不要清晰的轮廓线、不要写实细节、不要居中构图与留白、不要干净整齐的色块

### 65. 克里姆特金箔（Klimt Gold Leaf）
- **关键词**：Gustav Klimt, gold leaf, gold ground, ornamental pattern, Byzantine influence, decorative flattening, mosaic
- **术语锚点**：**gold leaf（金箔）**｜**gold ground（金底）**｜ornamental pattern（装饰纹样：漩涡、方块、眼形）｜decorative flattening（装饰性平面化）
- **参照物**：**古斯塔夫·克里姆特（Gustav Klimt）**《吻》《阿黛尔·布洛赫-鲍尔像》；拉文纳马赛克的直接影响
- **提示词模板**：`克里姆特（Gustav Klimt）风格，整幅大面积使用金箔（gold leaf）铺出耀眼的金底（gold ground）；人物与衣物被压缩为平面，其上覆盖密集的装饰纹样——同心漩涡、长方形与眼形图案、几何金线；面部与手部是全画唯一的三维写实区域，肌肤细腻柔和，与周围华丽的平面装饰形成强烈反差；色彩为金、黑、深红、翠绿与紫；整体华丽、感官、带拜占庭式的装饰感；保持主体五官特征与姿态可辨`
- **推荐 input_fidelity**：0.5
- **适合**：人像、双人像、装饰画
- **避免**：不要写实背景、不要平淡单色、不要廉价的金色渐变、不要 3D 渲染的金属材质
- **与 #58 拜占庭马赛克的分工**：#58 强调**小块拼贴的物理肌理 + 圣像程式**；#65 强调**金箔平面 + 装饰纹样 + 写实面孔的反差**。要"古教堂的镶嵌感"用 58，要"金色装饰画"用 65

---

## 十三、摄影与影像工艺

> v5 新增（66–73）。这一类拼的是**某一项具体的摄影／影像工艺**，而不是"胶片感"这种笼统的调子。
> 关键写法：**把该工艺独有的物理缺陷写出来**——湿版的药液流痕、蓝晒的普鲁士蓝、CRT 的扫描线、长曝的丝绢水流。

### 66. 湿版摄影（Wet Plate Collodion）
- **关键词**：wet plate collodion, tintype, ambrotype, uneven coating, vignetted edges, silver halide, antique portrait
- **术语锚点**：**wet plate collodion（湿版火棉胶）**｜tintype（锡版）／ambrotype（玻璃版）｜**uneven collodion pour（药液铺设不匀的流痕）**｜vignetted edge（边缘暗角）
- **参照物**：十九世纪肖像馆的湿版人像；美国内战时期的 tintype；朱莉娅·玛格丽特·卡梅隆
- **提示词模板**：`十九世纪湿版摄影（wet plate collodion）风格，影像呈现在一张涂布不均的深色金属或玻璃板上：边缘有明显的暗角与化学药液流淌的痕迹，四角发黑、轮廓不规则（药液铺设不匀的流痕）；画面为单色的深褐／灰黑，高光是乳白、暗部沉稳；正面硬光直打、曝光略长，被摄者保持长时间曝光下的僵直姿态，皮肤在蓝光敏化下略显苍白；板面有划痕、灰尘与手工涂布的条纹；保持主体五官特征与姿态不变`
- **推荐 input_fidelity**：0.6
- **适合**：人像、静物
- **避免**：不要现代照片的干净边缘、不要彩色、不要平滑无瑕的渐变、不要锐利的数码高光

### 67. 蓝晒（Cyanotype）
- **关键词**：cyanotype, Prussian blue, photogram, sun print, blueprint, botanical silhouette, brush coating marks
- **术语锚点**：**cyanotype（蓝晒法）**｜**Prussian blue（普鲁士蓝）**｜photogram（物影照片）｜brush coating mark（刷涂痕）
- **参照物**：安娜·阿特金斯（Anna Atkins）的藻类蓝晒图谱；工程蓝图
- **提示词模板**：`蓝晒（cyanotype）风格，整幅只有普鲁士蓝（Prussian blue）与纸白两色，深浅由曝光时间决定：受光处为深邃的蓝，遮挡处留下青白的纸底；底色上可见手工刷涂感光液时留下的笔刷痕与不匀的边，纸面有纤维肌理；主体以剪影般的锐利轮廓呈现、内部细节被大块简化，边缘过渡硬朗；整体是十九世纪植物图谱与工程蓝图的气息；保持主体轮廓、五官位置与构图可辨`
- **推荐 input_fidelity**：0.5
- **适合**：植物、静物、人像剪影
- **避免**：不要多色、不要柔和渐变、不要现代数码感、不要写实的皮肤质感

### 68. 反转片（Kodachrome）
- **关键词**：Kodachrome, slide film, reversal film, saturated reds, fine grain, high contrast, mid-century colour photography, slide projection
- **术语锚点**：**reversal film（反转片）**｜Kodachrome｜saturated red（饱和的红）｜fine grain（细颗粒）｜slide projection（幻灯投影）
- **参照物**：柯达克罗姆（Kodachrome）拍摄的二十世纪中叶彩色照片；《国家地理》的早期彩色报道
- **提示词模板**：`柯达克罗姆（Kodachrome）反转片风格，色彩浓郁而不失通透——红与黄格外饱满、蓝绿深沉；反差偏高，高光处带微微的暖调；颗粒极细、画面干净锐利，有幻灯片般的立体感与年代的距离感；光线为直射的自然阳光，阴影深而清晰；整体是二十世纪中叶彩色报道摄影的气质；保持主体五官特征、姿态与构图不变`
- **推荐 input_fidelity**：0.72
- **适合**：人像、街景、风光
- **避免**：不要褪色的怀旧黄调（那是 #21 拍立得）、不要现代 HDR 的高动态、不要青橙电影调（那是 #17）、不要低饱和

### 69. 长曝光（Long Exposure）
- **关键词**：long exposure, silky water, light trails, motion blur, ND filter, streaked clouds, ghosting
- **术语锚点**：**long exposure（长曝光）**｜**light trail（光轨）**｜**silky water（丝绢水流）**｜ND filter（中性密度滤镜）｜ghosting（人影拖影）
- **参照物**：经典风光长曝摄影；城市夜景车流；迈克尔·肯纳式的宁静长曝
- **提示词模板**：`长曝光摄影风格：流动的水面被抹平为丝绢般的乳白平面（silky water），云层拉出平滑的条带，车灯与光源成为连续的光轨（light trail），人流化作半透明的拖影；静止的建筑与主体保持绝对锐利、纹丝不动，与流动的部分形成强烈对比；整体画面光滑、干净，时间被压缩成一种超现实的静止；保持主体五官特征与静态姿态不变`
- **推荐 input_fidelity**：0.6
- **适合**：风光、城市、水面、静物
- **避免**：不要全画面模糊、不要手抖式的抖动模糊、不要过度 HDR、**不要主体也糊掉**（主体必须锐利）

### 70. 双重曝光（Double Exposure）
- **关键词**：double exposure, multiple exposure, overlay blend, silhouette fill, in-camera, dreamlike
- **术语锚点**：**double exposure（双重曝光）**｜overlay blend（叠加混合）｜**silhouette fill（剪影填充）**｜in-camera（机内合成）
- **参照物**：机内双重曝光的胶片实验；时尚摄影中的剪影叙事
- **提示词模板**：`双重曝光（double exposure）摄影风格，两张影像在同一张底片上叠加：主体被处理为半透明的剪影（剪影填充），其内部透出第二重影像——森林、山峦、花枝、城市天际线或水纹；两层的明暗关系彼此咬合，主体轮廓仍然清晰可辨，内部细节与外层风景共同呼吸；整体色调统一（可偏青绿、暖褐或冷灰），画面安静、诗意、略带梦的超现实感；保持主体轮廓与姿态可辨`
- **推荐 input_fidelity**：0.5
- **适合**：人像、动物、风景
- **避免**：不要生硬的图层粘贴感、不要两份内容各占一半、不要杂乱堆叠、不要丢掉主体轮廓

### 71. 移轴微缩（Tilt-Shift Miniature）
- **关键词**：tilt-shift, miniature effect, shallow focus band, high saturation, aerial viewpoint, toy-like scale
- **术语锚点**：**tilt-shift（移轴）**｜**miniature effect（微缩效果）**｜shallow focus band（窄焦平面带）｜aerial viewpoint（俯瞰视角）｜toy scale（玩具比例）
- **参照物**：移轴镜头拍摄的城市俯瞰照片；文森特·拉福雷式的微缩城市
- **提示词模板**：`移轴（tilt-shift）微缩景观摄影风格，从高处俯瞰，画面只在中间一条窄带内保持清晰，上下迅速虚化（miniature effect）；色彩被推高饱和度、对比略强，光线明亮干净，物体边缘锐利；比例感被改写——真实的场景看起来像一套精巧的玩具模型或沙盘；主体处于清晰带上、质感细致；保持主体轮廓与整体布局可辨`
- **推荐 input_fidelity**：0.5
- **适合**：风景、城市、街景
- **避免**：**不要普通的浅景深虚化**（必须是"上下两条虚化带 + 中间清晰带"的窄带式）、不要低饱和、不要阴沉的色调

### 72. 故障艺术（Glitch Art）
- **关键词**：glitch art, datamosh, pixel sorting, chromatic aberration, scanline displacement, RGB split, digital corruption
- **术语锚点**：**glitch（故障）**｜datamosh（数据压制）｜**pixel sorting（像素排序拉伸）**｜**RGB split／chromatic aberration（通道分离）**｜scanline displacement（扫描线错位）
- **参照物**：数字故障艺术；视频压缩伪影；RGB 分离的当代设计
- **提示词模板**：`故障艺术（glitch art）风格，画面呈现数字文件损坏后的视觉：横向的像素条带被拉伸、错位与撕裂，颜色通道相互分离（RGB split）在边缘产生红绿青的色差，局部出现像素排序式的拉伸条纹（pixel sorting）与压缩产生的块状噪点，扫描线不规则地跳变；主体在故障中仍然可辨认，但被切碎、重排、部分丢失；整体是深色底配高饱和的电子色；保持主体轮廓的关键特征可辨`
- **推荐 input_fidelity**：0.45
- **适合**：人像、城市、产品
- **避免**：不要整齐的滤镜特效、不要柔和渐变、不要可爱化、**不要破坏到看不出主体**

### 73. 模拟录像 · CRT（Analog Video / CRT）
- **关键词**：analog video, CRT scanlines, VHS, phosphor glow, chromatic bleeding, interlace, tracking error
- **术语锚点**：**CRT scanline（阴极射线管的扫描线）**｜**phosphor glow（荧光粉辉光）**｜chromatic bleeding（色溢）｜tracking error（磁迹错位）｜interlace（隔行扫描）
- **参照物**：八十年代的家用录像带画面；老式显像管电视的播出画面；电视录制的演唱会录像
- **提示词模板**：`模拟录像／显像管（CRT）画面风格：屏幕上有细密清晰的水平扫描线（scanline）与隔行扫描的细微抖动，高光处溢出荧光粉般的柔和辉光（phosphor glow），颜色在边缘出现红蓝的横向色溢，画面有轻微的磁迹错位与噪点带，四角有球面管的暗角与轻微变形；整体色调偏暗、对比偏低，带旧录像带的褪色感；保持主体五官特征与姿态可辨`
- **推荐 input_fidelity**：0.55
- **适合**：人像、场景、怀旧题材
- **避免**：不要现代高清的锐利感、不要赛博朋克的霓虹双色（那是 #11）、**不要失真到看不清主体**、不要廉价滤镜包

---

## 十四、当代插画与数字

> v5 新增（74–80）。这一类是**当代插画／数字创作的流行语汇**，常见于独立出版物、品牌视觉与社媒插画。
> 关键是把**绘制工具与造型规则**写清楚（矢量、单线、等距体素、扁平淡彩、粗轮廓平涂），而不是笼统地说"插画风"。

### 74. 超扁平（Superflat）
- **关键词**：Superflat, Takashi Murakami, flat planes, kawaii, otaku culture, bold outline, pop surfaces
- **术语锚点**：**Superflat（超扁平）**｜flat plane（平面化）｜kawaii（可爱）｜bold flat outline（粗平涂轮廓）
- **参照物**：**村上隆（Takashi Murakami）**；奈良美智（作为"可爱但不超扁平"的对照）
- **提示词模板**：`超扁平（Superflat）插画风格，画面被彻底压平，没有任何透视、景深与体积，所有元素像贴纸一样并置在同一个平面上；粗而均匀的黑色轮廓线内填高饱和的平涂色块；造型可爱且高度符号化，图案化与重复性纹样（花朵、眼睛、云）铺满背景；色彩明快、对比强烈，带强烈的消费文化与御宅族审美；保持主体五官的关键特征与姿态可辨`
- **推荐 input_fidelity**：0.5
- **适合**：人像、角色、图形
- **避免**：不要立体光影、不要写实比例、不要柔和的渐变色、不要西式水彩的空气透视

### 75. 法式 BD · 墨比斯线（Bande Dessinée / Moebius Line）
- **关键词**：bande dessinée, Moebius, ligne claire, clean contour line, flat local colour, European graphic novel
- **术语锚点**：**bande dessinée（法比漫画）**｜**ligne claire（清晰线条）**｜clean contour（均匀轮廓线）｜flat local colour（平涂固有色）
- **参照物**：**墨比斯（Moebius / 让·吉罗）**；埃尔热《丁丁历险记》（ligne claire）；恩基·比拉尔
- **提示词模板**：`法比漫画（bande dessinée）风格，墨比斯式的清晰线条（ligne claire）：所有形体都由粗细均匀、干净利落的黑色轮廓线界定，轮廓内平涂固有色，仅用一层很淡的单色阴影交代体积，不做强烈光影；色彩为克制的灰蓝、赭黄与暖白，画面通透、精确、有呼吸感；背景细节繁而不乱、透视准确；整体是欧洲精装漫画的内页质感；保持主体五官特征与姿态不变`
- **推荐 input_fidelity**：0.5
- **适合**：人像、场景、科幻题材
- **避免**：**不要美漫的粗黑墨块与厚排线（那是 #24）**、不要日漫的大眼萌化（那是 #22）、不要写实厚涂、不要浓艳高饱和

### 76. 矢量扁平插画（Flat Vector Illustration）
- **关键词**：flat vector illustration, geometric shapes, solid fill, minimal outline, editorial illustration, limited palette
- **术语锚点**：**flat design（扁平设计）**｜solid fill（纯色填充）｜geometric simplification（几何简化）｜limited palette（有限调色板）
- **参照物**：当代品牌插画与报纸观点插画（如报纸 op-ed 配图一类）
- **提示词模板**：`矢量扁平插画（flat vector illustration）风格，形体被简化为几何形状的拼合（圆、矩形、椭圆、三角），纯色填充、没有渐变、没有噪点、没有体积光影；轮廓可选极细的深色描边或完全无线；色彩为有限而考究的调色板（如暖橙、砖红、靛蓝、灰绿、米白），色块之间以小空隙留出呼吸；画面概念化、秩序清晰，带编辑插画般的说明性；保持主体的辨识特征与姿态可辨`
- **推荐 input_fidelity**：0.45
- **适合**：人像、场景、概念图、编辑配图
- **避免**：不要渐变与阴影、不要手绘笔触、不要立体写实、不要过多细节

### 77. 单线画（Single Line Art）
- **关键词**：single line drawing, continuous line, one-line art, minimal, white ground, confident gesture
- **术语锚点**：**continuous line（连续不断的线）**｜one-line art（单线画）｜minimal contour（极简轮廓）｜negative space（留白）
- **参照物**：毕加索的单线动物与人体；马蒂斯的线条；当代极简单线插画
- **提示词模板**：`单线画（single line art）风格，整幅只由一条连续不断、不自交的线构成，从起笔到收笔一气呵成，粗细可有极轻微的变化，线条自信流畅；其余全部为空白（negative space），没有任何填充、阴影或第二笔；画面极简、现代、有设计感，线条在恰好的地方转折以交代发型、五官、姿态与衣褶；保持主体的辨识特征与姿态可辨`
- **推荐 input_fidelity**：0.4
- **适合**：人像、动物、极简设计
- **避免**：不要多笔、不要填充与阴影、不要抖动的细碎线（必须自信流畅）、不要背景元素

### 78. 低多边形（Low Poly）
- **关键词**：low poly, faceted triangles, polygon mesh, flat shading, geometric facets, low-poly render
- **术语锚点**：**low poly（低多边形）**｜polygon mesh（多边形网格）｜**flat shading（平直着色）**｜faceted surface（切面）
- **参照物**：早期 3D 游戏的低模造型；当代低多边形艺术海报
- **提示词模板**：`低多边形（low poly）艺术风格，主体的表面被分解为一块块清晰的三角形／多边形切面（faceted surface），每个切面为单一纯色、相邻切面之间靠明度差形成体积（flat shading），没有平滑过渡与抗锯齿；色彩为清新的有限调色板，背景可作同样的多边形化或干净的纯色渐变；整体是低模 3D 的几何秩序感；保持主体轮廓、五官位置与姿态可辨`
- **推荐 input_fidelity**：0.45
- **适合**：人像、动物、风景、产品
- **避免**：不要平滑曲面、不要圆润的过渡、不要写实皮肤纹理、不要过多小面导致糊成一团

### 79. 体素（Voxel Art）
- **关键词**：voxel art, cube-based, MagicaVoxel, isometric, blocky 3D, limited palette, diorama
- **术语锚点**：**voxel（体素）**｜**isometric（等距）**｜blocky geometry（方块化形体）｜limited palette（有限调色板）
- **参照物**：MagicaVoxel 风格的体素场景；方块式建筑与体素微缩立体模型
- **提示词模板**：`体素（voxel art）风格，整个世界由大小一致的立方体（voxel）堆叠而成，形体棱角分明、彻底方块化，可见清晰的格子与阶梯状边缘；采用等距（isometric）视角，光源多为单一平行光，每个立方体的顶面、正面与侧面呈现三个固定的明度层级；色彩为明亮饱和的有限调色板，背景为干净的纯色或同风格的小场景；保持主体轮廓、姿态与关键特征可辨`
- **推荐 input_fidelity**：0.4
- **适合**：人物、场景、物品、建筑
- **避免**：不要平滑曲面、不要真实光影与镜面反射、不要写实材质贴图

### 80. 稚拙蜡笔画（Naïve Crayon / Oil Pastel）
- **关键词**：naïve art, crayon, oil pastel, childlike, waxy texture, wobbly line, paper tooth, warm palette
- **术语锚点**：**naïve art（稚拙艺术）**｜**oil pastel（油画棒）**｜waxy bloom（蜡质白霜）｜paper tooth（纸面颗粒）｜wobbly line（歪斜的手绘线）
- **参照物**：儿童画的造型语法；让·杜布菲（Art Brut）；当代手绘绘本
- **提示词模板**：`稚拙手绘风格，用蜡笔或油画棒（oil pastel）在粗糙的纸上画出：笔触粗大、颜色厚重并露出纸张颗粒（paper tooth），用力处出现蜡质白霜与堆叠的反光，线条歪斜而不准（wobbly line），形体比例故意不准确、透视错误；配色为温暖明快的红黄绿蓝，色块可略微出界；整体是儿童画般天真直接、充满手工感的气息；保持主体可辨识的关键特征（发型、服装、姿态）`
- **推荐 input_fidelity**：0.4
- **适合**：人物、动物、场景、亲子题材
- **避免**：不要精致的写实、不要干净的数字线条、不要立体光影、不要刻意做旧

---

## 十五、风格推导公式（用于未收录的风格）

当用户要的风格不在上表时，按以下公式现场构造提示词，并在生成后把新条目追加到本文件：

```
最终提示词 = [风格锚点] + [精确术语] + [参照物] + [主材质/笔触/媒介] + [色彩与光影] + [构图与氛围] + [画质词] + [负向约束]
```

- **风格锚点**：把用户风格名翻译成 2–4 个英文美术术语（如 "art deco, gilded geometry"）。
- **精确术语**：**必填**。从本文件末尾的「术语速查」里挑（impasto / chiaroscuro / wet-on-wet / Ben-Day dots…），术语比形容词有效得多。
- **参照物**：点名一位艺术家、一部作品或一个品牌（"莫奈""葛饰北斋""银翼杀手""Kinfolk"），模型的响应远强于抽象描述。
- **主材质/媒介**：油画/水彩/木刻/3D/胶片……
- **色彩与光影**：主色调 + 光线方向与质感。
- **构图与氛围**：情绪词 + 留白/满构图。
- **画质词**：`细节清晰, 高清, 专业作品, 8k` 之类。
- **负向约束**：`不要变形, 不要多余肢体, 不要文字水印, 保持主体特征`。

**示例**（用户要"装饰艺术风"，不在库中）：
> `装饰艺术（Art Deco）风格，镀金几何纹样（gilded geometry），机械美学对称构图，黑金与祖母绿配色，金属光泽，平整的装饰性块面，参照克莱斯勒大厦式的装饰语汇，高清细节，保持主体五官与姿态，不要文字，不要变形`

---

## 十六、术语校准来源（GitHub 开放提示词资源）

v2 的术语与参照物来自以下公开资源（MIT/公开许可的提示词整理项目），仅用于术语校准，未复制其代码：

| 资源 | 用途 |
|------|------|
| `1fairyfox/random-ai-prompt` → `engine/data/lists/style/art-movement.txt` | 艺术流派术语 180+ 条（Impressionism / Fauvism / Ukiyo-e / Superflat / Cyberpunk…） |
| 同上 → `engine/data/lists/style/art-technique.txt` | 艺术技法术语 140+ 条（Impasto / Chiaroscuro / Cloisonnism / Ben-Day dots / Ink wash painting…） |
| 同上 → `engine/data/lists/look/color.txt` | 色彩词表（Oat / Sepia / Sage / Azure / Ochre / Sienna…） |
| 同上 → `engine/data/lists/look/mood.txt` | 情绪词表（Dreamy / Serene / Melancholy…） |
| 同上 → `engine/data/blocks/style/*.dpl` | 风格提示词块写法示范（**"点名艺术家 + 术语"** 的组合方式，如 `by makoto shinkai, wlop, rossdraws`） |
| `altryne/awesome-ai-art-image-synthesis` | AI 绘画提示词工程索引 |
| `dongyubin/Awesome-AI-Images-Prompts` | 中文提示词合集（多模型适配写法参考） |
| `BaYue-SYJ/shuixian-prompts` | 5000+ 中文提示词分类数据集（风格命名与分类参考） |

### 术语速查（写提示词时优先使用这些精确术语）

- **油画/绘画**：impasto（厚涂）、chiaroscuro（明暗对照）、tenebrism（暗色调）、glazing（罩染）、scumbling（干笔擦）、alla prima（一次性完成）、cloisonnism（景泰蓝式）、pointillism（点彩）、grisaille（灰色单彩）
- **水彩/纸本**：wet-on-wet（湿画法）、wet-on-dry、color wash（水色罩染）、granulation（颜料沉积）、gouache（水粉）、ink wash（水墨）、sumi-e（墨绘）
- **版画/平面**：ukiyo-e（浮世绘）、nishiki-e（锦绘）、shin-hanga（新版画）、sosaku-hanga（创作版画）、screen print（丝网印）、halftone（网点）、Ben-Day dots（本戴点）、linocut（麻胶版）
- **漫画/插画**：cel shading（赛璐璐）、lineart（线稿）、cross-hatching（交叉排线）、superflat（超扁平）、key visual（关键帧）
- **摄影/胶片**：negative space（留白）、high-key / low-key、anamorphic（变形宽银幕）、shallow DOF（浅景深）、film grain（胶片颗粒）、silver gelatin（银盐）、teal & orange（青橙调）、soft focus（柔焦）
- **流派锚点**：Expressionism（表现主义）、Fauvism（野兽派）、Impressionism（印象派）、Art Nouveau（新艺术）、Art Deco（装饰艺术）、Bauhaus（包豪斯）、Suprematism（至上主义）、Pop Art（波普）、Op Art（欧普）、Surrealism（超现实）、Cyberpunk（赛博朋克）、Vaporwave（蒸汽波）、Solarpunk、Steampunk（蒸汽朋克）、Retrofuturism（复古未来主义）
- **v4 新增术语（38–50）**：gilded geometry（镀金几何）、whiplash curve（鞭形曲线）、photomontage（摄影拼贴）、spot ink／overprint／misregistration（专色／叠印／套印偏移）、relief print／gouge mark（凸版／凿痕）、intaglio／guilloche（凹版／扭索饰纹）、divisionism／optical mixing（分色主义／视觉混合）、impossible juxtaposition／uncanny scale（不可能并置／异常比例）、moiré／optical vibration（摩尔纹／视觉振动）、buon fresco／craquelure（湿壁画／龟裂）、leaded glass／grisaille（铅条镶嵌玻璃／灰色单彩玻璃）、satin stitch／counted thread（缎面绣／数纱绣）、Carrara marble／drapery fold（卡拉拉大理石／衣褶）
- **v5 新增术语（51–80）**：
  - **东亚传统**：gongbi（工笔）、iron-wire line／silkworm-thread line（铁线描／游丝描）、qinglu shanshui（青绿山水）、gold outline（泥金勾线）、mineral pigment（矿物颜料）、oxidised flesh（变色发黑的肤色）、flying apsara（飞天）、underglaze cobalt（釉下钴蓝）、crackle（开片冰裂）、gold line（金线勾勒）、brocade mount（锦缎装裱）、ink rubbing（拓本）
  - **西方艺术史**：tessera／gold ground／hieratic frontal（马赛克小块／金底／圣像正面程式）、illuminated manuscript／vellum／gold leaf／marginalia（泥金手抄本／羊皮纸／金箔／页边装饰）、north light／ultramarine（北向窗光／群青）、tenebrism（暗色调主义）、fête galante／rocaille（雅宴画／贝壳涡卷）、analytic cubism／simultaneous viewpoint（分析立体主义／多视点并置）、action painting／drip／all-over composition（行动绘画／滴洒法／满幅构图）、gold leaf ground（金箔金底）
  - **摄影影像**：wet plate collodion／tintype／ambrotype（湿版火棉胶／锡版／玻璃版）、uneven collodion pour（药液流痕）、cyanotype／Prussian blue（蓝晒／普鲁士蓝）、photogram（物影照片）、reversal film（反转片）、long exposure／light trail／silky water（长曝光／光轨／丝绢水流）、double exposure／silhouette fill（双重曝光／剪影填充）、tilt-shift／miniature effect（移轴／微缩效果）、glitch／pixel sorting／RGB split／datamosh（故障／像素排序／通道分离／数据压制）、CRT scanline／phosphor glow／tracking error（扫描线／荧光粉辉光／磁迹错位）
  - **当代插画数字**：Superflat（超扁平）、bande dessinée／ligne claire（法比漫画／清晰线条）、flat vector／solid fill（矢量扁平／纯色填充）、continuous line／one-line art（连续线／单线画）、low poly／polygon mesh／flat shading（低多边形／多边形网格／平直着色）、voxel／isometric（体素／等距）、naïve art／oil pastel／paper tooth（稚拙艺术／油画棒／纸面颗粒）
