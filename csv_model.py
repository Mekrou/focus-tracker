import csv

class CSVModel:
    def __init__(self, file_path):
        self.file_path = file_path

    def create(self, data):
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def read_all(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
        return rows

    def update(self, index, data):
        rows = self.read_all()
        if index >= 0 and index < len(rows):
            rows[index] = data
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

    def delete(self, index):
        rows = self.read_all()
        if index >= 0 and index < len(rows):
            del rows[index]
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

