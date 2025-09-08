import os
import getpass
import requests
import csv
import logging
import argparse

def leer_apikey(path='api_key.txt'):
    if not os.path.exists(path):
        clave = getpass.getpass("Ingresa tu API key: ")
        with open(path, 'w') as archivo:
            archivo.write(clave.strip())
    with open(path, 'r') as archivo:
        return archivo.read().strip()

def obtener_argumentos():
    parser = argparse.ArgumentParser(
        description="Verifica si un correo ha sido comprometido usando la API de Have I Been Pwned."
    )
    parser.add_argument("correo", help="Correo electrónico a verificar.")
    parser.add_argument("-o", "--output", default="reporte.txt", 
                        help="Nombre del archivo CSV de salida.")
    return parser.parse_args()

def consultar_brechas(correo, api_key):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{correo}"
    headers = {"hibp-api-key": api_key, "user-agent": "PythonScript"}
    return requests.get(url, headers=headers)

def generar_csv(nombre_archivo, lista_detalles):
    with open(nombre_archivo, "w", newline='', encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow([
            "Title", "Domain", "BreachDate", "AddedDate", 
            "DataClasses", "Description"
        ])
        for detalle in lista_detalles:
            writer.writerow([
                detalle.get("Title"),
                detalle.get("Domain"),
                detalle.get("BreachDate"),
                ", ".join(detalle.get("DataClasses", [])),
                "Sí" if detalle.get("IsVerified") else "No",
                "Sí" if detalle.get("IsSensitive") else "No"
            ])

logging.basicConfig(
    filename="registro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)