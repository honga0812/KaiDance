# -*- coding: utf-8 -*-
"""
Build ultra-precise single-sentence segment timelines for all 10 songs in Album 1.
1. Every cue from uploaded SRT is mapped to its exact time start/end.
2. If song has an intro (start > 0), a dedicated 0s -> first_cue start intro segment is prepended.
3. If there is a noticeable musical interlude gap between cues (> 4.0s), an interlude segment is inserted.
4. Each segment has concise, elegant single-sentence lyrics and short kid-friendly action guidance.
"""

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

# Load existing album data to preserve Album 2 and album metadata
with open('web_app/album_data.js', 'r', encoding='utf-8') as f:
    orig_text = f.read()

json_text = orig_text.replace('window.KAI_ALBUM_DATABASE = ', '').rstrip().rstrip(';')
database = json.loads(json_text)

print("Original database keys:", list(database.keys()))
