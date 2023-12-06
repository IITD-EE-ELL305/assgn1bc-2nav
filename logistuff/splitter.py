from secret import add_splitter, delete_circuit

'''Usage - add_splitter(path, incoming_bits, split_list)'''

# modify to get your own path
path = 'logistuff/circuit.circ'

# bits to be split
incoming_bits = 16

# list of bits to split into
split_list = [3, 1, 1, 1, 1, 1, 1, 4]

add_splitter(path, incoming_bits, split_list)

'''Output - Added splitter to logistuff/circuit.circ in a new circuit'''
'''The reason why incoming_bits is not equal to sum(split_list) is because we might have some bits set to none and not used, so 
for example 
incoming_bits = 4
split_list = [2, 1]
splitter splits into 2 and 1 bit with last bit being unused
also split_list[0] = bit0 (little endian or whatever)  '''

# delete_circuit(path)
'''Deletes the extra circuit generated by add_splitter'''