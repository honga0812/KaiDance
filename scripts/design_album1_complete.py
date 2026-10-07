# -*- coding: utf-8 -*-
"""
Complete pedagogical dance animation, video prompts, and teacher voice script
for Album 1 (Songs 02 to 10).
Outputs:
1. Excel Workbook (docs/Album1_Dance_Production_Spec.xlsx & web_app/Album1_Dance_Production_Spec.xlsx)
2. Professional PDF Document (docs/Album1_Dance_Production_Spec.pdf & web_app/Album1_Dance_Production_Spec.pdf)
3. TTS Generation script & audio assets for all songs.
"""

import os, json, re

# Load current album data
with open('web_app/album_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

data = json.loads(text.replace('window.KAI_ALBUM_DATABASE = ', '').rstrip().rstrip(';'))
album1_songs = data['album_1']['songs']
print("Loaded songs:", [s['title'] for s in album1_songs])
