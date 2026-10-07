# -*- coding: utf-8 -*-
import glob, os, re

srt_files = sorted(glob.glob('Music_Album/Album 1_Little Steps Big World_Sing & Play Adventures/*.srt'))

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

for sf in srt_files:
    cues = parse_srt(sf)
    print(f"File: {os.path.basename(sf)}, total cues: {len(cues)}, starts at {cues[0]['start']}s, ends at {cues[-1]['end']}s")

