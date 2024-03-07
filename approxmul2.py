from helperfunctions import *

def approxmul2(a0:int, a1:int, b0:int, b1:int):
    out0 = (a0 & b1) & (a1 & b0)
    out1 = (a0 & b1) ^ (a1 & b0)
    out2 = out0 ^ (a1 & b1)
    out3 = out0
    out = 0
    out = set_bit(out, 0, out0)
    out = set_bit(out, 1, out1)
    out = set_bit(out, 2, out2)
    out = set_bit(out, 3, out3)
    return out

if __name__ == "__main__": 
    path = os.path.join('hw', 'verification', 'testData', 'approxmul2_data.txt')
    with open(path, 'w') as file:
        for i in range(2**4): # generates truth table for 2 bit approx multiplier
            b1 = (i & 0b1000) >> 3
            b0 = (i & 0b0100) >> 2
            a1 = (i & 0b0010) >> 1
            a0 = i & 0b0001
            out = approxmul2(a0, a1, b0, b1)
            data = f'{a1:b}{a0:b}{b1:b}{b0:b}{out:04b}\n'
            file.write(data)