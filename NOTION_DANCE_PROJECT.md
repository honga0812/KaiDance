# ☀️ 奇妙星律动：儿童 AI 萌趣火柴人舞蹈乐园 (Kids AI Stickman Dance World)

> 💡 **项目简介**：专为 4~6 岁（幼儿园中大班、家庭亲子）设计的全场景体感舞蹈教学系统。融合 **入镜自动变身萌趣发光火柴人**、**8 支动作专属循环示范视频**、**1~3 人多人体态骨架追踪**、**名师原声口令** 与 **卡拉OK式同步歌词**，支持电视大屏全屏跟跳与动作自动评分，并已完全就绪支持部署到 GitHub Pages 公开使用。
> 
> 📅 **最新更新**：2026-10-03 (v3.5.0 - 萌趣火柴人体态捕捉、首批AI真实动作影片集成、GitHub Pages更新)  
> 🏷️ **标签**：`儿童教育` `AI编舞` `发光火柴人` `骨架追踪` `AI视频生成` `GitHubPages` `Kai_Music`  
> 📁 **本地运行服务**：`http://localhost:8080/`

---

## 🤸 一、 萌趣发光火柴人（Cute Stickman Avatar）体态捕捉系统

针对低龄儿童特别喜欢的“火柴人”形象，彻底改造了视觉骨骼渲染逻辑：

```
┌────────────────────────────────────────────────────────┐
│  【摄像头画面（镜像）】                                  │
│                                                        │
│                    🌿 (小嫩芽天线，随身体摇晃)           │
│                  ╭──────╮                              │
│                  │ ^  ^ │  <-- 萌萌的大眼睛 (笑脸头部)    │
│                  │  ◡   │                              │
│                  ╰──────╯                              │
│                   / || \                               │
│        (左手星星) ★  ||  ★ (右手星星，举高发翡翠绿光)     │
│                    /  \                                │
│                   d    b   <-- 圆润发光小鞋子          │
│                                                        │
│   核心机制：                                            │
│   1. 当画面无小朋友时，提示“快站到镜头前变身火柴人！”；       │
│   2. 小朋友一入镜，火柴人立刻依附在身体上，四肢完全跟随运动； │
│   3. 手臂举高托起太阳或左右摆动时，火柴人瞬间绽放绿光与星星！ │
│   4. 支持【暖阳金 / 极光绿 / 糖果粉】三套炫酷火柴人皮肤！     │
└────────────────────────────────────────────────────────┘
```

---

## 🎬 二、 官方英文歌词与动作要领提示矩阵（对齐音乐结构与节拍）

为实现动作与歌曲的紧密融合，我们直接采用《Morning Sunshine Hello》官方英文歌词与段落时钟谱，为每个歌词段落量身定制了**动作要领提示**与**AI 视频生成提示词**：

### 1. 官方歌词全景动作要领与生成矩阵表

