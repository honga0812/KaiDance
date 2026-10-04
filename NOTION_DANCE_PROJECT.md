# ☀️ 奇妙星律動：兒童 AI 趣味火柴人舞蹈樂園 (Kids AI Stickman Dance World)

> 💡 **項目簡介**：專為 4~6 歲（幼兒園中大班、家庭親子）設計的全場景體感舞蹈教學系統。融合 **入鏡自動變身趣味發光火柴人**、**23 支動作專屬循環示範動畫影片**、**1~3 人多人員體態骨架追蹤**、**名師原聲童趣引導口令** 與 **卡拉OK式同步歌詞**，支援電視大螢幕全螢幕跟跳與動作自動評分，並已完全就緒支援部署到 GitHub Pages 公開使用。
> 
> 📅 **最新更新**：2026-10-05 (v3.8.0 - 繁體中文全介面適配、8-12拍具象動作引導、SRT精準毫秒對齊、AI影片提示詞全景矩陣)  
> 🏷️ **標籤**：`兒童教育` `AI編舞` `發光火柴人` `骨架追蹤` `AI影片生成` `GitHubPages` `Kai_Music` `繁體中文`  
> 📁 **本地運行服務**：`http://localhost:8080/`

---

## 🤸 一、 趣味發光火柴人（Cute Stickman Avatar）體態捕捉系統

針對低齡兒童特別喜歡的「火柴人」形象，徹底改造了視覺骨骼渲染邏輯：

```
┌────────────────────────────────────────────────────────┐
│  【攝影機鏡頭畫面（鏡像）】                              │
│                                                        │
│                    🌿 (小嫩芽天線，隨身體搖晃)           │
│                  ╭──────╮                              │
│                  │ ^  ^ │  <-- 萌萌的大眼睛 (笑臉頭部)    │
│                  │  ◡   │                              │
│                  ╰──────╯                              │
│                   / || \                               │
│        (左手星星) ★  ||  ★ (右手星星，舉高發翡翠綠光)     │
│                    /  \                                │
│                   d    b   <-- 圓潤發光小鞋子          │
│                                                        │
│   核心機制：                                            │
│   1. 當畫面無小朋友時，提示「快站到鏡頭前變身火柴人！」；       │
│   2. 小朋友一入鏡，火柴人立刻依附在身體上，四肢完全跟隨運動； │
│   3. 手臂舉高托起太陽或左右擺動時，火柴人瞬間綻放綠光與星星！ │
│   4. 支援【暖陽金 / 極光綠 / 糖果粉】三套炫酷火柴人皮膚！     │
└────────────────────────────────────────────────────────┘
```

---

## 🎬 二、 官方英文歌詞與動作要領提示矩陣（對齊音樂結構與 120 BPM 節奏）

### 1. 音樂速度與節拍物理規格（BPM = 120）
- **曲速**：120 BPM（每分鐘 120 拍）
- **每拍時長**：0.50 秒
- **4 拍（1 小節）**：2.0 秒
- **8 拍（2 小節）**：4.0 秒（多數分句動作長度）
- **12 拍（3 小節）**：6.0 秒（長句與副歌過門動作長度）
- **16 拍（4 小節）**：8.0 秒（前奏與間奏旋轉動作長度）

### 2. 具象童趣動作引導設計原則
1. **富有畫面感的情境隱喻**：
   - 幼兒在抽象指令下難以配合，必須採用**具體、生活化、充滿想像力的情境動作**（例如：「伸手向上抓取白雲放到口袋」、「雙手托起大太陽暖洋洋」、「小牙刷刷刷刷露出笑臉」、「背起小書包戴上小圓帽」、「跟貪睡小貓說拜拜」）。
2. **在 8-12 拍之內清晰表達**：
   - 引導口令在前 4~6 拍（約 2.0~2.5 秒）清脆有力地下達完畢，後 4~6 拍純留給小朋友聆聽音樂、觀察示範影片並盡情跟跳，徹底杜絕口令撞車與重疊。
