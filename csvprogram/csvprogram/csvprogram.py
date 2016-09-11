import csv
import numpy
from scipy import signal
import  matplotlib.pyplot as plt

path='C:\Users\Lu\Documents\csv'
read_in=path+'\csv1.csv'

result=numpy.genfromtxt(read_in,delimiter=',')
result.sort()
result2=numpy.dot(result,2)      
resultt=result.T
resultdot=numpy.dot(result,resultt)

write_out=path+'\csvt.csv'
numpy.savetxt(write_out,resultdot,delimiter=',')

result_d1p2=signal.savgol_filter(result,5,2,1,mode='mirror')
write_out=path+'\csv_d1p2.csv'
numpy.savetxt(write_out,result_d1p2,delimiter=',')

result_d2p2=signal.savgol_filter(result,5,2,2,mode='mirror')
write_out=path+'\csv_d2p2.csv'
numpy.savetxt(write_out,result_d2p2,delimiter=',')

result_d2p3=signal.savgol_filter(result,5,3,2,mode='mirror')
write_out=path+'\csv_d2p3.csv'
numpy.savetxt(write_out,result_d2p3,delimiter=',')

result_d3p3=signal.savgol_filter(result,5,3,3,mode='mirror')
write_out=path+'\csv_d3p3.csv'
numpy.savetxt(write_out,result_d3p3,delimiter=',')

#plt.figure()

plt.figure()
plt.plot(result.T,'*-')
plt.show()

plt.figure()
plt.plot(result_d1p2.T,'*-')
plt.show()

plt.figure()
plt.plot(result_d2p2.T,'*-')
plt.show()

plt.figure()
plt.plot(result_d2p3.T,'*-')
plt.show()

plt.figure()
plt.plot(result_d3p3.T,'*-')
plt.show()