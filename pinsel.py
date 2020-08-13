import sys
pin_type = int(sys.argv[1])
pin_num = int(sys.argv[2])
bits = list(sys.argv[3])
if pin_type == 0:
    if pin_num<=15:
        indices = [2*pin_num , 2*pin_num+1]
        pinsel_num = 0
    else:
        indices = [2*pin_num , 2*pin_num+1]
        pinsel_num = 1
        
else:
    indices = [2*(pin_num-16) , 2*(pin_num-16)+1]
    pinsel_num = 2
    

bit_string  = "0"*32

bit_string = list(bit_string)


bit_string[indices[0]] = bits[1]
bit_string[indices[1]] = bits[0]

bit_string.reverse()
bit_string = "".join(bit_string)
bit_string = "0b" + bit_string
print(hex(int(bit_string,2)))
print("pinsel"+str(pinsel_num))