3. **自然生動、情緒起伏飽滿的引導語氣**：
   - 像幼兒園明星領操老師一樣，充滿愛心與元氣，抑揚頓挫、帶動力極強！

---

### 3. 《Morning Sunshine Hello》官方歌詞、精準時間、具象口令與 AI 影片提示詞全景矩陣表（23 段）

| 序號與段落 | SRT 精確時間 | 節拍數與長度 | 官方英文歌詞 | 具象童趣名師口令 (8-12拍清晰引導) | 動作要領引導說明 (Movement Tips) | 配合影片動畫製作提示詞 (Video Prompts) | 骨骼捕捉識別重點 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **[Intro]<br>動作 01** | `00:00.00 - 00:07.87` | **16 拍**<br>(7.87s) | `[Intro] 🎵 Musical Awakening` | **「小手插腰，踩著拍子踏步走！」** | **晨光萌芽踏步**<br>⏰ 倒數預備！小手插腰，像精神的小士兵踩著節拍原地踏步！ | `Full-body 9:16 vertical shot, 3D animated preschool dance coach Leo in bright sunny tracksuit, marching energetically on place with hands on hips, bouncy knee lifts to 120 BPM tempo, warm smile, bright kindergarten studio, seamless loop, 8s.` | 髖膝垂直位移<br>雙腿交替抬起 |
| **[Verse 1]<br>動作 02** | `00:07.87 - 00:11.93` | **8 拍**<br>(4.06s) | `"Good morning sun, up in the sky,"` | **「雙手托起大太陽，暖洋洋！」** | **托起金色太陽**<br>☀️ 太陽升起啦！小手從胸口慢慢推上天空，捧出發光大太陽！ | `Full-body 9:16 vertical shot, 3D cute kid dance coach, bringing hands from chest up above head to hold a big imaginary glowing sun in the sky, fingers spread wide, tiptoe stretch, smiling radiantly, seamless loop, 8s.` | **雙手腕高過頭部**<br>(`y_wrist < y_head`) |
| **[Verse 1]<br>動作 03** | `00:11.93 - 00:15.97` | **8 拍**<br>(4.04s) | `"Waving your golden hands so high!"` | **「金色大光芒，左右大招手！」** | **金色大手高招手**<br>✨ 我們是太陽的金色光芒！雙手高舉過頭頂，向左招手、向右招手！ | `Full-body 9:16 vertical shot, 3D animated dance coach, arms stretched high overhead, waving both hands energetically from side to side like golden rays shining across the morning sky, joyful expression, seamless loop, 8s.` | **雙臂高舉大幅擺動**<br>(`y_wrist < y_head`) |
| **[Verse 1]<br>動作 04** | `00:15.97 - 00:19.73` | **8 拍**<br>(3.76s) | `"Wake up, brush your teeth and smile,"` | **「小牙刷刷刷刷，露出笑臉大聲笑！」** | **刷刷小牙大微笑**<br>🪥 小拳頭變身牙刷，上上下下刷乾淨，露出白白牙齒嘻嘻笑！ | `Full-body 9:16 vertical shot, 3D cute preschool coach, rubbing sleepy eyes cutely, making fun toothbrush brushing gestures across teeth with one hand, pointing to a huge sunny smile with the other hand, seamless loop, 8s.` | 單手近嘴部擺動<br>手指點向嘴角笑臉 |
| **[Verse 1]<br>動作 05** | `00:19.73 - 00:23.77` | **8 拍**<br>(4.04s) | `"Let’s go learn and play a while!"` | **「邁開大步，出發去探險做遊戲！」** | **歡快邁步去探險**<br>🎒 精神抖擻！雙手插腰大步往前踏，準備出發學本領、玩遊戲！ | `Full-body 9:16 vertical shot, 3D animated child coach, hands on hips, marching enthusiastically forward with rhythmic high knees, excited and cheerful expression, bright studio, seamless loop, 8s.` | 膝蓋高抬踏步<br>雙腳輕快交替 |
| **[Verse 1]<br>動作 06** | `00:23.77 - 00:27.73` | **8 拍**<br>(3.96s) | `"Birds are singing in the tree,"` | **「雙臂輕輕拍，學小鳥展翅高飛！」** | **樹上小鳥展翅飛**<br>🐦 手臂變成彩色羽毛翅膀，輕輕拍動，飛到大樹上跳舞！ | `Full-body 9:16 vertical shot, 3D kid dance coach, extending arms horizontally like bird wings, flapping gently and gracefully up and down, bouncing gently on toes, smiling, seamless loop, 8s.` | **雙臂水平展開扇動**<br>手腕輕柔起伏 |
| **[Verse 1]<br>動作 07** | `00:27.73 - 00:33.37` | **12 拍**<br>(5.64s) | `"Singing a morning song for me!"` | **「小手貼耳朵，聽聽小鳥唱晨曲！」** | **聆聽晨曲與蓄力**<br>🎶 一隻小手輕輕貼在耳邊，身體左右搖擺，靜靜聽小鳥唱歌！ | `Full-body 9:16 vertical shot, 3D cute preschool coach, cupping one hand behind ear to playfully listen to music, swaying torso and hips gently from side to side in 120 BPM rhythm, happy expression, seamless loop, 8s.` | 軀幹左右微傾<br>單手貼耳側傾聽 |
| **[Chorus]<br>動作 08** | `00:33.37 - 00:37.80` | **8 拍**<br>(4.43s) | `"Hello, hello, it's a brand new day!"` | **「熱情招招手，跟新的一天說哈囉！」** | **熱情招手說哈囉**<br>👋 站直身體，一隻手叉腰，另一手向外大畫半圓大聲說 Hello！ | `Full-body 9:16 vertical shot, 3D animated dance coach, dynamic waving motion with right hand drawing wide circle greeting friends enthusiastically, left hand on hip, wide joyful smile, seamless loop, 8s.` | **單側手肘高位招手**<br>(`wrist.y < neck.y`) |
| **[Chorus]<br>動作 09** | `00:37.80 - 00:41.60` | **8 拍**<br>(3.80s) | `"Jump up and shout: Hip-hip-hooray!"` | **「用力蹦起來！雙手高舉喊萬歲！」** | **歡呼起跳大萬歲**<br>🌟 雙膝微彎蓄力，雙腳用力向上一跳，雙手衝天高喊萬歲！ | `Full-body 9:16 vertical shot, 3D preschool coach, bending knees and exploding into an energetic celebratory jump, both fists pumped up in the air shouting hooray, radiant smile, seamless loop, 8s.` | **垂直起跳位移**<br>雙手高舉歡呼 |
| **[Chorus]<br>動作 10** | `00:41.60 - 00:45.70` | **8 拍**<br>(4.10s) | `"Put on your shoes and count to three,"` | **「彎腰摸摸小鞋子，伸指數一二三！」** | **穿上小鞋數一二三**<br>👟 彎腰輕拍左右小鞋子，站起來手指俏皮點數：一、二、三！ | `Full-body 9:16 vertical shot, 3D animated coach, bending smoothly to touch left shoe then right shoe, popping back up and counting 1-2-3 with cute finger gestures, cheerful and lively, seamless loop, 8s.` | 俯身觸踝動作<br>手指胸前比數字 |
| **[Chorus]<br>動作 11** | `00:45.70 - 00:51.40` | **12 拍**<br>(5.70s) | `"Come along and sing"` | **「張開雙手，邀請好朋友一起唱！」** | **牽手齊唱早安曲**<br>🎶 雙手像花朵向兩側熱情盛開，踩著節拍邀請好朋友一起唱！ | `Full-body 9:16 vertical shot, 3D kid coach, extending both arms wide forward in a warm welcoming embrace gesture, inviting everyone to sing along, gentle torso sway, seamless loop, 8s.` | 雙手向前平舉展開<br>掌心朝上熱情相邀 |
| **[間奏]<br>動作 12** | `00:51.40 - 00:59.87` | **16 拍**<br>(8.47s) | `"with me!" [Interlude 旋律間奏]` | **「手叉小蠻腰，輕輕轉個歡樂圓圈！」** | **歡樂旋轉小圓舞**<br>🌸 雙手插腰踩小碎步，輕快轉一個大圓圈，轉完站定比朵花！ | `Full-body 9:16 vertical shot, 3D animated coach, spinning a full graceful 360-degree circle with hands on hips and light tiptoes, striking a cute blooming flower pose under chin at the finish, seamless loop, 8s.` | 軀幹圓周位移<br>定格笑臉展開 |
| **[Verse 2]<br>動作 13** | `00:59.87 - 01:03.93` | **8 拍**<br>(4.06s) | `"Pack your bag and grab your hat,"` | **「背起小書包，戴上遮陽小圓帽！」** | **背起書包戴小帽**<br>🎒 雙手拉住書包背帶拍拍肩膀，再舉高雙手輕摸頭頂戴正帽子！ | `Full-body 9:16 vertical shot, 3D cute preschool coach, mimicking putting on backpack straps with proud shoulder taps, then patting head to adjust an adorable imaginary sun hat, confident posture, seamless loop, 8s.` | 雙手拉肩帶姿勢<br>雙手拍撫頭部小帽 |
| **[Verse 2]<br>動作 14** | `01:03.93 - 01:07.77` | **8 拍**<br>(3.84s) | `"Wave goodbye to the sleepy cat!"` | **「學貓咪揉揉眼，跟貪睡小貓說拜拜！」** | **告別貪睡小懶貓**<br>🐱 雙手變貓爪揉揉小臉蛋，再向斜下方輕輕揮手跟懶貓咪說拜拜！ | `Full-body 9:16 vertical shot, 3D preschool coach, mimicking a cute kitten rubbing whiskers with soft paws, then gently waving goodbye diagonally downward, playful expression, seamless loop, 8s.` | 雙手貓爪握拳揉頰<br>輕柔向斜下方揮手 |
| **[Verse 2]<br>動作 15** | `01:07.77 - 01:11.57` | **8 拍**<br>(3.80s) | `"Look outside, the sky is blue,"` | **「伸手向上抓取白雲放口袋，抬頭看藍天！」** | **抓取白雲放入口袋**<br>☁️ 墊起腳尖伸手向上抓一把柔軟白雲塞進口袋，單手遮眉望藍天！ | `Full-body 9:16 vertical shot, 3D animated kid, reaching high overhead on tiptoes to grab fluffy imaginary white clouds and tucking them into clothes pocket, then shielding brow to look up at blue sky, joyful wonder, seamless loop, 8s.` | 單手搭額前遠眺<br>單手高舉抓雲塞口袋 |
| **[Verse 2]<br>動作 16** | `01:11.57 - 01:17.33` | **12 拍**<br>(5.76s) | `"So many fun things waiting for you!"` | **「雙臂畫大圓，胸前比出跳動大愛心！」** | **快樂愛心大擁抱**<br>💖 雙臂在空中環抱大自然，收在胸口拼出跳動的大愛心送出去！ | `Full-body 9:16 vertical shot, 3D kid coach, gathering arms in a wide circle embracing the world, bringing hands together at chest to form a glowing heart shape, pulsing with joy, seamless loop, 8s.` | **雙手腕在胸骨前交匯**<br>(`dist(lWrist, rWrist) < 0.1`) |
| **[Chorus]<br>動作 17** | `01:17.33 - 01:21.87` | **8 拍**<br>(4.54s) | `"Hello, hello, it's a brand new day!"` | **「雙腳小跳步，雙手交替大招手！」** | **再度熱情大招手**<br>👋 雙腳踩節奏踏跳，雙手在耳側交替像波浪一樣大幅度招手！ | `Full-body 9:16 vertical shot, 3D animated dance coach, bouncing lightly on balls of feet, waving both hands alternately beside ears with huge energy and contagious laughter, seamless loop, 8s.` | **雙耳側連續大幅揮手**<br>雙腳輕跳律動 |
| **[Chorus]<br>動作 18** | `01:21.87 - 01:25.60` | **8 拍**<br>(3.73s) | `"Jump up and shout: Hip-hip-hooray!"` | **「深蹲彈跳起飛！雙手握拳喊耶！」** | **深蹲起跳大爆發**<br>🐰 蹲下蓄力、高高蹦跳！小拳頭在頭頂綻放爆米花，大喊耶！ | `Full-body 9:16 vertical shot, 3D preschool coach, performing a deep energetic crouch and springing up into a star jump in the air, shouting with pure delight, confetti effect, seamless loop, 8s.` | **高跳位移峰值**<br>雙臂高舉歡呼 |
| **[Chorus]<br>動作 19** | `01:25.60 - 01:29.80` | **8 拍**<br>(4.20s) | `"Put on your shoes and count to three,"` | **「小手插腰，左右小腳尖輕輕點地！」** | **動感腳尖踢點步**<br>👟 雙手插腰站穩，左右腳尖輪流往前踩小水坑，踢一踢點一點！ | `Full-body 9:16 vertical shot, 3D animated kid, hands firmly on hips, playfully tapping alternating toes forward on the ground to 120 BPM drum beats, charming and rhythmic, seamless loop, 8s.` | 左右腳前踢點步<br>身體輕快律動 |
| **[Chorus]<br>動作 20** | `01:29.80 - 01:35.37` | **12 拍**<br>(5.57s) | `"Come along and sing"` | **「跟著大重音，整整齊齊拍拍手！」** | **歡快齊聲拍拍手**<br>👏 踩著歡樂重音在胸前大聲拍手：啪！啪！啪！身體快樂彈動！ | `Full-body 9:16 vertical shot, 3D animated coach, clapping hands right in front of chest in sync with snappy snare beats, laughing and bouncing happily, seamless loop, 8s.` | 胸前雙手合拍碰觸<br>節拍清晰響應 |
| **[Bridge]<br>動作 21** | `01:35.37 - 01:43.87` | **16 拍**<br>(8.50s) | `"with me!" [Bridge 宏大過門]` | **「展開白鴿翅膀，像微風在天空滑翔！」** | **白鴿展翅大滑翔**<br>🕊️ 雙手水平張開像大鳥滑翔，腳踩小碎步輕柔起伏，微風吹過來！ | `Full-body 9:16 vertical shot, 3D kid coach, arms stretched wide like a majestic soaring dove gliding in the gentle breeze, floating on light tiptoes, cinematic studio light, seamless loop, 8s.` | **雙臂水平展開扇動**<br>身體中軸圓周位移 |
| **[Outro]<br>動作 22** | `01:43.87 - 01:47.73` | **8 拍**<br>(3.86s) | `"Good morning, world!"` | **「雙臂畫出大金色圓圈，擁抱全世界！」** | **擁抱全世界早安**<br>🌍 雙臂向外展開畫出最大的金色大圓，挺胸抬頭向世界道早安！ | `Full-body 9:16 vertical shot, 3D animated dance coach, sweeping arms out and up in a massive welcoming circle embracing the universe, chest high, radiant joyful expression, seamless loop, 8s.` | 雙臂展開最大開角<br>頭胸挺拔舒展 |
| **[Outro]<br>動作 23** | `01:47.73 - 02:00.00` | **24 拍**<br>(12.27s) | `"Let's have fun today!"` | **「雙手合十胸前鞠躬，定格燦爛大微笑！」** | **燦爛定格大比心**<br>🌟 深呼吸雙臂上揚，雙手胸前合十或頭頂大比心，燦爛微笑定格！ | `Full-body 9:16 vertical shot, 3D preschool coach, inhaling and raising arms in a grand finish arc, bringing palms together at heart with a sweet gentle bow and winning smile, golden star sparkle finish, seamless loop, 8s.` | 雙臂頭頂合十比心<br>華麗定格笑臉 |

