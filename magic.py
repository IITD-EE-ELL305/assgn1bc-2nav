'''Author : Navneet Raj'''
import csv
def write_rom():
    addr_width = 8
    g = open('rom_stuff', 'w')
    g.write('v3.0 hex words addressed\n')
    with open('Book1.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        # Skip the header row
        header = next(csv_reader)
        data = list(csv_reader)
        sortedlist = sorted(data, key=lambda row: int(row[-1]))
        j = 0
        # print(sortedlist)
        for i in range(2**addr_width):
            row = sortedlist[j]
            # print(i, row[-1])
            if i == int(row[-1]):
                g.write(row[4] + ': ' + row[15] + '\n')
                if j < len(sortedlist) - 1:
                    j += 1
            else:
                g.write(hex(i).zfill(2)[2:] + ': ' + '0'*4 + '\n')
        # for row in sortedlist:
        #     g.write(row[4] + ': ' + row[15] + '\n')
    g.close()
write_rom()
'''with open('Book2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(sortedlist)
f.close()'''
