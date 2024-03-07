from helperfunctions import *
from approxadd1 import *

def approxaddN(a:int, b:int, N:int): 
    cin = [0] * (N+1)
    out = [0] * N
    cin[0] = 0
    for i in range(N):
        out[i], cin[i+1] = approxadd1(get_bit(a,i), get_bit(b,i), cin[i])
    approxRes = binary_array_to_int(out)
    return ((a >> N) << N) + ((b >> N) << N) + cin[N] * 2**N + approxRes

if __name__ == "__main__": 
    test_vec_size = 100
    bits_approx = 2
    in1, in2 = generate_input_vectors(test_vec_size, 8)
    path = os.path.join('hw', 'verification', 'testData', 'approxaddN_data.txt')
    with open(path, 'w') as file:
        for i in range(test_vec_size):
            result = approxaddN(in1[i], in2[i], bits_approx)
            result = limitlen(result, 8)    
            data = f'{in1[i]:08b}_{in2[i]:08b}_{result:08b}\n'
            file.write(data)