| 段落与序号 | 官方英文歌词 | 时间区间 | 动作名称与要领提示 (Movement Tips) | AI 视频生成精准提示词 (Video Prompt) | 骨骼捕捉识别重点 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **[Intro]<br>动作 01** | `[Intro] 🎵 Musical Awakening` | **00:00 - 00:08** | **萌芽踏步踩节拍**<br>⏰ 倒数准备！双手叉腰，随着节拍原地轻快踏步，身体微微弹动！ | `Full-body 9:16 vertical shot, 3D animated preschool dance coach, cheerful cute boy/girl, hands on hips, marching in place with bouncy knee raises on 16 beats, smiling warmly, bright pastel kindergarten studio, seamless loop, 8s, 60fps.` | 髋膝垂直位移<br>双手叉腰贴合 |
| **[Intro]<br>动作 02** | `[Intro] 🍃 Morning breeze softly blowing` | **00:08 - 00:15** | **小草迎风大波浪**<br>🌱 微风吹拂！双脚站稳，身体和双臂如小草左右波浪大摇摆！ | `Full-body 9:16 vertical shot, 3D kid dance coach, swaying torso and arms smoothly from left to right like gentle grass in the morning breeze, rhythmic wave, happy expression, bright studio, seamless loop, 8s.` | 躯干中轴倾角<br>双臂左右波浪 |
| **[Verse 1]<br>动作 03** | `"Good morning sun, up in the sky,"` | **00:15 - 00:22** | **托起天空小太阳**<br>☀️ 早安太阳！双手从胸前推向天空，掌心朝上托出金色大太阳！ | `Full-body 9:16 vertical shot, 3D cute kid dance coach, bringing hands from chest up above head to hold a big imaginary glowing sun in the sky, fingers spread, tiptoe stretch, smiling, seamless loop, 8s.` | **双手腕高过头部**<br>(`y_wrist < y_head`) |
| **[Verse 1]<br>动作 04** | `"Waving your golden hands so high!"` | **00:22 - 00:28** | **金色大手高招手**<br>✨ 双臂高高举过头顶，像太阳的金色光芒一样向左向右大幅度招手！ | `Full-body 9:16 vertical shot, 3D animated dance coach, arms stretched high overhead, waving both hands energetically like golden sun rays across the sky, joyful expression, seamless loop, 8s.` | **双臂高举大幅招手**<br>左右对称大挥动 |
| **[Verse 1]<br>动作 05** | `"Wake up, brush your teeth and smile,"` | **00:28 - 00:32** | **刷刷小牙大微笑**<br>🪥 揉揉小眼睛，小手握牙刷左右刷刷刷，露出灿烂大笑容！ | `Full-body 9:16 vertical shot, 3D cute preschool coach, rubbing eyes cutely, making fun toothbrush brushing gesture across teeth with one hand, pointing to a huge sunny smile, seamless loop, 8s.` | 单手近嘴部摆动<br>手指点向嘴角笑脸 |
| **[Verse 1]<br>动作 06** | `"Let’s go learn and play a while!"` | **00:32 - 00:35** | **欢快踏步向前冲**<br>🎒 双手叉腰微屈膝，轻快抬腿踏步，准备出发去学本领、做游戏！ | `Full-body 9:16 vertical shot, 3D animated child coach, hands on hips, marching energetically forward with high knees, excited and ready to learn and play, bright studio, seamless loop, 8s.` | 膝盖高抬大踏步<br>身体前倾冲劲 |
| **[Verse 1]<br>动作 07** | `"Birds are singing in the tree, Singing a morning song for me!"` | **00:35 - 00:40** | **树上小鸟展翅飞**<br>🐦 双臂如小鸟翅膀上下轻快扇动，手贴耳旁静静聆听早安鸟鸣！ | `Full-body 9:16 vertical shot, 3D animated kid, arms extended like bird wings flapping gracefully, then cupping one hand to ear to listen to birds singing, smiling gently, seamless loop, 8s.` | **双臂水平展开扇动**<br>单手贴耳聆听姿态 |
| **[Chorus]<br>动作 08** | `"Hello, hello, it's a brand new day!"` | **00:40 - 00:45** | **招手问候新一天**<br>👋 身体微倾，左边挥挥手、右边挥挥手，热情大声说 Hello！ | `Full-body 9:16 vertical shot, 3D animated dance coach, enthusiastically waving right hand then left hand beside ears, dynamic body sway greeting a brand new day, seamless loop, 8s.` | **高位手肘弯曲招手**<br>(`wrist.y < neck.y`) |
| **[Chorus]<br>动作 09** | `"Jump up and shout: Hip-hip-hooray!"` | **00:45 - 00:50** | **跳起欢呼万岁耶**<br>🌟 双脚用力向上蹦跳，双手握拳冲天欢呼：Hip-hip-hooray！ | `Full-body 9:16 vertical shot, 3D kid coach, jumping high with both feet off the ground, pumping fists up in high celebration shouting hooray, ecstatic joyful expression, seamless loop, 8s.` | **垂直起跳位移**<br>双手高举握拳 |
| **[Chorus]<br>动作 10** | `"Put on your shoes and count to three, Come along and sing with me!"` | **00:50 - 00:55** | **穿上小鞋数一二三**<br>👟 弯腰做穿鞋动作，手指点数 1-2-3，张开双臂邀请大家一起唱！ | `Full-body 9:16 vertical shot, 3D animated coach, bending to tap shoes, counting 1-2-3 with fingers, then opening arms wide to invite everyone to sing along, seamless loop, 8s.` | 俯身触脚腕判定<br>双手前伸大开合 |
| **[间奏]<br>动作 11** | `[Interlude] 🌸 Spinning happy dance` | **00:55 - 01:00** | **转个魔法快乐圈**<br>🌸 双手微提衣角踩小碎步，顺时针轻快旋转一圈，定格开出小花！ | `Full-body 9:16 vertical shot, 3D cute dance coach, spinning a full 360-degree circle with arms lightly extended, stepping gracefully, finishing with a blooming flower gesture under chin, seamless loop, 8s.` | 躯干连续侧移旋转<br>定格花朵托腮姿态 |
| **[Verse 2]<br>动作 12** | `"Pack your bag and grab your hat,"` | **01:00 - 01:07** | **背上书包戴小帽**<br>🎒 双手拉拉小书包肩带，再双手高举在头顶戴上一顶可爱小圆帽！ | `Full-body 9:16 vertical shot, 3D animated kid, mimicking putting on backpack straps with both hands, then patting head to adjust an imaginary cute hat, proud posture, seamless loop, 8s.` | 双手拉肩带姿势<br>双手拍抚头部小帽 |
| **[Verse 2]<br>动作 13** | `"Wave goodbye to the sleepy cat!"` | **01:07 - 01:12** | **告别贪睡小猫咪**<br>🐱 学小猫咪伸懒腰揉揉脸，轻手轻脚向贪睡的小猫招手说拜拜！ | `Full-body 9:16 vertical shot, 3D preschool coach, doing cute cat paw stretch, rubbing whiskers cutely, then waving gentle goodbye, playful and charming expression, seamless loop, 8s.` | 双手猫爪握拳揉颊<br>轻柔向斜下方挥手 |
| **[Verse 2]<br>动作 14** | `"Look outside, the sky is blue, So many fun things waiting for you!"` | **01:12 - 01:17** | **眺望蓝天踢踢脚**<br>🌈 单手搭凉棚探头眺望蓝天，双脚欢快前踢点地，充满期待！ | `Full-body 9:16 vertical shot, 3D kid coach, hand over brow looking out at blue sky, kicking feet forward with rhythm, excited for fun adventures, seamless loop, 8s.` | 单手搭额前眺望<br>双腿交替前踢点地 |
| **[Chorus]<br>动作 15** | `"Hello, hello, it's a brand new day!"` | **01:17 - 01:23** | **再度热情说早安**<br>👋 双脚跳跃踩点，双手在耳侧大幅度交替大招手，热情拉满！ | `Full-body 9:16 vertical shot, 3D animated dance coach, enthusiastically waving both hands beside ears, bouncing on feet, big joyful smile, seamless loop, 8s.` | **双耳侧连续大幅挥手**<br>双脚轻跳律动 |
| **[Chorus]<br>动作 16** | `"Jump up and shout: Hip-hip-hooray!"` | **01:23 - 01:29** | **高空蹦跳大欢呼**<br>🐰 双脚轻盈高高跳起，双手向两侧绽放爆星：Hip-hip-hooray！ | `Full-body 9:16 vertical shot, 3D kid coach, bursting into an energetic high jump, throwing hands up in the air shouting hip-hip-hooray, celebration energy, seamless loop, 8s.` | **高跳位移峰值**<br>双臂放射状展臂 |
| **[Chorus]<br>动作 17** | `"Put on your shoes and count to three, Come along and sing with me!"` | **01:29 - 01:35** | **点点脚尖爱心唱**<br>💖 脚尖向前点步，双手胸前拼出大爱心送光波，甜蜜大合唱！ | `Full-body 9:16 vertical shot, 3D animated child coach, tapping feet to the rhythm, forming a big heart shape at chest and pushing it forward warmly, singing along, seamless loop, 8s.` | **双手腕在胸骨前交汇**<br>(`dist(lWrist, rWrist) < 0.1`) |
| **[Bridge]<br>动作 18** | `[Bridge] 🕊️ Soaring like a gentle breeze` | **01:35 - 01:43** | **微风滑翔大旋转**<br>🕊️ 双臂如翅膀展开在空中柔和滑翔，踩着节拍轻快转圈起伏！ | `Full-body 9:16 vertical shot, 3D cute dance coach, arms extended horizontally soaring like a bird in the gentle morning breeze, smooth glide and gentle spin, graceful, seamless loop, 8s.` | **双臂水平展开扇动**<br>身体中轴圆周位移 |
| **[Outro]<br>动作 19** | `"Good morning, world! Let's have fun today!"` | **01:43 - 01:51** | **张开怀抱迎世界**<br>🌍 双臂向天空与大地划出最广阔的大怀抱，迎接新的一天！ | `Full-body 9:16 vertical shot, 3D kid coach, opening arms as wide as possible to embrace the whole world, smiling radiantly, chest open, full of happiness, seamless loop, 8s.` | 双臂向外展开最大夹角<br>头胸挺拔舒展 |
| **[Outro]<br>动作 20** | `"Good morning, world! Let's have fun today!"` | **01:51 - 02:00** | **深呼吸合十定格**<br>🌟 深深吸气双臂划大圆上扬，呼气双手胸前合十，微鞠躬定格微笑！ | `Full-body 9:16 vertical shot, 3D kid coach, inhaling deeply while raising arms up in a grand circle, bringing palms together at chest in prayer pose, gentle bow with sweet smile, graceful finish, seamless loop, 8s.` | 双臂划大圆上扬<br>胸前合十收操定格 |

