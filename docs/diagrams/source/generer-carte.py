#!/usr/bin/env python3
"""Génère la carte de continuité « Resugo Evidence » (SVG) depuis la spec JSON.

Usage : python3 source/generer-carte.py
Entrée : source/carte-continuite.json
Sortie : export/carte-continuite.svg

La carte est statique et accessible : textes en éléments <text> réels,
<title> + <desc> complets (alternative textuelle), contrastes vérifiés
(blanc sur #2b4c7e ≈ 9,9:1 ; blanc sur #b45a3c ≈ 5,6:1). Rien d'indispensable
uniquement graphique : le CV reprend tout le contenu en texte.
"""
import json
from pathlib import Path

# Palette (charte chaud v2 : crème, navy, terracotta — contrastes vérifiés)
CREME = "#f6f1e7"
NAVY = "#2b4c7e"
TERRA = "#b45a3c"
ENCRE = "#1c2b3a"

BLEU_BLOC = NAVY
BLEU_TEXTE = "#ffffff"

BLOCK_W = 172
GAP = 24
MARGIN = 10
ROW_TOP = 64          # y du haut des blocs
BLOCK_H = 56          # hauteur du bloc nom
LEVEL_GAP = 10        # espace sous le bloc
TEXT_GAP = 26         # première ligne de texte sous le niveau
LINE_H = 20

SRC = Path(__file__).resolve().parent
SPEC = SRC / "carte-continuite.json"
OUT = SRC.parent / "export" / "carte-continuite.svg"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main() -> None:
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    blocs = spec["blocs"]
    n = len(blocs)
    width = MARGIN * 2 + n * BLOCK_W + (n - 1) * GAP
    height = ROW_TOP + BLOCK_H + LEVEL_GAP + TEXT_GAP + LINE_H * 2 + 64

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'role="img" aria-labelledby="carte-titre carte-desc" lang="fr">'
    )
    parts.append(f'<title id="carte-titre">{esc(spec["titre"])}</title>')
    parts.append(f'<desc id="carte-desc">{esc(spec["description"])}</desc>')

    # Fond crème
    parts.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="{CREME}"/>')

    # Rôle — trait d'union (en tête)
    parts.append(
        f'<text x="{MARGIN}" y="30" font-family="sans-serif" font-size="17" '
        f'font-weight="700" fill="{NAVY}">{esc(spec["role"])}</text>'
    )
    parts.append(
        f'<text x="{MARGIN}" y="50" font-family="sans-serif" font-size="12" '
        f'fill="{ENCRE}">{esc(spec["sous-role"])}</text>'
    )

    for i, b in enumerate(blocs):
        x = MARGIN + i * (BLOCK_W + GAP)
        traversant = b.get("traversant", False)
        fill = CREME if traversant else BLEU_BLOC
        stroke = NAVY
        text_fill = NAVY if traversant else BLEU_TEXTE
        cx = x + BLOCK_W / 2

        # Flèche vers le bloc suivant
        if i < n - 1:
            ax0 = x + BLOCK_W + 2
            ax1 = x + BLOCK_W + GAP - 2
            ay = ROW_TOP + BLOCK_H / 2
            parts.append(
                f'<line x1="{ax0}" y1="{ay}" x2="{ax1}" y2="{ay}" '
                f'stroke="{NAVY}" stroke-width="2"/>'
            )
            parts.append(
                f'<polygon points="{ax1},{ay} {ax1 - 7},{ay - 4} {ax1 - 7},{ay + 4}" fill="{NAVY}"/>'
            )

        # Bloc nom
        parts.append(
            f'<rect x="{x}" y="{ROW_TOP}" width="{BLOCK_W}" height="{BLOCK_H}" rx="8" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
        )
        parts.append(
            f'<text x="{cx}" y="{ROW_TOP + 33}" text-anchor="middle" '
            f'font-family="sans-serif" font-size="17" font-weight="700" '
            f'fill="{text_fill}">{esc(b["nom"])}</text>'
        )

        # Niveau (pill)
        py = ROW_TOP + BLOCK_H + LEVEL_GAP
        parts.append(
            f'<rect x="{cx - 52}" y="{py}" width="104" height="22" rx="11" fill="{TERRA}"/>'
        )
        parts.append(
            f'<text x="{cx}" y="{py + 15}" text-anchor="middle" '
            f'font-family="sans-serif" font-size="12" font-weight="700" '
            f'fill="#ffffff">{esc(b["niveau"])}</text>'
        )

        # Lignes de contenu
        ty = py + TEXT_GAP
        for ligne in b["lignes"]:
            parts.append(
                f'<text x="{cx}" y="{ty}" text-anchor="middle" '
                f'font-family="sans-serif" font-size="12.5" fill="{ENCRE}">{esc(ligne)}</text>'
            )
            ty += LINE_H

    # Légende (bas de carte)
    ly = height - 18
    parts.append(
        f'<text x="{MARGIN}" y="{ly}" font-family="sans-serif" font-size="12" '
        f'fill="{ENCRE}">{esc(spec["legende"])}</text>'
    )

    parts.append("</svg>\n")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"OK → {OUT}")


if __name__ == "__main__":
    main()
