import asyncio
import os
import subprocess
import edge_tts

VOICE = "zh-TW-HsiaoChenNeural"
RATE = "+24%"
PITCH = "+8Hz"

CUES = [
    (1, "小手插腰，踩著拍子踏步走！"),
    (2, "雙手托起大太陽，高高舉起左右大招手！"),
    (3, "拿好小牙刷刷刷刷，露出笑臉大步走！"),
    (4, "雙臂展翅學小鳥，小手貼耳聽晨曲！"),
    (5, "熱情揮手說哈囉，用力高跳喊萬歲！"),
    (6, "彎腰摸摸小鞋子，伸指數一二三！"),
    (7, "張開雙手，邀請好朋友一起唱！"),
    (8, "手叉小蠻腰，輕輕轉個歡樂圓圈！"),
    (9, "背上小書包戴正小帽子，跟貪睡小貓說拜拜！"),
    (10, "伸手向上抓取白雲放口袋，抬頭看藍天！"),
    (11, "雙臂畫大圓，胸前比出跳動大愛心！"),
    (12, "雙腳小跳步，雙手交替大招手！"),
    (13, "深蹲彈跳起飛！雙手握拳喊耶！"),
    (14, "小手插腰，左右小腳尖輕輕點地！"),
    (15, "跟著大重音，整整齊齊拍拍手！"),
    (16, "展開白鴿翅膀，像微風在天空滑翔！"),
    (17, "雙臂畫出大金色圓圈，擁抱全世界！"),
    (18, "雙手合十胸前鞠躬，定格燦爛大微笑！"),
]

async def synthesize():
    os.makedirs("web_app/voices", exist_ok=True)
    os.makedirs("docs/voices", exist_ok=True)

    # Clean old voice files from 19 to 23
    for old_i in range(19, 30):
        for folder in ["web_app/voices", "docs/voices"]:
            p = f"{folder}/voice_{old_i:02d}.mp3"
            if os.path.exists(p):
                os.remove(p)

    for idx, text in CUES:
        raw_mp3 = f"web_app/voices/raw_{idx:02d}.mp3"
        final_mp3 = f"web_app/voices/voice_{idx:02d}.mp3"
        docs_mp3 = f"docs/voices/voice_{idx:02d}.mp3"

        print(f"Synthesizing [{idx:02d}/18]: {text}")
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await communicate.save(raw_mp3)

        # Broadcast audio filter with ffmpeg
        cmd = [
            "ffmpeg", "-y", "-i", raw_mp3,
            "-af", "volume=1.25, highpass=f=80, treble=g=1.5",
            "-b:a", "128k", final_mp3
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        if os.path.exists(raw_mp3):
            os.remove(raw_mp3)

        # Copy to docs/voices
        subprocess.run(["cp", final_mp3, docs_mp3], check=True)

        # Probe duration
        probe = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", final_mp3],
            capture_output=True, text=True
        )
        duration = float(probe.stdout.strip()) if probe.stdout.strip() else 0
        print(f"  -> Generated {final_mp3}: {duration:.2f}s")

if __name__ == "__main__":
    asyncio.run(synthesize())
