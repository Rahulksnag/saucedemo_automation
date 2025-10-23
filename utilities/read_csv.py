import csv

def read_csv(file_path):
    """
    Returns list of dictionaries: [{'username': '...', 'password': '...'}, ...]
    """
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
