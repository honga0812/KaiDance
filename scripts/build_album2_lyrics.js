const fs = require("fs");
const path = require("path");

// 1. Load Cues
const cuesData = JSON.parse(fs.readFileSync("/tmp/album2_cues.json", "utf8"));

// 2. High-quality Traditional Chinese guidance metadata for each song and cue
const trackMeta = {
  a2_s01: {
    intro: { title: "[前奏] 派對晨光蓄力預備", sub: "🌟 雙手插腰精神好，原地踩著動感鼓點預備！", pose: "march" },
    cues: [
      { title: "雙手彈動數一二", sub: "🎸 雙手像彈吉他輕快撥動，跟著節奏數一二！", pose: "march" },
      { title: "閃耀出發向前衝", sub: "✨ 雙臂向前用力揮出，大喊 Let's Go 出發！", pose: "reach" },
      { title: "晨光敲打小窗台", sub: "☀️ 抬頭仰望，雙手在眼前輕輕敲響晨光窗台！", pose: "reach" },
      { title: "時鐘滴答早安到", sub: "⏰ 雙臂像時針左右擺動，滴答滴答早安來！", pose: "sway" },
      { title: "音響重音大蹦跳", sub: "🎵 雙腳踩節奏，跟著重低音高高跳起來！", pose: "jump" },
      { title: "門外魔法在等待", sub: "🚪 雙手推開神奇大門，迎接滿滿魔法！", pose: "reach" },
      { title: "一步一步三二一", sub: "👟 雙腳一步一步向前踩，大聲數 3、2、1！", pose: "march" },
      { title: "金色太陽升起來", sub: "☀️ 雙手從胸前向上托起，大太陽高高升起！", pose: "sun_rise" },
      { title: "感受律動聽聲音", sub: "👂 小手貼在耳朵旁，身體隨著鼓點輕輕彈動！", pose: "sway" },
      { title: "歡樂轉個大圓圈", sub: "🌀 雙手張開轉個漂亮大圓圈，站定比個耶！", pose: "jump" },
      { title: "預備起步閃耀光", sub: "⭐ 雙手胸前交叉後向外展開，迎接嶄新一天！", pose: "sun_rise" },
      { title: "鑽石一般閃亮亮", sub: "💎 雙手比出閃亮小星星，全身耀眼發光！", pose: "wave" },
      { title: "雙手高舉摸藍天", sub: "☁️ 雙臂向上全力伸直，腳尖墊起摸摸藍天！", pose: "reach" },
      { title: "萬物為你閃晶晶", sub: "✨ 雙手由上往下畫出星光小雨，亮晶晶！", pose: "wave" },
      { title: "啦啦啦啦閃耀光", sub: "🎶 拍拍小手左右踩點，啦啦啦啦放聲唱！", pose: "march" },
      { title: "啦啦啦啦晨光照", sub: "🌅 雙手像微風左右搖擺，迎接溫暖晨光！", pose: "sway" },
      { title: "白雲變出奇妙形", sub: "☁️ 雙手在空中畫出大雲朵，猜猜變出什麼！", pose: "wave" },
      { title: "摘下草莓紫葡萄", sub: "🍇 雙手上下採摘甜莓果，放進美味野餐籃！", pose: "reach" },
      { title: "微笑漫步大街上", sub: "👟 雙手插腰精神邁步，臉上掛著甜甜微笑！", pose: "march" },
      { title: "一路跳舞向前行", sub: "💃 跟著節奏盡情跳舞，每一步都是快樂！", pose: "jump" },
      { title: "齊聲歡呼大喊耶", sub: "🎉 雙臂向上揮舞，開心大喊 Woo！", pose: "jump" },
      { title: "跳躍邁步閃星光", sub: "⭐ 下蹲起跳，踢踢小腳，閃亮星光齊舞！", pose: "jump" },
      { title: "預備起步閃耀光", sub: "🌟 雙手胸前交叉再展開，全新一天火力全開！", pose: "sun_rise" },
      { title: "鑽石閃亮齊狂歡", sub: "💎 雙手高高揮舞，像鑽石般閃耀全場！", pose: "wave" },
      { title: "雙手高舉摸藍天", sub: "☁️ 伸長小手臂，向著晴朗藍天用力招手！", pose: "reach" },
      { title: "專屬你的閃亮秀", sub: "✨ 雙手環繞胸前比個心，全場為你喝采！", pose: "heart" },
      { title: "啦啦啦啦閃耀光", sub: "🎶 雙腳打節拍，啦啦啦啦歡樂合唱！", pose: "march" },
      { title: "啦啦啦啦晨光照", sub: "🌅 左右輕柔擺動，享受溫柔晨光撫摸！", pose: "sway" },
      { title: "啦啦啦啦閃耀光", sub: "🌟 雙手畫大圓弧，展現最自信的帥氣動作！", pose: "sun_rise" },
      { title: "晨光定格大微笑", sub: "💖 雙手合十胸前鞠躬，定格最燦爛甜美笑容！", pose: "heart" }
    ]
  },

  a2_s02: {
    intro: { title: "[前奏] 彩虹雲端夢幻預備", sub: "🌸 雙臂像輕柔微風輕輕拂動，漫步粉彩夢境！", pose: "sway" },
    cues: [
      { title: "粉紅棉花糖飄飄", sub: "🍬 雙手像棉花糖輕柔托起，在微風中飄呀飄！", pose: "sway" },
      { title: "黃色檸檬樹梢滴", sub: "🍋 雙臂伸向綠樹梢，接住黃色甜甜小檸檬！", pose: "reach" },
      { title: "小小畫筆蘸深藍", sub: "🎨 拿著神奇小畫筆，蘸進溫柔蔚藍大海！", pose: "wave" },
      { title: "為你畫出小宇宙", sub: "🌌 雙臂在空中畫出大圓弧，創造美麗小宇宙！", pose: "sun_rise" },
      { title: "溫柔色彩旋轉舞", sub: "🌀 腳尖點地輕輕旋轉，柔和色彩旋轉飛揚！", pose: "sway" },
      { title: "黑夜化作溫暖光", sub: "🕯️ 雙手捧起微光，點亮身邊每一個角落！", pose: "heart" },
      { title: "閉上雙眼許個願", sub: "✨ 雙手合十胸前，輕輕閉眼許下甜甜心願！", pose: "heart" },
      { title: "潑灑一道大彩虹", sub: "🌈 雙臂向外大弧度拋灑，劃出一道亮麗彩虹！", pose: "sun_rise" },
      { title: "刷刷畫筆真輕盈", sub: "🖌️ 小手像畫筆輕快左右擺動，刷刷刷！", pose: "wave" },
      { title: "越過繽紛彩虹橋", sub: "🌈 踮起腳尖邁大步，踏上美麗彩虹橋！", pose: "march" },
      { title: "畫出我的小幻想", sub: "🎨 雙手展開畫布，隨心描繪心中的奇妙世界！", pose: "reach" },
      { title: "每種顏色跳跳舞", sub: "💃 每個色彩都在跳舞，左右擺動快樂轉身！", pose: "jump" },
      { title: "珊瑚粉桃薰衣草", sub: "🪻 抬頭看紫霞天空，微風吹拂甜甜花香！", pose: "reach" },
      { title: "甜甜糖果高高飛", sub: "🍭 雙手用力向上拋，看彩色糖果漫天飛舞！", pose: "jump" },
      { title: "甜蜜美好齊讚嘆", sub: "💖 雙手捧臉甜甜笑，感覺無比溫馨幸福！", pose: "heart" },
      { title: "金色亮粉灑畫紙", sub: "✨ 手指輕輕彈灑，將金色星星灑在畫紙上！", pose: "wave" },
      { title: "神奇色彩動感拍", sub: "🎵 踩著節奏輕拍雙手，每個顏色都充滿活力！", pose: "march" },
      { title: "紅黃相映橘光耀", sub: "🍊 雙手在胸前旋轉交融，變出溫暖橘色光芒！", pose: "sway" },
      { title: "美麗故事展現出", sub: "📖 雙手像翻開童話繪本，精彩故事登場！", pose: "reach" },
      { title: "越過繽紛彩虹橋", sub: "🌈 腳步輕快向前跨，漫步在七彩彩虹上！", pose: "march" },
      { title: "畫出我的小幻想", sub: "🎨 雙臂展翅滑翔，讓想像力自在翱翔！", pose: "sway" },
      { title: "每種顏色跳跳舞", sub: "💃 跟著節奏輕跳，粉彩雲端盡情舞動！", pose: "jump" },
      { title: "珊瑚粉桃薰衣草", sub: "🌸 雙手畫圈，沈浸在夢幻柔和花海中！", pose: "sway" },
      { title: "彩色糖果高高飛", sub: "🍬 雙手向上托舉，看糖果雨高高飄落！", pose: "reach" },
      { title: "夢幻傑作大功成", sub: "🎉 雙手叉腰擺出優雅 Pose，我們的傑作完成！", pose: "heart" }
    ]
  },

  a2_s03: {
    intro: { title: "[前奏] 數字派對動感倒數", sub: "🔢 動動手指活動腳尖，數字狂歡派對即刻引爆！", pose: "march" },
    cues: [
      { title: "歡呼吶喊耶耶耶", sub: "🎉 雙手高高揮舞，大聲歡呼 Yeah Yeah Yeah！", pose: "jump" },
      { title: "熱情搖擺耶耶耶", sub: "🎶 身體左右律動，跟著節奏嗨起來！", pose: "sway" },
      { title: "一二三四大倒數", sub: "🔢 伸出手指大聲數：1、2、3、4！", pose: "march" },
      { title: "一二拍拍小舞鞋", sub: "👟 左右小腳尖輕輕點地，拍拍鞋子打節奏！", pose: "march" },
      { title: "三四趕走小煩惱", sub: "💃 扭扭肩膀擺動手臂，把煩惱通通跳開！", pose: "sway" },
      { title: "五塊甜餅排整齊", sub: "🍪 伸出五指像小盤子，排好五塊香甜餅乾！", pose: "reach" },
      { title: "數字寶寶長好快", sub: "🌱 蹲下慢慢長高高，看數字越長越多！", pose: "reach" },
      { title: "能不能數我們行", sub: "🙋 高高舉起小右手：我們能做到，大聲答應！", pose: "reach" },
      { title: "跟著節奏大作戰", sub: "🥁 精神小隊員原地踏步，踩著節拍向前進！", pose: "march" },
      { title: "六七高舉摸摸天", sub: "☁️ 伸出六和七，雙手用力伸長去摸摸天！", pose: "reach" },
      { title: "八九十數字狂歡", sub: "🎉 拍拍手轉個圈，八九十狂歡派對開始！", pose: "jump" },
      { title: "動動身體別遲到", sub: "🏃 扭扭腰、動動腳，跟緊隊伍別掉隊！", pose: "march" },
      { title: "一二三跟我數數", sub: "👏 伸出手指数 1、2、3，大家齊唱真開心！", pose: "march" },
      { title: "跳到左邊跳到右", sub: "↔️ 往左邊輕輕跳一步，再往右邊跳一步！", pose: "jump" },
      { title: "霓虹燈下閃晶晶", sub: "✨ 雙手比出閃亮小星星，霓虹光芒好耀眼！", pose: "wave" },
      { title: "數數天空大氣球", sub: "🎈 抬頭指指天空，一顆兩顆數著彩色氣球！", pose: "reach" },
      { title: "數數身旁小狗狗", sub: "🐶 雙手扮可愛小狗爪，數數幾隻汪汪小狗！", pose: "wave" },
      { title: "快樂相加樂趣多", sub: "➕ 雙手畫大愛心，把所有快樂通通加倍！", pose: "heart" },
      { title: "最強數學特攻隊", sub: "🏆 雙手插腰神氣挺胸，我們是最棒數學小英雄！", pose: "sun_rise" },
      { title: "一二三呼八九十", sub: "🌟 拍手歡呼 Woo，八九十數字大狂歡！", pose: "jump" },
      { title: "動動身體跳起來", sub: "💃 全身一起搖擺，派對舞步嗨到頂點！", pose: "sway" },
      { title: "一二三數得開心", sub: "🎶 牽起身邊好朋友，一二三數得好快樂！", pose: "march" },
      { title: "所有數字通通懂", sub: "🌟 雙手比出大大勝利 V，數字全都學會囉！", pose: "heart" }
    ]
  },

  a2_s04: {
    intro: { title: "[前奏] 叢林重低音大巡遊", sub: "🥁 咚咚咚！叢林鼓點敲響，全體動物隊員準備出發！", pose: "march" },
    cues: [
      { title: "獅子王重音踏步", sub: "🦁 戴上威風王冠，學獅子大王重重踏步！", pose: "march" },
      { title: "長頸鹿高聳入雲", sub: "🦒 雙臂向上伸直像長頸鹿，長高高看大街！", pose: "reach" },
      { title: "猴子樹梢玩規矩", sub: "🐒 雙手學猴子抓抓撓撓，樹梢上盪來盪去！", pose: "wave" },
      { title: "展示叢林新舞步", sub: "🌴 扭動腰部大跳特跳，展示最強野生舞步！", pose: "sway" },
      { title: "大象號角蹦蹦破", sub: "🐘 雙手當大象長鼻子，吹響號角砰砰發射！", pose: "reach" },
      { title: "大家快快來排隊", sub: "🚶 跟緊巡遊隊伍，一二一二快快排好隊！", pose: "march" },
      { title: "拍拍翅膀聽合唱", sub: "🦜 雙臂展開當大鳥翅膀，拍動聽叢林歡唱！", pose: "wave" },
      { title: "動物園巡遊踏步", sub: "🥁 精神抖擻繞圈踏步，巡遊隊伍大步走！", pose: "march" },
      { title: "重低音震動大地", sub: "💥 雙腳重重踩踏，感受地面震撼動感鼓點！", pose: "jump" },
      { title: "重重踏步大聲吼", sub: "🦁 踏踏踏大步走，張開雙手大聲吼 Roar！", pose: "march" },
      { title: "高高躍起藍天下", sub: "☁️ 下蹲蓄力高高跳起，藍天下齊步歡呼！", pose: "jump" },
      { title: "感受熱情野性風", sub: "🌴 雙臂左右搖擺，全身體會滿滿熱情活力！", pose: "sway" },
      { title: "小兔子嘻哈蹦跳", sub: "🐰 雙手放頭頂當兔耳朵，跟著 Hip-Hop 輕快跳！", pose: "jump" },
      { title: "角落準備出擊囉", sub: "🐾 輕輕下蹲縮起身體，準備好下一波爆發！", pose: "march" },
      { title: "酷企鵝戴上墨鏡", sub: "😎 雙手在眼前戴起酷墨鏡，擺出最潮姿勢！", pose: "wave" },
      { title: "陽光泳池濺水花", sub: "💦 雙腳輕輕踢踢水，濺起快樂清涼小水花！", pose: "jump" },
      { title: "重擊銅管節奏踏", sub: "🥁 雙手握拳敲打重節奏，節奏踩點踏步走！", pose: "march" },
      { title: "齊心合力來一段", sub: "🔥 Break it down！身體下壓，擺出最帥動作！", pose: "jump" },
      { title: "動物巡遊繞全場", sub: "🚶 全場邁步大踏步，巡遊隊伍浩浩蕩蕩！", pose: "march" },
      { title: "重低音撼動全場", sub: "💥 感受最燃低音震撼，全身細胞動起來！", pose: "march" },
      { title: "用力踏地高高跳", sub: "⭐ 踏踏踏地動山搖，下蹲後用力跳向天空！", pose: "jump" },
      { title: "藍天下齊步巡遊", sub: "☀️ 仰望晴空，歡笑聲在整個森林迴盪！", pose: "reach" },
      { title: "表現太棒大定格", sub: "🏆 雙手抱胸帥氣微笑，大聲喊出 Good Job！", pose: "heart" }
    ]
  },

  a2_s05: {
    intro: { title: "[前奏] 清潔特攻隊集合", sub: "🧹 拿起小抹布、準備小收納箱，特攻隊出動！", pose: "march" },
    cues: [
      { title: "全體隊員出發囉", sub: "🚀 雙拳緊握向前衝，大喊 Go 全力以赴！", pose: "jump" },
      { title: "迅速蹲下大搜索", sub: "🔍 輕輕蹲下身子，找找地上有沒有小玩具！", pose: "march" },
      { title: "彩色蠟筆收進盒", sub: "🖍️ 雙手撿起小蠟筆，整整齊齊收進盒子裡！", pose: "reach" },
      { title: "故事書籍排書架", sub: "📚 雙手抱起厚繪本，一本一本放回小書架！", pose: "reach" },
      { title: "自己收拾我最棒", sub: "🌟 拍拍小胸脯，我自己整理真能幹！", pose: "heart" },
      { title: "泰迪熊坐小椅子", sub: "🧸 抱緊心愛泰迪熊，溫柔放進專屬小椅子！", pose: "heart" },
      { title: "清涼微風陣陣吹", sub: "🍃 雙手像微風吹過，房間空氣好清新！", pose: "sway" },
      { title: "擦擦左邊擦右邊", sub: "🧽 雙手畫圈圈，擦擦左邊、擦擦右邊！", pose: "wave" },
      { title: "水晶一般亮晶晶", sub: "✨ 伸出手指亮閃閃，地板桌子晶瑩剔透！", pose: "wave" },
      { title: "團隊合作魔法現", sub: "🤝 牽起好朋友的手，一起合作變魔法！", pose: "heart" },
      { title: "三二一出發衝衝", sub: "🏃 倒數 3、2、1，我們衝衝衝！", pose: "march" },
      { title: "特攻隊閃閃發光", sub: "⭐ 雙臂朝天閃爍，清潔特攻隊大放異彩！", pose: "sun_rise" },
      { title: "看看我們多能幹", sub: "💪 秀出小手臂肌肉，看我們多麼神氣！", pose: "reach" },
      { title: "積木高高堆成塔", sub: "🧱 一塊一塊疊積木，堆成高聳大城堡！", pose: "reach" },
      { title: "我們是大廳冠軍", sub: "🏆 雙手比大拇指，我們是打掃大冠軍！", pose: "heart" },
      { title: "房間閃亮任務清", sub: "✨ 雙眼發亮看四周，任務圓滿達成！", pose: "sun_rise" },
      { title: "最亮最美的大廳", sub: "🌟 轉圈展示新房間，乾淨整齊好舒服！", pose: "sway" },
      { title: "拼圖收好疊被子", sub: "🧩 拼圖放進抽屜，雙手把小毯子折整齊！", pose: "reach" },
      { title: "跟著節奏邊收邊跳", sub: "💃 一邊踩著音樂節拍，一邊快樂收玩具！", pose: "march" },
      { title: "給夥伴比大拇指", sub: "👍 轉向身邊好夥伴，大方比個大大讚！", pose: "heart" },
      { title: "漂亮收拾最有型", sub: "😎 雙手叉腰甩甩頭，最酷最帥的收拾達人！", pose: "wave" },
      { title: "特攻隊閃耀全場", sub: "⭐ 雙臂向上伸展，閃亮光芒照耀全場！", pose: "sun_rise" },
      { title: "看看我們多厲害", sub: "🎉 拍手跳跳，為所有努力的大家鼓掌！", pose: "jump" },
      { title: "積木收好整齊放", sub: "🧱 輕輕收好小積木，房間井井有條！", pose: "reach" },
      { title: "我們是終極冠軍", sub: "🏆 雙拳向上擊天，歡呼終極大勝利！", pose: "jump" },
      { title: "任務達成亮晶晶", sub: "🌟 整個房間都在發光，乾乾淨淨無可挑剔！", pose: "sun_rise" },
      { title: "完美清潔大定格", sub: "💖 雙手在胸前比個大愛心，完美定格微笑！", pose: "heart" }
    ]
  },

  a2_s06: {
    intro: { title: "[前奏] 太空超新星火箭蓄力", sub: "🚀 雙手合成火箭尖頂，啟動推進器準備升空！", pose: "reach" },
    cues: [
      { title: "戴銀頭盔漂群星", sub: "👨‍🚀 雙手在頭上戴緊太空頭盔，輕飄飄漫遊星際！", pose: "sway" },
      { title: "跟紅火星說哈囉", sub: "🔴 向遠方紅色火星用力招招手：哈囉你好！", pose: "wave" },
      { title: "銀河雷射星光閃", sub: "⚡ 雙手向外發射雷射星光光束，閃耀銀河！", pose: "reach" },
      { title: "小小太空探險家", sub: "🪐 踩著太空飄浮步，我們是勇敢探險家！", pose: "march" },
      { title: "零重力空中漂浮", sub: "🌌 雙腳慢慢離地，像羽毛在太空中輕輕飄！", pose: "sway" },
      { title: "流星尾巴滿天飛", sub: "🌠 雙手畫出道道流星雨軌跡，燦爛劃過！", pose: "wave" },
      { title: "握緊太空方向盤", sub: "🛸 雙手緊握飛船方向盤，向左轉向右轉！", pose: "sway" },
      { title: "感受奇幻魔法境", sub: "✨ 閉上眼睛深深呼吸，體驗奇妙星際魔法！", pose: "heart" },
      { title: "超新星飛掠月亮", sub: "🌕 砰一聲超新星爆發，飛船飛快擦過月球！", pose: "jump" },
      { title: "齊唱浩瀚星系歌", sub: "🎶 張開雙手擁抱宇宙，放聲齊唱銀河曲！", pose: "sun_rise" },
      { title: "光速穿梭大宇宙", sub: "💫 雙手向前衝刺，以光速穿越無盡星系！", pose: "march" },
      { title: "璀璨星座放光明", sub: "⭐ 雙手點亮十二星座，漫天星斗閃耀！", pose: "wave" },
      { title: "超級新星照高空", sub: "🌟 全身聚滿金色星能，向上綻放最耀眼光！", pose: "sun_rise" },
      { title: "小小火箭巡太空", sub: "🚀 雙手併攏化作小火箭，穿梭浩瀚星空！", pose: "reach" },
      { title: "土星轉動呼啦圈", sub: "🪐 扭動小蠻腰，學土星光環旋轉呼啦圈！", pose: "sway" },
      { title: "外星DJ播電音", sub: "🎧 雙手戴耳機學外星 DJ 搓盤，發出有趣聲音！", pose: "wave" },
      { title: "渦輪加速噴烈火", sub: "🔥 按下加速鍵，尾部噴出熊熊金色火焰！", pose: "jump" },
      { title: "史上最快小飛船", sub: "🛸 側身滑翔飛馳，我們是宇宙最快飛船！", pose: "march" },
      { title: "超新星飛掠月亮", sub: "🌕 轟鳴聲再次響起，向著銀河中心大飛躍！", pose: "jump" },
      { title: "銀河旋律大合唱", sub: "🎶 昂首挺胸合唱，歌聲響徹整個星際！", pose: "sun_rise" },
      { title: "光速巡航穿星空", sub: "💫 雙臂展開穩定巡航，速度超越光芒！", pose: "sway" },
      { title: "星宿閃爍耀天際", sub: "⭐ 雙手向上點綴群星，美麗夜空永不落幕！", pose: "wave" },
      { title: "平安著陸大勝利", sub: "🏆 飛船平穩著陸，雙拳插腰擺出勝利 Pose！", pose: "heart" }
    ]
  },

  a2_s07: {
    intro: { title: "[前奏] 韓流 K-ABC 街舞準備", sub: "😎 左右踩點帥氣換步，跟著 K-Pop 動感鼓點動起來！", pose: "march" },
    cues: [
      { title: "歡樂嘻哈笑開懷", sub: "😄 拍拍大腿開懷大笑，嘻哈鼓點熱力全開！", pose: "jump" },
      { title: "A是飛機飛上天", sub: "✈️ 雙臂平舉當大飛機，在天空中展翅滑翔！", pose: "sway" },
      { title: "衝上雲霄大歡呼", sub: "☁️ 飛機衝破雲層，開心大喊 Ahhhhh！", pose: "jump" },
      { title: "衝刺雲端真刺激", sub: "🚀 雙手向上拉起機頭，直衝美麗雲端！", pose: "reach" },
      { title: "B是棕毛大熊熊", sub: "🐻 雙手比出毛茸茸熊爪，學大熊笨拙搖晃！", pose: "sway" },
      { title: "C是圓圓甜餅乾", sub: "🍪 雙手在身前畫出大大圓形香甜餅乾！", pose: "sun_rise" },
      { title: "D是大鼓咚咚咚", sub: "🥁 雙手握鼓棒用力敲打大鼓，咚咚作響！", pose: "march" },
      { title: "EFG街頭跳跳", sub: "💃 腳尖左右滑步，字母跟著音樂跳起街舞！", pose: "jump" },
      { title: "字母合拍踩節奏", sub: "👟 左右踩拍換重心，每個字母精準對拍！", pose: "march" },
      { title: "HIJK牽牽手", sub: "🤝 伸出雙手牽好朋友，一起歡樂向前走！", pose: "heart" },
      { title: "LMNO傳遍大地", sub: "🌍 雙手像廣播向外放送，聲音傳遍大地！", pose: "sun_rise" },
      { title: "大聲唱響最嘹亮", sub: "📢 雙手放在嘴巴旁，放聲大唱最清楚！", pose: "reach" },
      { title: "魔法聲音齊降臨", sub: "✨ 手指輕輕彈出魔法音符，神奇美妙！", pose: "wave" },
      { title: "ABC動感律動", sub: "🎵 聳聳肩膀左右晃動，感受潮酷 ABC 律動！", pose: "sway" },
      { title: "跟我一起拼出來", sub: "🔤 雙手在胸前比劃字母，跟我一起拼！", pose: "reach" },
      { title: "PQRS開心唱TUV", sub: "🎶 踩著節拍唱出 PQRS，再接 TUV 和 W！", pose: "march" },
      { title: "掌握魔法萬能鑰", sub: "🔑 雙手做出轉鑰匙手勢，打開知識寶庫大門！", pose: "reach" },
      { title: "每個字母有旋律", sub: "🎵 身體像波浪流暢起伏，每個字母都在唱歌！", pose: "sway" },
      { title: "雙腳快樂跳不停", sub: "👟 腳步靈巧踢踏跳，快樂停不下來！", pose: "jump" },
      { title: "翻開故事小讀本", sub: "📖 雙手平攤當書本，好奇閱讀精彩童話！", pose: "reach" },
      { title: "好奇目光仔細瞧", sub: "👀 雙手在眼睛比出小望遠鏡，仔細觀察！", pose: "reach" },
      { title: "文字就像小拼圖", sub: "🧩 雙手一塊一塊拼湊起神奇智慧小拼圖！", pose: "heart" },
      { title: "腦袋靈巧動一動", sub: "🧠 食指輕點太陽穴，開動聰明小腦袋！", pose: "wave" },
      { title: "尋獲最酷大寶藏", sub: "💎 雙手向上托起發光寶箱，收穫滿滿寶藏！", pose: "sun_rise" },
      { title: "ABC律動跟我拼", sub: "🔤 全場齊聲歡唱 ABC，潮酷手勢擺出來！", pose: "march" },
      { title: "字母大合唱齊歡樂", sub: "🎉 拍手跳跳接續唱歌，滿滿活力充沛！", pose: "jump" },
      { title: "掌握關鍵大金匙", sub: "🔑 轉動大金鑰匙，我們是字母大高手！", pose: "reach" },
      { title: "我們深愛 ABC", sub: "💖 雙手放在胸口比心，我們最喜歡 ABC！", pose: "heart" },
      { title: "噠噠噠噠齊歡呼", sub: "🎶 踩著動感步伐，噠噠噠噠歡樂伴唱！", pose: "march" },
      { title: "拍手齊歌高亢唱", sub: "👏 雙手胸前用力拍掌，歡呼節奏最高潮！", pose: "wave" },
      { title: "完美街舞終極定格", sub: "😎 雙腳站穩、單手插腰、另一手比耶定格！", pose: "heart" }
    ]
  },

  a2_s08: {
    intro: { title: "[前奏] 氣球定格暖身預備", sub: "🎈 拍拍身邊彩色大氣球，音樂一停立刻定格！", pose: "march" },
    cues: [
      { title: "原地定格大喊嘿", sub: "🧊 身體一秒定格不動，大聲喊 Hey！", pose: "march" },
      { title: "聳聳肩膀彈彈膝", sub: "🦵 聳聳雙肩、膝蓋彈動，像小彈簧一樣！", pose: "march" },
      { title: "揮舞雙臂夏日樹", sub: "🌳 雙手高舉像大樹枝葉，隨夏日微風搖動！", pose: "sway" },
      { title: "蟋蟀快跳真輕巧", sub: "🦗 像小蟋蟀一樣輕巧快速在草地跳躍！", pose: "jump" },
      { title: "轉圈轉到節奏緊", sub: "🌀 雙手張開快速轉圈圈，跟緊動感鼓點！", pose: "jump" },
      { title: "感受氣氛漸高漲", sub: "🔥 腳步越來越快，期待下一秒的驚喜！", pose: "march" },
      { title: "杯中珍珠泡泡冒", sub: "🥤 雙手做出咕嚕咕嚕小泡泡，冒出杯口！", pose: "wave" },
      { title: "預備站穩別摔倒", sub: "🧘 雙腳站穩抓牢地面，平衡身體保持穩定！", pose: "reach" },
      { title: "三二一立刻停下", sub: "🛑 倒數 3、2、1，停！停！停！一秒變成木頭人！", pose: "march" },
      { title: "波波抖動別定格", sub: "💃 音樂響起快抖動，搖動身體別被抓到！", pose: "sway" },
      { title: "跳舞小蜜蜂拂風", sub: "🐝 學勤勞小蜜蜂採蜜，扭動屁股輕盈跳舞！", pose: "sway" },
      { title: "音樂一停辨方向", sub: "👂 豎起耳朵聽仔細，音樂一停立刻煞車！", pose: "reach" },
      { title: "雙手筆直指天空", sub: "☝️ 伸出手指筆直指著天空，一動也不動！", pose: "reach" },
      { title: "數到十再次定格", sub: "🔢 1 到 10 快速動動，時間一到立刻雕像定格！", pose: "march" },
      { title: "動動手指踢腳趾", sub: "🦶 甩甩手指、踢踢腳趾，放鬆全身肌肉！", pose: "wave" },
      { title: "鼻子平衡保持穩", sub: "👃 伸出食指點鼻子，單腳站立試試平衡！", pose: "reach" },
      { title: "跳到前面跳後面", sub: "↔️ 雙腳往前跳一步，再往後跳一步！", pose: "jump" },
      { title: "踩緊節奏軌道上", sub: "🚂 跟緊舞蹈小火車，穩穩行駛在軌道上！", pose: "march" },
      { title: "滿分定格大喊耶", sub: "🎉 穩穩站住，大聲歡呼一聲 Yeah！", pose: "jump" },
      { title: "波波晃動全身舞", sub: "💃 伴隨熱烈音樂，全身各個關節大解放！", pose: "sway" },
      { title: "微風蜜蜂輕跳步", sub: "🌸 踩出最可愛小碎步，輕盈靈活跳舞！", pose: "march" },
      { title: "音樂暫停神反應", sub: "⚡ 超強反應力，一秒站定擺出雕塑造型！", pose: "reach" },
      { title: "高舉雙手王者定格", sub: "🏆 雙手高舉指天，定格成為反應力之王！", pose: "heart" }
    ]
  },

  a2_s09: {
    intro: { title: "[前奏] 綠茵草地野餐預備", sub: "🧺 提著美味小野餐籃，走向陽光灑落的綠草地！", pose: "march" },
    cues: [
      { title: "草地鋪開格子墊", sub: "🧺 雙手向前推開，把紅白格子野餐墊鋪整齊！", pose: "reach" },
      { title: "倒杯香濃冰牛奶", sub: "🥛 拿著小牛奶壺，往玻璃杯裡倒香甜牛奶！", pose: "reach" },
      { title: "紅紅草莓圓又甜", sub: "🍓 雙手比出小草莓形狀，摘下又紅又甜草莓！", pose: "heart" },
      { title: "最棒野餐美食籃", sub: "🧺 打開大野餐籃，滿滿美味點心真豐盛！", pose: "sun_rise" },
      { title: "搓搓手洗洗乾淨", sub: "🧼 肥皂搓搓手，手心手背洗得好乾淨！", pose: "wave" },
      { title: "夥伴圍坐同歡樂", sub: "👭 跟小夥伴們圍坐在一起，開開心心分享！", pose: "heart" },
      { title: "咬一口微笑好甜", sub: "😋 大口咬下甜點心，露出無比滿足大微笑！", pose: "heart" },
      { title: "陽光河畔春意濃", sub: "🏞️ 雙臂張開深呼吸，享受河邊暖洋洋微風！", pose: "sway" },
      { title: "甜蜜莓果野餐天", sub: "🍓 左右踩步轉個圈，甜蜜野餐日最快樂！", pose: "jump" },
      { title: "健康蔬果助玩耍", sub: "🥦 吃下營養好蔬果，全身充滿運動大能量！", pose: "march" },
      { title: "香脆蘋果甜香蕉", sub: "🍎 雙手咬蘋果、剝香蕉，脆脆甜甜真好吃！", pose: "reach" },
      { title: "每一口都是美味", sub: "✨ 摸摸小肚子，每一口都是愛心的滋味！", pose: "heart" },
      { title: "細嚼慢嚥喀嚓嚼", sub: "🦷 慢慢咀嚼，嘴巴動動，健康飲食好習慣！", pose: "march" },
      { title: "營養食物助長高", sub: "🌱 蹲下慢慢長高高，身體壯壯像小樹！", pose: "reach" },
      { title: "胡蘿蔔橘紅閃耀", sub: "🥕 拿著脆胡蘿蔔，喀嚓喀嚓大口咬！", pose: "reach" },
      { title: "翠綠芹菜脆生生", sub: "🥬 綠綠小芹菜，清爽又脆口，營養滿分！", pose: "wave" },
      { title: "最棒美味健康餐", sub: "🌟 豎起雙手大拇指，健康點心天下第一棒！", pose: "sun_rise" },
      { title: "分享甜瓜給好友", sub: "🍈 切一塊甜甜大西瓜，雙手送給身邊好朋友！", pose: "heart" },
      { title: "野餐派對永不散", sub: "🎉 牽起手轉圈圈，歡樂野餐派對笑聲不斷！", pose: "jump" },
      { title: "甜蜜莓果野餐日", sub: "🍓 踩著輕快節拍，再次唱起野餐歡樂歌！", pose: "march" },
      { title: "盡情享受好美食", sub: "😋 快樂進餐、快樂運動，每天都健健康康！", pose: "sway" },
      { title: "脆脆蘋果甜香蕉", sub: "🍌 香甜水果入肚子，能量滿滿活力十足！", pose: "reach" },
      { title: "感恩健康大微笑", sub: "🙏 雙手合十胸前鞠躬，謝謝大自然美味點心！", pose: "heart" }
    ]
  },

  a2_s10: {
    intro: { title: "[前奏] 暖心睡衣派對預備", sub: "🌙 穿好軟綿綿睡衣，踩在毛茸茸地毯上輕輕搖擺！", pose: "sway" },
    cues: [
      { title: "輕輕哼唱搖籃曲", sub: "🎶 溫柔哼著旋律，全身肌肉慢慢放鬆！", pose: "sway" },
      { title: "微風輕吹夜安寧", sub: "🍃 雙手像夜風撫過，室內一片溫馨寧靜！", pose: "sway" },
      { title: "蓬鬆睡衣拖鞋脫", sub: "🥿 脫下小拖鞋，穿著軟綿綿睡衣準備睡覺！", pose: "reach" },
      { title: "關上遊戲小屋門", sub: "🚪 輕輕關好遊戲屋小木門，玩具們也都休息！", pose: "reach" },
      { title: "群星點亮小夜燈", sub: "🌟 滿天小星星亮起柔和微光，像溫暖小夜燈！", pose: "sun_rise" },
      { title: "照亮祥和安寧夜", sub: "🌌 溫和星光灑滿房間，夜晚好平靜好安詳！", pose: "sway" },
      { title: "泰迪熊深深打哈欠", sub: "🥱 抱著泰迪熊輕輕打個哈欠，眼睛瞇瞇笑！", pose: "heart" },
      { title: "倦意雙眼該入眠", sub: "😴 小揉眼睛，該讓辛苦一整天的小眼睛休息！", pose: "sway" },
      { title: "給微笑月亮送飛吻", sub: "🌙 雙手捧在嘴邊，給彎彎月亮送一個甜甜飛吻！", pose: "heart" },
      { title: "聆聽甜蜜安眠曲", sub: "🎶 閉上眼睛，靜靜聽這首溫柔晚安小搖籃！", pose: "sway" },
      { title: "星光睡衣入夢鄉", sub: "✨ 乘著星光小船，慢慢飄向奇妙夢鄉！", pose: "sway" },
      { title: "今天過得真美好", sub: "💖 雙手抱緊胸膛，今天真是快樂充實的一天！", pose: "heart" },
      { title: "漂浮蔚藍棉花雲", sub: "☁️ 身體像躺在藍色棉花糖雲朵上，好輕好軟！", pose: "sway" },
      { title: "甜甜美夢在等待", sub: "🍭 閉上雙眼，無數奇妙好夢等著你探險！", pose: "heart" },
      { title: "晚安星星晚安天", sub: "⭐ 輕輕揮動小手，跟滿天星空溫柔道晚安！", pose: "wave" },
      { title: "溫柔星光搖籃曲", sub: "🎶 身體像小搖籃左右輕輕晃動，安然入眠！", pose: "sway" },
      { title: "蓋上溫暖輕軟被", sub: "🛏️ 雙手拉起蓬鬆小被子，蓋好肩膀好暖和！", pose: "reach" },
      { title: "安安穩穩到天明", sub: "🌅 縮進暖和被窩，一覺睡到天色大亮！", pose: "heart" },
      { title: "安心睡到朝陽起", sub: "☀️ 帶著安心與被愛，做個甜甜的好夢！", pose: "heart" },
      { title: "明天迎來新遊戲", sub: "🎈 睡飽飽長高高，明天又有很多新遊戲！", pose: "sun_rise" },
      { title: "呼喚快樂小朋友", sub: "👭 夢裡和小夥伴手拉手，快樂奔跑！", pose: "heart" },
      { title: "輕輕嘆息甜入睡", sub: "😌 輕呼一口氣，全身沉浸在最舒服的放鬆裡！", pose: "sway" },
      { title: "星光睡衣入夢鄉", sub: "🌙 乘著星光搖籃，靜靜航向美麗夢之島！", pose: "sway" },
      { title: "感謝美好每一天", sub: "🙏 懷著感恩與幸福，甜甜進入夢鄉！", pose: "heart" },
      { title: "漫步棉花藍雲端", sub: "☁️ 在軟軟的雲朵上打滾，無憂無慮！", pose: "sway" },
      { title: "甜美夢鄉等著你", sub: "✨ 最美好的夢，正溫柔包圍著你！", pose: "heart" },
      { title: "晚安明天見定格", sub: "💤 雙手合十貼臉頰，閉上眼睛甜甜入睡！", pose: "heart" }
    ]
  }
};

