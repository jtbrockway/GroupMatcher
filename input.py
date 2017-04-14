import csv

file = ""
def set_file(filename):
    file = filename

def read_csv():
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(reader)

