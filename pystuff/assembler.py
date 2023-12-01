import math


def bin_to_hex(bin_str):
    return (hex(int(bin_str, 2))[2:].zfill(8))


def encode(hex_str):
    l = ''
    for i in range(0, len(hex_str), 2):
        l += ' ' + hex_str[i: i + 2][:: -1]
    return l[::-1].strip()

# print(encode(bin_to_hex('00000000000000110000000000110011')))


instructions = {"add": '00000', "sub": '00001', "cmp": '00101', "ld": '01110', "st": '01111', "beq": '10000',
                "call": '10011', "ret": '10100', "nop": '01101', "halt": '11111', "and": '00110', "or": '00111', "bgt": '10001'}

# imm/r3 r2 r1 i op


def inst_to_bin(inst):
    bincode = ''
    opcode = ''
    i = ''
    l = inst.split()
    opcode += instructions[l[0]]
    if l[-1].isnumeric():
        i = '1'
    else:
        i = '0'
    if len(l) == 1:
        bincode += '0'*26
        bincode += i + opcode
        return bincode
    elif len(l) == 2:
        bincode += bin(int(l[1]))[2:].zfill(18)
        bincode += '0'*8
        bincode += i + opcode
        return bincode
    elif len(l) == 3:
        if l[-1].isnumeric():
            bincode += bin(int(l[2]))[2:].zfill(18)
        else:
            bincode += '0'*14
            bincode += bin(int(l[2][1:]))[2:].zfill(4)
        bincode += bin(int(l[1][1:]))[2:].zfill(4)
        bincode += '0'*4
        bincode += i + opcode
        return bincode
    else:
        if l[-1].isnumeric():
            bincode += bin(int(l[3]))[2:].zfill(18)
        else:
            bincode += '0'*14
            bincode += bin(int(l[3][1:]))[2:].zfill(4)

        bincode += bin(int(l[2][1:]))[2:].zfill(4)
        bincode += bin(int(l[1][1:]))[2:].zfill(4)
        bincode += i + opcode
    return bincode


def assemble():
    f = open('pystuff/input.txt', 'r')
    g = open('pystuff/output', 'w')
    g.write('v3.0 hex words addressed\n')
    count = 0
    st = f.readlines()
    sz = len(st)
    for line in st:
        g.write(hex(count)[2:].zfill(math.ceil(math.log(sz, 4))) +
                ': ' + encode(bin_to_hex(inst_to_bin(line))) + '\n')
        count += 4
    f.close()
    g.close()
