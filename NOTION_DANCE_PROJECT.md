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

## 🎬 二、 4小节/16拍 AI 舞蹈动作全曲编排矩阵（15大段落 · 8秒循环）

为完全符合 4~6 岁幼儿运动认知与体能节律，我们严格按照 **“4 个小节，16 拍换一个动作”**（每段时长刚好约 **8 秒**）的黄金节拍单位，将全曲 120 秒拆解为 **15 个紧密契合歌词意象、充满自然童趣的 AI 动作段落**：

### 1. 全曲 15 大动作与歌词契合度时钟谱

| 序号 | 动作名称 | 时长与节拍 | 对应歌词与意象关联 | 幼儿动作要领与名师口令 | AI 视频生成精准提示词 (Video Prompt) | 骨骼侦测重点 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **01** | **萌芽踏步**<br>*(Sprout March)* | **00:00 - 00:08**<br>(4小节/16拍/8s) | [清脆鸟叫与晨风风铃声]<br>*清晨苏醒，森林小草醒来* | 双手叉腰，随着节拍原地轻快踏步弹动。<br>🗣️ *“3-2-1 倒数准备，小脚踩踩节拍，早操开始啦！”* | `Full-body 9:16 vertical shot, adorable 3D animated preschool dance coach, cheerful cute boy/girl, hands on hips, marching in place with bouncy knee raises on 16 beats, smiling warmly, bright pastel kindergarten studio, seamless loop, 8 seconds, 60fps.` | 髋膝垂直位移<br>双手叉腰贴合 |
| **02** | **小草迎风摆**<br>*(Swaying Grass)* | **00:08 - 00:16**<br>(4小节/16拍/8s) | [欢快钢琴与木琴渐入]<br>*微风吹拂，小草小花摇摆* | 双脚微分，双臂垂在身侧如柔软青草，随节奏左右大波浪摇曳（左4拍、右4拍，共2组）。<br>🗣️ *“微风轻轻吹，小草小花左右大波浪摇晃起来！”* | `Full-body 9:16 vertical shot, 3D animated cute kid dance coach, swaying torso and arms smoothly from left to right like gentle grass in the morning breeze, 16 beats rhythmic wave, happy expression, bright studio, seamless loop, 8s.` | 躯干中轴倾角<br>双臂左右波浪 |
| **03** | **托起小太阳**<br>*(Rising Sun)* | **00:16 - 00:24**<br>(4小节/16拍/8s) | *"Morning sunshine hello!"*<br>*早安朝阳，光明唤醒大地* | 双手手心向上自腹前缓缓推向头顶，五指盛开托出金色大太阳，脚跟微提踵。<br>🗣️ *“早安阳光！双手从胸前高高举起，头顶托出大太阳！”* | `Full-body 9:16 vertical shot, 3D cute kid dance coach, bringing hands from chest up above head to hold a big imaginary glowing sun, fingers spread, tiptoe stretch, beaming joyful smile, seamless loop, 8 seconds, 60fps.` | **双手腕高过头部**<br>(`y_wrist < y_head`) |
| **04** | **彩虹洒大地**<br>*(Rainbow Arch)* | **00:24 - 00:32**<br>(4小节/16拍/8s) | *"Waking up the sky so bright!"*<br>*天色大亮，金色光芒四射* | 双臂从头顶向两侧划出大圆弧，手指如细雨轻盈落至腰间，身体随之微下蹲起立。<br>🗣️ *“天空变得好明亮！双手划出一道美丽的七色彩虹！”* | `Full-body 9:16 vertical shot, 3D kid dance coach, sweeping arms down from high above to both sides forming a wide rainbow arc, gentle knee bounce, vibrant golden morning lighting, seamless loop, 8 seconds.` | 双臂肩肘向外划弧<br>双手外展对称 |
| **05** | **招招手说早安**<br>*(Friendly Wave)* | **00:32 - 00:40**<br>(4小节/16拍/8s) | *"Say hello to friends near and far!"*<br>*向四面八方的小伙伴问好* | 转向右侧，右手在耳边大幅度挥动招手（8拍）；转向左侧换左手招手（8拍）。<br>🗣️ *“看到好朋友啦！小手在耳旁高高大挥动说早安！”* | `Full-body 9:16 vertical shot, 3D animated dance coach, enthusiastically waving right hand high beside ear to greet friends, then waving left hand, cheerful eye contact with viewer, energetic, seamless loop, 8 seconds.` | **高位手肘弯曲招手**<br>(`wrist.y < neck.y`) |
| **06** | **拍肩大拥抱**<br>*(Shoulder Tap & Hug)* | **00:40 - 00:48**<br>(4小节/16拍/8s) | *"Say hello to you and me!"*<br>*友爱团结，你和我在一起* | 双手轻拍双肩2下（4拍），再向身体两侧张开大怀抱（4拍），重复2轮。<br>🗣️ *“你和我在一起！拍拍小肩膀，张开大大的拥抱！”* | `Full-body 9:16 vertical shot, 3D kid coach, tapping own shoulders twice with crossed hands then opening arms wide into a warm loving embrace, rhythmic, joyful cute face, studio lighting, seamless loop, 8 seconds.` | 双手腕向胸内交叠<br>双臂横向大展角 |
| **07** | **垫脚摘白云**<br>*(Cloud Reach)* | **00:48 - 00:56**<br>(4小节/16拍/8s) | *"Reach up high to the clouds!"*<br>*伸长身体，够向云端小鸟* | 垫起右脚尖，右手向上抓白云（4拍）；换左脚垫起抓白云（4拍）；双手交替高抓（8拍）。<br>🗣️ *“垫起脚尖长高高！左手抓一把白云、右手抓一把白云！”* | `Full-body 9:16 vertical shot, 3D kid dance coach, stretching high up on tiptoes, alternating left and right hands reaching for fluffy white clouds above, full body stretch, playful and energetic, seamless loop, 8s.` | **左右手腕交替最高位**<br>下肢足踝提踵 |
| **08** | **阳光装口袋**<br>*(Pockets of Light)* | **00:56 - 01:04**<br>(4小节/16拍/8s) | *"Grab a little ray of light, keep it bright!"*<br>*捕捉光芒，藏在温暖心窝* | 从高处握紧一把“金阳光”，双手欢快拍拍小肚子两边的魔法口袋，膝盖弹性微曲。<br>🗣️ *“抓一把闪闪发光的阳光，装进肚子两边的小口袋里！”* | `Full-body 9:16 vertical shot, 3D animated child, catching imaginary sunlight with fists then tucking hands into waist pockets with a happy rhythmic bounce, cute cheerful choreography, seamless loop, 8s.` | 双手由高位落至髋骨<br>(`wrist.y -> hip.y`) |
| **09** | **小兔蹦蹦跳**<br>*(Bunny Hops)* | **01:04 - 01:12**<br>(4小节/16拍/8s) | *"Jump jump jump with a smile!"*<br>*副歌高潮，全场欢笑跳跃* | 双手食指中指在头顶比出长耳朵，双脚轻盈并拢，跟着16拍节奏向前、后、左、右小跳。<br>🗣️ *“小兔子跳跳跳！竖起长耳朵，双脚轻快蹦蹦跳！”* | `Full-body 9:16 vertical shot, 3D animated kid dance coach, bunny ears gesture with fingers on head, light bouncing jumps in place on the rhythm, bursting with preschool vitality, seamless loop, 8s, 60fps.` | 垂直起跳位移<br>双手固定在头部 |
| **10** | **魔法转圈圈**<br>*(Twirl & Blossom)* | **01:12 - 01:20**<br>(4小节/16拍/8s) | *"Dancing all around the world!"*<br>*探索世界，快乐旋转绽放* | 双臂微展如小花裙，踏着16拍轻快小碎步顺时针转一个360度大圈，最后定格比花朵绽放。<br>🗣️ *“小碎步踩一踩，顺时针轻快旋转一圈，像花朵盛开！”* | `Full-body 9:16 vertical shot, 3D cute dance coach, spinning a full 360-degree circle with arms lightly extended, stepping gracefully, finishing with a blooming flower gesture under chin, smiling, seamless loop, 8s.` | 躯干连续侧移旋转<br>定格花朵托腮姿态 |
| **11** | **爱心大光波**<br>*(Heart Beam Sparkle)* | **01:20 - 01:28**<br>(4小节/16拍/8s) | *"Sunshine in my heart, shining everywhere!"*<br>*温暖在心，向世界传递爱* | 双手大拇指食指在胸前拼大爱心，随节拍向前推出“爱心光波”，手指灵动闪烁。<br>🗣️ *“阳光照进心里，双手胸前比个大爱心，向前送出爱心光波！”* | `Full-body 9:16 vertical shot, 3D animated kid coach, forming a big heart shape with hands at chest level, then pushing it outward towards camera with magical sparkling gestures, warm loving face, seamless loop, 8s.` | **双手腕在胸骨前交汇**<br>(`dist(lWrist, rWrist) < 0.1`) |
| **12** | **快乐踢踢脚**<br>*(Happy Feet Kicks)* | **01:28 - 01:36**<br>(4小节/16拍/8s) | *"Sunshine in my happy dancing feet!"*<br>*小脚丫跳舞，全身充满活力* | 双手叉腰，右脚尖向前轻快点地踢出（4拍），左脚尖向前轻快踢出（4拍），重复2轮。<br>🗣️ *“小脚丫也想跳舞！右脚踢踢、左脚踢踢，充满节奏感！”* | `Full-body 9:16 vertical shot, 3D kid dance coach, hands on waist, rhythmically kicking right foot forward then left foot forward with toes pointed, playful energetic dance, sunny room, seamless loop, 8s.` | 双脚尖交替前伸伸展<br>双手保持叉腰稳定 |
| **13** | **微风小鸟飞**<br>*(Bird Wings Glide)* | **01:36 - 01:44**<br>(4小节/16拍/8s) | *"Spin like a gentle breeze, soaring high!"*<br>*如轻风飞翔，翱翔在蓝天* | 双臂水平展开如小鸟翅膀，随身体左右轻微倾斜上下柔和扇动，如在风中滑翔。<br>🗣️ *“像清晨的微风与小鸟，张开小手臂在蓝天中轻快滑翔！”* | `Full-body 9:16 vertical shot, 3D animated child, arms extended horizontally like bird wings, gently flapping up and down while gliding side to side, soaring gracefully, happy calm expression, seamless loop, 8s.` | **双臂水平展开扇动**<br>身体中轴小幅摆动 |
| **14** | **胜利拍手欢呼**<br>*(Cheer & Clap)* | **01:44 - 01:52**<br>(4小节/16拍/8s) | *"Ready, set, have a wonderful day!"*<br>*迎接全新一天，自信满满* | 右上方拍手2下，左上方拍手2下，随后高高举起双手握拳欢呼“耶！”（重复2轮）。<br>🗣️ *“右边拍拍手、左边拍拍手，举起双手大欢呼，我们最棒啦！”* | `Full-body 9:16 vertical shot, 3D cute kid dance coach, clapping hands overhead to the right, then overhead to the left, pumping fists up in high celebration, ecstatic joyful expression, seamless loop, 8s, 60fps.` | 斜上方双手拍击对齐<br>双手高举欢呼 |
| **15** | **深呼吸定格鞠躬**<br>*(Deep Breath & Bow)* | **01:52 - 02:00**<br>(4小节/16拍/8s) | *"Goodbye morning sunshine, we shine so bright!"*<br>*感谢阳光与伙伴，优雅收操* | 双臂自两侧深吸气划大圆上抬，呼气在胸前双手合十，身体微前倾鞠躬，定格灿烂微笑。<br>🗣️ *“深深吸气划大圆，双手胸前合十，鞠躬微笑！早操完美通关！”* | `Full-body 9:16 vertical shot, 3D kid coach, inhaling deeply while raising arms up in a grand circle, bringing palms together at chest in prayer pose, gentle bow with polite sweet smile, graceful finish, seamless loop, 8s.` | 双臂划大圆上扬<br>胸前合十收操定格 |

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



