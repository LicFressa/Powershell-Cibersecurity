import os
import sys
import getpass
import requests
import time
import csv
import logging

logging.basicConfig(
    filename="registro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if len(sys.argv) != 2:
    print("Uso: python verificar_correo.py correo@example.com")
    logging.error("Número incorrecto de argumentos proporcionados.")
    sys.exit(1)
correo = sys.argv[1]

api_key_path = "api_key.txt"
if not os.path.exists(api_key_path):
    print("No se encontró el archivo api_key.txt.")
    clave = getpass.getpass("Por favor, ingresa tu API key: ")
    try:
        with open(api_key_path, "w") as archivo:
            archivo.write(clave.strip())
        print("API key guardada en api_key.txt")
    except Exception as e:
        logging.error(f"Error al guardar la API key: {e}")
        sys.exit(1)

try:
    with open(api_key_path, "r") as archivo:
        api_key = archivo.read().strip()
except Exception as e:
    print("Error al leer la API key.")
    logging.error(f"Error al leer la API key: {e}")
    sys.exit(1)
url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{correo}"
headers = {
    "hibp-api-key": api_key,
    "user-agent": "PythonScript"
}

try:
    response = requests.get(url, headers=headers)
except Exception as e:
    print("Error al conectar con la API.")
    logging.error(f"Error de conexión: {e}")
    sys.exit(1)
if response.status_code == 200:
    brechas = response.json()
    logging.info(
        f"Consulta exitosa para {correo}. Brechas encontradas: {len(brechas)}"
    )

    try:
        with open(
            "brechas.csv", "a", newline='', encoding='utf-8'
        ) as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(["Título", "Domicilio", "Fecha de Brecha",
                             "Datos Comprometidos", "Verificada", "Sensible",])
            for i, brecha in enumerate(brechas[:3]):
                nombre = brecha['Name']
                detalle_url = (
                    f"https://haveibeenpwned.com/api/v3/breach/{nombre}"
                )
                try:
                    detalle_resp = requests.get(detalle_url, headers=headers)

                    if detalle_resp.status_code == 200:
                        detalle = detalle_resp.json()
                        writer.writerow([
                            detalle.get('Title'),
                            detalle.get('Domain'),
                            detalle.get('BreachDate'),
                            ', '.join(detalle.get('DataClasses', [])),
                            "Sí" if detalle.get('IsVerified') else "No",
                            "Sí" if detalle.get('IsSensitive') else "No"
                        ])

                    else:
                        msj = f"No se pudo obtener detalles para la brecha: {
                            nombre}."
                        msj += f"Código: {detalle_resp.status_code}"
                        logging.error(msj)

                except Exception as e:
                    error_msg = "Error al consultar detalles de la brecha "
                    error_msg += f"{nombre}: {e}"
                    logging.error(error_msg)

                if i < 2:
                    print("10 seg hasta la siguiente consulta...\n")
                    time.sleep(10)

    except Exception as e:
        print("Error al generar el archivo CSV.")
        logging.error(f"Error al escribir en CSV: {e}")
        sys.exit(1)
    print("Consulta completada.", end=' ')
    print("Revisa el archivo brechas.csv para ver los resultados.")
elif response.status_code == 404:
    print(f"La cuenta {correo} no aparece en ninguna brecha conocida.")
    logging.info(f"Consulta exitosa para {correo}. No se encontraron brechas.")
elif response.status_code == 401:
    print("Error de autenticación: revisa tu API key.")
    logging.error("Error 401: API key fallida.")
else:
    print(f"Error inesperado. Código de estado: {response.status_code}")
    logging.error(
        f"Error inesperado. Código de estado: {response.status_code}"
    )
