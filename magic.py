'''Author : Navneet Raj'''
import csv
g = open('rom_stuff', 'w')
g.write('v3.0 hex words addressed\n')
with open('Book1.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    # Skip the header row
    next(csv_reader)
    for row in csv_reader:
        g.write(row[4] + ': ' + row[15] + '\n')
g.close()
