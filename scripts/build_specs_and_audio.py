# -*- coding: utf-8 -*-
"""
Full Production Pipeline for KaiDance Album 1 (Songs 2 to 10):
1. Detailed Pedagogy Design & Video Generation Prompts (AI Animation Prompts) for each segment of songs 02-10
2. Professional Teacher Voice Acting Prompts (亲切自然的引导式中文口令)
3. Excel Spreadsheet (.xlsx) with clean multi-sheet formatting & master overview
4. High-quality PDF Document (.pdf) using ReportLab with Chinese Font
5. Audio Generation for all teacher voice prompts using edge-tts (zh-TW-HsiaoChenNeural)
6. Updating album_data.js and synchronizing to docs/ and web_app/
"""

import os, sys, json, asyncio
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import edge_tts

# Register Chinese Font
FONT_NAME = "STHeiti"
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
if os.path.exists(FONT_PATH):
    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))
    print(f"Registered {FONT_NAME} successfully from {FONT_PATH}")
else:
    FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))
    print(f"Registered {FONT_NAME} from fallback Arial Unicode")

# Load existing database
with open('web_app/album_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

db = json.loads(text.replace('window.KAI_ALBUM_DATABASE = ', '').rstrip().rstrip(';'))
album1_songs = db['album_1']['songs']

print("Ready to process songs 2 to 10...")