---

### 2. AI 视频批量生成参数与统一提示词模板（Runway Gen-3 / Luma / Kling / Minimax）

为保证生成的 15 支 8 秒视频在人物外貌、服装、光影与背景画风上 **100% 保持一致**，生成时请直接套用以下 Master Prompt 模板：

```text
[Master Style Prompt]:
Full-body 9:16 vertical framing, master animation 3D Disney Pixar style, a cheerful 5-year-old preschool dance coach named Leo (cute boy with short brown hair, wearing bright orange-blue athletic hoodie, white sneakers) OR Mia (sweet girl with twin pigtails, pink-yellow star tracksuit). Inside a warm, sunlit kindergarten dance studio with pastel rainbow floor and large floor-to-ceiling windows showing green trees and blue sky. Studio soft morning lighting, clean background, perfectly centered full body from head to shoes, child-friendly atmosphere.

[Action Instruction]:
{填入上方表格中的动作英文提示词}

[Parameters]:
- Duration: 8 seconds (Seamless Loop)
- Aspect Ratio: 9:16 (Vertical)
- Frame Rate: 60fps / 30fps
- Negative Prompt: blurry, distorted limbs, extra fingers, deformed face, flickering, sudden cut, horizontal bars, cropped head, cropped feet, text, watermark.
```

