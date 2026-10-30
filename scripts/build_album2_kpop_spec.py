# -*- coding: utf-8 -*-
"""
Build KaiDance Album 2 ("Super Groove Party" - K-pop Style) Complete Choreography & AI Animation Prompt Specification:
- Sheet 1: 曲目總覽與K-pop角色分配 (10 Songs Overview & 5 Kids Character Assignment)
- Sheet 2: 5位主角K-pop造型提示詞 (5 Kids × 2 K-pop Fashion Versions = 10 Reference Image Prompts)
- Sheet 3: 全曲目K-pop動作與動畫提示詞總表 (All 287 Segments across 10 Songs)
- Sheets 4-13: Individual Song Tabs (Track 01 ~ Track 10) for easy copy-pasting into MiniMax / Kling / Runway / Sora
- Also updates web_app/album_data.js and docs/album_data.js with K-pop videoPrompt & voiceScript
"""

import json
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# 1. Load current album_data.js
with open("web_app/album_data.js", "r", encoding="utf-8") as f:
    raw = f.read()

json_str = raw.replace("window.KAI_ALBUM_DATABASE = ", "").rstrip().rstrip(";")
db = json.loads(json_str)
album2 = db["album_2"]

# 2. Define the 5 Kids & Their 2 K-Pop Fashion Versions
KIDS_PROFILES = [
    {
        "kid_id": "Kid 1",
        "name": "Kai (陽光刺蝟頭男孩)",
        "gender": "Boy",
        "songs": "Track 03《Number Party 1-2-3》、Track 06《Galaxy Supernova》",
        "appearance_zh": "3D Pixar 風格陽光小男孩，標誌性微翹棕色層次短髮、明亮圓潤大棕眼、紅潤臉頰與燦爛露齒笑",
        "appearance_en": "3D Pixar Disney style cheerful toddler boy with spiky tousled medium-brown hair, big bright brown eyes, rosy cheeks, wide happy smile",
        "v1_name": "版本 A：K-Pop 銀藍星際棒球夾克風 (Street Idol Bomber)",
        "v1_outfit_zh": "金屬光澤銀藍拼接 K-pop 棒球外套、內搭潮流白 T、黑色工裝束口褲配霓虹青色飄帶、發光 LED 高筒球鞋",
        "v1_pose_zh": "雙腳與肩同寬帥氣站立，左手插腰或握拳蓄力，右手自然微擺，露出自信偶像笑容（預備跳舞起始姿態）",
        "v1_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful toddler boy with spiky tousled medium-brown hair, big bright brown eyes, rosy cheeks, wide happy smile, wearing trendy K-pop idol streetwear: metallic silver and royal blue varsity bomber jacket over a graphic white tee, black cargo joggers with neon cyan straps, glowing LED high-top sneakers. Standing in a confident K-pop starting pose ready to dance in a modern neon K-pop dance practice studio with wooden floor. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "v2_name": "版本 B：K-Pop 潮流紫黃撞色連帽背心風 (Stage Pop Hoodie)",
        "v2_outfit_zh": "粉紫與純白拼接 Oversize 連帽背心、內搭螢光黃短袖、潮流刷破感牛仔五分褲、厚底星星運動鞋、反戴潮流棒球帽",
        "v2_pose_zh": "身體微側踩著 K-pop 律動預備步，單手輕放胸前比出帥氣手勢，眼神明亮期待音樂響起",
        "v2_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful toddler boy with spiky tousled medium-brown hair, big bright brown eyes, rosy cheeks, wearing stylish K-pop stage fashion: pastel purple and white oversized hoodie vest layered over a neon yellow shirt, trendy denim shorts, chunky star sneakers, backwards cap. Standing in a cool K-pop basic groove waiting pose in a bright neon K-pop studio with polished wooden floor. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "generated_files": "web_app/images/album2_kpop/kid1_boy_kpop_v1.jpg (已生成)"
    },
    {
        "kid_id": "Kid 2",
        "name": "Jessie (波浪雙馬尾女孩)",
        "gender": "Girl",
        "songs": "Track 01《Ready, Set, Shine!》、Track 07《K-ABC Groove》",
        "appearance_zh": "3D Pixar 風格甜美小女孩，淺棕色大波浪捲雙馬尾（綁閃亮絲帶）、水汪汪棕色大眼、甜美酒窩笑容",
        "appearance_en": "3D Pixar Disney style cheerful toddler girl with wavy light-brown hair tied into two high pigtails with sparkling ribbons, big brown eyes, sweet radiant smile",
        "v1_name": "版本 A：K-Pop 夢幻鐳射粉紫女團風 (Holographic Girl Group)",
        "v1_outfit_zh": "炫彩鐳射粉紫短版偶像外套（附星星徽章）、百褶炫光白短裙（內搭安全褲）、粉色中筒襪與厚底女團舞鞋",
        "v1_pose_zh": "雙腳微開站穩，雙手在胸前比出可愛 K-pop 雙手愛心手勢，甜美微笑等候開跳",
        "v1_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful toddler girl with wavy light-brown hair in two high pigtails with sparkling ribbons, big brown eyes, sweet smile, wearing K-pop girl group holographic pop star outfit: iridescent pastel pink and lavender cropped jacket with star badges, pleated holographic white skirt, knee-high socks with pink platform sneakers. Standing in a cute K-pop idol starting pose making a heart gesture in a glowing pastel purple K-pop dance studio. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "v2_name": "版本 B：K-Pop 桃紅酷甜街舞運動風 (Sporty Street Dance)",
        "v2_outfit_zh": "亮桃紅與白色拼接 K-pop 短版運動球衣、粉紫漸層寬版工裝跳舞長褲（附青色與紫色飄帶）、撞色厚底潮鞋、星星髮夾",
        "v2_pose_zh": "雙手帥氣叉腰、雙腳微開踩點站立，展現自信女團 Center 預備氣場",
        "v2_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful toddler girl with wavy light-brown hair in two high pigtails with star hair clips, big brown eyes, wearing trendy K-pop street dance outfit: bright magenta and white sporty jersey top, stylish pastel purple wide-leg cargo pants with cyan and lilac straps, colourful chunky sneakers. Standing with hands on hips in a confident K-pop idol ready pose in a neon K-pop dance studio. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "generated_files": "web_app/images/album2_kpop/kid2_girl_kpop_v1.jpg (已生成)、kid2_girl_kpop_v2.jpg (已生成)"
    },
    {
        "kid_id": "Kid 3",
        "name": "Tim (蓬鬆呆毛棕髮男孩)",
        "gender": "Boy",
        "songs": "Track 04《Zoo Beat Parade》、Track 08《Pop Pop Freeze!》",
        "appearance_zh": "3D Pixar 風格可愛小男孩，蓬鬆厚實微捲棕髮與頭頂呆毛、圓滾滾棕色大眼、小巧圓鼻與陽光笑容",
        "appearance_en": "3D Pixar Disney style cheerful toddler boy with fluffy layered brown hair and cute cowlick fringe, big round brown eyes, button nose, cute grin",
        "v1_name": "版本 A：K-Pop 翠綠霓虹嘻哈街舞風 (Hip-Hop Windbreaker)",
        "v1_outfit_zh": "翡翠綠與曜石黑撞色 K-pop 街舞防風外套、側邊螢光綠條紋束口跳舞褲、潮流高筒球鞋、兒童安全星星項鍊",
        "v1_pose_zh": "膝蓋微彎保持彈性律動預備姿勢，雙手自然張開在身側準備隨重低音起跳",
        "v1_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful toddler boy with fluffy layered brown hair and cute cowlick fringe, big round brown eyes, button nose, wearing K-pop hip-hop idol outfit: vibrant emerald green and black color-block windbreaker jacket, stylish black jogger pants with neon lime stripes, cool high-top sneakers, cute silver star necklace. Standing in a bouncy K-pop ready stance in a neon K-pop dance studio with wooden floor. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "v2_name": "版本 B：K-Pop 天藍星光學院偶像風 (Preppy Idol Cardigan)",
        "v2_outfit_zh": "天藍與亮黃撞色星星徽章針織開襟衫、內搭白襯衫與亮色領結、修身五分跳舞短褲、條紋運動長襪與潮鞋",
        "v2_pose_zh": "直立微笑預備姿勢，一手輕舉在胸前比出 K-pop 指尖星星動作，充滿朝氣",
        "v2_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful toddler boy with fluffy layered brown hair and cute cowlick fringe, big round brown eyes, wearing K-pop preppy pop-star fashion: trendy sky-blue and yellow varsity cardigan with star patches over a crisp white shirt, tailored navy knee-length shorts, striped socks and trendy sneakers. Standing in a cheerful K-pop starting pose in a modern K-pop dance studio. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "generated_files": "web_app/images/album2_kpop/kid3_boy_kpop_v1.jpg (已生成)"
    },
    {
        "kid_id": "Kid 4",
        "name": "Mina (烏黑妹妹頭短髮女孩)",
        "gender": "Girl",
        "songs": "Track 02《Pastel Rainbow Dream》、Track 09《Sweet Berry Picnic》",
        "appearance_zh": "3D Pixar 風格亞裔可愛小女孩，整齊烏黑妹妹頭短髮（齊瀏海）、閃亮深邃大眼、粉嫩臉頰、佩戴小花耳釘",
        "appearance_en": "3D Pixar Disney style cheerful East Asian toddler girl with straight black bob haircut and bangs, bright dark eyes, rosy cheeks, tiny flower stud earrings, beaming smile",
        "v1_name": "版本 A：K-Pop 星光丁香紫小香風舞台裝 (Chic Tweed Idol)",
        "v1_outfit_zh": "閃亮丁香紫與銀絲編織感 K-pop 舞台短外套與同色系百褶短裙、星星扣環白色短靴、黑色短髮別著閃亮珍珠星星髮夾",
        "v1_pose_zh": "優雅甜美站立，一手輕叉腰、一手在臉頰旁比出 K-pop 臉頰愛心（Cheek Heart）預備動作",
        "v1_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful East Asian toddler girl with straight black bob haircut and bangs, bright dark eyes, rosy cheeks, pearl star hair clip, wearing chic K-pop center idol outfit: sparkling lilac and silver tweed-style K-pop stage jacket and matching pleated skirt set, white ankle boots with star buckles. Standing in an adorable K-pop starting pose with one hand on hip in a dreamy neon K-pop studio. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "v2_name": "版本 B：K-Pop 霓虹珊瑚粉Y2K潮流街舞裝 (Cyber-Pop Streetwear)",
        "v2_outfit_zh": "珊瑚粉與電光青撞色短版連帽衛衣（印有未來感星星圖騰）、純白降落傘寬版街舞長褲、彩色厚底運動鞋",
        "v2_pose_zh": "充滿活力的 K-pop 街舞預備站姿，雙手自然微抬準備隨節拍律動",
        "v2_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful East Asian toddler girl with straight black bob haircut and bangs, bright dark eyes, rosy cheeks, wearing cool K-pop cyber-pop streetwear: neon coral-pink and cyan cropped hoodie with futuristic star graphics, white parachute dance pants, colourful chunky sneakers. Standing in an energetic K-pop ready stance in a vibrant K-pop dance studio. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "generated_files": "web_app/images/album2_kpop/kid4_girl_kpop_v1.jpg (已生成)"
    },
    {
        "kid_id": "Kid 5",
        "name": "MiMi (健康小麥肌雙丸子捲髮女孩)",
        "gender": "Girl",
        "songs": "Track 05《Sparkle Clean Team》、Track 10《Starlight Pajama Party》",
        "appearance_zh": "3D Pixar 風格健康小麥色肌膚小女孩，蓬鬆棕色捲髮綁成高高的雙丸子頭（配彩色串珠髮圈）、明亮大棕眼、陽光笑容",
        "appearance_en": "3D Pixar Disney style cheerful tan-skinned toddler girl with voluminous curly brown hair tied in two high puffs with colorful beaded hair ties, big expressive brown eyes, radiant smile",
        "v1_name": "版本 A：K-Pop 閃耀金粉巨星夾克風 (Glam Gold & Berry Star)",
        "v1_outfit_zh": "閃耀香檳金與莓果粉拼接 K-pop 飛行外套、內搭星星印花短T、金屬光澤紫色跳舞短褲、高筒炫彩街舞鞋",
        "v1_pose_zh": "自信滿滿的 K-pop 舞台預備站姿，雙手叉腰、腳尖微點地面，笑容燦爛",
        "v1_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful tan-skinned toddler girl with voluminous curly brown hair in two high puffs with colorful beaded hair ties, big brown eyes, wearing glam K-pop starlet outfit: shimmering gold and berry-pink bomber jacket over a star-print top, metallic purple dance shorts, high-top dance sneakers. Standing in a confident K-pop idol ready pose with hands on hips in a glowing neon K-pop dance studio. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "v2_name": "版本 B：K-Pop 湖水綠Y2K牛仔吊帶潮流風 (Y2K Denim Pop)",
        "v2_outfit_zh": "湖水綠與亮黃拼接運動短上衣、潮流徽章貼布牛仔吊帶短褲（單邊吊帶俏皮造型）、螢光撞色運動鞋",
        "v2_pose_zh": "輕快放鬆的 K-pop 預備律動姿勢，雙手在身前微握拳準備隨著音樂 Bounce",
        "v2_prompt_en": "9:16 vertical full-body shot, 3D Pixar Disney style cheerful tan-skinned toddler girl with voluminous curly brown hair in two high puffs with colorful beads, big brown eyes, wearing fresh K-pop Y2K street dance fashion: turquoise and yellow sporty dance top with star emblem, stylish denim overall shorts with colourful patches, neon sneakers. Standing in a joyful K-pop basic starting pose in a modern K-pop dance studio. Full body head to toe visible, 4k, Disney Pixar render, no text.",
        "generated_files": "web_app/images/album2_kpop/kid5_girl_kpop_v1.jpg (已生成)"
    }
]

