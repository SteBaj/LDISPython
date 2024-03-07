import os
from sys import argv
import random

from helperfunctions import *
from approxadd1 import *
from approxaddN import *
from approxmul2 import *

debug = False # if true, prints the truth tables of the functions

test_vec_size = 100
n16=13
n8=14
n4=3


filenamemodifier = ""
if len(argv) == 5: # 4 parameters must be given, test vector size, N16, N8, N4, argv[0] is reserved
    test_vec_size = int(argv[1])
    n16=int(argv[2])
    n8=int(argv[3])
    n4=int(argv[4])
    print("Input parameters received\n")

if len(argv) == 6: # 4 parameters must be given, test vector size, N16, N8, N4, argv[0] is reserved
    test_vec_size = int(argv[1])
    n16=int(argv[2])
    n8=int(argv[3])
    n4=int(argv[4])
    filenamemodifier = argv[5]
    print("Input parameters and filename received\n")

test1 = 100
test2 = 100
testresult = approxaddN(test1, test2, 12)
if debug:
    print(test1, "+", test2, "~", testresult,  bin(test1), bin(test2), bin(testresult))
    print("here" + bin(binary_array_to_int([0,1])))


N_ = {16: n16, 8: n8, 4: n4}

def approxmulN(a:int, b:int, N:int):
    if N % 2 != 0:
        raise ValueError("N is odd, this shouldn't happen")
    if a.bit_length()>N or b.bit_length()>N:
            print("\n here\n")
            print(a, b)
            raise ValueError("Values too long!")
    a0, a1 = split_bits(a, int(N/2))
    b0, b1 = split_bits(b, int(N/2))
    if N == 2:
        
        return approxmul2(a0, a1, b0, b1)
    
    HH = approxmulN(a1, b1, int(N/2))
    HH = HH << int(N)

    HL = approxmulN(a1, b0, int(N/2))
    HL = HL << int(N/2)

    LH = approxmulN(a0, b1, int(N/2))
    LH = LH << int(N/2)

    LL = approxmulN(a0, b0, int(N/2))
    LL = LL

    LL_LH = limitlen(approxaddN(LL, LH, N_[N]), 2*N)
    HL_HH = limitlen(approxaddN(HL, HH, N_[N]), 2*N)
    result = limitlen(approxaddN(LL_LH, HL_HH, N_[N]), 2*N)
    return limitlen(result, 32)
# in1 = 50000
# in2 = 45000
# result=approxmulN(in1, in2, 16)
# print(in1, "*", in2, "~" , result, bin(in1), "*", bin(in2), "~", bin(result))
if __name__ == "__main__":
    in1, in2 = generate_input_vectors(test_vec_size, 16)
    path = os.path.join('hw', 'verification', 'testData', 'approxmulN_data' + filenamemodifier + '.txt')
    with open(path, 'w') as file:
        for i in range(test_vec_size):
            result = approxmulN(in1[i], in2[i], 16)
            #print(f"{in1[i]} * {in2[i]} = {result}")
            # data = f'{a1:b}{a0:b}{b1:b}{b0:b}{out:04b}\n'
            data = f'{in1[i]:016b}{in2[i]:016b}{result:032b}\n'
            file.write(data)


