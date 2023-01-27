import multiprocessing as mp
#print(mp.cpu_count())
from time import perf_counter
import math

result1=[]
result2=[]
def cal_one(number):
    for i in number:
        result1.append(math.sqrt(i**3))
def cal_two(number):
    for i in number:
        result2.append(math.sqrt(i**5))

if __name__=='__main__':
    start=perf_counter()
    numlist=list(range(200000))
    p1=mp.Process(target=cal_one,args=(numlist,))
    p2=mp.Process(target=cal_two,args=(numlist,))
    p1.start()
    p2.start()
    end=perf_counter()
    print(f'{end-start} secounds taken')