# Map each song in Album 2 to its assigned Kid and K-pop style metadata
SONG_KPOP_ASSIGNMENT = {
    "a2_s01": {
        "kid": KIDS_PROFILES[1], # Mia
        "coach_image": "./images/album2_kpop/kid2_girl_kpop_v1.jpg",
        "kpop_style": "Upbeat K-Pop Girl Group Center Dance (元氣女團主打風)",
        "outfit_en": "iridescent pastel pink and lavender K-pop cropped jacket with star badges, pleated holographic white skirt, pink platform sneakers",
        "core_point_dance": "鑽石閃耀手勢舞 (Diamond Shine Point Dance) + 偶像開合跳"
    },
    "a2_s02": {
        "kid": KIDS_PROFILES[3], # Hana
        "coach_image": "./images/album2_kpop/kid4_girl_kpop_v1.jpg",
        "kpop_style": "Dreamy Pastel K-Pop Synth-Pop (夢幻仙氣女團抒情律動風)",
        "outfit_en": "sparkling lilac and silver tweed K-pop stage jacket and pleated skirt set, white star ankle boots",
        "core_point_dance": "彩虹畫筆手部波浪舞 (Rainbow Brush Arm Wave) + 仙女轉圈"
    },
    "a2_s03": {
        "kid": KIDS_PROFILES[0], # Leo
        "coach_image": "./images/album2_kpop/kid1_boy_kpop_v1.jpg",
        "kpop_style": "Funky K-Pop Boy Group Electro Groove (動感男團電子節奏風)",
        "outfit_en": "metallic silver and royal blue K-pop varsity bomber jacket, black cargo joggers with neon cyan straps, LED high-top sneakers",
        "core_point_dance": "1-2-3 手指卡點舞 (Finger Count Tutting) + 霓虹滑步踢踏"
    },
    "a2_s04": {
        "kid": KIDS_PROFILES[2], # Max
        "coach_image": "./images/album2_kpop/kid3_boy_kpop_v1.jpg",
        "kpop_style": "K-Pop Hip-Hop Heavy Bass Bounce (街頭嘻哈重低音 Bounce 風)",
        "outfit_en": "vibrant emerald green and black K-pop hip-hop windbreaker jacket, black joggers with neon lime stripes, high-top sneakers",
        "core_point_dance": "皇冠獅王重拍踩點 (King Crown Stomp) + Hip-Hop 墨鏡企鵝搖擺"
    },
    "a2_s05": {
        "kid": KIDS_PROFILES[4], # Zoe
        "coach_image": "./images/album2_kpop/kid5_girl_kpop_v1.jpg",
        "kpop_style": "Energetic K-Pop Teen-Crush Funk (活力滿滿 Teen-Crush 節奏風)",
        "outfit_en": "shimmering gold and berry-pink K-pop bomber jacket, metallic purple dance shorts, colourful high-top sneakers",
        "core_point_dance": "亮晶晶擦窗卡點舞 (Sparkle Wipe Groove) + 雙人擊掌比讚 Pose"
    },
    "a2_s06": {
        "kid": KIDS_PROFILES[0], # Leo
        "coach_image": "./images/album2_kpop/kid1_boy_kpop_v1.jpg",
        "kpop_style": "Futuristic Cyber K-Pop Dance Pop (未來感太空電音男團風)",
        "outfit_en": "metallic silver and royal blue K-pop varsity bomber jacket, black cargo joggers with neon cyan straps, LED high-top sneakers",
        "core_point_dance": "零重力太空滑步 (Moonwalk Glide) + 超新星爆發跳躍 (Supernova Jump)"
    },
    "a2_s07": {
        "kid": KIDS_PROFILES[1], # Mia
        "coach_image": "./images/album2_kpop/kid2_girl_kpop_v2.jpg",
        "kpop_style": "Signature K-Pop Idol Pop Groove (正統 K-Pop 洗腦字母手勢舞)",
        "outfit_en": "bright magenta and white K-pop sporty jersey top, pastel purple wide-leg cargo pants with straps, chunky sneakers",
        "core_point_dance": "K-ABC 字母手指舞 (Alphabet Point Choreography) + 韓流聳肩律動"
    },
    "a2_s08": {
        "kid": KIDS_PROFILES[2], # Max
        "coach_image": "./images/album2_kpop/kid3_boy_kpop_v1.jpg",
        "kpop_style": "K-Pop Popping & Freeze Challenge (韓流 Popping 震點與木頭人定格風)",
        "outfit_en": "vibrant emerald green and black K-pop hip-hop windbreaker jacket, black joggers with neon lime stripes, high-top sneakers",
        "core_point_dance": "Pop-Pop 雙肩震點舞 (Shoulder Pop Bounce) + 3-2-1 偶像Ending妖精定格"
    },
    "a2_s09": {
        "kid": KIDS_PROFILES[3], # Hana
        "coach_image": "./images/album2_kpop/kid4_girl_kpop_v1.jpg",
        "kpop_style": "Refreshing Summer K-Pop Pop (清爽夏日女團甜美律動風)",
        "outfit_en": "sparkling lilac and silver tweed K-pop stage jacket and pleated skirt set, white star ankle boots",
        "core_point_dance": "草莓臉頰愛心舞 (Berry Cheek Heart Dance) + 輕快左右踏併步"
    },
    "a2_s10": {
        "kid": KIDS_PROFILES[4], # Zoe
        "coach_image": "./images/album2_kpop/kid5_girl_kpop_v1.jpg",
        "kpop_style": "Cozy K-Pop R&B Lullaby Groove (溫馨韓流 R&B 星光慢搖風)",
        "outfit_en": "shimmering gold and berry-pink K-pop bomber jacket, metallic purple dance shorts, colourful high-top sneakers",
        "core_point_dance": "星光飛吻手勢舞 (Starlight Blow Kiss) + 偶像結尾晚安 Ending Fairy"
    }
}

