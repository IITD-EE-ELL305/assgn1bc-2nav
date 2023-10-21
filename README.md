# Design the microarchitecture for a SimpleRISC CPU that implements a subset of instructions that we studied in the class.

## Here are the specifications for the ISA

- 32 bit instructions and data
- 16 registers
- The following instructions will be supported (see opcodes from Sarangi pg. 112):
  - add reg, reg, (reg/imm)
  - sub reg, reg, (reg/imm)
  - cmp reg, (reg/imm)*** (store it in a 1-bit 'flags' register for easy implementation later on)
  - **ld reg, imm[reg]**
  - **st reg, imm[reg]**
  - **beq label**
  - **call label**
  - **ret**
  - **nop**
  - **halt**
- The instruction formats (branch, register and immediate) are summarized on Sarangi pg. 118 Table 3.11. Use that for the definition of the different fields within the instruction.

## Instructions

You have two options:
1. You can continue with the same circuit that you built for assignment 1a
   It is recommended to avoid this option because the circuit in option 2 below is already organized to be more friendly for this assignment. But you can still continue with your own circuit from 1a, and you will have to work a little harder to implement everything in this assignment.
3. You can clone this repository and use it as a starter circuit  
   This circuit is the same as what was created in the tutorials, but the different parts have been rearranged to make it look nice. It has been tested to work properly, so you may want to use it as a starting point. All tutorials for assignment 1b will use this circuit as a starting point.

We have made it easier to keep track of different register values when you test and debug the circuit.

You will find some new components on the left that you will use for this assignment. Basically we separated the control circuit from the datapath, and you will find two control circuits: ctrl_combi and ctrl_rom. You will also find a keyboard and a TTY component.

The datapath now looks similar to the one we see in the slides. The control signals are seen at the bottom. You will have to add more of the control signals here as you do the assignment.  
The CTRL_COMBI circuit is where the control circuit is actually implemented, instead of implementing it in the same 'main' circuit. When you add more control signals, you will have to modify:
1. The "connections to control unit" box to add more signals in CTRL_COMBI (just follow the convention that you will already see in the box)
2. The actually circuit to generate the control signals in CTRL_COMBI
3. Add the modified CTRL_COMBI to main and connect the correct control signals to the correct pins

This will make the later part of this assignment easier for you.

## Assignment 1b (Due date: 28/10/2023)

1. Implement the load and store instructions
- [ ] load
  - [ ] Add a data memory (DMEM) to load (store) data from (to)
  - [ ] Connect the output from ALU to the address bus of the data memory
  - [ ] You want to write back the data from that address, so you will have to add a Mux with ALU and DMEM_R_data as inputs and add an appropriate control signal to choose which one to write back
  - [ ] Appropriately modify the writeback path
  - [ ] **Commit and push to Github with message "load instruction"**
- [ ] store
  - [ ] To store rd data into memory, it has to be connected to the write port of DMEM
  - [ ] Provide appropriate control signal to correctly enable DMEM memory write for store instruction
  - [ ] Modify the control circuit to generate the control signal, and the main circuit to use the modified control circuit
- [ ] Test
  - [ ] Store some data to DMEM using the store instruction and see the contents of DMEM to check if it is there
  - [ ] Load data from the same location into a register (choose form among the first 5 registers in regfile)  
        *Checking register values: Under the 'Simulate' menu you will find "Timing diagram". Open that and click on the 'Add or remove signals' button. Expand "REGFILE" and select r1...r5 (whichever register you stored to). Now when you simulate, you can directly see the value of the registers at each time step.
  - [ ] **Commit and push to Github with message "store instruction"**
