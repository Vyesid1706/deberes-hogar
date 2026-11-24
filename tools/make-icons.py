"""Genera los iconos y el SVG del corazon pixelado (diseno original 11x10)."""
from PIL import Image
import os

# K = contorno negro, R = rojo, W = brillo, . = transparente
GRID = [
    "..KKK.KKK..",
    ".KRRRKRRRK.",
    "KRRRRRRWRRK",
    "KRRRRRRRWRK",
    "KRRRRRRRRRK",
    ".KRRRRRRRK.",
    "..KRRRRRK..",
    "...KRRRK...",
    "....KRK....",
    ".....K.....",
]
N = len(GRID[0])
M = len(GRID)
COLORS = {"K": (0, 0, 0, 255), "R": (252, 24, 24, 255), "W": (255, 255, 255, 255)}
for i, row in enumerate(GRID):
    assert len(row) == N, (i, len(row), row)


def png(size, path):
    cell = size // N
    w, h = cell * N, cell * M
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ox, oy = (size - w) // 2, (size - h) // 2
    for y, row in enumerate(GRID):
        for x, ch in enumerate(row):
            if ch not in COLORS:
                continue
            col = COLORS[ch]
            for py in range(cell):
                for px in range(cell):
                    img.putpixel((ox + x * cell + px, oy + y * cell + py), col)
    img.save(path)


here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
png(512, os.path.join(here, "icon-512.png"))
png(192, os.path.join(here, "icon-192.png"))

HEX = {"K": "#000000", "R": "#fc1818", "W": "#ffffff"}
rects = []
for y, row in enumerate(GRID):
    x = 0
    while x < N:
        ch = row[x]
        if ch not in COLORS:
            x += 1
            continue
        x0 = x
        while x < N and row[x] == ch:
            x += 1
        rects.append('<rect x="%d" y="%d" width="%d" height="1" fill="%s"/>' % (x0, y, x - x0, HEX[ch]))

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" shape-rendering="crispEdges">' % (N, M)
       + "".join(rects) + "</svg>")
with open(os.path.join(here, "heart.svg"), "w", encoding="utf-8") as f:
    f.write(svg)

print("icon-512", os.path.getsize(os.path.join(here, "icon-512.png")))
print("icon-192", os.path.getsize(os.path.join(here, "icon-192.png")))
print("heart.svg", len(svg))