# Detailed K-pop dance movement mapping based on targetPose and segment context
KPOP_POSE_DETAILS = {
    "march": {
        "en": "performing a crisp K-pop idol rhythmic step-touch bounce, knees popping to the beat, groovy shoulder isolation, confident idol charisma",
        "zh": "【K-pop 節奏踩點步】雙膝隨鼓點彈性律動（Groove Bounce），搭配韓流偶像標誌性微聳肩與左右踏併步（Step-Touch），眼神自信放電"
    },
    "wave": {
        "en": "performing a smooth K-pop idol body wave and stylish overhead hand wave with finger-tutting star gestures, swaying hips rhythmically",
        "zh": "【K-pop 波浪手勢舞】手臂呈流暢波浪擺動（Arm Wave），手指比出韓流閃耀星光手勢，搭配骨盆輕快左右律動"
    },
    "reach": {
        "en": "performing a sharp K-pop point choreography reaching up diagonally to the sky with crisp arm angles, dynamic hip-hop bounce",
        "zh": "【K-pop 斜角卡點伸展】手臂俐落定點向天空斜上方延伸（Point Dance），下肢帶動輕快彈跳步，展現帥氣延伸線條"
    },
    "sway": {
        "en": "performing a trendy K-pop groovy hip sway and smooth shoulder roll, fluid upper body isolation, charming idol smile",
        "zh": "【K-pop 律動搖擺步】上身流暢轉肩（Shoulder Roll）結合骨盆左右節奏搖擺，步伐輕盈滑順，展現韓流洗腦律動感"
    },
    "jump": {
        "en": "performing a high-energy K-pop center jump-step with synchronized arm pump, landing in a cool idol power stance on the beat",
        "zh": "【K-pop 舞台中心爆發跳】跟隨重拍雙腳輕快彈跳換步（Jump & Pop），雙手同步帥氣擊拍，落地瞬間精準卡點站穩"
    },
    "sun_rise": {
        "en": "performing a glamorous K-pop sweeping arm formation drawing a glowing halo overhead, chest pop on the beat, radiant center idol aura",
        "zh": "【K-pop 星光光環開展】胸口先做一個輕巧律動震點（Chest Pop），雙臂由胸前向頭頂畫出耀眼偶像光環，氣場全開"
    },
    "heart": {
        "en": "performing a signature K-pop Ending Fairy pose with cute finger-hearts and cheek-hearts, winking playfully at the camera",
        "zh": "【K-pop 結尾妖精比心】擺出韓流偶像經典 Ending Fairy 定格姿勢，雙手比出臉頰愛心（Cheek Heart）與手指愛心，對鏡頭甜美放電"
    }
}

