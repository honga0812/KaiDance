# -*- coding: utf-8 -*-
import json, os, subprocess

with open('web_app/album_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

db = json.loads(text.replace('window.KAI_ALBUM_DATABASE = ', '').rstrip().rstrip(';'))
album1_songs = db['album_1']['songs']

def get_audio_duration(file_path):
    if not os.path.exists(file_path):
        return 0.0
    try:
        cmd = [
            "ffprobe", "-v", "error", "-show_entries",
            "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
            file_path
        ]
        out = subprocess.check_output(cmd).decode().strip()
        return float(out)
    except Exception as e:
        return 0.0

total_segs = 0
overlap_count = 0
songs_stats = {}

for s in album1_songs:
    s_num = s['trackNumber']
    s_title = s['title']
    tl = s['timeline']
    songs_stats[s_num] = {"title": s_title, "total": len(tl), "overlaps": []}
    
    for i in range(len(tl)):
        seg = tl[i]
        voice_file = seg.get('voice')
        if not voice_file:
            continue
        actual_path = os.path.join("docs", voice_file.replace("./", ""))
        audio_dur = get_audio_duration(actual_path)
        seg_dur = seg['end'] - seg['start']
        
        # Check against segment duration AND next segment start
        # If there is a next segment with voice, overlap happens if audio_dur > (next_seg_start - seg_start)
        allowed_dur = seg_dur
        if i < len(tl) - 1:
            allowed_dur = tl[i+1]['start'] - seg['start']
            
        total_segs += 1
        if audio_dur > allowed_dur - 0.2: # buffer of 0.2s
            overlap_count += 1
            excess = audio_dur - allowed_dur
            songs_stats[s_num]["overlaps"].append({
                "seg": i + 1,
                "title": seg['title'],
                "seg_dur": round(seg_dur, 2),
                "allowed": round(allowed_dur, 2),
                "audio_dur": round(audio_dur, 2),
                "excess": round(excess, 2),
                "script": seg.get('voiceScript', '')
            })

print(f"Total voice files: {total_segs}, Overlapping files: {overlap_count}")
for s_num, st in songs_stats.items():
    print(f"\n--- Track #{s_num:02d}: {st['title']} ---")
    print(f"Overlaps: {len(st['overlaps'])} / {st['total']}")
    for ov in st['overlaps'][:4]:
        print(f"  Seg #{ov['seg']:02d} [{ov['title']}]: allowed={ov['allowed']}s, voice={ov['audio_dur']}s (EXCESS +{ov['excess']}s)")
        print(f"     Script ({len(ov['script'])} chars): {ov['script']}")
