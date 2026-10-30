import asyncio
import os
import subprocess
import edge_tts

os.makedirs("web_app/audio/kids", exist_ok=True)
os.makedirs("docs/audio/kids", exist_ok=True)

KIDS_VOICES = [
    {
        "id": "kid1_leo",
        "name": "Kai",
        "voice": "zh-CN-YunxiaNeural",
        "rate": "+14%",
        "pitch": "+14Hz",
        "text": "Let's go! 我是 Kai，讓我們一起來跳舞吧！",
        "ffmpeg_af": "highpass=f=90,treble=g=2,volume=1.45"
    },
    {
        "id": "kid2_mia",
        "name": "Jessie",
        "voice": "zh-CN-XiaoyiNeural",
        "rate": "+16%",
        "pitch": "+24Hz",
        "text": "耶！我是 Jessie，準備好了嗎？跟我一起閃亮搖擺吧！",
        "ffmpeg_af": "highpass=f=90,treble=g=2,volume=1.45"
    },
    {
        "id": "kid3_max",
        "name": "Tim",
        "voice": "zh-CN-YunxiaNeural",
        "rate": "+18%",
        "pitch": "+4Hz",
        "text": "Yo! Let's party! 我是 Tim，跟上節拍一起跳起來！",
        "ffmpeg_af": "highpass=f=90,treble=g=2,volume=1.45"
    },
    {
        "id": "kid4_hana",
        "name": "Mina",
        "voice": "zh-CN-XiaoyiNeural",
        "rate": "+12%",
        "pitch": "+18Hz",
        "text": "Hi! Let's dance! 我是 Mina，快樂音樂開始囉，一起開心跳舞吧！",
        "ffmpeg_af": "highpass=f=90,treble=g=2,volume=1.45"
    },
    {
        "id": "kid5_zoe",
        "name": "MiMi",
        "voice": "zh-CN-XiaoyiNeural",
        "rate": "+15%",
        "pitch": "+12Hz",
        "text": "One, two, three, jump! 我是 MiMi，派對時間到，大家一起嗨起來！",
        "ffmpeg_af": "highpass=f=90,treble=g=2,volume=1.45"
    }
]

async def generate_all():
    for k in KIDS_VOICES:
        raw_path = f"/tmp/{k['id']}_raw.mp3"
        out_web = f"web_app/audio/kids/{k['id']}.mp3"
        out_docs = f"docs/audio/kids/{k['id']}.mp3"
        comm = edge_tts.Communicate(k["text"], k["voice"], rate=k["rate"], pitch=k["pitch"])
        await comm.save(raw_path)
        cmd = [
            "ffmpeg", "-y", "-i", raw_path,
            "-af", k["ffmpeg_af"],
            "-ar", "44100", "-b:a", "128k",
            out_web
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["cp", out_web, out_docs], check=True)
        print(f"Generated {out_web} ({os.path.getsize(out_web)} bytes) -> {k['text']}")

asyncio.run(generate_all())
