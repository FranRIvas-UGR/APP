import csv
from collections import defaultdict

# Leer el archivo CSV y almacenar los datos en una lista
file_path = '/home/francisco/Escritorio/App/output.csv'
categories = defaultdict(set)

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        category_id = row['Categoría ID']
        category_name = row['Categoría Nombre']
        categories[category_name].add(category_id)

# Encontrar categorías con el mismo nombre pero diferente ID
duplicate_categories = {name: ids for name, ids in categories.items() if len(ids) > 1}

# Imprimir las categorías duplicadas
print("Categorías con el mismo nombre pero diferente ID:")
for name, ids in duplicate_categories.items():
    print(f"Nombre: {name}, IDs: {', '.join(ids)}")