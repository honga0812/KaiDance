# -*- coding: utf-8 -*-
"""
Generate 1:1 precise SRT cue-level timelines for all 10 songs in Album 1.
Every single cue in each song gets its own discrete segment with exact start/end,
concise natural bilingual translation & teacher cue, pose, and coach media.
"""
import glob, os, re, json

srt_files = {
    "a1_s01": "1.O.Morning Sunshine Hello.srt",
    "a1_s02": "2.O.Count with Me 1 to 10.srt",
    "a1_s03": "3.O.Rainbow Color Splash.srt",
    "a1_s04": "4.O.Animal Safari March.srt",
    "a1_s05": "5.O.Clean Up Little Helpers.srt",
    "a1_s06": "6.O.Space Rocket Countdown.srt",
    "a1_s07": "7.O.The Magic ABC Train.srt",
    "a1_s08": "8.O.Wiggle & Freeze! .srt",
    "a1_s09": "9.O.Yummy Healthy Snack.srt",
    "a1_s10": "10.O.Soft Pillow Goodnight.srt"
}

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

print("Loaded generator module...")
