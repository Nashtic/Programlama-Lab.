#Selahattin Ahmed Ataşoğlu Hafta 3 Yazılan Kodlar

list_1 = [0,5,25,100,5,5,0,100]

def my_h(list_1):
    my_d=dict() #{}
    for i in list_1:
        if i in my_d:
            my_d[i]=my_d[i]+1
        else:
            my_d[i]=1
    return my_d
print(my_h(list_1))


def lookup(d,v):
    for key in d:
        if d[key]==v:
            return key
        else:
            return -1
lookup(my_d,1)

#Fibonacci Recursive
n = int(input())
def fibo_rec(n):
    if n<2:
        return n
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)
fibo_rec(n)

#Diğeri

known={0:0,1:1}

def fibo_rec(n):
    if n in known:
        return known[n]
    else:
        result=fibo_rec(n-1)+fibo_rec(n-2)
        known[n]=result
        return result

from sympy import FiniteSet

s=FiniteSet(1,1.5,Fraction(1,5)) #aynı şeyleri tekrar yazsan da yazmaz çünkü küme elemanlarını yazıyor.
for member in s:
    print(member)

t=FiniteSet(Fraction(1,5),1.5,1,1)
if s==t:
    print("True")


list_1=[1,4,7,84,3,62,23]
my_d=dict()
my_d{1:"bir",2:2,"2":"three"}
print(my_d)
