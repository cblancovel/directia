import pytesseract
from PIL import Image

# Carga la imagen
image = Image.open("data/cuadro_mando_pagina1.png")

# Extraer texto
text = pytesseract.image_to_string(image, lang="spa")

print(text)
