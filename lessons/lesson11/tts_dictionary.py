#!/usr/bin/env python3
"""TTS 読み辞書（最小テンプレ）。読みはカタカナで（ひらがな「は/へ」は助詞化して化ける）。
長い複合語から先に置換。Stage3b の review_dict.py / tts_dict_review.md で育てる。"""
REPLACEMENTS = [
    # Eシラバス: ラテン文字 E を確実に「イー」と読ませる
    # Eシラバス (e-syllabus): force the Latin "E" to read as イー
    ("Eシラバス", "イーシラバス"),
]
def apply_dictionary(text: str) -> str:
    for src, dst in sorted(REPLACEMENTS, key=lambda kv: -len(kv[0])):
        text = text.replace(src, dst)
    return text
