#libreria_tiempo y suma de tiempo a la hora actual
from datetime import datetime, timedelta
import os
from components import envio_whatsaap, obtener_pdf_actual, transformacion_pdf_img

###### FECHA #####
# Obtener la fecha y hora actual
fecha_actual = datetime.now()
# Formatear la fecha y hora en el formato deseado
fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")

### ---- VARIABLES ---- ###
ruta_chromeperfil = "C:\\Users\\justinianoj\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
ruta_chromedriver = os.path.abspath( r".\utils\chromedriver.exe")
# Ruta del archivo PDF
# ruta_archivo_pdf = 'D:\\PYTHON_AUTOMATIZACIONES_GENERALES_2\\BOT_X_HORA_PY\\CARPETAS_GUARDADAS\\Pdf_historico'
ruta_archivo_pdf = 'D:\\BOT-ENVIO-INDICADORES\\assets\\pdf'
# Número de página a capturar (por ejemplo, página 1)
numero_pagina = 2
# Ruta donde se guardará la imagen
imagen_generada = os.path.abspath(r".\assets\img\imagen_reporte.png")
carpeta_imagenes = os.path.abspath(r".\assets\img")

###### ------------------ ######

##### OBTENER EL ULTIMO REPORTE GENERADO #####
# Obtener el nombre del último PDF en la carpeta
archivo_pdf = obtener_pdf_actual.obtener_pdf_actual(ruta_archivo_pdf)
#### ------- GENERAR RUTA DEL PDF ------ #####
# Creando la ruta completa del ultimo reporte encontrado
ruta_completa_archivo_pdf = f'{ruta_archivo_pdf}\\{archivo_pdf}'
# CAPTURAR LA PAGINA DEL REPORTE EN UNA IMAGEN PARA SU ENVIO POR WHATSAPP
transformacion_pdf_img.transformacion_pdf_img(ruta_completa_archivo_pdf, numero_pagina, imagen_generada)
# ENVIO DE LA IMAGEN POR WHATSAPP USANDO SELENIUM
envio_whatsaap.enviar_archivos_whatsapp(ruta_chromedriver, ruta_chromeperfil, carpeta_imagenes)
