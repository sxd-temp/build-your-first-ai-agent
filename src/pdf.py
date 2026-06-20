"""Markdown -> styled PDF conversion using fpdf2 (pure Python, no system deps).

fpdf2's built-in Helvetica is latin-1 only, so we transliterate emojis into
text equivalents before rendering. The web UI keeps the original emojis.

✅ PROVIDED — you don't need to edit this file. It powers the "Download PDF" button.
"""
from __future__ import annotations

import re

from fpdf import FPDF


# ---------- styling ----------
PRIMARY = (124, 92, 255)        # purple accent
TEXT = (34, 34, 34)
MUTED = (130, 130, 140)
H1_SIZE = 20
H2_SIZE = 14
H3_SIZE = 12
BODY_SIZE = 10.5


# ---------- emoji / unicode sanitization ----------
EMOJI_MAP = {
    "🎯": "[TARGET]",
    "🚀": "[BULL]",
    "🔪": "[BEAR]",
    "🟢": "[GO]",
    "🟡": "[PIVOT]",
    "🔴": "[STOP]",
    "✅": "[OK]",
    "❌": "[X]",
    "⚙️": "",
    "📋": "",
    "📄": "",
    "🧠": "",
    "🕘": "",
    "⬇️": "",
    "🔑": "",
    "💡": "",
    "👋": "",
}

# Smart-quote / dash normalizations
UNICODE_MAP = {
    "‘": "'", "’": "'",
    "“": '"', "”": '"',
    "–": "-", "—": "--",
    "…": "...",
    " ": " ",
    "•": "-",
    "→": "->",
    "←": "<-",
}


def _to_latin1_safe(text: str) -> str:
    for k, v in EMOJI_MAP.items():
        text = text.replace(k, v)
    for k, v in UNICODE_MAP.items():
        text = text.replace(k, v)
    # Strip any other characters latin-1 cannot encode
    return text.encode("latin-1", errors="replace").decode("latin-1")


# ---------- pdf class ----------
class MemoPDF(FPDF):
    def __init__(self):
        super().__init__(format="A4", unit="mm")
        self.set_margins(18, 18, 18)
        self.set_auto_page_break(auto=True, margin=18)
        self.add_page()
        self.set_text_color(*TEXT)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 6, f"Page {self.page_no()}", align="C")
        self.set_text_color(*TEXT)


# ---------- markdown rendering ----------
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")


def _clean_inline(text: str) -> str:
    text = _INLINE_CODE_RE.sub(r"\1", text)
    return _to_latin1_safe(text)


def _write_paragraph(pdf: MemoPDF, text: str, size: float = BODY_SIZE):
    pdf.set_font("Helvetica", "", size)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(0, 5.5, _clean_inline(text), markdown=True)
    pdf.ln(1.5)


def _write_heading(pdf: MemoPDF, text: str, level: int):
    text = _clean_inline(text).strip()
    if level == 1:
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", H1_SIZE)
        pdf.set_text_color(*PRIMARY)
        pdf.multi_cell(0, 9, text)
        y = pdf.get_y()
        pdf.set_draw_color(*PRIMARY)
        pdf.set_line_width(0.6)
        pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
        pdf.ln(4)
    elif level == 2:
        pdf.ln(3)
        pdf.set_font("Helvetica", "B", H2_SIZE)
        pdf.set_text_color(60, 60, 110)
        pdf.multi_cell(0, 7, text)
        pdf.ln(1)
    else:
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", H3_SIZE)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(0, 6, text)
        pdf.ln(0.5)
    pdf.set_text_color(*TEXT)


def _write_list_item(pdf: MemoPDF, text: str, ordered_index: int | None = None):
    pdf.set_font("Helvetica", "", BODY_SIZE)
    pdf.set_text_color(*TEXT)
    bullet = f"{ordered_index}. " if ordered_index is not None else "-  "
    pdf.set_x(pdf.l_margin + 4)
    pdf.cell(8, 5.5, bullet)
    remaining_w = pdf.w - pdf.r_margin - pdf.get_x()
    pdf.multi_cell(remaining_w, 5.5, _clean_inline(text), markdown=True)
    pdf.ln(0.5)


def _render_markdown(pdf: MemoPDF, md_text: str):
    lines = md_text.replace("\r\n", "\n").split("\n")
    i = 0
    ordered_counter = 0
    in_ordered_list = False

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            in_ordered_list = False
            ordered_counter = 0
            pdf.ln(2)
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            _write_heading(pdf, m.group(2), level=min(level, 3))
            in_ordered_list = False
            i += 1
            continue

        if re.match(r"^(\*\s*){3,}$|^(-\s*){3,}$|^(_\s*){3,}$", stripped):
            pdf.ln(1)
            y = pdf.get_y()
            pdf.set_draw_color(200, 200, 210)
            pdf.set_line_width(0.2)
            pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
            pdf.ln(3)
            i += 1
            continue

        m = re.match(r"^[-*+]\s+(.*)$", stripped)
        if m:
            _write_list_item(pdf, m.group(1))
            in_ordered_list = False
            i += 1
            continue

        m = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if m:
            if not in_ordered_list:
                in_ordered_list = True
                ordered_counter = 0
            ordered_counter += 1
            _write_list_item(pdf, m.group(2), ordered_index=ordered_counter)
            i += 1
            continue

        # Paragraph
        in_ordered_list = False
        paragraph = [stripped]
        j = i + 1
        while j < len(lines):
            nxt = lines[j].strip()
            if (not nxt
                or re.match(r"^#{1,6}\s+", nxt)
                or re.match(r"^[-*+]\s+", nxt)
                or re.match(r"^\d+\.\s+", nxt)):
                break
            paragraph.append(nxt)
            j += 1
        _write_paragraph(pdf, " ".join(paragraph))
        i = j


def markdown_to_pdf_bytes(markdown_text: str, footer: str | None = None) -> bytes:
    """Convert a Markdown string to PDF bytes."""
    pdf = MemoPDF()
    _render_markdown(pdf, markdown_text)

    if footer:
        pdf.ln(6)
        pdf.set_font("Helvetica", "I", 8)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(0, 4, _to_latin1_safe(footer), align="C")

    out = pdf.output(dest="S")
    return bytes(out)
