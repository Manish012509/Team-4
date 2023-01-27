from threading import *
import time
l=Lock()
'''
def wish(name):
    for i in range(10):
        print("Good evening",end='')
        time.sleep(2)
        print(name)
t1=Thread(target=wish,args={'Manish'})
t2=Thread(target=wish,args={'Mart'})
t1.start()
t2.start()
'''

'''
def wish(name):
    l.acquire()
    for i in range(10):
        print("Good Morning",end=' ')
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args={'Manish'})
t2=Thread(target=wish,args={"Rohan"})
t3=Thread(target=wish,args={"Sam"})
t1.start()
t2.start()
t3.start()
#t1.join(2)#Join will take secounds and after that it will go to the next thread after completing the sec
'''
s=Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(10):
        print("Good Morning",end=" ")
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args=('Manish',))
t2=Thread(target=wish,args=('Ama',))
t3=Thread(target=wish,args=('Josh',))
t4=Thread(target=wish,args=('Samuil',))
t5=Thread(target=wish,args=('Pop',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
