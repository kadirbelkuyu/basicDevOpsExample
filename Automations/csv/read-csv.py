import csv


def read_employees_list(filename):
    file = open(filename)
    csv_file = csv.reader(file)

    for row in csv_file:
        name, phone, role = row
        print(f"Name: {name}, Phone: {phone}, Role: {role}")

    file.close()
