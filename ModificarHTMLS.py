from mtranslate import translate
import os
import mtranslate
import re
from bs4 import BeautifulSoup
import time
from urllib.error import HTTPError
from langdetect import detect
from langdetect import detect_langs



def traducir(etiqueta, archivo):
    try:
        for p in soup.find_all(etiqueta):
                try:
                    print(f"Texto es idioma: {detect_langs(p.text)}")
                    p.string = mtranslate.translate(p.text, 'es')
                    print(f"LISTO {etiqueta} EN {archivo} Y EL NUEVO IDIOMA ES {detect(p.string)}")
                except:
                    print(f"ERROR EN {etiqueta} DE {archivo}")
                    continue
    except HTTPError as e:
        print(f"Error {e.code}: {e.reason}")
        print("Esperando 5 segundos antes de volver a intentar...")
        time.sleep(5)
        return traducir(etiqueta, archivo)

carpeta = 'C:\Downloaded Web Sites\www.classcentral.com - copia'
codificaciones = ['utf-8', 'ISO-8859-1', 'Windows-1252', 'cp850', 'cp858', 'cp860', 'cp437', 'cp737', 'cp775', 'ascii']

for root, dirs, files in os.walk(carpeta):
    for archivo in files:
        if archivo.endswith('.html'):
            archivo_path = os.path.join(root, archivo)
            for codif in codificaciones:
                try:
                    with open(archivo_path, encoding=codif) as f:
                        content = f.read()
                    # Si se logra abrir el archivo con la codificación, se rompe el ciclo
                    break
                except UnicodeDecodeError:
                    # Si se produce un error de decodificación, se prueba con la siguiente codificación
                    continue
            soup = BeautifulSoup(content, 'html.parser')
            traducir('h2',archivo)
            traducir('h1',archivo)
            traducir('p',archivo)
            traducir('a',archivo)