import csv

input_file = 'output.csv'
output_file = 'output_sorted.csv'

# Read the CSV file
with open(input_file, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    rows = list(reader)

# Sort the rows by the first column (Categoría ID)
rows.sort(key=lambda x: int(x[0]))

# Write the sorted rows to a new CSV file
with open(output_file, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Sorted CSV file has been saved as {output_file}")