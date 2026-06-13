#!/usr/bin/env python3
"""TTS 読み辞書（lesson13 固有）。読みはカタカナで（ひらがな「は/へ」は助詞化して化ける）。
共通DB（reference/tts_readings.json）に無い語・誤読のみをここに置く。長い複合語から先に置換。

検証メモ（pyopenjtalk G2P）:
- 斉次方程式 → 既定では「ヒトシジホーテーシキ」と誤読 → 正しい「セイジホウテイシキ」に固定。
  Fix the homogeneous-equation term: pyopenjtalk misreads 斉次方程式; force セイジホウテイシキ.
- 同相 → 既定では「ドーショー」と誤読 → 正しい「ドウソウ（in-phase）」に固定。
  Fix the in-phase term: pyopenjtalk misreads 同相 as ドーショー; force ドウソウ.
"""
REPLACEMENTS = [
    ("斉次方程式", "セイジホウテイシキ"),
    ("同相", "ドウソウ"),
]


def apply_dictionary(text: str) -> str:
    for src, dst in sorted(REPLACEMENTS, key=lambda kv: -len(kv[0])):
        text = text.replace(src, dst)
    return text
