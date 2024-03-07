from helperfunctions import *

def approxadd1(a:int, b:int, cin:int):
    cout = (a & b) | (cin & (a | b))
    result = ~cout
    return limitlen(result, 1), limitlen(cout, 1)

if __name__ == "__main__": 
    path = os.path.join('hw', 'verification', 'testData', 'approxadd_data.txt')
    with open(path, 'w') as file:
        for i in range(2**3): # generates truth table for 1 bit approx adder
            cin = (i & 0b100) >> 2
            b = (i & 0b010) >> 1
            a = i & 0b001
            out, cout = approxadd1(a, b, cin)
            data = f'{a:b}{b:b}{cin:b}{out:b}{cout:b}\n'
            file.write(data)