def generate_kpop_teacher_voice(seg_title, key_tip, pose):
    if "前奏" in seg_title:
        return "K-pop 派對開始囉！跟著重低音鼓點，膝蓋彈一彈，準備帥氣出發！"
    elif "間奏" in seg_title:
        return "Dance Break 時間！聳聳肩膀、左右踩點滑步，展現你最酷的 K-pop 律動！"
    elif "尾奏" in seg_title or "定格" in seg_title:
        return "Ending Fairy 時間！擺出最帥氣的臉頰愛心 Pose，對鏡頭眨眨眼定格！"
    elif pose == "march":
        return "跟著 K-pop 節拍，一二踩點、肩膀微聳，走出最帥氣的偶像台步！"
    elif pose == "wave":
        return "小手畫出流暢波浪，手指閃亮亮卡點，身體跟著音樂帥氣擺動！"
    elif pose == "reach":
        return "手臂俐落向天空定點伸展，眼神看向指尖，卡點超精準！"
    elif pose == "jump":
        return "預備跟上重拍——向上輕快彈跳換步，雙手帥氣揮舞嗨翻全場！"
    elif pose == "sun_rise":
        return "胸口輕輕律動，雙手向天空畫出大光環，你就是舞台最閃耀的 Center！"
    elif pose == "heart":
        return "比出超萌的 K-pop 臉頰愛心與手指愛心，給全場最甜美的微笑！"
    elif pose == "sway":
        return "轉轉小肩膀、搖搖小蠻腰，跟著韓流旋律輕快滑步律動！"
    return "跟著音樂節拍，跳出最潮的 K-pop 舞步！"