---

### 4. AI 影片動畫批次生成標準 Master Prompt 模板（Runway Gen-3 / Luma / Kling / Minimax）

為保證生成的 23 支示範動畫影片在人物長相、服裝、光影與背景畫風上 **100% 保持統一**，生成時請直接套用以下 Master Prompt 模板：

```text
[Master Style Prompt]:
Full-body 9:16 vertical framing, master animation 3D Disney Pixar style, a cheerful 5-year-old preschool dance coach named Leo (cute boy with short brown hair, wearing bright orange-blue athletic hoodie, white sneakers) OR Mia (sweet girl with twin pigtails, pink-yellow star tracksuit). Inside a warm, sunlit kindergarten dance studio with pastel rainbow floor and large floor-to-ceiling windows showing green trees and blue sky. Studio soft morning lighting, clean background, perfectly centered full body from head to shoes, child-friendly atmosphere.

[Action Instruction]:
{填入上方表格對應行中的英文提示詞}

[Parameters]:
- Duration: 8 seconds (Seamless Loop, 120 BPM tempo)
- Aspect Ratio: 9:16 (Vertical)
- Frame Rate: 60fps / 30fps
- Negative Prompt: blurry, distorted limbs, extra fingers, deformed face, flickering, sudden cut, horizontal bars, cropped head, cropped feet, text, watermark.
```

