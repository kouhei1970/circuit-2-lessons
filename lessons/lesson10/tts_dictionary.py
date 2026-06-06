#!/usr/bin/env python3
"""lesson10 固有 TTS 読み辞書（最小）。

term の標準読みは共通DB ~/.claude/skills/interactive-lecture/reference/tts_readings.json
にあり、gen_audio.py / verify_readings.py が自動で参照する（共通DB優先）。
ここには「共通DBに無い lesson10 固有の語・助詞補正」だけを追加する。

読みは必ずカタカナで（ひらがな は/へ は edge-tts が助詞ワ/エに化ける）。
追加したら verify_readings.py で読みを検証すること。
"""
REPLACEMENTS = [
    # 例: ("特有の語", "トクユウノゴ"),
]


def apply_dictionary(text: str) -> str:
    for src, dst in sorted(REPLACEMENTS, key=lambda kv: -len(kv[0])):
        text = text.replace(src, dst)
    return text
