#Author: Navneet Raj

# modify xml directly for imem
import xml.etree.ElementTree as ET
import assembler as asm
# Use asm.assemble() to convert to hex codes in 'output' file

def update_imem_rom(imem_path = 'output'):
    ''''''
    tree = ET.parse('simpleRISC_reduced.circ')
    root = tree.getroot()
    rom_element = root.find('.//comp[@name="ROM"]')
    data_element = rom_element.find('.//a[@name="contents"]')
    # print(data_element.text)
    l1 = data_element.text.split('\n')[0] # gets addr/data width
    # print(l1)

    with open(imem_path, 'r') as f:
        data = f.readlines()
    data = data[1:]
    data = [i.split(':')[1].strip(' ') for i in data]
    # print(data)
    file_data = ''.join(data)
    new_data = l1 + '\n' + file_data
    # print(new_data)

    data_element.text = new_data
    tree.write('simpleRISC_reduced.circ')


asm.assemble()
update_imem_rom('output')
    