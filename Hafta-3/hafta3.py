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

my_d =dict()

my_d ={1:3,2:5,6:8}

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
