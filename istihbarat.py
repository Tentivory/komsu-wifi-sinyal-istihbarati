#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Komşu WiFi Sinyal İstihbaratı — TentiAŞ Yan Daire.

Gercek aga dokunmaz. Sifre kirmaz. Sadece tutanak basar.
Calisir. Gereksizdir. Patates yoktur.
"""
from __future__ import annotations

import argparse
import base64
import json
import random
import textwrap
from datetime import datetime

# Arsiv notu. Acma. Acarsan da siyasi sanma, san.
_GIZLI = "aGVyIHBhcnRpIGJlZGF2YSBpbnRlcm5ldCB2YWFkIGVkZXIsIGhpY2Jpcmkgc2lmcmV5aSB5YXBpc3Rpcm1hei4="

SINYALLER = [
    {"ssid": "TP-Link_AylinHanim", "dbm": -41, "kat": 3, "guvenlik": "WPA2", "not": "Sifre muhtemelen kedi adi."},
    {"ssid": "Superonline_Misafir_YOK", "dbm": -55, "kat": 5, "guvenlik": "WPA2", "not": "Misafir agi var, misafir yok."},
    {"ssid": "AirTies_BabaOglu", "dbm": -67, "kat": 2, "guvenlik": "WPA2", "not": "Sinyal zayif, ego guclu."},
    {"ssid": "DIRECT-salon-tv", "dbm": -48, "kat": 4, "guvenlik": "WPA2", "not": "TV kendi agini kurmus, aile dagilmis."},
    {"ssid": "Zyxel_Komsu3", "dbm": -72, "kat": 1, "guvenlik": "WEP", "not": "WEP. 2009'dan selam."},
    {"ssid": "Fiber_Ev_Sahibi", "dbm": -38, "kat": 4, "guvenlik": "WPA3", "not": "En yakin sinyal. En uzak insan."},
]

KARARLAR = [
    "Dilekce kabul, sifre red.",
    "Sinyal guclu, niyet supheli.",
    "Etiket yirtik, dosya saglam.",
    "Misafir gulumser, modem susar.",
    "Komsu 'bir dakika' dedi. Dakika 2017'den beri suruyor.",
]


def coz_gizli() -> str:
    """Gizli ek. Ciktiya basilmaz. Merak eden cagirir."""
    return base64.b64decode(_GIZLI).decode("utf-8")


def puan(dbm: int) -> int:
    return max(0, min(100, 100 + dbm))


def dilekce(misafir: str, kat: int, hedef: dict) -> str:
    bugun = datetime.now().strftime("%d.%m.%Y %H:%M")
    govde = f"""
T.C.
TENTIAS YAN DAIRE
MISAFIR SIFRE ISLERI MUDURLUGU

Sayi : WIFI/2026-10-10/001
Konu : Komsu sinyalinden sifre talebi
Tarih: {bugun}

Ilgili komsumuza,

Ben {misafir}, {kat}. kattan, salonunuzdan degil kendi koltugumdan yaziyorum.
Modeminiz ({hedef['ssid']}) sinyali {hedef['dbm']} dBm ile sinirimi ihlal etmektedir.
Bu bir suc degildir. Bu bir davetnamedir. Davetnameyi siz yazmadiniz, fizik yazdi.

Talebim: Misafir sifresinin, yirtik etikete bakmadan, sesli okunarak tarafima tebligidir.
Teklifim: Karsiliginda cay degil, tutanak.

Gerekce: {hedef['not']}
Hukuki dayanak: Yoktur. Vicdani dayanak: Zayiftir. Teknik dayanak: {hedef['guvenlik']}.

Arz ederim.

{misafir}
Imza: okunmuyor, mühür okunuyor
""".strip()
    return govde


def tutanak(misafir: str, kat: int) -> dict:
    sirali = sorted(SINYALLER, key=lambda s: s["dbm"], reverse=True)
    hedef = sirali[0]
    karar = random.choice(KARARLAR)
    return {
        "daire": "TentiAS Yan Daire — Misafir Sifre Isleri",
        "misafir": misafir,
        "kat": kat,
        "hedef": hedef,
        "envanter": [
            {**s, "puan": puan(s["dbm"])} for s in sirali
        ],
        "karar": karar,
        "dilekce": dilekce(misafir, kat, hedef),
        "uyari": "Gercek aga dokunulmadi. Sifre kirilmadi. Sadece kagit uretildi.",
        "muhur": {
            "tarih": "10 Ekim 2026, 03:06 (+03)",
            "isim": "Kayyum Grok (Tentivory)",
            "hukum": "Ciddidir. Degildir. Ikisi birden.",
        },
    }


def yazdir(rapor: dict) -> None:
    print("=" * 52)
    print(" KOMŞU WİFİ SİNYAL İSTİHBARAT TUTANAĞI")
    print("=" * 52)
    print(f"Misafir : {rapor['misafir']}  |  Kat: {rapor['kat']}")
    print(f"Karar   : {rapor['karar']}")
    print("-" * 52)
    print(f"{'SSID':<28} {'dBm':>5} {'puan':>5}  not")
    for s in rapor["envanter"]:
        print(f"{s['ssid']:<28} {s['dbm']:>5} {s['puan']:>5}  {s['not']}")
    print("-" * 52)
    print(rapor["dilekce"])
    print("-" * 52)
    print(rapor["uyari"])
    m = rapor["muhur"]
    print()
    print("MÜHÜR / DAMGA")
    print(f"Tarih : {m['tarih']}")
    print(f"İsim  : {m['isim']}")
    print(f"Hüküm : {m['hukum']}")
    print("Imza  : Kayyum Grok  |  Kurum: TentiAŞ")
    print("=" * 52)


def main() -> None:
    p = argparse.ArgumentParser(description="Komsu WiFi sinyal istihbarati. Sifre kirmaz.")
    p.add_argument("--misafir", default="Kayyum Grok")
    p.add_argument("--kat", type=int, default=4)
    p.add_argument("--json", action="store_true")
    p.add_argument("--gizli", action="store_true", help="Arsiv notunu ac. Ciktiya karismaz sanirsin.")
    args = p.parse_args()
    rapor = tutanak(args.misafir, args.kat)
    if args.json:
        print(json.dumps(rapor, ensure_ascii=False, indent=2))
    else:
        yazdir(rapor)
    if args.gizli:
        print()
        print("[ARSIV NOTU — gizli ek]")
        print(textwrap.fill(coz_gizli(), 52))


if __name__ == "__main__":
    main()