all_rows = []

for song in album2["songs"]:
    s_id = song["id"]
    s_num = song["trackNumber"]
    s_title = song["title"]
    s_zh = song["zhTitle"]
    assign = SONG_KPOP_ASSIGNMENT[s_id]
    kid = assign["kid"]
    song["coachImage"] = assign["coach_image"]

    for idx, seg in enumerate(song["timeline"]):
        seg_idx = idx + 1
        seg["image"] = assign["coach_image"]
        seg["video"] = None
        dur = round(seg["end"] - seg["start"], 2)
        pose = seg.get("targetPose", "march")
        p_info = KPOP_POSE_DETAILS.get(pose, KPOP_POSE_DETAILS["march"])

        # Enrich Chinese K-pop description
        orig_sub = seg["sub"]
        kpop_desc_zh = f"{orig_sub}｜{p_info['zh']}"
        voice_script = generate_kpop_teacher_voice(seg["title"], orig_sub, pose)

        # Build 9:16 Vertical AI Video Generation Prompt (English & Chinese)
        video_file_name = f"a2_t{s_num}_seg_{seg_idx:02d}.mp4"
        clean_lyric = seg["lyric"].replace('"', '')

        prompt_en = (
            f"9:16 vertical full-body shot, {kid['appearance_en']}, wearing {assign['outfit_en']}. "
            f"In a vibrant neon K-pop dance practice studio with LED light strips and polished wooden floor. "
            f"Song '{s_title}' ({assign['kpop_style']}), Segment '{seg['title']}'. "
            f"Action: {orig_sub}. The character is {p_info['en']}. "
            f"Smooth 60fps K-pop dance animation, crisp rhythmic bounce on the beat, full body head to shoes clearly visible, Disney Pixar 3D render, no text."
        )

        prompt_zh = (
            f"【9:16 直式全身鏡位】主角：{kid['name']}（著 K-pop 潮流舞台服）。"
            f"場景：韓流霓虹星光舞蹈教室（木質地板與柔和 LED 燈條）。"
            f"段落：{seg['title']}（歌詞：{clean_lyric}）。"
            f"動作指令：{kpop_desc_zh}。"
            f"運鏡與風格：正面全身入鏡（頭頂至舞鞋完整保留安全邊距），60fps 流暢 K-pop 律動卡點，3D 皮克斯精緻渲染。"
        )

        seg["voiceScript"] = voice_script
        seg["videoPrompt"] = prompt_en
        seg["videoPromptZh"] = prompt_zh
        seg["kpopCoach"] = kid["name"]

        start_str = f"{int(seg['start']//60):02d}:{seg['start']%60:05.2f}"
        end_str = f"{int(seg['end']//60):02d}:{seg['end']%60:05.2f}"

        all_rows.append({
            "trackNumber": s_num,
            "songId": s_id,
            "songTitle": s_title,
            "songZhTitle": s_zh,
            "kpopStyle": assign["kpop_style"],
            "coachName": kid["name"],
            "segIndex": seg_idx,
            "videoFileName": video_file_name,
            "timeRange": f"{start_str} ~ {end_str}",
            "startSec": seg["start"],
            "endSec": seg["end"],
            "durationSec": dur,
            "segTitle": seg["title"],
            "lyric": seg["lyric"],
            "kpopActionZh": kpop_desc_zh,
            "voiceScript": voice_script,
            "targetPose": pose,
            "promptEn": prompt_en,
            "promptZh": prompt_zh
        })

