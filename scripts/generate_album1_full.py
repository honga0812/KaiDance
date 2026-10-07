# -*- coding: utf-8 -*-
import json, os, re

def parse_srt(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = re.split(r'\n\s*\n', content.strip())
    cues = []
    for b in blocks:
        lines = [l.strip() for l in b.split('\n') if l.strip()]
        if len(lines) >= 3 and '-->' in lines[1]:
            m = re.match(r'(\d+):(\d+):(\d+)[,\.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,\.](\d+)', lines[1])
            if m:
                s_h, s_m, s_s, s_ms, e_h, e_m, e_s, e_ms = map(int, m.groups())
                start_sec = round(s_h*3600 + s_m*60 + s_s + s_ms/1000.0, 2)
                end_sec = round(e_h*3600 + e_m*60 + e_s + e_ms/1000.0, 2)
                text = ' '.join(lines[2:])
                cues.append({'index': int(lines[0]), 'start': start_sec, 'end': end_sec, 'text': text})
    return cues

# Dictionary of song specific configurations
song_configs = {
    "a1_s01": {
        "srt": "1.O.Morning Sunshine Hello.srt",
        "intro": {"title": "[前奏] 晨光萌芽踏步", "sub": "⏰ 精神小士兵，原地踩著節拍踏步走！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg", "vid": "./videos/loop_01_march.mp4"},
        "cues": {
            1: {"title": "托起太陽高高舉", "sub": "☀️ 雙手從胸前托起大太陽高高升起！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg", "vid": "./videos/托起太陽高空大招手.mp4"},
            2: {"title": "金色小手大招手", "sub": "👋 雙手在天空左右大弧度歡快招手！", "pose": "wave", "img": "./images/boy_sun_stretch_1790914097504.jpg", "vid": "./videos/托起太陽高空大招手.mp4"},
            3: {"title": "刷刷小牙笑一笑", "sub": "🪥 小牙刷刷刷刷，露出最燦爛笑容！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg", "vid": "./videos/刷牙微笑大步走.mp4"},
            4: {"title": "邁開大步出發囉", "sub": "👟 雙手插腰精神抖擻，大步邁開去探險！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg", "vid": "./videos/刷牙微笑大步走.mp4"},
            5: {"title": "樹梢小鳥展翅飛", "sub": "🐦 雙臂輕快拍動，學小鳥在樹梢滑翔！", "pose": "sway", "img": "./images/girl_dance_coach_1790908344383.jpg"},
            6: {"title": "貼耳聽清晨鳥鳴", "sub": "🎶 小手貼耳，身體左右輕輕搖擺聽晨曲！", "pose": "sway", "img": "./images/girl_dance_coach_1790908344383.jpg"},
            7: {"title": "熱情招手說哈囉", "sub": "👋 揮舞雙手大聲喊 Hello，全新一天開始！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            8: {"title": "活力蹦跳喊萬歲", "sub": "⭐ 雙膝下蹲蓄力，高高跳起喊萬歲！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            9: {"title": "穿上小鞋數一二三", "sub": "👟 摸摸左右小鞋子，伸指數：一、二、三！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            10: {"title": "張開雙手齊邀請", "sub": "🎶 雙手像花朵向外盛開，邀請好朋友唱歌！", "pose": "reach", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            11: {"title": "同唱早安小圓舞", "sub": "🌸 雙手插腰轉個歡樂大圓圈，站定比個花！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            12: {"title": "背起書包戴正帽", "sub": "🎒 背起小書包、摸摸小帽子，準備好！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            13: {"title": "跟貪睡小貓說拜拜", "sub": "🐱 雙手揉揉眼睛學小貓咪，俏皮說拜拜！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            14: {"title": "抬頭看天空好藍", "sub": "☁️ 墊起腳尖手遮額頭，抬頭仰望美麗藍天！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            15: {"title": "精彩探險等著你", "sub": "💖 雙手在胸前比個大愛心，滿滿期待！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            16: {"title": "再次熱情大招手", "sub": "👋 雙腳踩節奏，雙手像波浪歡樂招手！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            17: {"title": "深蹲起跳歡呼耶", "sub": "🐰 蹲下蓄力、高高起飛，小拳頭喊耶！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            18: {"title": "動感腳尖踢點步", "sub": "👟 雙手插腰，左右小腳尖輕輕點地數數！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            19: {"title": "歡樂拍手合唱曲", "sub": "👏 胸前大聲拍手：啪啪啪，身體彈動！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            20: {"title": "白鴿展翅大滑翔", "sub": "🕊️ 雙手水平展開像大鳥，隨微風滑翔！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            21: {"title": "擁抱世界道早安", "sub": "🌍 雙臂向外畫大圓，擁抱美麗全世界！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            22: {"title": "定格燦爛大微笑", "sub": "🌟 雙手胸前比心鞠躬，定格燦爛笑容！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"}
        }
    },
    "a1_s02": {
        "srt": "2.O.Count with Me 1 to 10.srt",
        "intro": {"title": "[前奏] 數字小士兵預備踏步", "sub": "🔢 準備好小手小腳，踩出節拍踏步走！", "pose": "march", "img": "./images/girl_dance_coach_1790908344383.jpg"},
        "cues": {
            1: {"title": "伸指比 1 摸蘋果", "sub": "🍎 右手比 1 摘樹上紅蘋果！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            2: {"title": "伸指比 2 學小鳥", "sub": "🐦 雙手比 2 當小鳥翅膀搧呀搧！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            3: {"title": "伸指比 3 滾滾球", "sub": "⚽ 雙手比 3 在地面滾滾彩色小球！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            4: {"title": "伸指比 4 敲敲門", "sub": "🐱 伸出 4 隻手指學小貓敲門咚咚咚！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            5: {"title": "伸出 5 指小蜜蜂", "sub": "🐝 張開 5 隻手指學蜜蜂嗡嗡飛！", "pose": "wave", "img": "./images/girl_dance_coach_1790908344383.jpg"},
            6: {"title": "數數朋友 1 到 5", "sub": "🔢 伸出手指數一數身邊好朋友！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            7: {"title": "節奏拍手 1 2 3 4 5", "sub": "👏 跟著重音連拍 5 下：1、2、3、4、5！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            8: {"title": "數字寶寶動起來", "sub": "✨ 雙手插腰身體左右快樂扭一扭！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            9: {"title": "拍拍雙手踩踩鞋", "sub": "👟 胸前大聲拍手，腳尖輕快踏地！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            10: {"title": "大家數數真開心", "sub": "🌟 雙手高舉揮舞，數數越數越開心！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            11: {"title": "伸指比 6 游水鴨", "sub": "🦆 雙手比 6 學小鴨搖擺游游水！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            12: {"title": "伸指比 7 吹蠟燭", "sub": "🎂 雙手比 7 當生日蛋糕上的閃亮蠟燭！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            13: {"title": "伸指比 8 划小船", "sub": "⛵ 雙手比 8 當小帆船雙手划槳！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            14: {"title": "伸指比 9 升氣球", "sub": "🎈 伸指比 9 抬頭看彩色氣球飄上天！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            15: {"title": "十顆星星閃亮亮", "sub": "⭐ 雙手高舉十指張開，像繁星閃爍！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            16: {"title": "點亮夜空數數星", "sub": "✨ 左右輕柔擺手，繁星照亮整片天空！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            17: {"title": "大家齊數 1 到 10", "sub": "🔢 伸出十根手指頭，大聲數 1 到 10！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            18: {"title": "全體高聲齊歡唱", "sub": "🎶 張開雙臂放聲歌唱，整齊踩步！", "pose": "reach", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            19: {"title": "動感拍手踩踩鞋", "sub": "👟 拍拍手拍拍膝蓋，小腳踏踏踏！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            20: {"title": "數數大師好神氣", "sub": "🎉 雙手叉腰挺胸，我們都是數數小神童！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            21: {"title": "完美的 10 大定格", "sub": "⭐ 雙手比出十全十美大招手定格！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"}
        }
    },
    "a1_s03": {
        "srt": "3.O.Rainbow Color Splash.srt",
        "intro": {"title": "[前奏] 彩虹畫筆小預備", "sub": "🎨 拿起神奇彩色畫筆，準備為天空塗鴉！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
        "cues": {
            1: {"title": "紅紅櫻桃與玫瑰", "sub": "🍒 雙手胸前抱大圓，比出紅紅甜櫻桃！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            2: {"title": "紅紅按鈕小鼻子", "sub": "👃 食指輕輕點點小鼻子，俏皮笑一笑！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            3: {"title": "暖暖金黃大太陽", "sub": "☀️ 雙手向外劃出金色大圓圈，暖洋洋！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            4: {"title": "夜空星星黃澄澄", "sub": "⭐ 雙手向上摘星星，小手指眨呀眨！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            5: {"title": "大海蔚藍又寬廣", "sub": "🌊 雙臂像波浪左右推動，學大海起伏！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            6: {"title": "藍色浪花向前衝", "sub": "🏄 身體微蹲向前划水，浪花四濺！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            7: {"title": "紅黃綠藍齊點名", "sub": "🎨 雙手輪流前推點出四種神奇顏色！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            8: {"title": "搭起彩色大虹橋", "sub": "🌈 雙臂在頭頂畫出橫跨天空的彩虹橋！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            9: {"title": "色彩魔法融合轉", "sub": "🔄 雙手交疊攪拌魔法色彩，轉個小圈！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            10: {"title": "閃亮色彩好耀眼", "sub": "✨ 雙手十指向外綻放，像煙火閃爍！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            11: {"title": "青青小草小兔跳", "sub": "🐰 雙手放頭頂當兔耳，輕快蹦蹦跳！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            12: {"title": "綠綠大樹參天長", "sub": "🌲 雙腳站穩雙手上伸，像大樹高高生長！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            13: {"title": "圓圓南瓜甜又香", "sub": "🎃 雙臂胸前抱出圓滾滾大南瓜！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            14: {"title": "紫色葡萄摘一串", "sub": "🍇 伸手向上摘葡萄，大口吃進嘴裡！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            15: {"title": "畫筆蘸色轉一轉", "sub": "🖌️ 手握大畫筆在空中旋轉畫圈圈！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            16: {"title": "彩繪快樂全世界", "sub": "🌍 雙手大幅度揮灑，給全世界塗上色彩！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            17: {"title": "紅黃綠藍唱彩虹", "sub": "🎶 跟著節拍拍拍手，唱響彩虹之歌！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            18: {"title": "友情彩虹永相連", "sub": "🤝 雙手向兩側伸出，搭起友誼橋樑！", "pose": "reach", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            19: {"title": "魔法色彩閃閃光", "sub": "✨ 身體輕快彈動，十指閃爍小星星！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            20: {"title": "繽紛色彩你和我", "sub": "💖 雙手收回胸前比愛心，相親相愛！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            21: {"title": "天空彩虹好美麗", "sub": "🌈 雙手由兩側向上畫大彩虹，定格微笑！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"}
        }
    },
    "a1_s04": {
        "srt": "4.O.Animal Safari March.srt",
        "intro": {"title": "[前奏] 森林號角精神踏步", "sub": "🎺 聽號角吹響！雙手插腰，膝蓋抬高大步踏走！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
        "cues": {
            1: {"title": "一二踏步進行曲", "sub": "🥁 喊出一二一二，整齊精神原地踏步！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            2: {"title": "大象重重踏步走", "sub": "🐘 雙手放鼻子前做長長鼻子，重重踏步！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            3: {"title": "粉紅小豬泥巴滾", "sub": "🐷 雙手小拳揉鼻鼻，學小豬拱拱叫！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            4: {"title": "猴子樹梢盪鞦韆", "sub": "🐵 雙手交替向上攀爬樹枝，身體擺盪！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            5: {"title": "叢林高處真自在", "sub": "🌴 展開雙手左右搖晃，像猴子自由快樂！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            6: {"title": "小狗汪汪小貓喵", "sub": "🐶 雙手放在耳邊搖搖，伸出小貓爪抓抓！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            7: {"title": "大家一起學叫聲", "sub": "🐾 拍拍小手，開開心心模仿動物叫！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            8: {"title": "齊步走過綠叢林", "sub": "🌿 挺起胸膛踏步前進，穿過茂密森林！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            9: {"title": "最開心的動物群", "sub": "⭐ 歡樂轉個圈圈，每隻動物都笑嘻嘻！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            10: {"title": "搖搖尾巴拍拍翅", "sub": "🦚 雙手放背後扭動尾巴，雙臂輕拍翅膀！", "pose": "wave", "img": "./images/girl_dance_coach_1790908344383.jpg"},
            11: {"title": "森林合唱團開唱", "sub": "🎶 雙手像花朵盛開，全體高聲齊合唱！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            12: {"title": "小兔草地蹦蹦跳", "sub": "🐰 雙手放頭頂比兔耳，雙腳輕輕彈跳！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            13: {"title": "高高長頸鹿走過", "sub": "🦒 單手高高舉過頭頂，脖子長長漫步！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            14: {"title": "獅子大王威武吼", "sub": "🦁 雙手張開成尖爪胸前用力一吼：Roar！", "pose": "jump", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            15: {"title": "小企鵝搖擺招手", "sub": "🐧 雙臂貼大腿內側，左右小碎步搖擺招手！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            16: {"title": "小鴨嘎嘎叫不停", "sub": "🦆 雙手在嘴前開合做鴨嘴巴：嘎嘎嘎！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            17: {"title": "小青蛙呱呱大跳", "sub": "🐸 蹲下雙手撐地，用力蹦起呱呱叫！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            18: {"title": "池塘濺起小水花", "sub": "💦 雙腳輕輕踩踏，雙手拍水花四濺！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            19: {"title": "動物大軍向前進", "sub": "🥁 踩著堅定有力的節拍，精神大步邁！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            20: {"title": "歡樂巡遊最精彩", "sub": "✨ 雙手高高揮舞，全場動物熱情巡遊！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            21: {"title": "擺尾拍翅再齊舞", "sub": "🐾 左右快速搖擺，拍動翅膀一起跳！", "pose": "wave", "img": "./images/girl_dance_coach_1790908344383.jpg"},
            22: {"title": "森林大合奏吼叫", "sub": "🦁 獅子吼！鴨子叫！小貓喵！全場合奏！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            23: {"title": "軍鼓重響定格秀", "sub": "🌟 雙手叉腰胸前定格，最棒動物探險家！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"}
        }
    },
    "a1_s05": {
        "srt": "5.O.Clean Up Little Helpers.srt",
        "intro": {"title": "[前奏] 時鐘滴答整理預備", "sub": "⏰ 時鐘滴答走，玩具小幫手挽起袖子集合！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
        "cues": {
            1: {"title": "遊戲結束時鐘響", "sub": "⏰ 雙手叉腰身體跟著時鐘左右擺動！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            2: {"title": "收拾積木排排隊", "sub": "🧱 彎下腰撿起積木，輕輕放進收納籃！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            3: {"title": "鉛筆蠟筆回小盒", "sub": "✏️ 雙手捧著筆筒，把彩色蠟筆放進盒子！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            4: {"title": "幫小熊襪子配對", "sub": "🧸 雙手拍拍小腳踝，幫小熊摺好小襪子！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            5: {"title": "看看桌子看看毯", "sub": "👀 彎腰轉頭找一找，桌面地毯都乾淨！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            6: {"title": "給房間一個大擁抱", "sub": "💖 雙臂張開大大環抱，給房間滿滿愛！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            7: {"title": "動作快快收乾淨", "sub": "⚡ 腳步輕快小碎步，快快收拾小房間！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            8: {"title": "人人幫忙好計畫", "sub": "🤝 拍拍雙手豎起大拇指，大家都是小幫手！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            9: {"title": "物歸原位放整齊", "sub": "📦 雙手由低到高把物品整齊歸位！", "pose": "reach", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            10: {"title": "迎接快樂新一天", "sub": "☀️ 雙手高舉托起朝陽，迎接全新明天！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            11: {"title": "圖書立在書架上", "sub": "📚 雙手合十像小書本，整齊排排站好！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            12: {"title": "玩具小車回小籃", "sub": "🚗 雙手握方向盤轉轉，開進玩具籃！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            13: {"title": "一二三樣樣乾淨", "sub": "✨ 數數一二三，房間變得整整齊齊！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            14: {"title": "擊掌好朋友拍個手", "sub": "✋ 伸出雙手向同伴高高擊掌：High-Five！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            15: {"title": "整齊任務大成功", "sub": "🎉 歡快原地小跳步，任務順利通關！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            16: {"title": "收拾乾淨速度快", "sub": "⚡ 雙手左右揮舞，保持乾淨不落後！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            17: {"title": "大家團結力量大", "sub": "🤝 握緊小拳頭胸前一拉，團結第一名！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            18: {"title": "撿起放好不亂丟", "sub": "📦 彎腰再放好，地板乾乾淨淨！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            19: {"title": "天天都是開心天", "sub": "🌟 雙手比出大愛心，每天都開心！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            20: {"title": "超級幫手大明星", "sub": "⭐ 雙手高高舉起，我們是家務大明星！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            21: {"title": "歡呼 Oh Oh 一起跳", "sub": "🎶 跟著音樂大喊 Oh Oh，小腳彈跳！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            22: {"title": "歡呼 Oh Oh 再跳躍", "sub": "🎶 再喊一聲 Oh Oh，拍拍小手！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            23: {"title": "歡呼 Oh Oh 燦爛定格", "sub": "🌟 雙手叉腰豎大拇指，完美定格大笑容！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"}
        }
    },
    "a1_s06": {
        "srt": "6.O.Space Rocket Countdown.srt",
        "intro": {"title": "[前奏] 宇宙電波呼叫訊號", "sub": "📡 嗶嗶嗶！戴上太空頭盔，發射台準備完畢！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
        "cues": {
            1: {"title": "宇宙電波嗶嗶響", "sub": "🛸 小手放耳邊，接收太空站訊號！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            2: {"title": "太空任務準備好", "sub": "👨‍🚀 雙手叉腰立正站好，準備起飛！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            3: {"title": "五四三二一倒數", "sub": "🚀 雙膝微蹲蓄力，跟著大聲倒數：5 4 3 2 1！", "pose": "march", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            4: {"title": "穿好太空服太空靴", "sub": "👢 摸摸雙腿穿上太空靴，拉緊拉鍊！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            5: {"title": "扣緊銀色安全帶", "sub": "💺 雙手交叉胸前扣緊安全帶，穩穩坐好！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            6: {"title": "檢查紅綠儀表板", "sub": "🎛️ 手指在前方點擊紅燈與綠燈按鈕！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            7: {"title": "最酷銀河太空船", "sub": "✨ 雙臂張開像銀色機翼，左右平穩滑動！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            8: {"title": "引擎轟鳴準備點火", "sub": "🔥 雙手握拳身旁蓄力震動，引擎啟動！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            9: {"title": "衝入燦爛星空中", "sub": "⭐ 雙手向上發射，直衝燦爛星空！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            10: {"title": "咻咻咻急速出發", "sub": "🚀 雙手在頭頂合攏成火箭尖，用力高跳！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            11: {"title": "閃耀神秘宇宙光", "sub": "🌌 雙手在身側輕輕波浪搖動，沐浴星光！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            12: {"title": "飛越月球比天高", "sub": "🌙 腳尖點地伸手飛越圓圓大月亮！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            13: {"title": "銀色小火箭穿黑夜", "sub": "🚀 身體前傾平穩飛行，穿越黑夜！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            14: {"title": "看火星緩緩轉動", "sub": "🪐 雙臂在身前畫出旋轉的火星大球！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            15: {"title": "太空安靜無聲息", "sub": "🤫 食指放嘴唇輕輕噓，感受安靜！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            16: {"title": "跟土星光環大招手", "sub": "🪐 伸出雙手向美麗土星光環大招手！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            17: {"title": "無線電滴答唱歌", "sub": "📻 小手放耳邊，跟著無線電節奏拍手！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            18: {"title": "無重力漂浮漫步", "sub": "🎈 雙腳緩慢踩步，像失重一樣輕飄飄！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            19: {"title": "抓一把星塵閃光", "sub": "✨ 雙手在空中抓取閃亮星光放進口袋！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            20: {"title": "咻咻咻再次衝刺", "sub": "🚀 火箭尖尖再次指向宇宙，全力加速！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            21: {"title": "穿越銀河大光芒", "sub": "🌌 雙手由內向外綻放，穿過光芒！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            22: {"title": "飛越高山與月球", "sub": "🌙 單腿微抬雙臂翱翔，比天空更高！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            23: {"title": "最棒火箭在夜空", "sub": "⭐ 雙手向上托起星空，神氣無比！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            24: {"title": "太空任務大成功", "sub": "🎉 雙手叉腰歡呼大喊：任務完成！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            25: {"title": "平穩降落回地球", "sub": "🌍 雙手緩慢下落，平穩降落藍色地球！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            26: {"title": "外星朋友揮手告別", "sub": "👽 雙手放頭頂比外星觸角，定格大笑！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"}
        }
    },
    "a1_s07": {
        "srt": "7.O.The Magic ABC Train.srt",
        "intro": {"title": "[前奏] 蒸汽火車汽笛響起", "sub": "🚂 嗚嗚！拉響火車汽笛，ABC 字母列車準備開動！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
        "cues": {
            1: {"title": "ABC 列車全員上車", "sub": "🎫 揮手招呼大家快上車，踩著節拍小碎步！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            2: {"title": "A 是蘋果 B 是皮球", "sub": "🍎 右手比圓圓大蘋果，左手拍拍小皮球！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            3: {"title": "C 是小貓爬上牆", "sub": "🐱 雙手像貓咪爪爪，交替向上抓抓爬牆！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            4: {"title": "D 是小狗 E 是大象", "sub": "🐘 雙手放耳朵搖搖，雙手做長長大象鼻！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            5: {"title": "F 是小魚游向前", "sub": "🐟 雙手合十左右擺動，像小魚游水！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            6: {"title": "G H I J K L 六字母", "sub": "🔢 伸出手指跟著節拍有節奏地點一點！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            7: {"title": "聽火車汽笛鈴聲", "sub": "🔔 單手拉響汽笛：嗚嗚！聽車鈴叮噹響！", "pose": "reach", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            8: {"title": "字母 M 露出微笑", "sub": "😊 雙手在嘴角畫出最甜的微笑波浪！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            9: {"title": "指引列車迎向光明", "sub": "✨ 雙臂向前上方伸出，指引光明方向！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            10: {"title": "咔嚓咔嚓車輪滾", "sub": "🚂 雙手在腰側做車輪旋轉動作向前滾！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            11: {"title": "字母歌聲唱呀唱", "sub": "🎶 張開雙臂放聲歌唱，身體輕快彈動！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            12: {"title": "鐵軌從 A 開到 Z", "sub": "🛤️ 雙手臂向兩側平展，像長長鐵軌！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            13: {"title": "快快樂樂學字母", "sub": "🎉 歡快原地踏步拍拍手，學習好快樂！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            14: {"title": "N 是鳥巢 O 是貓頭鷹", "sub": "🦉 雙手捧起溫暖鳥巢，雙手圈眼睛當大眼！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            15: {"title": "P 是圓圓黑眼大熊貓", "sub": "🐼 雙手揉揉黑眼圈，學小熊貓吃竹子！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            16: {"title": "Q R S T 快快衝", "sub": "⚡ 雙腳加速踩踏步，列車飛速奔馳！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            17: {"title": "看美麗字母飛過", "sub": "👀 伸手指向窗外，欣賞美麗字母飄過！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            18: {"title": "U V W X Y Z 全學會", "sub": "🌟 雙手高舉揮舞，26 個字母全認識啦！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            19: {"title": "每個字母都有聲音", "sub": "👂 小手貼耳仔細聽，每個發音都動聽！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            20: {"title": "拼出魔法奇妙單字", "sub": "✨ 雙手像施魔法在前方抓一抓灑一灑！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            21: {"title": "咔嚓咔嚓鈴兒響", "sub": "🔔 再次轉動火車小輪子，聽鈴鐺叮叮！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            22: {"title": "字母歌聲唱呀唱", "sub": "🎶 大聲齊聲合唱：Sing! Sing! Sing!", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            23: {"title": "沿著軌道 A 到 Z", "sub": "🛤️ 雙臂大幅度擺動，列車一路暢通！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            24: {"title": "字母列車真好玩", "sub": "⭐ 雙手胸前比心，身體快樂搖晃！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            25: {"title": "閱讀車站到站啦定格", "sub": "🚉 敬禮拉汽笛：叮叮！全劇歡樂定格！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"}
        }
    },
    "a1_s08": {
        "srt": "8.O.Wiggle & Freeze! .srt",
        "intro": {"title": "[前奏] 動感節拍身體預備", "sub": "🎵 聽歡快鼓點！肩膀準備，聽到指令立刻變木頭人！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
        "cues": {
            1: {"title": "節奏鼓點咚咚咚", "sub": "🥁 腳尖踩拍子，雙手輕快拍拍大腿！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            2: {"title": "口哨響起準備扭", "sub": "🎶 雙手插腰，肩膀跟著旋律左右擺動！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            3: {"title": "全身扭動別忘定格", "sub": "💃 全身快樂扭動，耳朵豎起聽指令！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            4: {"title": "搖搖肩膀搖搖膝蓋", "sub": "🦵 左右肩膀抖一抖，膝蓋跟著彈一彈！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            5: {"title": "像秋天落葉隨風飄", "sub": "🍂 雙手像樹葉在微風中輕輕飄落！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            6: {"title": "高高跳起摸摸天地", "sub": "⭐ 向上跳摸天花板，下蹲摸摸小地板！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            7: {"title": "原地小跑步跑起來", "sub": "🏃 原地快速小碎步跑步，越跑越快！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            8: {"title": "仔細聽停下腳步", "sub": "👂 停下腳步站穩，準備倒數！", "pose": "reach", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            9: {"title": "三二一定格成雕像", "sub": "🗿 3 2 1... 定格！像雕像一樣一動不動！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            10: {"title": "安靜定格不許動", "sub": "🤫 憋住笑不許動，維持雕像姿勢！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            11: {"title": "扭扭扭動跳舞囉", "sub": "🎉 解凍啦！扭動全身，滿場飛舞！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            12: {"title": "大腳重重踏地上", "sub": "👣 雙腳大踏步：咚！咚！咚！踏在地上！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            13: {"title": "往左扭扭往右扭扭", "sub": "↔️ 身體向左扭一扭，向右扭一扭！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            14: {"title": "使出全力快樂跳", "sub": "🔥 使出全身力氣，跳出最帥舞蹈！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            15: {"title": "像陀螺旋轉轉圈", "sub": "🔄 雙手平展像小陀螺，旋轉轉個圈！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            16: {"title": "墊起腳尖悄悄走", "sub": "🐾 墊起腳尖輕輕走，一點聲音都沒有！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            17: {"title": "雄鷹展翅翱翔天", "sub": "🦅 雙臂像雄鷹拍打翅膀，飛上天空！", "pose": "wave", "img": "./images/girl_dance_coach_1790908344383.jpg"},
            18: {"title": "雙手舉高高大招手", "sub": "👋 雙手舉過頭頂，熱情大幅度招手！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            19: {"title": "準備好擺好姿勢", "sub": "🎯 保持好平衡姿勢，馬上要定格啦！", "pose": "reach", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            20: {"title": "三二一定格摸鼻子", "sub": "👃 3 2 1... 定格！食指摸著小鼻子！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            21: {"title": "安靜定格摸鼻子", "sub": "🤫 保持摸鼻子的造型，一動也不動！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            22: {"title": "解凍繼續扭扭跳", "sub": "🎉 解凍！滿場歡跳，跟著節奏搖擺！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            23: {"title": "大腳踏地震天響", "sub": "👣 跟著大鼓重重踩踩腳，地面咚咚響！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            24: {"title": "向左向右齊搖擺", "sub": "↔️ 雙手左右擺動，身體快樂起伏！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            25: {"title": "盡情釋放活力跳", "sub": "⚡ 雙臂高舉甩動，活力拉滿！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            26: {"title": "你完全沒動！你贏了", "sub": "🏆 太厲害啦！你一動都沒動，大獲全勝！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            27: {"title": "坐下深呼吸大定格", "sub": "🧘 雙手慢慢撫胸，做個深呼吸，微笑定格！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"}
        }
    },
    "a1_s09": {
        "srt": "9.O.Yummy Healthy Snack.srt",
        "intro": {"title": "[前奏] 肚子咕嚕嚕美食預備", "sub": "🥣 肚子咕嚕嚕！戴上小廚師帽，健康點心開動囉！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
        "cues": {
            1: {"title": "脆脆橘色甜胡蘿蔔", "sub": "🥕 雙手拿著胡蘿蔔，喀嚓喀嚓大口咬！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            2: {"title": "綠色花椰菜好好吃", "sub": "🥦 雙手像綠色小樹，嚼一嚼真美味！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            3: {"title": "肥皂清水把手洗淨", "sub": "🧼 雙手手心搓搓手背搓搓，洗乾淨！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            4: {"title": "最棒的小廚師登場", "sub": "👨‍🍳 摸摸高高廚師帽，豎起大拇指！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            5: {"title": "咬一小口慢慢嚼", "sub": "🍎 一口一口慢慢咬，細嚼慢嚥最健康！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            6: {"title": "健康食物幫忙長高", "sub": "🌱 雙腳踩直向上拔高，天天長高長壯！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            7: {"title": "阿姆阿姆大口嚼", "sub": "😋 雙手摸肚肚，嘴巴嚼呀嚼真香！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            8: {"title": "營養食物身體棒", "sub": "💪 雙臂展示小肌肉，身體強壯壯！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            9: {"title": "盤子盛滿蔬果盤", "sub": "🥗 雙手在胸前端起五彩繽紛蔬果盤！", "pose": "reach", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            10: {"title": "吃下彩虹身體好棒", "sub": "🌈 雙臂在空中畫出大彩虹，精神好！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            11: {"title": "紅紅蘋果香蕉笑臉", "sub": "🍌 雙手托起紅蘋果，嘴角揚起香蕉大笑！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            12: {"title": "喝杯牛奶歇一歇", "sub": "🥛 雙手捧杯咕嚕咕嚕喝牛奶，休息一下！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            13: {"title": "碗裡草莓閃亮亮", "sub": "🍓 伸手進碗裡抓一把小草莓放嘴裡！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            14: {"title": "健康點心營養滿分", "sub": "⭐ 拍拍雙手，全身元氣滿滿！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            15: {"title": "揉揉肚肚說好好吃", "sub": "😋 雙手揉揉圓滾滾肚肚，說聲好好吃！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            16: {"title": "滿滿活力玩遊戲", "sub": "🏃 雙腳原地快速跑動，隨時去玩耍！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            17: {"title": "阿姆阿姆大口嚼", "sub": "🍽️ 跟著節奏大口大口吃點心！", "pose": "march", "img": "./images/boy_dance_coach_1790908303698.jpg"},
            18: {"title": "健康食物最美味", "sub": "💪 雙臂再次展現健康活力！", "pose": "jump", "img": "./images/girl_jump_dance_1790912250093.jpg"},
            19: {"title": "蔬果吃光盤子空", "sub": "🥗 把蔬菜水果吃光光，營養好寶寶！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            20: {"title": "彩色營養能量足", "sub": "✨ 雙手向上綻放金色光芒！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            21: {"title": "全吃完啦太美味", "sub": "👏 拍拍小手舔舔嘴唇，美味滿分！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            22: {"title": "謝謝美味健康點心", "sub": "🙏 雙手合十胸前鞠躬，定格感恩大微笑！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"}
        }
    },
    "a1_s10": {
        "srt": "10.O.Soft Pillow Goodnight.srt",
        "intro": {"title": "[前奏] 夜幕低垂搖籃曲", "sub": "🌙 月亮升起，微風吹拂，輕輕左右搖擺放鬆身體！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
        "cues": {
            1: {"title": "閉上雙眼日光落", "sub": "🌅 雙手在眼前輕輕抹過，溫柔閉上雙眼！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            2: {"title": "太陽身後靜靜歇", "sub": "☀️ 雙手慢慢下落，像夕陽落到山後！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            3: {"title": "紫夜繁星眨眼睛", "sub": "⭐ 雙手抬至夜空，小手指如星星眨眼！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            4: {"title": "輕柔飄盪催眠曲", "sub": "🎶 雙手像水波在胸前輕柔滑動！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            5: {"title": "小熊緊抱在胸前", "sub": "🧸 雙臂胸前緊緊抱住心愛的小熊玩偶！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            6: {"title": "疲憊雙眼歇一歇", "sub": "😴 雙手合十貼在右臉頰，輕輕閉目！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            7: {"title": "安睡吧小腦袋", "sub": "🛏️ 頭部輕靠在左側枕頭，身體放鬆！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            8: {"title": "柔軟被窩好溫暖", "sub": "🛌 雙手向上拉起被角，縮進溫暖被窩！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            9: {"title": "雲朵之上輕漂浮", "sub": "☁️ 雙臂平展，身體像在雲朵上漂浮！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            10: {"title": "小天使晚安好夢", "sub": "👼 雙手在胸口化作小翅膀輕拍，晚安！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            11: {"title": "月光透過窗櫺照", "sub": "🌕 抬頭望向窗外銀色月光，手撫窗櫺！", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            12: {"title": "銀色雨滴小巷跳", "sub": "💧 手指輕柔如細雨從空中緩緩落下！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            13: {"title": "快樂思緒飄入夢", "sub": "💭 雙手由胸前向外輕撫，放飛好夢！", "pose": "reach", "img": "./images/boy_sun_prep_1790915666059.jpg"},
            14: {"title": "數數跳跳毛毛羊", "sub": "🐑 食指輕輕點數：一隻羊、兩隻羊...", "pose": "reach", "img": "./images/boy_reach_pose_1790914159202.jpg"},
            15: {"title": "明天晴天再來玩", "sub": "☀️ 嘴角泛起微笑，期待明天的晴朗！", "pose": "sun_rise", "img": "./images/boy_sun_stretch_1790914097504.jpg"},
            16: {"title": "夢幻泡泡飛向遠", "sub": "🎈 雙手輕輕吹出夢想泡泡，隨風飛走！", "pose": "wave", "img": "./images/boy_wave_dance_1790912234179.jpg"},
            17: {"title": "安睡吧小腦袋", "sub": "😴 雙手再次合十貼在臉頰，輕輕搖曳！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            18: {"title": "柔軟被窩好安全", "sub": "🛌 雙手收於胸前，感受平靜與安穩！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"},
            19: {"title": "雲朵之上軟綿綿", "sub": "☁️ 身體緩緩微晃，像睡在羽毛雲朵上！", "pose": "sway", "img": "./images/boy_sway_pose_1790914141304.jpg"},
            20: {"title": "甜美夢鄉祝晚安", "sub": "🌟 雙手合十胸前，輕輕定格，祝大家晚安！", "pose": "heart", "img": "./images/boy_heart_pose_1790914112947.jpg"}
        }
    }
}

# Now, generate the full precise timeline for each song
with open('web_app/album_data.js', 'r', encoding='utf-8') as f:
    orig_text = f.read()

json_text = orig_text.replace('window.KAI_ALBUM_DATABASE = ', '').rstrip().rstrip(';')
database = json.loads(json_text)

album1 = database['album_1']

for song in album1['songs']:
    sid = song['id']
    if sid not in song_configs:
        continue
    cfg = song_configs[sid]
    srt_path = os.path.join('Music_Album/Album 1_Little Steps Big World_Sing & Play Adventures', cfg['srt'])
    cues = parse_srt(srt_path)
    
    new_timeline = []
    
    # 1. Intro check
    first_cue_start = cues[0]['start']
    if first_cue_start > 0.5:
        intro_cfg = cfg['intro']
        new_timeline.append({
            "start": 0,
            "end": first_cue_start,
            "title": intro_cfg['title'],
            "video": intro_cfg.get('vid', None),
            "image": intro_cfg.get('img', song['coachImage']),
            "voice": "./voices/voice_01.mp3" if sid == "a1_s01" else None,
            "lyric": "[Intro 🎵 歡樂前奏]",
            "sub": intro_cfg['sub'],
            "promptText": intro_cfg['sub'],
            "next": cues[0]['text'][:20] + " ➜",
            "targetPose": intro_cfg['pose']
        })
    
    # 2. Iterate through cues
    for idx, c in enumerate(cues):
        cue_num = c['index']
        cue_cfg = cfg['cues'].get(cue_num, cfg['cues'].get(idx + 1, {}))
        
        # Next text
        if idx < len(cues) - 1:
            next_text = cfg['cues'].get(cues[idx+1]['index'], {}).get('title', cues[idx+1]['text']) + " ➜"
        else:
            next_text = "🎉 完美通關！獲得 3 顆大金星！"
            
        title = f"第 {cue_num:02d} 節: {cue_cfg.get('title', c['text'])}"
        sub = cue_cfg.get('sub', f"跟著節奏跳舞：{c['text']}")
        pose = cue_cfg.get('pose', 'march')
        img = cue_cfg.get('img', song['coachImage'])
        vid = cue_cfg.get('vid', None)
        voice = f"./voices/voice_{cue_num:02d}.mp3" if (sid == "a1_s01" and cue_num <= 18) else None
        
        # Calculate timeline segment start and end
        # segment start is cue['start']
        seg_start = c['start']
        # seg_end extends until next cue start or cue end if gap is small
        if idx < len(cues) - 1:
            next_cue_start = cues[idx+1]['start']
            gap = next_cue_start - c['end']
            if gap > 6.0:
                # noticeable interlude
                seg_end = c['end']
            else:
                seg_end = next_cue_start
        else:
            seg_end = max(c['end'], song['duration'])

        new_timeline.append({
            "start": seg_start,
            "end": seg_end,
            "title": title,
            "video": vid,
            "image": img,
            "voice": voice,
            "lyric": f"\"{c['text']}\"",
            "sub": sub,
            "promptText": sub,
            "next": next_text,
            "targetPose": pose
        })
        
        # If there's a big gap > 6.0s after this cue, add an interlude segment
        if idx < len(cues) - 1 and (cues[idx+1]['start'] - c['end']) > 6.0:
            interlude_start = c['end']
            interlude_end = cues[idx+1]['start']
            new_timeline.append({
                "start": interlude_start,
                "end": interlude_end,
                "title": f"[旋律間奏] 動作接續歡樂跳",
                "video": None,
                "image": song['coachImage'],
                "voice": None,
                "lyric": "[Interlude 🎵 輕快旋律間奏]",
                "sub": "🔄 雙手插腰踩小碎步，轉個歡樂大圓圈，保持微笑！",
                "promptText": "轉個小圓圈，等待下一句歌詞！",
                "next": cfg['cues'].get(cues[idx+1]['index'], {}).get('title', cues[idx+1]['text']) + " ➜",
                "targetPose": "sway"
            })
            
    # sort timeline by start time
    new_timeline.sort(key=lambda x: x['start'])
    song['timeline'] = new_timeline
    print(f"Song {sid} ({song['title']}) updated with {len(new_timeline)} segments.")

output_js = "window.KAI_ALBUM_DATABASE = " + json.dumps(database, ensure_ascii=False, indent=2) + ";\n"

with open('web_app/album_data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

with open('docs/album_data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print("Saved updated database to web_app/album_data.js and docs/album_data.js successfully!")
