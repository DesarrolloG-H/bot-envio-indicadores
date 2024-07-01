import fitz  # PyMuPDF

def transformacion_pdf_img(ruta_completa_archivo_pdf, numero_pagina, imagen_generada):
    # Abrir el archivo PDF
    pdf_document = fitz.open(ruta_completa_archivo_pdf)
    
    # Obtener la página especificada
    page = pdf_document.load_page(numero_pagina)
    
    # Renderizar la página como una imagen (pixmap)
    pixmap = page.get_pixmap()
    
    # Guardar la imagen en el disco
    pixmap._writeIMG(imagen_generada, format_='png', jpg_quality=95)  # Especificar formato y calidad (opcional para PNG)

    # Cerrar el documento PDF
    pdf_document.close()