// 3. Process each song in Album 2
const albumDataPath = path.resolve("web_app/album_data.js");
let rawCode = fs.readFileSync(albumDataPath, "utf8");

// Extract current database object
const win = {};
const vm = require("vm");
vm.runInContext(rawCode, vm.createContext({ window: win }));
const db = win.KAI_ALBUM_DATABASE;

const album2 = db.album_2;
console.log("Processing Album 2 songs...");

album2.songs.forEach((song, sIdx) => {
  const songId = song.id;
  const tNum = song.trackNumber;
  const meta = trackMeta[songId];
  const tData = cuesData[`track_${tNum}`];
  if (!meta || !tData) {
    throw new Error(`Missing meta or cues for song ${songId} (track ${tNum})`);
  }

  const cues = tData.cues.map(c => ({ ...c }));
  const timeline = [];

  // Check if we need an intro
  if (cues[0].start > 1.5) {
    timeline.push({
      start: 0,
      end: cues[0].start,
      title: meta.intro.title,
      video: null,
      image: song.coachImage,
      lyric: "[Intro 🎵 歡樂前奏]",
      sub: meta.intro.sub,
      promptText: meta.intro.sub,
      next: cues[0].text.substring(0, 20) + " ➜",
      targetPose: meta.intro.pose
    });
  } else {
    cues[0].start = 0;
  }

  // Loop through cues
  for (let i = 0; i < cues.length; i++) {
    const cue = cues[i];
    const isLast = (i === cues.length - 1);
    const cueMeta = meta.cues[i] || {
      title: `第 ${String(i+1).padStart(2, '0')} 節: 歡樂律動`,
      sub: "🎶 跟著節拍快樂舞動！",
      pose: "march"
    };

    let segEnd = 0;
    let hasInterlude = false;
    let nextPreview = "";

    if (isLast) {
      if (120 - cue.end >= 5.0) {
        segEnd = cue.end;
        nextPreview = "[尾奏] 歡呼慶祝完美定格 ➜";
      } else {
        segEnd = 120.0;
        nextPreview = "🎉 完美通關！獲得 3 顆大金星！";
      }
    } else {
      const nextCue = cues[i + 1];
      const gap = nextCue.start - cue.end;
      if (gap >= 5.0) {
        segEnd = cue.end;
        hasInterlude = true;
        nextPreview = "[旋律間奏] 動作接續歡樂跳 ➜";
      } else {
        segEnd = nextCue.start;
        nextPreview = nextCue.text.substring(0, 20) + " ➜";
      }
    }

    // Add main cue segment
    timeline.push({
      start: cue.start,
      end: segEnd,
      title: `第 ${String(i+1).padStart(2, '0')} 節: ${cueMeta.title}`,
      video: null,
      image: song.coachImage,
      lyric: `"${cue.text}"`,
      sub: cueMeta.sub,
      promptText: cueMeta.sub,
      next: nextPreview,
      targetPose: cueMeta.pose
    });

    // If interlude
    if (hasInterlude) {
      const nextCue = cues[i + 1];
      timeline.push({
        start: cue.end,
        end: nextCue.start,
        title: "[旋律間奏] 動作接續歡樂跳",
        video: null,
        image: song.coachImage,
        lyric: "[Interlude 🎵 輕快旋律間奏]",
        sub: "🎶 跟著動感節拍左右輕快律動，準備下一段舞步！",
        promptText: "跟著動感節拍左右輕快律動！",
        next: nextCue.text.substring(0, 20) + " ➜",
        targetPose: "sway"
      });
    }

    // If outro
    if (isLast && segEnd < 120.0) {
      timeline.push({
        start: segEnd,
        end: 120.0,
        title: "[尾奏] 歡呼慶祝完美定格",
        video: null,
        image: song.coachImage,
        lyric: "[Outro 🎵 歡樂尾奏完美定格]",
        sub: "🎉 擺出最棒的帥氣 Pose，為自己大聲歡呼喝采！",
        promptText: "擺出最棒的帥氣 Pose，為自己歡呼！",
        next: "🎉 完美通關！獲得 3 顆大金星！",
        targetPose: "heart"
      });
    }
  }

  // Update song timeline
  song.timeline = timeline;
  console.log(`Updated ${song.id} (${song.title}): ${timeline.length} segments created.`);
});

// 4. Serialize back to album_data.js
const newJsContent = "window.KAI_ALBUM_DATABASE = " + JSON.stringify(db, null, 2) + ";\n";
fs.writeFileSync("web_app/album_data.js", newJsContent, "utf8");
fs.writeFileSync("docs/album_data.js", newJsContent, "utf8");
console.log("Successfully wrote web_app/album_data.js and docs/album_data.js");
