'''Author : Navneet Raj'''
import csv
def write_rom():
    g = open('rom_stuff', 'w')
    g.write('v3.0 hex words addressed\n')
    with open('Book1.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        # Skip the header row
        header = next(csv_reader)
        data = list(csv_reader)
        sortedlist = sorted(data, key=lambda row: int(row[-1]))
        for row in sortedlist:
            g.write(row[4] + ': ' + row[15] + '\n')
    g.close()
'''with open('Book2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(sortedlist)
f.close()'''