---

## 🚀 三、 GitHub & GitHub Pages 公开部署指南

本地仓库已完成全套静态资源编译与 Git 提交（包含多人体态火柴人与所有视频），只需一条命令即可推送到 GitHub：

```bash
cd "/Volumes/4T M2 SSD/AI Native Company OS/Kai_Music"

# 1. 运行一键部署脚本（填入你的 GitHub 仓库地址）
./deploy_to_github.sh https://github.com/<你的GitHub用户名>/kai-music-ai-dance.git

# 2. 前往 GitHub 仓库 Settings -> Pages
#    Source 选择 Deploy from a branch
#    Branch 选择 main, Folder 选择 /docs -> 点击 Save 保存！
# 3. 约 1 分钟后即可在全球公开访问：https://<用户名>.github.io/<仓库名>/
```

---

## 🔬 四、 摄像头人体追踪与火柴人节点专项检查与全面升级

针对您提出的**“开启镜头后抓取人物并转化为发光火柴人节点”**的实际效果，我们进行了深度测试与算法重构，彻底解决以下隐患：

1. **镜像反转手部交叉 Bug 修复**：
   - 原先在镜像视频渲染时，由于水平翻转计算未对齐屏幕物理左右，导致举起右手时火柴人左手臂发生交叉。
   - **已修复**：重写屏幕镜像坐标映射系统，确保真实右手（屏幕右侧）严格驱动火柴人右手臂与手掌，左手驱动左手臂，完全镜像对齐。
2. **站定不动时火柴人消失/闪烁问题彻底解决**：
   - 原先仅对比相邻帧间差异，当小朋友站在镜头前定格摆动作时，帧差变小会导致误判“无人入镜”而闪烁或回退为虚线框。
   - **已修复**：引入自适应背景差分模型（Adaptive Background Model）与置信度平滑衰减累加器（Presence Confidence Accumulator），即使小朋友站定定格数秒，火柴人依然稳固锁住，绝不丢帧闪烁。
3. **双引擎自适应驱动 (MediaPipe Pose AI + 端侧视觉引擎)**：
   - **MediaPipe Pose 引擎**：支持侦测人体 33 个 3D 骨骼与手指节点（鼻子、眼、双肩、双肘、双手腕、左右手指食指、双膝、双脚踝），手指手部动作细腻逼真。
   - **离线端侧视觉引擎**：在离线或无外网状态下无缝自动降级保障，保证任何环境 100% 顺畅运行。
4. **视频 object-cover 比例精确校准**：
   - 彻底消除了摄像头视频画面（如 16:9 / 4:3）在不同屏幕尺寸裁剪时的坐标位移差，火柴人的头部、肩部、四肢 100% 贴合在小朋友的真人体态上。
