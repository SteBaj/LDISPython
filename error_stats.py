from goldenmodel import *

# statistics
# in case smaller output file is wanted
N16s=[30, 15, 10, 5, 2, 0]
N8s=[15, 10, 5, 2, 0]
N4s=[7, 4, 2, 0]
#

path = os.path.join('sw', 'testData', 'error_stats.txt')
with open(path, 'w') as file:
    file.write("#N16\tN8\tN4\tError Rate\tMean Error\n")
    for N16_ in range(32+1):
        N_[16]=N16_
        for N8_ in range(16+1):
            N_[8]=N8_
            for N4_ in range(8+1):
                N_[4]=N4_
                MeanError = 0
                ErrorCount = 0
                ErrorRate = 0
                for i in range(test_vec_size):
                    if N16_ == 31 and N8_ == 15 and N4_==7:
                            1+1 
                    resultApprox = approxmulN(in1[i], in2[i], 16)
                    resultExact = in1[i]*in2[i]
                    MeanError += abs(resultApprox-resultExact)*100/(test_vec_size*resultExact)
                    if resultApprox != resultExact:
                        ErrorCount+=1
                ErrorRate=ErrorCount*100/test_vec_size
                data = f'{N16_:>2}\t{N8_:>2}\t{N4_:>2}\t{round(ErrorRate,2):>5}\t{round(MeanError,2)}\n'
                file.write(data)
