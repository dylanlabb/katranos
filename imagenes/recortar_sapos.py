from PIL import Image
import os

src = os.path.join(os.path.dirname(__file__), "sapo.jpeg")
out_dir = os.path.dirname(__file__)

# Coordenadas (x, y, x2, y2) ajustadas al tamaño 736x1308
frogs = {
    "sapo_manchado":    (15,  10,  290, 328),   # sapo café manchado arriba-izq
    "sapo_flores":      (295, 5,   736, 312),   # sapo verde con flores y libélulas
    "sapo_mini":        (305, 260, 415, 435),   # sapito mini simple centro
    "sapo_pizza":       (10,  322, 348, 638),   # sapo con pizza y sombrero hongo
    "sapo_pincel":      (400, 402, 718, 622),   # sapo pintando con brocha
    "sapo_abrazo":      (15,  762, 315, 918),   # dos sapos abrazados
    "sapo_impermeable": (0,   900, 240, 1300),  # sapo con impermeable amarillo (abajo)
    "sapo_sonrisa":     (200, 878, 460, 1058),  # sapo con sombrero de seta sonriendo
    "sapo_torre":       (392, 728, 736, 1308),  # torre de tres sapos
}

BG = (204, 246, 238)   # color exacto del fondo celeste

def remove_bg(img, tolerance=32):
    img_rgba = img.convert("RGBA")
    pixels = list(img_rgba.getdata())
    new_pixels = []
    for r, g, b, a in pixels:
        if (abs(int(r)-BG[0]) < tolerance and
            abs(int(g)-BG[1]) < tolerance and
            abs(int(b)-BG[2]) < tolerance):
            new_pixels.append((r, g, b, 0))
        else:
            new_pixels.append((r, g, b, a))
    img_rgba.putdata(new_pixels)
    return img_rgba

src_img = Image.open(src)
print(f"Imagen fuente: {src_img.size}")

for name, box in frogs.items():
    cropped = src_img.crop(box)
    no_bg = remove_bg(cropped)
    out_path = os.path.join(out_dir, f"{name}.png")
    no_bg.save(out_path)
    print(f"Guardado: {name}.png  ({box[2]-box[0]}x{box[3]-box[1]}px)")

print("\nListo! Todos los sapos recortados.")
