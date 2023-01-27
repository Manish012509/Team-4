from threading import *
import time

def double(num):
    for n in num:
        time.sleep(2)
        print(2*n)
def square(num):
    for n in num:
        time.sleep(2)
        print(n *n)
n=[1,2,3,4,5]
begintime=time.time()
t1=Thread(target=double,args=(n,))
t2=Thread(target=square,args=(n,))
t1.start()#It will get t1 and t2 as a output
t1.join()
t2.start()
t2.join()
endtime=time.time()
print(endtime-begintime)