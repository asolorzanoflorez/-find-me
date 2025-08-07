#!/usr/bin/env python3
import os, shutil, sys
from pathlib import Path

SRC = Path("/data/data/com.termux/files/home/storage/shared/.FileManagerRecycler")
DST = Path("/data/data/com.termux/files/home/storage/shared/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Audio")

def same_file(a: Path, b: Path):
    return b.exists() and a.stat().st_size == b.stat().st_size and int(a.stat().st_mtime) == int(b.stat().st_mtime)

if not SRC.is_dir():
    sys.exit(f"Fuente no encontrada: {SRC}")

copied = skipped = 0
for root, _, files in os.walk(SRC):
    for name in files:
        src = Path(root) / name
        dst = DST / name
        if same_file(src, dst):
            skipped += 1
            continue
        try:
            shutil.copy2(src, dst)      # usa shutil.move() si quieres mover
            copied += 1
        except Exception as e:
            print(f"Error copiando {src}: {e}", file=sys.stderr)

print(f"Copiados: {copied} | Omitidos: {skipped}")

