from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#retraso
import time
# import pytz
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def enviar_archivos_whatsapp(ruta_chromedriver, ruta_chromeperfil, carpeta_imagenes):
    # INSTANCIA PRINCIPAL DE CHROME
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument(ruta_chromedriver)

    # INSTANCIA SECUNDARIA DE CHROME PARA WSP
    profile_path = ruta_chromeperfil
    options.add_argument("--user-data-dir=" + profile_path)
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    time.sleep(60)

    buscadorWhatsaap_xpath = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
    input_element_buscador = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, buscadorWhatsaap_xpath)))

    # grupo_whatsaap = "Gestión HITSS - Proyecto MINPUB"
    grupo_whatsaap = "yo"
    for letra in grupo_whatsaap:
        input_element_buscador.send_keys(letra)
        time.sleep(0.1)
    time.sleep(5)
    input_element_buscador.send_keys(Keys.RETURN)
    time.sleep(10)


    for imagen in os.listdir(carpeta_imagenes):
        ruta_imagen = os.path.join(carpeta_imagenes, imagen)
        attachment_button = driver.find_element(By.XPATH, '//div[@title="Adjuntar"]')
        attachment_button.click()
        time.sleep(5)
        file_input = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        file_input.send_keys(ruta_imagen)
        time.sleep(5)
        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()
        time.sleep(5)
    time.sleep(8)
    driver.quit()
    