"""
head_file.py

Функция, которая возвращает первые N байт файла.
Если файл не найден -> 404
Если файл текстовый -> возвращает текст
Если бинарный -> помечает как бинарный
"""

import os
from typing import Dict, Any


def _is_likely_text(data: bytes, nonprintable_threshold: float = 0.30) -> bool:
    if not data:
        return True  # пустой файл считаем текстовым
    if b"\x00" in data:
        return False
    try:
        data.decode("utf-8")
    except UnicodeDecodeError:
        return False
    nonprintable = 0
    for b in data:
        if b in (9, 10, 13):  # tab, LF, CR
            continue
        if 32 <= b <= 126:
            continue
        nonprintable += 1
    ratio = nonprintable / max(1, len(data))
    return ratio <= nonprintable_threshold


def head_file(path: str, n: int = 100) -> Dict[str, Any]:
    if not isinstance(path, str):
        raise TypeError("path must be a string")

    if not os.path.exists(path) or not os.path.isfile(path):
        return {"status": 404, "error": "Not found"}

    with open(path, "rb") as f:
        data = f.read(n)

    is_text = _is_likely_text(data)

    return {
        "status": 200,
        "is_text": is_text,
        "content": data.decode("utf-8", errors="replace") if is_text else "<binary>",
    }