# 3. Save updated album_data.js to web_app/ and docs/
new_js = "window.KAI_ALBUM_DATABASE = " + json.dumps(db, ensure_ascii=False, indent=2) + ";\n"
with open("web_app/album_data.js", "w", encoding="utf-8") as f:
    f.write(new_js)
with open("docs/album_data.js", "w", encoding="utf-8") as f:
    f.write(new_js)
print(f"Updated album_data.js with K-pop prompts for {len(all_rows)} segments.")

# 4. Build Excel Workbook (Album2_Kpop_Dance_Production_Spec.xlsx)
wb = openpyxl.Workbook()

# Fonts & Fills
font_title = Font(name="Microsoft JhengHei", size=15, bold=True, color="FFFFFF")
font_sec = Font(name="Microsoft JhengHei", size=12, bold=True, color="1E1B4B")
font_header = Font(name="Microsoft JhengHei", size=10, bold=True, color="FFFFFF")
font_cell = Font(name="Microsoft JhengHei", size=10, color="0F172A")
font_bold = Font(name="Microsoft JhengHei", size=10, bold=True, color="1E1B4B")

fill_title_purple = PatternFill(start_color="6D28D9", end_color="6D28D9", fill_type="solid")
fill_header_pink = PatternFill(start_color="DB2777", end_color="DB2777", fill_type="solid")
fill_header_indigo = PatternFill(start_color="4F46E5", end_color="4F46E5", fill_type="solid")
fill_header_teal = PatternFill(start_color="0D9488", end_color="0D9488", fill_type="solid")
fill_zebra = PatternFill(start_color="F5F3FF", end_color="F5F3FF", fill_type="solid")

thin_border = Border(
    left=Side(style="thin", color="CBD5E1"),
    right=Side(style="thin", color="CBD5E1"),
    top=Side(style="thin", color="CBD5E1"),
    bottom=Side(style="thin", color="CBD5E1")
)

# ==============================================================================
# SHEET 1: 曲目總覽與K-pop角色分配
# ==============================================================================
ws1 = wb.active
ws1.title = "1_曲目總覽與Kpop角色分配"
ws1.views.sheetView[0].showGridLines = True