---

## 🚀 三、 GitHub & GitHub Pages 公開部署指南

本地倉庫已完成全套靜態資源編譯與 Git 提交（包含多人員體態火柴人與繁體中文所有介面），只需一條命令即可推送到 GitHub：

```bash
cd "/Volumes/4T M2 SSD/AI Native Company OS/Kai_Music"

# 1. 運行一鍵部署腳本（填入你的 GitHub 倉庫地址）
./deploy_to_github.sh https://github.com/<你的GitHub用戶名>/kai-music-ai-dance.git

# 2. 前往 GitHub 倉庫 Settings -> Pages
#    Source 選擇 Deploy from a branch
#    Branch 選擇 main, Folder 選擇 /docs -> 點擊 Save 保存！
# 3. 約 1 分鐘後即可在全球公開訪問：https://<用戶名>.github.io/<倉庫名>/
```

---

## 🔬 四、 攝影鏡頭人體追蹤與火柴人節點專項檢查與全面升級

針對您提出的**「開啟鏡頭後抓取人物並轉化為發光火柴人節點」**的實際效果，我們進行了深度測試與演算法重構，徹底解決以下隱患：

1. **鏡像反轉手部交叉 Bug 修復**：
   - 原先在鏡像影片渲染時，由於水平翻轉計算未對齊螢幕物理左右，導致舉起右手時火柴人左手臂發生交叉。
   - **已修復**：重寫螢幕鏡像座標映射系統，確保真實右手（螢幕右側）嚴格驅動火柴人右手臂與手掌，左手驅動左手臂，完全鏡像對齊。
