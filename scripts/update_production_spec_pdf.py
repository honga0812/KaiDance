import os
import json
import shutil
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_NAME = 'ArialUnicode'
FONT_PATH = '/Library/Fonts/Arial Unicode.ttf'
if not os.path.exists(FONT_PATH):
    FONT_PATH = '/System/Library/Fonts/PingFang.ttc'
pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

# Load album database
with open('web_app/album_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

db = json.loads(text.replace('window.KAI_ALBUM_DATABASE = ', '').rstrip().rstrip(';'))
songs = db['album_1']['songs']

doc = SimpleDocTemplate(
    "docs/Album1_Dance_Production_Spec.pdf",
    pagesize=landscape(A4),
    leftMargin=20,
    rightMargin=20,
    topMargin=20,
    bottomMargin=20
)

styles = getSampleStyleSheet()

style_title = ParagraphStyle(
    'DocTitle', parent=styles['Normal'], fontName=FONT_NAME, fontSize=17, leading=22, textColor=colors.HexColor('#1E293B'), alignment=1, spaceAfter=4
)
style_subtitle = ParagraphStyle(
    'DocSubtitle', parent=styles['Normal'], fontName=FONT_NAME, fontSize=10, leading=14, textColor=colors.HexColor('#64748B'), alignment=1, spaceAfter=10
)
style_h2 = ParagraphStyle(
    'SongH2', parent=styles['Normal'], fontName=FONT_NAME, fontSize=11, leading=15, textColor=colors.HexColor('#0F172A'), spaceBefore=6, spaceAfter=5, keepWithNext=True
)
style_th = ParagraphStyle(
    'TableHead', parent=styles['Normal'], fontName=FONT_NAME, fontSize=8, leading=10, textColor=colors.white, alignment=1
)
style_td = ParagraphStyle(
    'TableCell', parent=styles['Normal'], fontName=FONT_NAME, fontSize=7, leading=9.5, textColor=colors.HexColor('#1E293B')
)
style_td_center = ParagraphStyle(
    'TableCellCenter', parent=styles['Normal'], fontName=FONT_NAME, fontSize=7, leading=9.5, textColor=colors.HexColor('#1E293B'), alignment=1
)
style_td_code = ParagraphStyle(
    'TableCellCode', parent=styles['Normal'], fontName=FONT_NAME, fontSize=5.5, leading=7.5, textColor=colors.HexColor('#334155')
)
style_td_video = ParagraphStyle(
    'TableCellVideo', parent=styles['Normal'], fontName=FONT_NAME, fontSize=6.5, leading=8.5, textColor=colors.HexColor('#0369A1')
)
style_td_video_missing = ParagraphStyle(
    'TableCellMissing', parent=styles['Normal'], fontName=FONT_NAME, fontSize=6.5, leading=8.5, textColor=colors.HexColor('#DC2626')
)

story = []
story.append(Paragraph("KaiDance 第一輯《小小腳步 大大世界》名師口令優化與動畫規格企劃書", style_title))
story.append(Paragraph("親切精簡短句 · 語音防打到 · 3D 動畫 Prompt · AI 示範影片/靜態寫真整合規格", style_subtitle))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#F59E0B'), spaceBefore=0, spaceAfter=8))

for s_num in range(1, 11):
    s_info = next(s for s in songs if s['trackNumber'] == s_num)
    timeline = s_info['timeline']
    
    video_summary = ""
    if s_num == 1:
        video_summary = " · 🎬 影片: 23/23 支全就緒 (T1 目錄)"
    elif s_num == 2:
        video_summary = " · 🎬 影片: 20 支就緒，2 支缺漏暫以寫真代替 (T2 目錄)"
    else:
        video_summary = " · 📸 導引模式: 9:16 高畫質角色寫真"

    story.append(Paragraph(f"<b>Track #{s_num:02d}: {s_info['title']} ({s_info['zhTitle']})</b> · 標籤: {s_info['tag']} · 長度: {s_info['duration']}秒 · 口令: {len(timeline)}段{video_summary}", style_h2))
    
    table_data = [[
        Paragraph("段落", style_th),
        Paragraph("時間/時長", style_th),
        Paragraph("動作主題", style_th),
        Paragraph("對應歌詞", style_th),
        Paragraph("動作要領", style_th),
        Paragraph("精簡名師口令", style_th),
        Paragraph("AI 動畫/影片狀態", style_th),
        Paragraph("AI 生成提示詞 (Prompt)", style_th)
    ]]
    
    for idx, item in enumerate(timeline, start=1):
        s_m = int(item['start'] // 60)
        s_s = int(item['start'] % 60)
        e_m = int(item['end'] // 60)
        e_s = int(item['end'] % 60)
        window = round(item['end'] - item['start'], 2)
        time_info = f"{s_m:02d}:{s_s:02d}~{e_m:02d}:{e_s:02d}<br/>區間:{window}s|音訊:{item.get('audioDuration', window)}s"
        
        # Video status formatting
        v_url = item.get('video')
        if v_url:
            v_style = style_td_video
            v_text = f"<b>🎬 已接入</b><br/>{v_url.replace('./', '')}"
        else:
            if s_num == 2 and idx in [7, 17]:
                v_style = style_td_video_missing
                v_text = "<b>❌ 缺少影片</b><br/>(📸 靜態寫真代替)"
            else:
                v_style = style_td
                v_text = "📸 靜態引導寫真"

        row = [
            Paragraph(f"#{idx:02d}", style_td_center),
            Paragraph(time_info, style_td_center),
            Paragraph(f"<b>{item['title']}</b>", style_td),
            Paragraph(item.get('lyric', ''), style_td),
            Paragraph(item.get('sub', item.get('promptText', '')), style_td),
            Paragraph(f"<b>{item.get('voiceScript', '')}</b>", style_td),
            Paragraph(v_text, v_style),
            Paragraph(item.get('videoPrompt', ''), style_td_code)
        ]
        table_data.append(row)
        
    # Total width = 801 (A4 landscape usable width)
    # 24 + 56 + 82 + 88 + 120 + 130 + 110 + 190 = 800
    col_widths = [24, 56, 82, 88, 120, 130, 110, 190]
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0284C7')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 2.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2.5)
    ]))
    
    story.append(t)
    story.append(Spacer(1, 8))
    if s_num < 10:
        story.append(PageBreak())

doc.build(story)
shutil.copy("docs/Album1_Dance_Production_Spec.pdf", "web_app/Album1_Dance_Production_Spec.pdf")
print("Successfully generated updated docs and web_app Album1_Dance_Production_Spec.pdf!")