5. **萌趣发光视觉升级**：
   - 头顶萌芽会随动作动态晃动，脸部带有可爱红晕腮红与笑脸。
   - 动作高举到位时，眼睛自动变闪亮星星眼 `★ ★`，双掌爆出金色星光与即时连击加分！

---

## 🎨 五、 视觉比例重构与普通窗口追踪Bug彻底修复（最新更新）

针对您提出的**“非全屏幕时无法捕捉人物”**以及**“摄影镜头占比较大、示范人物缩小至左侧1/3并以9:16长形裁剪（不压缩）”**的需求，已完成以下重构：

1. **彻底解决“只有点全屏幕才能抓到火柴人”的问题**：
   - **根本原因**：之前 Canvas 初始化在大厅隐藏视图中执行，窗口模式下父容器尺寸未触发重绘，只有点击全屏幕触发 `window.resize` 才能获得实际像素宽高，导致非全屏状态下骨骼渲染器跳过了绘制。
   - **解决方案**：
     - 在 `renderStickmanLoop()` 每一帧加入动态几何校准，并在进入房间时通过 `ResizeObserver` 实时监听父容器像素；
     - 取消 MediaPipe 对端侧视觉引擎的阻断，无论是否开启全屏、窗口被拖动为任意尺寸，**普通窗口下毫秒级直接锁定人物并附着火柴人**；
     - 选歌进入房间后**自动无感拉起摄像头**，无需小朋友或家长手动找按钮开启。

2. **画面比例重构（左侧 1/3 示范，右侧 2/3 大屏互动）**：
   - 整体布局由 50/50 升级为专业舞蹈演播室格局：
     - **左侧示范区域**：缩减为优雅的 **1/3** 紧凑示范台（`lg:col-span-1`）；
     - **右侧摄像区域**：扩充为 **2/3** 宽敞大舞台（`lg:col-span-2`），给小朋友留出最大的跳舞与手臂挥动空间。

3. **示范动作 9:16 竖屏原画居中裁剪（拒绝横向压扁变形）**：
   - 示范视频外层采用标准的 `aspect-[9/16]` 竖屏长形画框；
   - 视频内部采用 CSS `object-cover object-center` **纯净原画居中裁剪**，保留人物 1:1 的身体原画长宽比，**杜绝任何压扁、拉伸或变形**，让舞蹈教练的肢体形态纤细自然、动作清晰易学！

---

## 👥 六、 多人模式（2人/3人）独立体态侦测技术机制说明与解耦升级

针对您提出的**“选两个人或三个人时，是真正侦测不同人，还是只是侦测同一个人克隆同步动作”**的关键疑问，我们已完成算法解析与升级：

### 1. 过去版本机制分析（镜像克隆阶段）
- 在初期演示版本中，由于重心算法仅针对全屏最大单一人体，当切换为 2 人或 3 人时，系统为了展示视觉舞台效果，将 P1 的体态数据附加了左右偏移量（Offset），导致当时几位火柴人会同步做出完全相同的动作。

### 2. 全新升级：真正的**空间扇区解耦独立多人体态侦测系统（Multi-Person Spatial Sector Tracking）**
现已完成架构重构，彻底实现了**“不同小朋友、独立骨骼节点、独立姿态反应”**：
- **2 人模式（双人对舞/亲子同乐）**：
  - 画面空间自动解耦为**左半区（Zone 1: `0.0~0.52`）** 与 **右半区（Zone 2: `0.48~1.0`）**；
  - **P1 乐乐（暖阳金）** 严格绑定站在左侧的小朋友；
  - **P2 欢欢（极光蓝）** 严格绑定站在右侧的小朋友；
  - **完全解耦独立动作**：当左边小朋友举起左手时，**只有 P1 举手**；右边小朋友在做挥手或跳跃时，**P2 会做出专属右边小朋友的动作**，互不干扰！
- **3 人模式（三人齐舞/同伴派对）**：
  - 空间细分为 **左（`0.0~0.38`）**、**中（`0.32~0.68`）**、**右（`0.62~1.0`）** 三个独立侦测走廊；
  - P1、P2、P3 分别由三位小朋友各自独立驱动。
- **独舞伴舞保护机制（智能降级）**：
  - 如果选择“2人模式”但实际只有 1 个小朋友站在左侧，右侧区域未检测到人时，右侧火柴人会优雅保持在专属待命站位轻柔打招呼，作为可爱的“AI 伴舞同伴”，绝不会出现莫名重叠或乱晃。



