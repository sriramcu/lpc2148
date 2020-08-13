import maze_solver as ms
from matplotlib import pyplot as plt

#common anode; active low
config = {'tp':0,'btm':3,'mid':6,'lb':4,'rb':2,'lt':5,'rt':1}

def top(positions=[]):
    ms.ph(1,3,5)
    positions.append(config['tp'])
    
def btm(positions=[]):
    ms.ph(1,3,1)
    positions.append(config['btm'])
    
def mid(positions=[]):
    ms.ph(1,3,3)
    positions.append(config['mid'])
    
def lb(positions=[]):
    ms.pv(1,1,3)
    positions.append(config['lb'])
    
def rb(positions=[]):
    ms.pv(3,1,3)
    positions.append(config['rb'])
    
def lt(positions=[]):
    ms.pv(1,3,5)
    positions.append(config['lt'])
    
def rt(positions=[]):
    ms.pv(3,3,5)
    positions.append(config['rt'])

if __name__=='__main__':
    pos = []
    bit_string = list('11111111') #active low
    
    #INSERT SEGMENTS BELOW
    lt(pos)
    lb(pos)
    rt(pos)
    mid(pos)
    rb(pos)
    #SEGMENTS COMPLETED
    for p in pos:
        bit_string[p] = '0'
    bit_string.reverse()
    bit_string = "".join(bit_string)
    bit_string = "0b" + bit_string
    print(hex(int(bit_string,2)))
    plt.axis('scaled')
    plt.show()
