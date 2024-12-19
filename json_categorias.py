import csv
import json

# Path to the CSV file
csv_file_path = 'output_sorted.csv'

# Initialize a dictionary to hold the categories
categories_dict = {"categories": []}

# Read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Use a set to keep track of added categories to avoid duplicates
    added_categories = set()
    for row in csv_reader:
        category_id = int(row['Categoría ID'])
        category_name = row['Categoría Nombre']
        if category_id not in added_categories:
            categories_dict["categories"].append({"name": category_name, "id": category_id})
            added_categories.add(category_id)

# Convert the dictionary to a JSON string
json_output = json.dumps(categories_dict, ensure_ascii=False, indent=4)

# Path to the output JSON file
json_file_path = 'json/categories.json'

# Write the JSON string to the file
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json_file.write(json_output)

print(f"JSON file has been created at {json_file_path}")