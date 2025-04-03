archivo = "reportes.txt"

with open(archivo, "r", encoding="utf-8") as file:
    lineas = [line.strip() for line in file.readlines()]




