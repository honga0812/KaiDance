import asyncio, os
import edge_tts

async def main():
    voice = "zh-TW-HsiaoChenNeural"
    text = "小朋友好棒！雙手插腰，準備好跟著音樂一起數數囉！"
    communicate = edge_tts.Communicate(text, voice, rate="+5%", pitch="+5Hz")
    os.makedirs("test_audio", exist_ok=True)
    await communicate.save("test_audio/test_voice.mp3")
    print("TTS test generated, file size:", os.path.getsize("test_audio/test_voice.mp3"))

asyncio.run(main())
