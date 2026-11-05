#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Album 3 (Sakura Neo Pop) & Album 4 (Sunset Soul Groove)
Dance Production Specification Excel files.
Follows Album 2 format, grouping slow/mid-tempo songs into cohesive 5-7 phrase segments
with comprehensive Kling/MiniMax/Runway 9:16 prompts.
"""

import os
import re
import json
import shutil
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Load album_data.js
with open('web_app/album_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

json_start = text.find('{')
json_end = text.rfind('};')
if json_end == -1:
    json_end = text.rfind('}') + 1
else:
    json_end += 1

db = json.loads(text[json_start:json_end])

FONT_NAME = 'Microsoft JhengHei'

def create_thin_border():
    thin = Side(border_style="thin", color="D1D5DB")
    return Border(top=thin, left=thin, right=thin, bottom=thin)

def format_time(seconds):
    m = int(seconds // 60)
    s = seconds % 60
    return f"{m:02d}:{s:05.2f}"

# Define Character specs for Album 3 (J-Pop) and Album 4 (Sunset R&B)
ALBUM3_CHARACTERS = [
    {
        "id": "Kid 1",
        "name": "Kai (陽光刺蝟頭男孩)",
        "feature": "3D Pixar 風格陽光小男孩，標誌性微翹棕色層次短髮、明亮圓潤大棕眼、紅潤臉頰與燦爛露齒笑",
        "tracks": "Track 02《晨光喜樂大跳躍》、Track 09《神奇小剎車·我有節制》",
        "version": "版本 A：J-Pop 櫻花粉藍拼接教練夾克風 (Sakura Neo Bomber)",
        "costume": "櫻花粉與青瓷綠拼接 J-Pop 飛行棒球外套、純白工裝束口五分褲、發光 LED 高筒球鞋、頭戴式偶像微型麥克風",
        "pose": "元氣滿滿雙手比耶 (Peace Sign)，雙腿微開隨節拍輕微跳躍，笑容燦爛",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old boy Kai, short spiky layered brown hair, big warm sparkling brown eyes, rosy cheeks, energetic beaming toothy smile. Wearing a chic pastel sakura-pink and neon teal Tokyo idol bomber jacket over a clean white graphic t-shirt, crisp white cargo dance shorts, light-up cyan high-top sneakers, tiny transparent idol headset mic. Cheerful coach dance pose, one hand flashing a cute peace sign, feet shoulder-width apart ready to jump. Vibrant pastel Tokyo Shibuya neon dance stage background with floating sakura cherry blossom petals, volumetric soft studio lighting, ultra-clean character render, 8k resolution, Disney Pixar animation style --no text, watermarks, deformed limbs, blur.",
        "status": "已生成第一幀底圖：web_app/images/album3_jpop/kid1_kai_jpop.jpg"
    },
    {
        "id": "Kid 1",
        "name": "Kai (陽光刺蝟頭男孩)",
        "feature": "3D Pixar 風格陽光小男孩，標誌性微翹棕色層次短髮、明亮圓潤大棕眼、紅潤臉頰與燦爛露齒笑",
        "tracks": "Track 02《晨光喜樂大跳躍》、Track 09《神奇小剎車·我有節制》",
        "version": "版本 B：原宿街頭活力電玩紫綠背心裝 (Harajuku Cyber Vest)",
        "costume": "電玩薄荷綠與亮紫撞色連帽運動背心、內搭純白短袖T恤、深藍潮流寬版跳舞牛仔褲、亮色厚底球鞋、反戴星光棒球帽",
        "pose": "帥氣單手插腰，另一手向前伸出大拇指點讚，眼神充滿自信活力",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old boy Kai, spiky layered brown hair peeking from under a backwards pastel purple snapback cap, warm brown eyes, radiant smile. Wearing a Harajuku style mint-green and ultraviolet hooded sport vest over white tee, loose baggy dance denim pants with pastel patches, chunky colorful sneakers. Dynamic cool posture, one hand giving a friendly thumbs-up to camera, joyful dance coach energy. Bright Harajuku street studio background, soft colorful neon rim lighting, 8k resolution, Disney Pixar render --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 2",
        "name": "Jessie (波浪雙馬尾女孩)",
        "feature": "3D Pixar 風格甜美小女孩，淺棕色大波浪捲雙馬尾（綁櫻花粉絲帶）、水汪汪棕色大眼、甜美酒窩笑容",
        "tracks": "Track 01《快樂分享超能力》、Track 05《禮貌魔法小咒語》",
        "version": "版本 A：J-Pop 夢幻櫻花馬卡龍女團偶像裙 (Macaron Idol Dress)",
        "costume": "櫻花粉與丁香紫層次偶像舞台蓬蓬裙（配透明歐根紗花瓣邊）、珍珠白色泡泡袖短外套、粉色荷葉邊中筒襪、白色厚底瑪莉珍舞鞋",
        "pose": "雙手在胸前比出招牌手指愛心 (Finger Heart)，微微歪頭甜美微笑",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old girl Jessie, wavy light-brown hair in high bouncy twin pigtails tied with sparkling pastel sakura ribbon bows, sparkling large brown eyes, rosy cheeks, lovely dimpled smile. Wearing an exquisite Tokyo idol stage dress in layered pastel cherry-blossom pink and dreamy lavender with sheer organza petal ruffle skirt, pearl-white puff-sleeve cropped jacket, frilly pastel socks, glossy white platform dance Mary Janes. Adorable center idol pose, cute finger heart at chest, head tilted slightly. Dreamy pastel wonderland stage with cherry blossom trees, luminous fairy lights, Disney Pixar masterpiece, 8k resolution --no text, watermarks, blur.",
        "status": "已生成第一幀底圖：web_app/images/album3_jpop/kid2_jessie_jpop.jpg"
    },
    {
        "id": "Kid 2",
        "name": "Jessie (波浪雙馬尾女孩)",
        "feature": "3D Pixar 風格甜美小女孩，淺棕色大波浪捲雙馬尾（綁櫻花粉絲帶）、水汪汪棕色大眼、甜美酒窩笑容",
        "tracks": "Track 01《快樂分享超能力》、Track 05《禮貌魔法小咒語》",
        "version": "版本 B：原宿元氣學院風百褶裙裝 (Harajuku Preppy Pop)",
        "costume": "奶油白學院風針織開衫（繡有櫻花星星徽章）、嫩粉色格紋百褶裙、內搭圓領蕾絲邊襯衫、學院小皮鞋與白色條紋長襪",
        "pose": "雙手輕輕拉起百褶裙襬，輕盈單腳點地踮步，宛如元氣魔法少女",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old girl Jessie, wavy brown twin pigtails with pastel hair clips, joyful expression. Wearing a cream-white knit school idol cardigan with embroidered star blossom crest, cute pastel pink plaid pleated skirt, crisp Peter-Pan collar blouse, white crew socks with pink stripes, shiny patent leather dance loafers. Joyful curtsy dance pose, lightly lifting skirt hem, beaming smile. Japanese academy stage set with warm pastel morning glow, Disney Pixar render, 8k resolution --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 3",
        "name": "Tim (蓬鬆呆毛棕髮男孩)",
        "feature": "3D Pixar 風格可愛小男孩，蓬鬆厚實微捲棕髮與頭頂呆毛、圓滾滾棕色大眼、小巧圓鼻與陽光笑容",
        "tracks": "Track 04《耐心排隊小火車》、Track 07《約定小精靈·信實守諾》",
        "version": "版本 A：J-Pop 原宿薄荷黃拼接活力防風背心裝 (Harajuku Mint Runner)",
        "costume": "薄荷綠與檸檬黃亮眼拼接多口袋工裝背心、純白短T、淺卡其跳舞束口縮口褲、亮黃厚底運動鞋、俏皮星星髮夾",
        "pose": "雙手在腰間握拳做「小火車站長拉鳴笛」動作，右腳向前輕快踩點踏步",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old boy Tim, fluffy soft curly light-brown hair with a playful hair cowlick ahoge on top, large warm brown eyes, button nose, wide cheerful smile. Wearing a bright Harajuku street dance outfit: mint-green and sunny-yellow colorblock utility zip vest over a white t-shirt, comfy light-khaki joggers, bright yellow chunky high-top sneakers, cute star hairpin in messy curls. Fun conductor dance pose, pretending to pull train whistle, energetic step forward. Cheerful colorful toy train station studio background, volumetric sunlight, Disney Pixar render, 8k resolution --no text, blur.",
        "status": "已生成第一幀底圖：web_app/images/album3_jpop/kid3_tim_jpop.jpg"
    },
    {
        "id": "Kid 3",
        "name": "Tim (蓬鬆呆毛棕髮男孩)",
        "feature": "3D Pixar 風格可愛小男孩，蓬鬆厚實微捲棕髮與頭頂呆毛、圓滾滾棕色大眼、小巧圓鼻與陽光笑容",
        "tracks": "Track 04《耐心排隊小火車》、Track 07《約定小精靈·信實守諾》",
        "version": "版本 B：東京潮童亮彩工裝吊帶褲裝 (Tokyo Dungaree Beat)",
        "costume": "天藍色休閒牛仔吊帶褲（上面貼有小熊與彩虹刺繡布貼）、內搭亮橘黃條紋短T、白色高筒帆布鞋、彩色軟呢漁夫帽",
        "pose": "雙手輕拉吊帶，挺起小胸膛，露齒大笑向鏡頭敬禮",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old boy Tim, fluffy brown hair peeking from cute bucket hat, round brown eyes, sunny toothy grin. Wearing sky-blue denim overalls with fun colorful rainbow patches over an orange-yellow striped tee, clean white high-top canvas sneakers. Playful salute pose, thumbs tucked in overall straps, stand tall with proud friendly expression. Sunny Japanese park stage background, soft natural lighting, Disney Pixar 3D render, 8k resolution --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 4",
        "name": "Hana (烏黑齊瀏海亞裔女孩)",
        "feature": "3D Pixar 風格亞裔精緻小女孩，柔順烏黑妹妹頭齊短髮（齊瀏海）、深邃明亮黑眼、白皙肌膚與粉嫩臉頰",
        "tracks": "Track 03《彩虹深呼吸·和平心》、Track 08《溫柔小手抱抱你》",
        "version": "版本 A：J-Pop 和風櫻雪和紙印花蓬蓬裙 (Sakura Blossom Kimono-Pop)",
        "costume": "改良式粉白櫻花和風短版短袖上衣、櫻粉色千層雪紡短裙、腰間淡金絲質蝴蝶結、白色棉質花邊襪、淡粉芭蕾平底舞鞋",
        "pose": "雙手合十在胸前做「深呼吸和平祈禱手勢」，身形如優雅櫻花仙子輕輕微蹲",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old Asian girl Hana, sleek shiny jet-black bob haircut with neat straight bangs, big expressive obsidian-brown eyes, fair skin, rosy pink cheeks, serene gentle smile. Wearing a modern Japanese neo-pop sakura stage outfit: pastel pink and white kimono-inspired cropped blouse with delicate cherry petal motifs, multi-layered blush chiffon bubble skirt, soft golden sash bow at waist, white frilled ankle socks, pastel pink dance flats. Graceful starting pose, palms gently touching at chest in peaceful deep breath posture, serene and gentle demeanor. Magical cherry blossom garden pavilion background with gently falling petals, ethereal soft lighting, Disney Pixar 3D masterpiece, 8k resolution --no text, watermarks, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 4",
        "name": "Hana (烏黑齊瀏海亞裔女孩)",
        "feature": "3D Pixar 風格亞裔精緻小女孩，柔順烏黑妹妹頭齊短髮（齊瀏海）、深邃明亮黑眼、白皙肌膚與粉嫩臉頰",
        "tracks": "Track 03《彩虹深呼吸·和平心》、Track 08《溫柔小手抱抱你》",
        "version": "版本 B：原宿雲朵棉花糖淡紫日常洋裝 (Cotton Candy Lavender)",
        "costume": "淡紫與鵝黃撞色棉花糖雲朵泡泡袖連身裙、白色透氣褲襪、銀白亮粉小皮鞋、頭戴立體櫻花珍珠髮箍",
        "pose": "雙臂向兩側優雅舒展如小天鵝，腳尖輕巧交叉站立，眼神溫柔注視鏡頭",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old Asian girl Hana, sleek black bob with neat bangs, pearl sakura headband, sparkling dark eyes, sweet gentle expression. Wearing a soft pastel lavender and buttercup-yellow cotton candy puff dress with cloud ruffles, white dance tights, shimmering silver ballet shoes. Poised graceful posture, arms extended softly like swan wings, serene peaceful dance stance. Pastel gradient dreamscape studio background with floating glowing stars, Disney Pixar 3D render, 8k resolution --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 5",
        "name": "MiMi (健康小麥肌捲髮雙丸子女孩)",
        "feature": "3D Pixar 風格小麥色健康肌膚小女孩，蓬鬆黑棕自然捲髮紮成高高的雙丸子頭（配彩色串珠）、明亮深棕大眼、感染力極強的燦笑",
        "tracks": "Track 06《小小好幫手·良善心》、Track 10《抱抱和好·愛的奇蹟》",
        "version": "版本 A：J-Pop 原宿彩虹糖果高彩工裝吊帶裙 (Rainbow Candy Pop)",
        "costume": "亮橘與櫻草黃漸層高腰吊帶裙、內搭純白短T、腳穿彩虹條紋長筒襪與電光紫運動鞋、雙丸子頭點綴彩色糖果髮夾",
        "pose": "雙手在頭頂上方比出大大的「愛心拱門」，一隻腳俏皮後踢，笑容充滿暖洋洋的愛",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old girl MiMi, warm golden bronze skin, curly dark brown hair tied in two high puffy space buns decorated with colorful candy beads and sakura clips, huge sparkling brown eyes, radiant joyful open-mouth smile. Wearing a bright Harajuku pop outfit: sunset orange and primrose-yellow gradient overall skirt with cute patch pockets over a white tee, vibrant rainbow striped knee-high socks, electric purple dance sneakers. Energetic love pose, hands forming a large heart over head, one foot kicked back playfully. Colorful Tokyo pop candy street background, sunny glowing studio lights, Disney Pixar 3D render, 8k resolution --no text, watermarks, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 5",
        "name": "MiMi (健康小麥肌捲髮雙丸子女孩)",
        "feature": "3D Pixar 風格小麥色健康肌膚小女孩，蓬鬆黑棕自然捲髮紮成高高的雙丸子頭（配彩色串珠）、明亮深棕大眼、感染力極強的燦笑",
        "tracks": "Track 06《小小好幫手·良善心》、Track 10《抱抱和好·愛的奇蹟》",
        "version": "版本 B：東京街頭熱帶水果風跳舞運動裝 (Tokyo Fruit Energy)",
        "costume": "西瓜紅透氣運動開襟連帽拉鍊衫、亮黃五分單車短褲、厚底繽紛球鞋、手腕佩戴發光螢光手環",
        "pose": "側身做熱情擁抱姿勢，雙手大張像要給全世界一個最溫暖的抱抱",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old girl MiMi, warm tan skin tone, curly twin space buns with fruit hairpins, big expressive eyes, happiest toothy grin. Wearing watermelon-red breathable track jacket, lemon-yellow bike shorts, chunky rainbow sneakers, glowing neon wristbands. Big warm hug dance pose, arms wide open to embrace the viewer, chest proud and welcoming. Warm tropical Tokyo studio dance stage, dynamic soft lighting, Disney Pixar 3D render, 8k resolution --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    }
]

ALBUM4_CHARACTERS = [
    {
        "id": "Kid 1",
        "name": "Kai (陽光刺蝟頭男孩)",
        "feature": "3D Pixar 風格陽光小男孩，微翹棕髮、明亮大棕眼、溫暖治癒笑容",
        "tracks": "Track 02《口袋裡的快樂小音符》、Track 07《堅定小燈塔·守信夥伴》",
        "version": "版本 A：日落復古燈芯絨大地色暖心裝 (Sunset Corduroy Soul)",
        "costume": "焦糖暖棕細條燈芯絨休閒夾克、內搭奶油燕麥色高領針織衫、炭灰微錐形跳舞長褲、焦糖皮質復古休閒鞋",
        "pose": "雙手插在夾克口袋，身體隨著 96 BPM 慢板 R&B 放鬆左右輕微搖擺，眼神溫暖",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old boy Kai, spiky layered soft brown hair, large expressive brown eyes, gentle charming warm smile. Wearing a cozy retro R&B outfit: warm caramel-brown fine corduroy chore jacket over a cream-white knit sweater, charcoal relaxed dance trousers, vintage tan leather casual shoes. Relaxed soul groove stance, hands loosely tucked into jacket pockets, gentle rhythmic swaying pose, cozy and cool. Golden hour sunset lounge background, warm amber and terracotta lighting, wooden acoustic floor, Disney Pixar 3D render, 8k resolution --no text, watermarks, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 1",
        "name": "Kai (陽光刺蝟頭男孩)",
        "feature": "3D Pixar 風格陽光小男孩，微翹棕髮、明亮大棕眼、溫暖治癒笑容",
        "tracks": "Track 02《口袋裡的快樂小音符》、Track 07《堅定小燈塔·守信夥伴》",
        "version": "版本 B：暖陽羊羔毛落日拼接背心裝 (Sunset Fleece Vest)",
        "costume": "米白與土紅拼色羊羔毛防寒拉鍊背心、薑黃色長袖棉T、深卡其工裝褲、厚底棕色復古靴",
        "pose": "右手順著節奏在胸前輕輕彈指打拍子，左手伸向前方邀請小朋友一起跳舞",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old boy Kai, messy brown hair, sparkling eyes, welcoming smile. Wearing cream and terracotta fleece zip vest over a mustard-yellow long-sleeve tee, relaxed khaki cargo pants, brown retro boots. Inviting dance pose, snapping fingers gently to a smooth R&B rhythm, warm inviting gesture. Sunset terrace studio with golden sunlight rays, cozy atmosphere, Disney Pixar 3D render, 8k resolution --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 2",
        "name": "Jessie (波浪雙馬尾女孩)",
        "feature": "3D Pixar 風格甜美小女孩，淺棕色波浪捲雙馬尾（換上琥珀暖金絲帶）、溫柔大眼、治癒微笑",
        "tracks": "Track 01《暖陽擁抱之歌》、Track 08《蝴蝶細語·溫柔的聲音》",
        "version": "版本 A：日落餘暉暖橘羊毛針織長版毛衣裝 (Amber Sunset Knit)",
        "costume": "焦糖南瓜暖橘色粗麻花針織 Oversize 軟萌毛衣、米白細褶軟裙、咖啡色棉質暖腿襪、焦糖棕復古牛津鞋",
        "pose": "雙手環抱自己的肩膀做「自我擁抱暖陽」動作，雙眼微閉享受音樂，笑容無比甜美",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old girl Jessie, wavy light-brown hair in twin low pigtails tied with amber satin ribbons, warm brown eyes, angelic sweet smile. Wearing an oversized chunky cable-knit sweater in cozy sunset pumpkin-orange, soft cream pleat skirt, espresso-brown knit leg warmers, caramel vintage oxford shoes. Tender self-hug pose, arms gently wrapping across shoulders embracing the warmth, soft gentle sway to soul music. Dreamy sunset living room studio with warm velvet curtains, soft amber dusk rays, Disney Pixar 3D masterpiece, 8k resolution --no text, watermarks, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 2",
        "name": "Jessie (波浪雙馬尾女孩)",
        "feature": "3D Pixar 風格甜美小女孩，淺棕色波浪捲雙馬尾（換上琥珀暖金絲帶）、溫柔大眼、治癒微笑",
        "tracks": "Track 01《暖陽擁抱之歌》、Track 08《蝴蝶細語·溫柔的聲音》",
        "version": "版本 B：奶油燕麥色燈芯絨連身裙 (Oatmeal Velvet Pinafore)",
        "costume": "燕麥奶油色細條燈芯絨吊帶裙、內搭暖薑黃荷葉領長袖襯衫、深棕小皮鞋、頭戴暖黃軟毛貝雷帽",
        "pose": "雙手輕輕放在下巴旁如蝴蝶拍翅，腳步輕巧點踏，優雅恬靜",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old girl Jessie, twin brown pigtails under a mustard-yellow felt beret, delicate rosy cheeks, radiant smile. Wearing an oatmeal corduroy pinafore dress over a warm ginger-yellow ruffle-collar shirt, deep brown leather shoes. Butterfly hand pose, fluttering fingers softly by cheeks, graceful slow dance posture. Warm autumn sunset meadow background, magical golden dust, Disney Pixar 3D render, 8k resolution --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 3",
        "name": "Tim (蓬鬆呆毛棕髮男孩)",
        "feature": "3D Pixar 風格可愛小男孩，蓬鬆棕髮呆毛、圓潤大眼、憨厚治癒微笑",
        "tracks": "Track 04《慢步小烏龜·學會耐心》、Track 09《停一下·想一想·明智節制》",
        "version": "版本 A：復古黑膠唱片行爵士休閒西裝背心裝 (Vinyl Jazz Barista)",
        "costume": "深苔蘚綠復古西裝背心、內搭米黃棉麻長袖襯衫（挽起袖子）、深棕燈芯絨九分寬褲、復古麂皮樂福鞋",
        "pose": "身體微微前傾，雙手做出「慢步滑步」平穩手勢，表情充滿耐心與專注",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old boy Tim, fluffy soft curly brown hair with iconic cowlick, big round brown eyes, thoughtful kind smile. Wearing a retro soul barista outfit: moss-green tweed waistcoat vest over a cream linen long-sleeve shirt with rolled sleeves, rich chocolate-brown corduroy cropped trousers, tan suede loafers. Slow steady turtle dance pose, arms extended gently gliding smoothly to the slow tempo, relaxed and patient posture. Vintage cozy vinyl record shop setting with warm incandescent table lamps, wooden shelves, Disney Pixar 3D render, 8k resolution --no text, watermarks, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 3",
        "name": "Tim (蓬鬆呆毛棕髮男孩)",
        "feature": "3D Pixar 風格可愛小男孩，蓬鬆棕髮呆毛、圓潤大眼、憨厚治癒微笑",
        "tracks": "Track 04《慢步小烏龜·學會耐心》、Track 09《停一下·想一想·明智節制》",
        "version": "版本 B：暖棕格紋落肩休閒開衫裝 (Cozy Brown Check Cardigan)",
        "costume": "焦糖色大格紋落肩毛線開衫、內搭純白純棉圓領衫、深卡其寬版工裝休閒褲、棕色休閒帆布鞋",
        "pose": "食指輕點太陽穴做出「停一下、想一想」的節制思考 Pose，俏皮眨眼",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old boy Tim, messy curly hair, playful wink and warm grin. Wearing a warm caramel plaid oversized cardigan over white tee, baggy olive-khaki trousers, brown sneakers. Pause and think pose, one index finger gently tapping temple, playful wise expression. Cozy library dance studio, warm glowing sunset illumination, Disney Pixar 3D render, 8k resolution --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 4",
        "name": "Hana (烏黑齊瀏海亞裔女孩)",
        "feature": "3D Pixar 風格亞裔小女孩，烏黑順滑齊短髮、黑亮杏眼、平靜恬雅氣質",
        "tracks": "Track 03《平靜溪流深呼吸》、Track 06《誠實小樹苗·良善之心》",
        "version": "版本 A：落日大地色莫蘭迪茶歇長裙裝 (Morandi Earth Tea Dress)",
        "costume": "莫蘭迪灰粉與奶茶棕拼色長版亞麻棉連身裙、米白針織小披肩、深木色復古平底皮鞋、珍珠小髮夾",
        "pose": "雙手在胸前緩緩劃出如同「平靜溪水」般的波浪手勢，雙膝隨流水旋律輕緩微屈",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old Asian girl Hana, silky jet-black bob haircut with neat straight bangs, pearl hairpin, deep luminous dark eyes, calm graceful smile. Wearing a soothing Morandi tea dress in muted dusty-rose and milk-tea brown linen with a delicate cream-knit shoulder shawl, dark wood vintage leather flats. Peaceful water-flow dance pose, hands making gentle undulating wave gestures like a calm forest creek, knees bending softly in tranquil rhythm. Serene golden sunset forest riverbank setting, warm sunbeams filtering through trees, Disney Pixar 3D masterpiece, 8k resolution --no text, watermarks, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 4",
        "name": "Hana (烏黑齊瀏海亞裔女孩)",
        "feature": "3D Pixar 風格亞裔小女孩，烏黑順滑齊短髮、黑亮杏眼、平靜恬雅氣質",
        "tracks": "Track 03《平靜溪流深呼吸》、Track 06《誠實小樹苗·良善之心》",
        "version": "版本 B：暖杏色高領毛衣配燈芯絨吊帶裙裝 (Warm Apricot Corduroy)",
        "costume": "暖杏黃色柔軟高領羊絨衫、深墨綠細條燈芯絨吊帶長裙、米白棉襪、復古瑪莉珍鞋",
        "pose": "雙手在胸口捧著一株象徵誠實的小樹苗手勢，抬頭仰望微風，目光清澈明亮",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old Asian girl Hana, black bob, neat bangs, innocent clear eyes, gentle smile. Wearing a warm apricot turtleneck cashmere sweater under a forest-green corduroy overall dress, white socks, classic Mary Janes. Holding hands cupped like nurturing a little seedling sprout, looking gently upward with pure honest expression. Warm sunlit botanical greenhouse studio, golden hour glow, Disney Pixar 3D render, 8k resolution --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 5",
        "name": "MiMi (健康小麥肌捲髮雙丸子女孩)",
        "feature": "3D Pixar 風格小麥色健康肌膚小女孩，蓬鬆黑棕自然捲雙丸子頭、明亮深褐大眼、暖陽般燦爛笑容",
        "tracks": "Track 05《蜂蜜甜甜話·口出恩慈》、Track 10《星光晚安靈魂漫步》",
        "version": "版本 A：蜜糖琥珀金絨面復古連身休閒套裝 (Velvet Honey Amber Jumpsuit)",
        "costume": "蜜糖琥珀金色短絨休閒連身短褲裝（腰間繫同色細絨帶）、內搭純白短T、暖棕短靴、雙丸子頭搭配琥珀色木質髮珠",
        "pose": "雙手在嘴角兩側做「甜甜微笑花朵」手勢，頭輕輕向右歪，神態甜美如蜜糖",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old girl MiMi, warm golden-tan skin tone, curly dark brown hair in two fluffy space buns with polished amber wooden beads, huge twinkling brown eyes, sweetest radiant smile. Wearing a luxurious velvet jumpsuit in warm honey-amber over a soft white tee, comfy tan suede ankle boots. Honey-sweet smile pose, cupping hands like blooming petals beside cheeks, head tilted with joyful sweetness. Cozy golden sunset honeycomb-inspired lounge studio, soft amber rim light, Disney Pixar 3D masterpiece, 8k resolution --no text, watermarks, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    },
    {
        "id": "Kid 5",
        "name": "MiMi (健康小麥肌捲髮雙丸子女孩)",
        "feature": "3D Pixar 風格小麥色健康肌膚小女孩，蓬鬆黑棕自然捲雙丸子頭、明亮深褐大眼、暖陽般燦爛笑容",
        "tracks": "Track 05《蜂蜜甜甜話·口出恩慈》、Track 10《星光晚安靈魂漫步》",
        "version": "版本 B：星光晚安薰衣草天鵝絨睡衣裝 (Starlight Velvet Pajama)",
        "costume": "暮色深藍與薰衣草紫漸層柔軟天鵝絨睡衣套裝（印有淡淡金星）、毛絨絨米白拖鞋、手抱一顆發光柔軟小抱枕",
        "pose": "雙手抱著發光小星星抱枕，打著輕輕的小哈欠，隨 84 BPM 晚安曲緩緩搖晃",
        "prompt": "9:16 vertical full-body shot, Disney Pixar 3D CGI style, adorable 5-year-old girl MiMi, rich bronze skin, twin puffy buns with sleepy star clips, sleepy affectionate smile. Wearing cozy twilight-blue velvet pajamas with faint gold constellation prints, fluffy cream slippers, hugging a soft glowing star plushie. Gentle lullaby bedtime sway, swaying side to side peacefully to a slow soul rhythm. Starlit cozy nursery stage with soft moonbeam and twinkling warm fairy lights, Disney Pixar 3D render, 8k resolution --no text, blur.",
        "status": "提示詞已就緒（排定第二梯次批次生圖）"
    }
]

# Track summaries for Sheet 1
ALBUM3_TRACK_SUMMARY = [
    {
        "num": "Track #01",
        "en": "Super Share Smile",
        "zh": "快樂分享超能力",
        "dancer": "Jessie (波浪雙馬尾女孩)",
        "style": "J-Pop Upbeat Shibuya Pop (原宿澀谷活力偶像手勢舞)",
        "phrases": 7,
        "duration": "02:00.00",
        "point": "【分享超能力手勢舞】雙手向外送出禮物，接雙手合十放胸前，最後展開大微笑跳躍！"
    },
    {
        "num": "Track #02",
        "en": "Jump for Joy Morning",
        "zh": "晨光喜樂大跳躍",
        "dancer": "Kai (陽光刺蝟頭男孩)",
        "style": "Energetic J-Pop Anime Opening Beat (元氣動漫熱血晨操彈跳風)",
        "phrases": 7,
        "duration": "02:00.00",
        "point": "【喜樂晨光大彈跳】雙臂高舉向天空抓取晨光，左右交叉踏跳踩點，爆發力十足！"
    },
    {
        "num": "Track #03",
        "en": "Deep Breath Rainbow",
        "zh": "彩虹深呼吸·和平心",
        "dancer": "Hana (烏黑齊瀏海女孩)",
        "style": "Gentle J-Pop Neo-Acoustic Ballad (慢歌 · 和風櫻花抒情優雅呼吸舞)",
        "phrases": 6,
        "duration": "02:00.00",
        "point": "【彩虹深呼吸拱門】雙手由丹田緩慢上升吸氣，在頭頂劃開七彩大彩虹，緩緩吐氣微蹲！"
    },
    {
        "num": "Track #04",
        "en": "One by One, Waiting Line",
        "zh": "耐心排隊小火車",
        "dancer": "Tim (蓬鬆呆毛棕髮男孩)",
        "style": "Playful J-Pop Shuffle Beat (童趣歡樂搖擺站長踩步舞)",
        "phrases": 7,
        "duration": "02:00.00",
        "point": "【小火車站長鳴笛步】雙手輪流拉響汽笛，雙腳踏點前進，轉身排成筆直小火車！"
    },
    {
        "num": "Track #05",
        "en": "Magic Words: Please & Thanks",
        "zh": "禮貌魔法小咒語",
        "dancer": "Jessie (波浪雙馬尾女孩)",
        "style": "Sweet J-Pop Idol Choreo (甜美日系女團禮貌鞠躬魔法舞)",
        "phrases": 7,
        "duration": "02:00.00",
        "point": "【禮貌魔法蝴蝶步】雙手合十微躬請請請，掌心向上送出謝謝，優雅旋轉微蹲！"
    },
    {
        "num": "Track #06",
        "en": "Helping Hands Together",
        "zh": "小小好幫手·良善心",
        "dancer": "MiMi (健康小麥肌女孩)",
        "style": "Bouncy J-Pop Funk Pop (活力滿點小幫手推推推律動風)",
        "phrases": 7,
        "duration": "02:00.00",
        "point": "【愛心推推幫手步】雙手向前推開溫暖，左右揮手打掃乾淨，牽起雙手歡呼！"
    },
    {
        "num": "Track #07",
        "en": "Promise Keepers Club",
        "zh": "約定小精靈·信實守諾",
        "dancer": "Tim (蓬鬆呆毛棕髮男孩)",
        "style": "Marching J-Pop Brass Beat (陽光管樂行進童軍守約手勢舞)",
        "phrases": 7,
        "duration": "02:00.00",
        "point": "【打勾勾蓋印章舞】小指打勾勾、大拇指相碰蓋印章，踏正步展現信實守諾精神！"
    },
    {
        "num": "Track #08",
        "en": "Gentle Touch Little Puppy",
        "zh": "溫柔小手抱抱你",
        "dancer": "Hana (烏黑齊瀏海女孩)",
        "style": "Warm J-Pop Lullaby Waltz (慢歌 · 櫻花小圓舞曲撫摸溫柔律動)",
        "phrases": 6,
        "duration": "02:00.00",
        "point": "【溫柔小手摸摸舞】掌心輕柔向下撫摸小狗狗，雙臂合攏輕柔搖晃，展現極致溫柔！"
    },
    {
        "num": "Track #09",
        "en": "Freeze & Stop! My Super Brake",
        "zh": "神奇小剎車·我有節制",
        "dancer": "Kai (陽光刺蝟頭男孩)",
        "style": "J-Pop Electro Dance Freeze (電音節奏跑跳與瞬間定格挑戰)",
        "phrases": 7,
        "duration": "02:00.00",
        "point": "【超級剎車定格姿態】快跑三步後雙腳急停踩剎車，雙臂張開瞬間 Freeze 靜止！"
    },
    {
        "num": "Track #10",
        "en": "Star Friends Hug It Out",
        "zh": "抱抱和好·愛的奇蹟",
        "dancer": "MiMi (健康小麥肌女孩)",
        "style": "Uplifting J-Pop Grand Finale (盛大櫻花祭大合唱抱抱舞)",
        "phrases": 7,
        "duration": "02:00.00",
        "point": "【奇蹟大擁抱旋轉】張開雙臂大跨步向前，緊緊抱住身旁好朋友，原地溫暖轉圈圈！"
    }
]

ALBUM4_TRACK_SUMMARY = [
    {
        "num": "Track #01",
        "en": "Warm Hug Symphony",
        "zh": "暖陽擁抱之歌",
        "dancer": "Jessie (波浪雙馬尾女孩)",
        "style": "Warm Soul Groove (92 BPM 溫暖日落靈魂樂暖心擁抱舞)",
        "phrases": 6,
        "duration": "02:00.00",
        "point": "【暖陽自抱雙臂舞】雙臂如擁抱金色太陽緩緩收攏於胸前，雙膝隨 92 BPM 慢搖微蹲！"
    },
    {
        "num": "Track #02",
        "en": "Sunshine in My Pocket",
        "zh": "口袋裡的快樂小音符",
        "dancer": "Kai (陽光刺蝟頭男孩)",
        "style": "Chillhop Acoustic R&B (98 BPM 輕鬆放鬆口袋彈指小滑步)",
        "phrases": 6,
        "duration": "02:00.00",
        "point": "【口袋取寶彈指步】雙手從口袋抓出金色小音符灑向空中，側身隨節奏輕快滑步！"
    },
    {
        "num": "Track #03",
        "en": "Quiet Water Flow",
        "zh": "平靜溪流深呼吸",
        "dancer": "Hana (烏黑齊瀏海女孩)",
        "style": "Ambient Meditation Soul (88 BPM 極致慢速流水冥想深呼吸)",
        "phrases": 5,
        "duration": "02:00.00",
        "point": "【平靜溪流如水舞】雙臂如水波平緩向兩側舒展，深呼吸吐氣，身心完全平靜！"
    },
    {
        "num": "Track #04",
        "en": "Slow & Steady Turtle Walk",
        "zh": "慢步小烏龜·學會耐心",
        "dancer": "Tim (蓬鬆呆毛棕髮男孩)",
        "style": "Slow-tempo Acoustic Funk (86 BPM 慢板小烏龜耐心滑步律動)",
        "phrases": 6,
        "duration": "02:00.00",
        "point": "【耐心烏龜漫步手】雙手縮在胸前如小烏龜殼，腳步穩健緩慢踩步，學會沉住氣！"
    },
    {
        "num": "Track #05",
        "en": "Honey Sweet Words",
        "zh": "蜂蜜甜甜話·口出恩慈",
        "dancer": "MiMi (健康小麥肌女孩)",
        "style": "Smooth Velvet R&B (90 BPM 甜美絲絨蜂蜜慢搖手勢舞)",
        "phrases": 5,
        "duration": "02:00.00",
        "point": "【蜂蜜蜜糖嘴型舞】手指沾取甜蜜在嘴角綻放笑容，雙手捧心送出最恩慈的話語！"
    },
    {
        "num": "Track #06",
        "en": "Little Honest Tree",
        "zh": "誠實小樹苗·良善之心",
        "dancer": "Hana (烏黑齊瀏海女孩)",
        "style": "Acoustic Soul Lullaby (94 BPM 溫柔樹苗向上萌芽舒展身姿)",
        "phrases": 6,
        "duration": "02:00.00",
        "point": "【誠實小樹苗生長姿】雙手自胸前合十如小幼苗，隨旋律慢慢向上穿透天空長成大樹！"
    },
    {
        "num": "Track #07",
        "en": "Rock Solid Friend",
        "zh": "堅定小燈塔·守信夥伴",
        "dancer": "Kai (陽光刺蝟頭男孩)",
        "style": "Mid-tempo Gospel Soul (96 BPM 堅定信實拍掌與腳踏大地舞)",
        "phrases": 6,
        "duration": "02:00.00",
        "point": "【堅定燈塔指引步】一手如燈塔高舉照亮前方，雙腿重重踩實大地，眼神無比信實！"
    },
    {
        "num": "Track #08",
        "en": "Butterfly Whisper",
        "zh": "蝴蝶細語·溫柔的聲音",
        "dancer": "Jessie (波浪雙馬尾女孩)",
        "style": "Delicate Soul Breeze (86 BPM 極致輕柔蝴蝶振翅慢速舞)",
        "phrases": 5,
        "duration": "02:00.00",
        "point": "【蝴蝶拍翅耳語步】大拇指相扣在胸前化作蝴蝶輕柔拍動，躡手躡腳側步輕聲說話！"
    },
    {
        "num": "Track #09",
        "en": "Pause, Think, and Choose",
        "zh": "停一下·想一想·明智節制",
        "dancer": "Tim (蓬鬆呆毛棕髮男孩)",
        "style": "Jazzy R&B Swing (92 BPM 爵士靈魂節奏思考思考再決定舞)",
        "phrases": 6,
        "duration": "02:00.00",
        "point": "【明智思考指尖步】單掌往前伸出 Pause 手勢，另一手輕點腦袋想一想，微笑點頭！"
    },
    {
        "num": "Track #10",
        "en": "Starlight Goodnight Lullaby",
        "zh": "星光晚安靈魂漫步",
        "dancer": "MiMi (健康小麥肌女孩)",
        "style": "Velvet Sleepy R&B Lullaby (84 BPM 沉靜晚安搖籃星光慢步)",
        "phrases": 5,
        "duration": "02:00.00",
        "point": "【星光晚安搖籃步】雙手捧著發光小星星入懷，身體左右緩緩入眠慢搖，道聲晚安！"
    }
]

def group_song_timeline(timeline, target_groups):
    n = len(timeline)
    groups = []
    chunk_size = max(1, n // target_groups)
    idx = 0
    while idx < n:
        if len(groups) == target_groups - 1:
            group_segs = timeline[idx:]
            idx = n
        else:
            group_segs = timeline[idx:idx + chunk_size]
            idx += chunk_size
        
        start_time = group_segs[0]['start']
        end_time = group_segs[-1]['end']
        dur = round(end_time - start_time, 2)
        
        lyrics_list = [s.get('lyric', '').strip(' "') for s in group_segs if s.get('lyric') and not s.get('lyric').startswith('[')]
        if not lyrics_list:
            lyrics_str = group_segs[0].get('lyric', '').strip(' "')
        else:
            lyrics_str = " / ".join(lyrics_list)
        
        subs_list = [s.get('sub', '').strip() for s in group_segs if s.get('sub')]
        subs_str = " ➜ ".join(subs_list[:3])
        
        title_str = group_segs[0].get('title', '')
        if len(group_segs) > 1:
            title_str += f" 至 {group_segs[-1].get('title', '')}"
        
        poses = [s.get('targetPose', 'march') for s in group_segs]
        pose = poses[len(poses)//2]
        
        groups.append({
            'start': start_time,
            'end': end_time,
            'duration': dur,
            'lyrics': lyrics_str,
            'subs': subs_str,
            'title': title_str,
            'pose': pose,
            'segs': group_segs
        })
    return groups

def build_album3_spec():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    
    # ----------------- SHEET 1: 曲目總覽 -----------------
    ws1 = wb.create_sheet('1_曲目總覽與角色分配')
    ws1.views.sheetView[0].showGridLines = True
    
    ws1.merge_cells('A1:H1')
    title_cell = ws1['A1']
    title_cell.value = "🌸 KaiDance 第三顆星球《Sakura Neo Pop 櫻花星球》J-Pop 幼兒舞蹈動作與動畫製作規格總表"
    title_cell.font = Font(name=FONT_NAME, size=15, bold=True, color="FFFFFF")
    title_cell.fill = PatternFill(start_color="9D174D", end_color="9D174D", fill_type="solid")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[1].height = 42
    
    headers1 = ['曲目編號', '英文歌名', '中文歌名', '負責領舞主角 (5位小朋友)', 'J-Pop 曲風與舞蹈風格定位', '整合樂句幕數', '總時長', '核心 J-Pop 記憶點舞步 (Point Dance)']
    ws1.append(headers1)
    ws1.row_dimensions[2].height = 28
    for col_idx in range(1, 9):
        cell = ws1.cell(row=2, column=col_idx)
        cell.font = Font(name=FONT_NAME, size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="BE185D", end_color="BE185D", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = create_thin_border()
        
    for r_idx, t in enumerate(ALBUM3_TRACK_SUMMARY, start=3):
        row_vals = [
            t['num'], t['en'], t['zh'], t['dancer'], t['style'], f"{t['phrases']} 幕 (樂句整合)", t['duration'], t['point']
        ]
        ws1.append(row_vals)
        ws1.row_dimensions[r_idx].height = 36
        for c_idx in range(1, 9):
            cell = ws1.cell(row=r_idx, column=c_idx)
            cell.font = Font(name=FONT_NAME, size=10)
            cell.border = create_thin_border()
            if c_idx in [1, 6, 7]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
                
    ws1_widths = {'A': 14.0, 'B': 28.0, 'C': 24.0, 'D': 28.0, 'E': 38.0, 'F': 16.0, 'G': 12.0, 'H': 45.0}
    for col, width in ws1_widths.items():
        ws1.column_dimensions[col].width = width

    # ----------------- SHEET 2: 角色造型提示詞 -----------------
    ws2 = wb.create_sheet('2_五位主角Jpop造型圖提示詞')
    ws2.views.sheetView[0].showGridLines = True
    
    ws2.merge_cells('A1:H1')
    t2_cell = ws2['A1']
    t2_cell.value = "🌸 第三輯《Sakura Neo Pop》5 位主角 J-Pop 櫻花偶像時尚造型（每人 2 種版本，共 10 組 9:16 靜態底圖規格與提示詞）"
    t2_cell.font = Font(name=FONT_NAME, size=14, bold=True, color="FFFFFF")
    t2_cell.fill = PatternFill(start_color="9D174D", end_color="9D174D", fill_type="solid")
    t2_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws2.row_dimensions[1].height = 42
    
    headers2 = ['角色編號', '主角名稱与特徵', '負責曲目', '造型版本', 'J-Pop 時尚服裝設計細節 (中文)', '起始等候跳舞動作 (Starting Pose)', '9:16 靜態底圖生成提示詞 (英文 Prompt - 複製至生圖模型)', '已生成圖片路徑 / 狀態']
    ws2.append(headers2)
    ws2.row_dimensions[2].height = 28
    for col_idx in range(1, 9):
        cell = ws2.cell(row=2, column=col_idx)
        cell.font = Font(name=FONT_NAME, size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="BE185D", end_color="BE185D", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = create_thin_border()
        
    for r_idx, c in enumerate(ALBUM3_CHARACTERS, start=3):
        row_vals = [
            c['id'], f"{c['name']}\n({c['feature']})", c['tracks'], c['version'], c['costume'], c['pose'], c['prompt'], c['status']
        ]
        ws2.append(row_vals)
        ws2.row_dimensions[r_idx].height = 70
        for col_idx in range(1, 9):
            cell = ws2.cell(row=r_idx, column=col_idx)
            cell.font = Font(name=FONT_NAME, size=9)
            cell.border = create_thin_border()
            if col_idx in [1]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            elif col_idx in [8]:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
                if "已生成" in str(cell.value):
                    cell.font = Font(name=FONT_NAME, size=9, bold=True, color="047857")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    ws2_widths = {'A': 10.0, 'B': 30.0, 'C': 26.0, 'D': 30.0, 'E': 38.0, 'F': 32.0, 'G': 65.0, 'H': 32.0}
    for col, width in ws2_widths.items():
        ws2.column_dimensions[col].width = width

    # ----------------- SHEET 3: 全曲目整合樂句總表 -----------------
    ws3 = wb.create_sheet('3_全曲目68幕動畫提示詞總表')
    ws3.views.sheetView[0].showGridLines = True
    
    headers3 = [
        '曲目與幕次', '建議影片檔名', '時間區間 (分:秒)', '時長(秒)', '領舞主角', '段落主題', '對應英文歌詞 (SRT同步整合)',
        'J-Pop 幼兒舞蹈動作拆解說明 (中文)', '名師動感口令 (中文)', '火柴人姿態', 'AI 動畫生成提示詞 (英文 Prompt - 適用於 MiniMax/Kling/Runway 9:16)',
        'AI 動畫生成提示詞 (中文對照說明)'
    ]
    ws3.append(headers3)
    ws3.row_dimensions[1].height = 28
    for col_idx in range(1, 13):
        cell = ws3.cell(row=1, column=col_idx)
        cell.font = Font(name=FONT_NAME, size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="9D174D", end_color="9D174D", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = create_thin_border()

    ws3_widths = {'A': 16.0, 'B': 18.0, 'C': 18.0, 'D': 10.0, 'E': 22.0, 'F': 26.0, 'G': 32.0, 'H': 45.0, 'I': 32.0, 'J': 12.0, 'K': 65.0, 'L': 55.0}
    for col, width in ws3_widths.items():
        ws3.column_dimensions[col].width = width

    # Individual Track Sheets
    album_songs = db['album_3']['songs']
    ws3_row_idx = 2
    
    for s_idx, song in enumerate(album_songs):
        track_num = song['trackNumber']
        track_summary = ALBUM3_TRACK_SUMMARY[s_idx]
        target_phrases = track_summary['phrases']
        
        short_title = re.sub(r'[^\w\s]', '', song['zhTitle'])[:10]
        sheet_name = f"T{track_num:02d}_{short_title}"
        ws_track = wb.create_sheet(sheet_name)
        ws_track.views.sheetView[0].showGridLines = True
        
        ws_track.merge_cells('A1:L1')
        t_header = ws_track['A1']
        t_header.value = f"🌸 Track #{track_num:02d}: {song['title']} ({song['zhTitle']}) ｜ 領舞：{track_summary['dancer']} ｜ 風格：{track_summary['style']}"
        t_header.font = Font(name=FONT_NAME, size=12, bold=True, color="FFFFFF")
        t_header.fill = PatternFill(start_color="9D174D", end_color="9D174D", fill_type="solid")
        t_header.alignment = Alignment(horizontal="left", vertical="center")
        ws_track.row_dimensions[1].height = 36
        
        ws_track.append(headers3)
        ws_track.row_dimensions[2].height = 26
        for col_idx in range(1, 13):
            cell = ws_track.cell(row=2, column=col_idx)
            cell.font = Font(name=FONT_NAME, size=9, bold=True, color="FFFFFF")
            cell.fill = PatternFill(start_color="BE185D", end_color="BE185D", fill_type="solid")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            cell.border = create_thin_border()
        for col, width in ws3_widths.items():
            ws_track.column_dimensions[col].width = width
            
        phrases = group_song_timeline(song['timeline'], target_phrases)
        dancer_name = track_summary['dancer']
        
        if "Kai" in dancer_name:
            char_en = "5-year-old boy Kai with spiky layered brown hair and sunny smile, wearing pastel sakura-pink and neon teal Tokyo idol bomber jacket and white shorts"
            char_zh = "Kai (陽光刺蝟頭男孩，穿著櫻花粉藍拼接教練夾克)"
        elif "Jessie" in dancer_name:
            char_en = "5-year-old girl Jessie with wavy twin pigtails with sakura ribbons, wearing pastel macaron idol stage dress with ruffled organza skirt"
            char_zh = "Jessie (波浪雙馬尾女孩，穿著櫻花馬卡龍女團偶像蓬蓬裙)"
        elif "Tim" in dancer_name:
            char_en = "5-year-old boy Tim with fluffy curly brown hair and playful cowlick, wearing mint-green and sunny-yellow Harajuku utility vest and light joggers"
            char_zh = "Tim (蓬鬆呆毛棕髮男孩，穿著薄荷黃拼接活力工裝背心)"
        elif "Hana" in dancer_name:
            char_en = "5-year-old Asian girl Hana with sleek black bob haircut and straight bangs, wearing delicate pastel sakura kimono-pop top and layered blush bubble skirt"
            char_zh = "Hana (烏黑齊瀏海亞裔女孩，穿著和風櫻雪改良式偶像裙)"
        else: # MiMi
            char_en = "5-year-old girl MiMi with warm bronze skin and curly twin space buns, wearing vibrant orange-yellow overall dress with cute patches"
            char_zh = "MiMi (健康小麥肌雙丸子捲髮女孩，穿著高彩原宿糖果吊帶裙)"
            
        track_row_idx = 3
        for p_idx, phrase in enumerate(phrases, start=1):
            seg_code = f"Track {track_num:02d} - #{p_idx:02d}"
            seg_code_short = f"#{p_idx:02d}"
            filename = f"a3_t{track_num}_phrase_{p_idx:02d}.mp4"
            time_range = f"{format_time(phrase['start'])} ~ {format_time(phrase['end'])}"
            dur = phrase['duration']
            
            theme_title = f"第 {p_idx:02d} 樂句: {phrase['title'][:20]}"
            lyrics_text = f'"{phrase["lyrics"]}"' if phrase["lyrics"] else '🎵 [音樂間奏律動]'
            
            dance_action = f"🌸 【J-Pop 律動樂句 {p_idx:02d}】{phrase['subs']} ｜ 腳步配合輕快踩點與左右踏併步（Step-Touch），眼神自信放電、笑容甜美朝氣！"
            coach_call = f"小朋友跟著節拍，一二跳躍踩點，做出最棒的 J-Pop 偶像舞步！"
            
            en_prompt = f"9:16 vertical full-body shot, Disney Pixar 3D CGI animation style, adorable {char_en}. Smooth natural dance choreography for song '{song['title']}', phrase {p_idx}: {phrase['subs']}. Joyful rhythmic dance movement, energetic cheerful expression, looking into camera. Vibrant Tokyo Harajuku sakura stage with soft pink cherry blossom petals, bright colorful lighting, ultra-fluid 60fps CGI animation, 4k render, Disney Pixar musical style --no text, watermarks, distorted limbs."
            zh_prompt = f"【9:16 直式全身鏡位】主角：{char_zh}。場景：東京原宿櫻花星光舞台（漂浮櫻花花瓣與柔和 LED 霓虹燈）。樂句 {p_idx:02d}：{lyrics_text}。動作：{dance_action}。鏡頭運鏡平穩流暢，角色動作富有彈性與朝氣。"
            
            row_data_ws3 = [
                seg_code, filename, time_range, dur, dancer_name, theme_title, lyrics_text,
                dance_action, coach_call, phrase['pose'], en_prompt, zh_prompt
            ]
            
            row_data_track = [
                seg_code_short, filename, time_range, dur, dancer_name, theme_title, lyrics_text,
                dance_action, coach_call, phrase['pose'], en_prompt, zh_prompt
            ]
            
            ws3.append(row_data_ws3)
            ws3.row_dimensions[ws3_row_idx].height = 65
            for c_idx in range(1, 13):
                cell = ws3.cell(row=ws3_row_idx, column=c_idx)
                cell.font = Font(name=FONT_NAME, size=9)
                cell.border = create_thin_border()
                if c_idx in [1, 2, 3, 4, 10]:
                    cell.alignment = Alignment(horizontal="center", vertical="center")
                else:
                    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            ws3_row_idx += 1
            
            ws_track.append(row_data_track)
            ws_track.row_dimensions[track_row_idx].height = 65
            for c_idx in range(1, 13):
                cell = ws_track.cell(row=track_row_idx, column=c_idx)
                cell.font = Font(name=FONT_NAME, size=9)
                cell.border = create_thin_border()
                if c_idx in [1, 2, 3, 4, 10]:
                    cell.alignment = Alignment(horizontal="center", vertical="center")
                else:
                    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            track_row_idx += 1
            
    return wb

def build_album4_spec():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    
    # ----------------- SHEET 1: 曲目總覽 -----------------
    ws1 = wb.create_sheet('1_曲目總覽與角色分配')
    ws1.views.sheetView[0].showGridLines = True
    
    ws1.merge_cells('A1:H1')
    title_cell = ws1['A1']
    title_cell.value = "🌅 KaiDance 第四顆星球《Sunset Soul Groove 日落星球》R&B / Soul 幼兒舒緩律動與動畫製作規格總表"
    title_cell.font = Font(name=FONT_NAME, size=15, bold=True, color="FFFFFF")
    title_cell.fill = PatternFill(start_color="9A3412", end_color="9A3412", fill_type="solid")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[1].height = 42
    
    headers1 = ['曲目編號', '英文歌名', '中文歌名', '負責領舞主角 (5位小朋友)', 'R&B 曲風與舞蹈風格定位', '整合樂句幕數', '總時長', '核心 R&B 記憶點舞步 (Point Dance)']
    ws1.append(headers1)
    ws1.row_dimensions[2].height = 28
    for col_idx in range(1, 9):
        cell = ws1.cell(row=2, column=col_idx)
        cell.font = Font(name=FONT_NAME, size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="B45309", end_color="B45309", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = create_thin_border()
        
    for r_idx, t in enumerate(ALBUM4_TRACK_SUMMARY, start=3):
        row_vals = [
            t['num'], t['en'], t['zh'], t['dancer'], t['style'], f"{t['phrases']} 幕 (慢歌樂句整合)", t['duration'], t['point']
        ]
        ws1.append(row_vals)
        ws1.row_dimensions[r_idx].height = 36
        for c_idx in range(1, 9):
            cell = ws1.cell(row=r_idx, column=c_idx)
            cell.font = Font(name=FONT_NAME, size=10)
            cell.border = create_thin_border()
            if c_idx in [1, 6, 7]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
                
    ws1_widths = {'A': 14.0, 'B': 28.0, 'C': 24.0, 'D': 28.0, 'E': 38.0, 'F': 16.0, 'G': 12.0, 'H': 45.0}
    for col, width in ws1_widths.items():
        ws1.column_dimensions[col].width = width

    # ----------------- SHEET 2: 角色造型提示詞 -----------------
    ws2 = wb.create_sheet('2_五位主角RnB造型圖提示詞')
    ws2.views.sheetView[0].showGridLines = True
    
    ws2.merge_cells('A1:H1')
    t2_cell = ws2['A1']
    t2_cell.value = "🌅 第四輯《Sunset Soul Groove》5 位主角 R&B 暖心大地時尚造型（每人 2 種版本，共 10 組 9:16 靜態底圖規格與提示詞）"
    t2_cell.font = Font(name=FONT_NAME, size=14, bold=True, color="FFFFFF")
    t2_cell.fill = PatternFill(start_color="9A3412", end_color="9A3412", fill_type="solid")
    t2_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws2.row_dimensions[1].height = 42
    
    headers2 = ['角色編號', '主角名稱与特徵', '負責曲目', '造型版本', 'R&B 時尚服裝設計細節 (中文)', '起始等候跳舞動作 (Starting Pose)', '9:16 靜態底圖生成提示詞 (英文 Prompt - 複製至生圖模型)', '已生成圖片路徑 / 狀態']
    ws2.append(headers2)
    ws2.row_dimensions[2].height = 28
    for col_idx in range(1, 9):
        cell = ws2.cell(row=2, column=col_idx)
        cell.font = Font(name=FONT_NAME, size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="B45309", end_color="B45309", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = create_thin_border()
        
    for r_idx, c in enumerate(ALBUM4_CHARACTERS, start=3):
        row_vals = [
            c['id'], f"{c['name']}\n({c['feature']})", c['tracks'], c['version'], c['costume'], c['pose'], c['prompt'], c['status']
        ]
        ws2.append(row_vals)
        ws2.row_dimensions[r_idx].height = 70
        for col_idx in range(1, 9):
            cell = ws2.cell(row=r_idx, column=col_idx)
            cell.font = Font(name=FONT_NAME, size=9)
            cell.border = create_thin_border()
            if col_idx in [1]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    ws2_widths = {'A': 10.0, 'B': 30.0, 'C': 26.0, 'D': 30.0, 'E': 38.0, 'F': 32.0, 'G': 65.0, 'H': 32.0}
    for col, width in ws2_widths.items():
        ws2.column_dimensions[col].width = width

    # ----------------- SHEET 3: 全曲目整合樂句總表 -----------------
    ws3 = wb.create_sheet('3_全曲目56幕動畫提示詞總表')
    ws3.views.sheetView[0].showGridLines = True
    
    headers3 = [
        '曲目與幕次', '建議影片檔名', '時間區間 (分:秒)', '時長(秒)', '領舞主角', '段落主題', '對應英文歌詞 (SRT同步整合)',
        'R&B 幼兒舞蹈動作拆解說明 (中文)', '名師動感口令 (中文)', '火柴人姿態', 'AI 動畫生成提示詞 (英文 Prompt - 適用於 MiniMax/Kling/Runway 9:16)',
        'AI 動畫生成提示詞 (中文對照說明)'
    ]
    ws3.append(headers3)
    ws3.row_dimensions[1].height = 28
    for col_idx in range(1, 13):
        cell = ws3.cell(row=1, column=col_idx)
        cell.font = Font(name=FONT_NAME, size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="9A3412", end_color="9A3412", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = create_thin_border()

    ws3_widths = {'A': 16.0, 'B': 18.0, 'C': 18.0, 'D': 10.0, 'E': 22.0, 'F': 26.0, 'G': 32.0, 'H': 45.0, 'I': 32.0, 'J': 12.0, 'K': 65.0, 'L': 55.0}
    for col, width in ws3_widths.items():
        ws3.column_dimensions[col].width = width

    album_songs = db['album_4']['songs']
    ws3_row_idx = 2
    
    for s_idx, song in enumerate(album_songs):
        track_num = song['trackNumber']
        track_summary = ALBUM4_TRACK_SUMMARY[s_idx]
        target_phrases = track_summary['phrases']
        
        short_title = re.sub(r'[^\w\s]', '', song['zhTitle'])[:10]
        sheet_name = f"T{track_num:02d}_{short_title}"
        ws_track = wb.create_sheet(sheet_name)
        ws_track.views.sheetView[0].showGridLines = True
        
        ws_track.merge_cells('A1:L1')
        t_header = ws_track['A1']
        t_header.value = f"🌅 Track #{track_num:02d}: {song['title']} ({song['zhTitle']}) ｜ 領舞：{track_summary['dancer']} ｜ 風格：{track_summary['style']}"
        t_header.font = Font(name=FONT_NAME, size=12, bold=True, color="FFFFFF")
        t_header.fill = PatternFill(start_color="9A3412", end_color="9A3412", fill_type="solid")
        t_header.alignment = Alignment(horizontal="left", vertical="center")
        ws_track.row_dimensions[1].height = 36
        
        ws_track.append(headers3)
        ws_track.row_dimensions[2].height = 26
        for col_idx in range(1, 13):
            cell = ws_track.cell(row=2, column=col_idx)
            cell.font = Font(name=FONT_NAME, size=9, bold=True, color="FFFFFF")
            cell.fill = PatternFill(start_color="B45309", end_color="B45309", fill_type="solid")
            cell.alignment = Alignment(horizontal="center", vertical="center")
            cell.border = create_thin_border()
        for col, width in ws3_widths.items():
            ws_track.column_dimensions[col].width = width
            
        phrases = group_song_timeline(song['timeline'], target_phrases)
        dancer_name = track_summary['dancer']
        
        if "Kai" in dancer_name:
            char_en = "5-year-old boy Kai with spiky soft brown hair and warm smile, wearing cozy caramel-brown fine corduroy chore jacket and charcoal relaxed trousers"
            char_zh = "Kai (陽光刺蝟頭男孩，穿著焦糖暖棕燈芯絨休閒夾克)"
        elif "Jessie" in dancer_name:
            char_en = "5-year-old girl Jessie with wavy twin low pigtails with amber satin ribbons, wearing oversized cozy pumpkin-orange cable-knit sweater and cream pleat skirt"
            char_zh = "Jessie (波浪雙馬尾女孩，穿著日落暖橘羊毛針織長版毛衣)"
        elif "Tim" in dancer_name:
            char_en = "5-year-old boy Tim with fluffy curly brown hair with cowlick, wearing moss-green tweed waistcoat vest over cream linen shirt and chocolate corduroy pants"
            char_zh = "Tim (蓬鬆呆毛棕髮男孩，穿著復古西裝背心與燈芯絨長褲)"
        elif "Hana" in dancer_name:
            char_en = "5-year-old Asian girl Hana with silky black bob haircut and straight bangs, wearing soothing Morandi dusty-rose linen dress and cream knit shawl"
            char_zh = "Hana (烏黑齊瀏海亞裔女孩，穿著莫蘭迪茶歇長裙與針織披肩)"
        else: # MiMi
            char_en = "5-year-old girl MiMi with warm bronze skin and twin space buns with wooden beads, wearing luxurious honey-amber velvet jumpsuit"
            char_zh = "MiMi (健康小麥肌雙丸子捲髮女孩，穿著蜜糖琥珀金絨面連身短褲)"
            
        track_row_idx = 3
        for p_idx, phrase in enumerate(phrases, start=1):
            seg_code = f"Track {track_num:02d} - #{p_idx:02d}"
            seg_code_short = f"#{p_idx:02d}"
            filename = f"a4_t{track_num}_phrase_{p_idx:02d}.mp4"
            time_range = f"{format_time(phrase['start'])} ~ {format_time(phrase['end'])}"
            dur = phrase['duration']
            
            theme_title = f"第 {p_idx:02d} 樂句: {phrase['title'][:20]}"
            lyrics_text = f'"{phrase["lyrics"]}"' if phrase["lyrics"] else '🎵 [靈魂樂放鬆間奏]'
            
            dance_action = f"🌅 【R&B 舒緩樂句 {p_idx:02d}】{phrase['subs']} ｜ 雙臂優雅延展，身體隨慢速 R&B 鼓點溫柔放鬆慢搖（Groove Sway），充滿療癒與溫暖！"
            coach_call = f"感受溫暖夕陽，跟著慢拍輕輕搖擺，動作柔和放鬆～"
            
            en_prompt = f"9:16 vertical full-body shot, Disney Pixar 3D CGI animation style, adorable {char_en}. Smooth gentle dance choreography for slow R&B song '{song['title']}', phrase {p_idx}: {phrase['subs']}. Peaceful slow swaying dance movement, tender joyful smile, serene warm eye contact. Cozy golden-hour sunset lounge studio, warm amber volumetric sunlight, wooden acoustic floors, ultra-smooth 60fps CGI animation, 4k render, Disney Pixar musical style --no text, watermarks, distorted limbs."
            zh_prompt = f"【9:16 直式全身鏡位】主角：{char_zh}。場景：日落金色客廳錄音室（夕陽餘暉、原木地板與柔和壁燈）。樂句 {p_idx:02d}：{lyrics_text}。動作：{dance_action}。運鏡平緩柔美，角色全身肢體動作溫潤而舒緩。"
            
            row_data_ws3 = [
                seg_code, filename, time_range, dur, dancer_name, theme_title, lyrics_text,
                dance_action, coach_call, phrase['pose'], en_prompt, zh_prompt
            ]
            
            row_data_track = [
                seg_code_short, filename, time_range, dur, dancer_name, theme_title, lyrics_text,
                dance_action, coach_call, phrase['pose'], en_prompt, zh_prompt
            ]
            
            ws3.append(row_data_ws3)
            ws3.row_dimensions[ws3_row_idx].height = 65
            for c_idx in range(1, 13):
                cell = ws3.cell(row=ws3_row_idx, column=c_idx)
                cell.font = Font(name=FONT_NAME, size=9)
                cell.border = create_thin_border()
                if c_idx in [1, 2, 3, 4, 10]:
                    cell.alignment = Alignment(horizontal="center", vertical="center")
                else:
                    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            ws3_row_idx += 1
            
            ws_track.append(row_data_track)
            ws_track.row_dimensions[track_row_idx].height = 65
            for c_idx in range(1, 13):
                cell = ws_track.cell(row=track_row_idx, column=c_idx)
                cell.font = Font(name=FONT_NAME, size=9)
                cell.border = create_thin_border()
                if c_idx in [1, 2, 3, 4, 10]:
                    cell.alignment = Alignment(horizontal="center", vertical="center")
                else:
                    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            track_row_idx += 1
            
    return wb

print("Building Album 3 Spec...")
wb3 = build_album3_spec()
alb3_path = "Album3_Jpop_Dance_Production_Spec.xlsx"
wb3.save(alb3_path)
shutil.copy2(alb3_path, "web_app/" + alb3_path)
shutil.copy2(alb3_path, "docs/" + alb3_path)
print(f"Album 3 saved: {alb3_path} (copied to web_app and docs)")

print("Building Album 4 Spec...")
wb4 = build_album4_spec()
alb4_path = "Album4_RnB_Dance_Production_Spec.xlsx"
wb4.save(alb4_path)
shutil.copy2(alb4_path, "web_app/" + alb4_path)
shutil.copy2(alb4_path, "docs/" + alb4_path)
print(f"Album 4 saved: {alb4_path} (copied to web_app and docs)")

print("All Excel files generated successfully!")
