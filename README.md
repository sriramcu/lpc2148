# lpc2148  

This repository consists of programs to help in coding an LPC 2148. As of now, the following programs are present:

## 1. 7 segment display  
This program shows the register content for a desired character for a common anode, active low seven segment display. maze_solver.py is a module imported in 7seg.py which shows the character created and prints register content on STDOUT. To create your own character, go to 7seg.py and under the comment 'INSERT SEGMENTS BELOW', erase the positions pre made and make yor own, like mid(pos) for middle segment etc.
I made maze_solver.py for solving mazes in the following repo: https://github.com/sriramcu/maze_solver.  

## 2. PINSEL register

This program accepts IOPIN number and selection and outputs the PINSEL register to be used and the value stored in that register.  
#### Usage
`py pinsel.py <pin_type> <pin_num> <bits>`  
where pin_type is 0 or 1, corresponding to IO0PIN AND IO1PIN;  
pin_num is 0 to 31 for IO0PIN and 16 to 31 for IO1PIN;  
bits are 00,01,10,11 based on selection of GPIO(eg 11 for ADC, etc).  
