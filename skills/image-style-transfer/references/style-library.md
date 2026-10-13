# 风格提示词库（Style Prompt Library） — 共 37 个风格

本文件是 image-style-transfer 的核心资产。每个风格给出**可直接使用的提示词模板**、
**推荐输入保真度（input_fidelity）** 与 **适用场景**。

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

## 八、风格推导公式（用于未收录的风格）

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

## 九、术语校准来源（GitHub 开放提示词资源）

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
