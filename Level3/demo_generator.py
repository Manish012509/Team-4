def demo():
    yield 'a'
    yield 'b'
    yield 'c'

d=demo()
print(next(d))
print(next(d))
print(next(d))
#print(next(d))
print(d)

#num=[x*x for x in range(1000)]
num = (x * x for x in range(1000))
print(next(num))
print(next(num))
print(num)

