import xml.etree.ElementTree as ET


def delete_circuit_helper(root, circuit_name):
    # Delete the existing circuit if it exists
    existing_circuit = root.find(f".//circuit[@name='{circuit_name}']")
    if existing_circuit is not None:
        root.remove(existing_circuit)
        print(f"Deleted existing circuit: {circuit_name}")


def delete_circuit(circ_path):
    # Delete the existing circuit if it exists
    tree = ET.parse(circ_path)
    root = tree.getroot()
    delete_circuit_helper(root, 'new_circuit')


def add_splitter_helper(circ_path, new_circuit_name, incoming_bits=2, split_list=[1, 1]):
    tree = ET.parse(circ_path)
    root = tree.getroot()

    # Delete the existing circuit
    delete_circuit_helper(root, new_circuit_name)

    # Create a new circuit element
    new_circuit = ET.Element('circuit')
    new_circuit.set('name', new_circuit_name)

    # Add attributes to the new circuit
    attributes_list = [
        {'name': 'appearance', 'val': 'logisim_evolution'},
        {'name': 'circuit', 'val': new_circuit_name},
        {'name': 'circuitnamedboxfixedsize', 'val': 'true'},
        {'name': 'simulationFrequency', 'val': '1.0'}
    ]

    for attribute_data in attributes_list:
        attribute_element = ET.Element(
            'a', {'name': attribute_data['name'], 'val': attribute_data['val']})
        new_circuit.append(attribute_element)

    # Add the new circuit to the root
    root.append(new_circuit)
   # Add a splitter to the new circuit
    splitter_attributes = {'lib': '0', 'loc': '(100,100)', 'name': 'Splitter'}
    splitter_element = ET.Element('comp', splitter_attributes)

    # Add an incoming bit length element
    incoming_bit_length = incoming_bits
    incoming_bit_length_element = ET.Element(
        'a', {'name': 'incoming', 'val': str(incoming_bit_length)})
    splitter_element.append(incoming_bit_length_element)

    # Add a fanout element
    split_count = len(split_list)
    fanout_element = ET.Element(
        'a', {'name': 'fanout', 'val': str(split_count)})
    splitter_element.append(fanout_element)

    new_circuit.append(splitter_element)

    # Assign values to bits
    j = 0
    su = split_list[0]
    for i in range(0, incoming_bits):
        bit_element = ET.Element('a', {'name': f'bit{i}', 'val': 'none'})
        if i <= sum(split_list):
            if i < su:
                bit_element.set('val', str(j))
            else:
                j += 1
                if j < len(split_list):
                    su += split_list[j]
                    bit_element.set('val', str(j))
        splitter_element.append(bit_element)

    # Save the modified XML back to a file
    tree.write(circ_path)


def add_splitter(circ_path, incoming_bits=2, split_list=[1, 1]):
    add_splitter_helper(circ_path, 'new_circuit', incoming_bits, split_list)
    print(f"Added splitter to {circ_path}")


# path = 'logistuff/circuit.circ'
# add_splitter(path, 12, [2, 3, 5])