2. Add support for branch and call instructions
- [ ] We will only implement the _beq_ instruction in a slightly simplified format:  
      Use only the last 18 bits as the offset (same as for load and store). That way you do not need to modify the immediate generation circuit.
  - [ ] For branching, the PC has to be added to the _imm_ (add appropriate wires to send PC to ALU_X through a Mux
  - [ ] Add the corresponding control signal
  - [ ] Take the ALU output and put it back into PC through a Mux
  - [ ] Add the correct control signal depending on the Flags register to choose the correct input to PC
- [ ] Test
  - [ ] Load some value to two registers
  - [ ] Run the compare instruction to compare them and save the result in the Flags register
  - [ ] Run the branch instruction to make the PC jump to a positive and negative offset
  - [ ] You can simply check the value of _PC_ to see if your circuit works correctly
  - [ ] **Commit and push to Github with message "beq instruction"**
- [ ] call instruction
  - [ ] Add the _ra_ register which will hold PC+4; The remaining hardware is the same as for branch
  - [ ] Add appropriate control signals to enable write to _ra_ and choose the new _PC_
- [ ] ret instruction
  - [ ] You simply have to load _ra_ into PC, so add a connection from output of _ra_ tp input of _PC_ through the Mux (you will have to expand the Mux and modify the control signals)
- [ ] Test
  - [ ] Load 2 numbers in the regfile, then call a function that will add them and store result in regfile and return, then store that result in data memory
  - [ ] Check data memory for the correct result, and also verify that the PC behaves correctly through the call and return instructions
  - [ ] **Commit and push to Github with message "call and ret instructions"**
3. Add support for _nop_ and _halt_ instructions
- [ ] Do you need any hardware modification?
- [ ] Modify the control signals appropriately for _nop_
- [ ] With the _halt_ instruction, the _PC_ stops incrementing. Do you need hardware modification?
- [ ] Add appropriate control signals
- [ ] **Commit and push to Github with message "halt and nop instruction"**
- [ ] Write a small test program for all your instructions:
  - [ ] Load two numbers into r1 and r2
  - [ ] Add the two numbers and store result in r3
  - [ ] Compare that with your 'manual' addition (supplied as an _imm_ to _cmp__
  - [ ] If result is correct write 0x0 to r4 and skip next instruction; else branch to the next instruction and write 0xFFFFFFFF (all 1s) to r4
  - [ ] Call a new function that stores the value from r4 to the data memory
  - [ ] Return from the call
  - [ ] Load value from data memory to r5
  - [ ] Halt the CPU
  - [ ] Check values of all relevant registers to ensure that the CPU is working as expected
- [ ] **Commit and push to Github with message "assignment 1b final" only once you are fully sure and do not make edits after this**
     
  **End of assignment 1b. Due date: 28/10/2023**

## Assignment 1c (Due date: 4/11/2023)

4. Implementing a ROM based controller  
   In this part, you will implement a ROM based controller instead of the combinational controller from previous assignments
- [ ] Copy the "Connections to control unit" box fully from CTRL_COMBI to CTRL_ROM. These are just the input and output pins that appear on the device when you add it to the main circuit.
- [ ] Add a ROM memory to the CTRL_ROM circuit
- [ ] The address length of the ROM will be same as total number of input bits to the control circuit
- [ ] The data length of ROM will be the total number of output bits from the control unit (rounded to a full byte; ignoring the extra bits you needed to add for rounding)
- [ ] For each instruction in the list above, write down the control word values, encode them into little-endien hex and add it at the correct ROM address
- [ ] Test your previous program without any modifications. It should work.
- [ ] **Commit and push to Github with message "ROM controller"**
- [ ] Now we will see how easy it is to add new instructions to the ROM based controller:
  - [ ] Add instructions for and, or by simply generating the control word and putting it into the ROM
  - [ ] Think of other instructions you can implement without hardware modifications!
5. Adding input and output devices
- [ ] The MMAPPED_IO circuit component contains a keyboard and TTY (text terminal) that you will use, so add it to the circuit
- [ ] Connect the Address, Data In and Data Out busses appropriately
      Functioning of the devices:
      Both devices have a control register and data register; and the keyboard has a status register also. The details are as follows:
      - Keyboard status register address: 0x00000400 (only bit 0 of the status register is useful; indicating the availability of new data)
      - Keyboard control register address: 0x00000404 (only bit 0 is useful; setting it to 1 will empty the keyboard buffer)
      - Keyboard data register: 0x00000408 (lowest 7 bits encode character in ASCII format)
      - TTY control register: 0x0x00000804 (1 on bit 0 clears the screen; all other bits are unassigned)
      - TTY data register: 0x00000808 (accepts 7 bit ASCII data; all higher bits are ignored)
- [ ] Test
  - [ ] Clear the keyboard buffer
  - [ ] In a for loop, wait for a new character; read it when it becomes available from keyboard and print it out to the TTY, for 10 iterations
  - [ ] Clear the display
  - [ ] **Commit and push to Github with message "added mmapped io"**

End of assignment 1c. Congratulations! You now have a very fancy CPU that can do most things you may want to!
**Due date: 4/11/2023**

## Optional
- [ ] Add support for 'greater than' in comparison in addition to equal (the ALU and flags will need a small modification)
- [ ] Write an assembler in python (convert assembly instructions to machine language)
- [ ] Write a program to read a string of characters up to a newline and print it out in reverse
- [ ] Write a program to take in a string like `13 + 634`, `27 / 3`, identifies the correct operation and prints out the result.
- [ ] What other fancy programs can you write for your CPU+Kbd+TTY with your assembler? If you have working solutions, share them with the class!
- [ ] **Commit and push to Github with message "fancy PC"**. You might want to add some documentation about what your program does, how to use it etc.
