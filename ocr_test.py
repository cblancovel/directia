from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# Ruta a tesseract (ajusta si lo tienes en otro lugar)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Ruta a poppler
poppler_path = r"C:\Program Files\poppler-24.08.0\Library\bin"

# Convertir PDF → PNG
pages = convert_from_path(
    'data/cuadro_mando.pdf',
    dpi=300,
    poppler_path=poppler_path
)

# Guardar la primera página
pages[0].save('data/cuadro_mando_pagina1.png', 'PNG')

# Hacer OCR
image = Image.open('data/cuadro_mando_pagina1.png')

# OCR en español
text = pytesseract.image_to_string(image, lang='spa')

# Mostrar el texto
print(text)
