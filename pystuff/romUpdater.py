#Author: Navneet Raj

# modify xml directly for imem and ctrl_rom
import xml.etree.ElementTree as ET
import assembler as asm
import ctrlRom as ctrl_rom
# Use asm.assemble() to convert to hex codes in 'output' file
# use ctrl_rom.write_rom() to convert to hex codes in 'rom_stuff' file
path ='simpleRISC_reduced.circ'
def update_imem_rom(imem_path = 'output'):
    '''Updates imem values in .circ file, given the path to the output of assembler'''
    tree = ET.parse(path)
    root = tree.getroot()
    rom_element = root.find('.//comp[@name="ROM"]')
    data_element = rom_element.find('.//a[@name="contents"]')
    # print(data_element.text)
    l1 = data_element.text.split('\n')[0] # gets addr/data width
    # print(l1)

    with open('pystuff/'+imem_path, 'r') as f:
        data = f.readlines()
    data = data[1:]
    data = [i.split(':')[1].strip(' ') for i in data]
    # print(data)
    file_data = ''.join(data)
    new_data = l1 + '\n' + file_data
    # print(new_data)

    data_element.text = new_data
    tree.write(path)

def update_ctrl_rom(rom_path='rom_stuff'):
    '''updates ctrl_rom values in .circ file, given the path to the output of magic.py'''
    tree = ET.parse(path)
    root = tree.getroot()
    rom_element = root.findall('.//comp[@name="ROM"]')[1]
    data_element = rom_element.find('.//a[@name="contents"]')
    # print(data_element.text)
    
    l1 = data_element.text.split('\n')[0] # gets addr/data width

    with open('pystuff/'+rom_path, 'r') as f:
        data = f.readlines()
    data = data[1:]
    data = [i.split(':')[1].strip() for i in data]
    # print(data)
    file_data = ' '.join(data)
    new_data = l1 + '\n' + file_data
    # print(new_data)

    data_element.text = new_data
    tree.write(path)


asm.assemble()
update_imem_rom('output')
update_ctrl_rom('rom_stuff')
    