ws1.merge_cells("A1:H1")
ws1["A1"] = "🌟 KaiDance 第二顆星球《Groove Party 歡樂節奏派對》K-Pop 舞蹈動作與動畫製作規格總表"
ws1["A1"].font = font_title
ws1["A1"].fill = fill_title_purple
ws1["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws1.row_dimensions[1].height = 38

headers_s1 = ["曲目編號", "英文歌名", "中文歌名", "負責領舞主角 (5位小朋友)", "K-Pop 曲風與舞蹈風格定位", "時間軸總幕數", "總時長", "核心 K-Pop 記憶點舞步 (Point Dance)"]
ws1.append(headers_s1)
ws1.row_dimensions[2].height = 28
for col_idx in range(1, len(headers_s1) + 1):
    c = ws1.cell(row=2, column=col_idx)
    c.font = font_header
    c.fill = fill_header_pink
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

for song in album2["songs"]:
    s_id = song["id"]
    assign = SONG_KPOP_ASSIGNMENT[s_id]
    row = [
        f"Track #{song['trackNumber']:02d}",
        song["title"],
        song["zhTitle"],
        assign["kid"]["name"],
        assign["kpop_style"],
        f"{len(song['timeline'])} 幕",
        f"{song['duration']} 秒",
        assign["core_point_dance"]
    ]
    ws1.append(row)
    r_idx = ws1.max_row
    ws1.row_dimensions[r_idx].height = 28
    for c_idx in range(1, len(headers_s1) + 1):
        cell = ws1.cell(row=r_idx, column=c_idx)
        cell.font = font_bold if c_idx in [1, 2, 4] else font_cell
        cell.border = thin_border
        cell.alignment = Alignment(horizontal="center" if c_idx in [1, 6, 7] else "left", vertical="center", wrap_text=True)
        if r_idx % 2 == 1:
            cell.fill = fill_zebra

widths_s1 = [12, 26, 22, 26, 36, 14, 12, 42]
for i, w in enumerate(widths_s1, 1):
    ws1.column_dimensions[get_column_letter(i)].width = w

# ==============================================================================
# SHEET 2: 5位主角K-pop造型提示詞 (各2種版本共10組)
# ==============================================================================
ws2 = wb.create_sheet(title="2_五位主角Kpop造型圖提示詞")
ws2.views.sheetView[0].showGridLines = True

ws2.merge_cells("A1:I1")
ws2["A1"] = "🎤 第二輯《Groove Party》5 位小朋友 K-Pop 明星時尚造型（每人 2 種版本，共 10 組 9:16 靜態底圖規格與提示詞）"
ws2["A1"].font = font_title
ws2["A1"].fill = fill_title_purple
ws2["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws2.row_dimensions[1].height = 38

headers_s2 = [
    "角色編號", "主角名稱与特徵", "負責曲目", "造型版本", "K-Pop 時尚服裝設計細節 (中文)",
    "起始等候跳舞動作 (Starting Pose)", "9:16 靜態底圖生成提示詞 (英文 Prompt - 複製至生圖模型)", "已生成圖片路徑 / 狀態"
]
ws2.append(headers_s2)
ws2.row_dimensions[2].height = 28
for col_idx in range(1, len(headers_s2) + 1):
    c = ws2.cell(row=2, column=col_idx)
    c.font = font_header
    c.fill = fill_header_indigo
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

for k in KIDS_PROFILES:
    # Version A row
    ws2.append([
        k["kid_id"],
        f"{k['name']}\n({k['appearance_zh']})",
        k["songs"],
        k["v1_name"],
        k["v1_outfit_zh"],
        k["v1_pose_zh"],
        k["v1_prompt_en"],
        k["generated_files"]
    ])
    r1 = ws2.max_row
    ws2.row_dimensions[r1].height = 68
    for c_idx in range(1, len(headers_s2) + 1):
        cell = ws2.cell(row=r1, column=c_idx)
        cell.font = font_bold if c_idx in [1, 4] else font_cell
        cell.border = thin_border
        cell.alignment = Alignment(horizontal="center" if c_idx == 1 else "left", vertical="center", wrap_text=True)

    # Version B row
    ws2.append([
        k["kid_id"],
        f"{k['name']}\n({k['appearance_zh']})",
        k["songs"],
        k["v2_name"],
        k["v2_outfit_zh"],
        k["v2_pose_zh"],
        k["v2_prompt_en"],
        k["generated_files"]
    ])
    r2 = ws2.max_row
    ws2.row_dimensions[r2].height = 68
    for c_idx in range(1, len(headers_s2) + 1):
        cell = ws2.cell(row=r2, column=c_idx)
        cell.font = font_bold if c_idx in [1, 4] else font_cell
        cell.border = thin_border
        cell.alignment = Alignment(horizontal="center" if c_idx == 1 else "left", vertical="center", wrap_text=True)
        cell.fill = fill_zebra

widths_s2 = [10, 28, 28, 30, 38, 34, 65, 30]
for i, w in enumerate(widths_s2, 1):
    ws2.column_dimensions[get_column_letter(i)].width = w

# ==============================================================================
# SHEET 3: 全曲目 287 幕 K-Pop 動作與動畫提示詞總表
# ==============================================================================
ws3 = wb.create_sheet(title="3_全曲目287幕動畫提示詞總表")
ws3.views.sheetView[0].showGridLines = True

detail_headers = [
    "曲目與幕次", "建議影片檔名", "時間區間 (分:秒)", "時長(秒)", "領舞主角",
    "段落主題", "對應英文歌詞 (SRT同步)", "K-Pop 幼兒舞蹈動作拆解說明 (中文)",
    "名師動感口令 (中文)", "火柴人姿態",
    "AI 動畫生成提示詞 (英文 Prompt - 適用於 MiniMax/Kling/Runway 9:16)",
    "AI 動畫生成提示詞 (中文對照說明)"
]
ws3.append(detail_headers)
ws3.row_dimensions[1].height = 30
for col_idx in range(1, len(detail_headers) + 1):
    c = ws3.cell(row=1, column=col_idx)
    c.font = font_header
    c.fill = fill_header_teal
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

for item in all_rows:
    ws3.append([
        f"Track {item['trackNumber']:02d} - #{item['segIndex']:02d}",
        item["videoFileName"],
        item["timeRange"],
        item["durationSec"],
        item["coachName"],
        item["segTitle"],
        item["lyric"],
        item["kpopActionZh"],
        item["voiceScript"],
        item["targetPose"],
        item["promptEn"],
        item["promptZh"]
    ])
    curr_r = ws3.max_row
    ws3.row_dimensions[curr_r].height = 52
    for c_idx in range(1, len(detail_headers) + 1):
        cell = ws3.cell(row=curr_r, column=c_idx)
        cell.font = font_cell
        cell.border = thin_border
        cell.alignment = Alignment(horizontal="center" if c_idx in [1, 2, 3, 4, 10] else "left", vertical="center", wrap_text=True)
        if curr_r % 2 == 1:
            cell.fill = fill_zebra

detail_widths = [16, 18, 18, 10, 22, 24, 30, 42, 32, 12, 65, 55]
for i, w in enumerate(detail_widths, 1):
    ws3.column_dimensions[get_column_letter(i)].width = w

# ==============================================================================
# SHEETS 4 ~ 13: Individual Song Sheets (Track 01 ~ Track 10)
# ==============================================================================
for song in album2["songs"]:
    s_num = song["trackNumber"]
    s_id = song["id"]
    assign = SONG_KPOP_ASSIGNMENT[s_id]
    short_zh = song["zhTitle"].replace("，", "").replace("！", "").replace(" ", "")[:6]
    ws_s = wb.create_sheet(title=f"T{s_num:02d}_{short_zh}")
    ws_s.views.sheetView[0].showGridLines = True

    ws_s.merge_cells("A1:L1")
    ws_s["A1"] = f"🎵 Track #{s_num:02d}: {song['title']} ({song['zhTitle']}) ｜ 領舞：{assign['kid']['name']} ｜ 風格：{assign['kpop_style']}"
    ws_s["A1"].font = font_title
    ws_s["A1"].fill = fill_title_purple
    ws_s["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws_s.row_dimensions[1].height = 34

    ws_s.append(detail_headers)
    ws_s.row_dimensions[2].height = 28
    for col_idx in range(1, len(detail_headers) + 1):
        c = ws_s.cell(row=2, column=col_idx)
        c.font = font_header
        c.fill = fill_header_pink
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    s_items = [x for x in all_rows if x["trackNumber"] == s_num]
    for item in s_items:
        ws_s.append([
            f"#{item['segIndex']:02d}",
            item["videoFileName"],
            item["timeRange"],
            item["durationSec"],
            item["coachName"],
            item["segTitle"],
            item["lyric"],
            item["kpopActionZh"],
            item["voiceScript"],
            item["targetPose"],
            item["promptEn"],
            item["promptZh"]
        ])
        curr_r = ws_s.max_row
        ws_s.row_dimensions[curr_r].height = 54
        for c_idx in range(1, len(detail_headers) + 1):
            cell = ws_s.cell(row=curr_r, column=c_idx)
            cell.font = font_cell
            cell.border = thin_border
            cell.alignment = Alignment(horizontal="center" if c_idx in [1, 2, 3, 4, 10] else "left", vertical="center", wrap_text=True)
            if curr_r % 2 == 1:
                cell.fill = fill_zebra

    for i, w in enumerate(detail_widths, 1):
        ws_s.column_dimensions[get_column_letter(i)].width = w

# Save Excel files to root, web_app/, and docs/
excel_paths = [
    "Album2_Kpop_Dance_Production_Spec.xlsx",
    "web_app/Album2_Kpop_Dance_Production_Spec.xlsx",
    "docs/Album2_Kpop_Dance_Production_Spec.xlsx"
]
for p in excel_paths:
    wb.save(p)
    print(f"Saved Excel workbook to: {p}")