2. **站定不動時火柴人消失/閃爍問題徹底解決**：
   - 原先僅對比相鄰幀間差異，當小朋友站在鏡頭前定格擺動作時，幀差變小會導致誤判「無人入鏡」而閃爍或回退為虛線框。
   - **已修復**：引入自適應背景差分模型（Adaptive Background Model）與置信度平滑衰減累加器（Presence Confidence Accumulator），即使小朋友站定定格數秒，火柴人依然穩固鎖住，絕不丟幀閃爍。
3. **雙引擎自適應驅動 (MediaPipe Pose AI + 端側視覺引擎)**：
   - **MediaPipe Pose 引擎**：單人模式下支援偵測人體 33 個 3D 骨骼與手指節點（鼻子、眼、雙肩、雙肘、雙手腕、左右手指食指、雙膝、雙腳踝），手指手部動作細膩逼真。
   - **離線端側視覺引擎**：多人模式或離線狀態下無縫自動降級保障，保證任何環境 100% 順暢運行。
4. **影片 object-cover 比例精確校準**：
   - 徹底消除了攝影鏡頭畫面（如 16:9 / 4:3）在不同螢幕尺寸裁剪時的座標位移差，火柴人的頭部、肩部、四肢 100% 貼合在小朋友的真人員體態上。
