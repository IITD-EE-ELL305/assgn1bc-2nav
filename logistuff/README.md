# Splitter.py

## Description
While doing this assignment, especially when creating the splitter for ```CTRL_ROM```, I found it to be somewhat irritating to set each bit manually when the adjacent bits were to be split in adjacent splits

So for the case which is usual, I created a splitter which takes in the number of bits to be split and the splits defined in a list. This creates a new logisim circuit in your project, given path of the project, and creates the splitter in the new circuit.

## Usage
1. Modify the variables in the ```main()``` function in [```splitter.py``](logistuff/splitter.py)` to suit your needs.
    - ```path``` is the path to your logisim project
    - ```incoming_bits``` is the number of bits to be split
    - ```split_list``` is a list of the splits to be made
2. Run the script
3. Reopen your logisim file, and you should see a new circuit created in your project with the splitter. Copy paste the splitter into your desired circuit.
3. Comment `line 14` (add_splitter(path, incoming_bits, split_list)) and uncomment `line 24` (# delete_circuit(path)) to delete the newly created circuit.

## Example
Let's take the case of our CTRL_ROM, we have 16 bits to be split into 3,1,1,1,1,1,1,4,1,1,1 bit splits. So we define the following variables in the ```main()``` function in [```splitter.py``](logistuff/splitter.py)
path = `simpleRISC_reduced.circ`, `incoming_bits = 16`, `split_list = [3,1,1,1,1,1,1,4,1,1,1]`

Then we run the script, and we get a new circuit in our project with the splitter. Copy paste the splitter into our CTRL_ROM circuit, and we're done!

This seems to be somewhat time consuming but I find it easier than setting each bit manually.

Also, the `none` values at the end of the splitter in case `sum(split_list) < incoming_bits` are not connected to anything, don't seem to be of much use, and this might be updated later.
