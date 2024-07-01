import os

def obtener_pdf_actual(ruta_archivo_pdf):
    # Obtenemos la lista de todos los archivos de la carpeta donde se almacena los reportes
    archivos = os.listdir(ruta_archivo_pdf)
    
    # Filtrar los archivos para obtener solo los PDFs
    pdfs = [archivo for archivo in archivos if archivo.endswith('.pdf')]
    # Si no hay PDFs en la carpeta, retornar None
    if not pdfs:
        return None
    
    # Ordenar los PDFs por fecha de modificación (el más reciente primero)
    pdfs.sort(key=lambda archivo: os.path.getmtime(os.path.join(ruta_archivo_pdf, archivo)), reverse=True)
    # Devolver el nombre del último PDF (REPORTE)
    return pdfs[0]