5. **萌趣發光視覺升級**：
   - 頭頂嫩芽會隨動作動態晃動，臉部帶有可愛紅暈腮紅與笑臉。
   - 動作高舉到位時，眼睛自動變閃亮星星眼 `★ ★`，雙掌爆出金色星光與即時連擊加分！

---

## 🎨 五、 視覺比例重構與普通視窗追蹤Bug徹底修復

針對您提出的**「非全螢幕時無法捕捉人物」**以及**「攝影鏡頭佔比較大、示範人物縮小至左側1/3並以9:16長形裁剪（不壓縮）」**的需求，已完成以下重構：

1. **徹底解決「只有點全螢幕才能抓到火柴人」的問題**：
   - 在 `renderStickmanLoop()` 每一幀加入動態幾何校準，並在進入房間時通過 `ResizeObserver` 即時監聽父容器像素；
   - 取消 MediaPipe 對端側視覺引擎的阻斷，無論是否開啟全螢幕、視窗被拖動為任意尺寸，**普通視窗下毫秒級直接鎖定人物並附著火柴人**；
   - 選歌進入房間後**自動無感拉起攝影機**，無需小朋友或家長手動找按鈕開啟。

2. **畫面比例重構（左側 1/3 示範，右側 2/3 大螢幕互動）**：
   - 整體佈局升級為專業舞蹈演播室格局：
     - **左側示範區域**：縮減為優雅的 **1/3** 緊湊示範台（`lg:col-span-1`）；
     - **右側攝影區域**：擴充為 **2/3** 寬敞大舞台（`lg:col-span-2`），給小朋友留出最大的跳舞與手臂揮動空間。

