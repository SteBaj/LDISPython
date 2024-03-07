from goldenmodel import *

n16 = 3
n8 = 2
n4 = 0

if len(argv) == 5: # 4 parameters must be given, test vector size, N16, N8, N4, argv[0] is reserved
    test_vec_size = int(argv[1])
    n16=int(argv[2])
    n8=int(argv[3])
    n4=int(argv[4])
    print("Input parameters received\n")

N_[16] = n16
N_[8] = n8
N_[4] = n4

path = os.path.join('sw', 'testData', 'error_test.txt')
with open(path, 'w') as file:
    file.write("#N16=" + str(n16) + "  N8=" + str(n8) + "  N4="+ str(n4) + "\n")
    file.write("#A\tB\tresult\n")
    stepsize = int(round((2**16/100)))
    for i in range(100):
        A = i*stepsize
        for j in range(100):
            B = j*stepsize
            result = approxmulN(A, B, 16)
            data = f'{A:>2}\t{B:>2}\t{result:>2}\n'
            file.write(data)

    