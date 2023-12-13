import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read CSV file
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Assuming the first row contains column headers
        data = [row for row in csv_reader]

    # Convert data to JSON format
    json_data = []
    for row in data:
        json_data.append({
            "Title": row[0],
            "ActionResult": [row[1:]]
        })

    # Write JSON to file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

# Example usage
csv_file_path = "C:/Users/sayan.h.mukherjee/Downloads/Output.csv"
json_file_path = "C:/Users/sayan.h.mukherjee/Downloads/Output.json"
csv_to_json(csv_file_path, json_file_path)