3. **示範動作 9:16 豎屏原畫居中裁剪（拒絕橫向壓扁變形）**：
   - 示範影片外層採用標準的 `aspect-[9/16]` 豎屏長形畫框；
   - 影片內部採用 CSS `object-cover object-center` **純淨原畫居中裁剪**，保留人物 1:1 的身體原畫長寬比，**杜絕任何壓扁、拉伸或變形**，讓舞蹈教練的肢體形態纖細自然、動作清晰易學！

---

## 👥 六、 多人模式（2人/3人）獨立體態偵測技術機制說明與解耦升級

針對您提出的**「選兩個人或三個人時，是真正偵測不同人，還是只是偵測同一個人克隆同步動作」**的關鍵疑問，已完成演算法全面重構：

### 1. 空間扇區解耦獨立多人員體態偵測系統（Multi-Person Spatial Sector Tracking）
徹底實現了**「不同小朋友、獨立骨骼節點、獨立姿態反應」**：
- **2 人模式（雙人對舞/親子同樂）**：
  - 畫面空間自動解耦為**左半區（Zone 1: `0.0~0.52`）** 與 **右半區（Zone 2: `0.48~1.0`）**；
  - **P1 樂樂（暖陽金）** 嚴格綁定站在左側的小朋友；
  - **P2 歡歡（極光藍）** 嚴格綁定站在右側的小朋友；
  - **完全解耦獨立動作**：當左邊小朋友舉起左手時，**只有 P1 舉手**；右邊小朋友在做揮手或跳躍時，**P2 會做出專屬右邊小朋友的動作**，互不干擾！
- **3 人模式（三人齊舞/同伴派對）**：
  - 空間細分為 **左（`0.0~0.38`）**、**中（`0.32~0.68`）**、**右（`0.62~1.0`）** 三個獨立偵測走廊；
  - P1、P2、P3 分別由三位小朋友各自獨立驅動。
- **獨舞伴舞保護機制（智慧降級）**：
  - 如果選擇「2人模式」但實際只有 1 個小朋友站在左側，右側區域未檢測到人時，右側火柴人會優雅保持在專屬待命站位輕柔打招呼，作為可愛的「AI 伴舞同伴」，絕不會出現莫名重疊或亂晃。
