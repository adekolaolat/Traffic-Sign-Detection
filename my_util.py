import csv

# Convert csv to dictionary
def csv_to_dict(filename):
    result_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            key = int(row[0])
            value = row[1]
            result_dict[key] = value
    return result_dict