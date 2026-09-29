#!/usr/bin/env python3
"""Generate 50 Zola content files named INEgma_<i>.md, i random in 1..1000.

Run from the root of your Zola site:  python generate_inegma.py
"""
import random
from pathlib import Path

OUT_DIR = Path("content")   # where Zola looks for pages
TEMPLATE = "INEgma14.html"    # template each page will use

OUT_DIR.mkdir(exist_ok=True)

whatsapp = [
    'https://chat.whatsapp.com/FYhFeyKBbWg3h1NGJh4x4A',
    'https://chat.whatsapp.com/DsjtbktrOP3IhM119vuJ8e',
    'https://chat.whatsapp.com/Liw1Y35y70lDdrcQaMYsWi',
    'https://chat.whatsapp.com/J57HdZZgaVA1bBrTTCjIlx',
    'https://chat.whatsapp.com/EiMQU8st5ZQHzXbBuFEyjw',
    'https://chat.whatsapp.com/KF1CqKfX7l9E7jtHdp0beE',
    'https://chat.whatsapp.com/BdExchpMl3M854081GykKS',
    'https://chat.whatsapp.com/IoD9cFMFmyA1Lx2sw0eE9Z',
    'https://chat.whatsapp.com/B7sYvd1FORe5B8ePuQcjVb',
    'https://chat.whatsapp.com/GXxUPYnRkLz5KsZCeJXGI0',
    'https://chat.whatsapp.com/BSJQDxja7W3EoZqwWJVrTo',
    'https://chat.whatsapp.com/HjokKkPDv1J0QKah5hi0K9',
    'https://chat.whatsapp.com/FsZUykmHqua1w1SO4fixwr',
    'https://chat.whatsapp.com/BYblrI5oXUp1Q1VilSfo6n',
    'https://chat.whatsapp.com/Hc4Y7eyZUFeFLKlNH2oVdF',
    'https://chat.whatsapp.com/H8W4CbDVMOMFU5wDL5AJnr',
    'https://chat.whatsapp.com/HleVxMC12M6HN6wfzSDOdr',
    'https://chat.whatsapp.com/HlzYprvMNlV69SlqZ9RUxx',
    'https://chat.whatsapp.com/BAtOBp4UxApBF3c736A5eC',
    'https://chat.whatsapp.com/HL8asHLblYI9OLE0kXDj0G',
    'https://chat.whatsapp.com/HqbloMQzZpk6p2DzoSm0sE',
    'https://chat.whatsapp.com/CFsKAwi0u2E15gnwwmkO3L',
    'https://chat.whatsapp.com/De8RkoyR52dIP7We5AIyHA',
    'https://chat.whatsapp.com/Bmpp3jSczjl6s3f1n30CVb',
    'https://chat.whatsapp.com/F0RF9gyuB8t6au50k2tuid',
    'https://chat.whatsapp.com/EP03W0rsGU1HN2vKrjj8mY',
    'https://chat.whatsapp.com/EbYmPA4Wh0m3vHlhhDZPL2',
    'https://chat.whatsapp.com/FJDUtPGSsFM2LnnbGgFDhk',
    'https://chat.whatsapp.com/LQtNMnAAGKiCpfWPXZGyzb',
    'https://chat.whatsapp.com/D6KVNkiZ3gW7xi3VGnBzTn',
    'https://chat.whatsapp.com/KRawreVc9UsFJAWa59UIS0',
    'https://chat.whatsapp.com/LwuUqhWhYYzCsgas9bMstu',
    'https://chat.whatsapp.com/GQUIswsP9GHJUvpWUeNqJ2',
    'https://chat.whatsapp.com/Le89n3yjkaT9hsO8Ftk8Kx',
    'https://chat.whatsapp.com/Cms8jgYBCrZELV4LidjYK5',
    'https://chat.whatsapp.com/IBSkUA3buwi7WUGQRxHXis',
    'https://chat.whatsapp.com/KhfQwoEoLXqB05INZWPlLT',
    'https://chat.whatsapp.com/CJIXfP6PoOODsQvkRhFM23',
    'https://chat.whatsapp.com/Fhal6eX7lgHKPpKzoACXFJ',
    'https://chat.whatsapp.com/Dhm6jLZggPhJMqw3ANV1UC',
    'https://chat.whatsapp.com/BPzevUn4URQLVFhPQ0pVwi'
]
COUNT = len(whatsapp)
j = 0

# random.sample guarantees 50 unique numbers, so no file overwrites another
for i in random.sample(range(1, 1001), COUNT):
    name = f"INEgma_{i}"
    OOUT_DIR = Path(OUT_DIR) / name
    OOUT_DIR.mkdir(exist_ok=True)
    (OOUT_DIR / "_index.md").write_text(
        f'+++\ntitle = "{name}"\ntemplate = "{TEMPLATE}"\n+++\nLe trajet commencera depuis l’INPT et se terminera également à l’INPT.\n\n[rejoindre le groupe Wahtsapp de votre equipe]({whatsapp[j]})',
        encoding="utf-8",
    )
    j += 1
    print(f"created {OOUT_DIR / name}.md")

