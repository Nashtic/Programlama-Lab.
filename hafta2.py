import sys

liste_1=[4,-3,5,-2,-1,2,6,-2]
max_1=0
for i in range(8):
    for j in range(i,8):
        t=0
        for k in range(i,j):
            t=t+liste_1[k]
        if max_1<t:
            max_1=t
            i_1,i_2=i,j
print(max_1,i_1,i_2)

list_1=[4,-3,2,1,-2,6,-2]
n=len(list_1)
maxSum=0
for i in range(n):
    for j in range(i,n):
        #print(i,j)
        t=0
        for k in range(i,j):
            t=t+list_1[k]
        if(t>maxSum):
            maxSum=t
print(maxSum)

def my_f_1(list_1=[4,-3,5,-2,-1,2,6,-2]):

    n = len(list_1)
    maxSum=0
    for i in range(n):
        for j in range(i,n):
            #print(i,j)
            t=0
            for k in range(i,j):
                t=t+list_1[k]
            if(t>maxSum):
                maxSum=t
    return maxSum
my_f_1([4,-3,5,-2,-1,2,6,-2,4,-3,5,-2,-1,2,6,-2])

def my_f_2(list_1=[4,-3,5,-2,-1,2,6,-2]):

    n=len(list_1)
    maxSum=0
    for i in range(n):
        t=0
        for j in range(i,n):
            #print(i,j)
            t=t+list_1[k]
        if(t>maxSum):
            maxSum=t

    return maxSum
my_f_2([4,-3,5,-2,-1,2,6,-2,4,-3,5,-2,-1,2,6,-2])

def my_f_3(list_1=[4,-3,5,-2,-1,2,6,-2]):
    n=len(list_1)
    if(n==1):
        return list_1[0]
    left_i=0
    left_j=n//2

    right_i=n//2
    right_j=n

    left_sum=my_f_3(list_1[left_i:left_j])
    right_sum=my_f_3(list_1[right_i:right_j])

    temp_left_sum=0
    t=0
    for i in range(left_j-1,left_i-1,-1):
        t=t+list_1[i]
        if(t>temp_left_sum):
            temp_left_sum=t

    temp_right_sum=0
    t=0
    for i in range(right_i,right_j):
        t=t+list_1[i]
        if(t>temp_right_sum):
            temp_right_sum=t

    center_sum=temp_left_sum+temp_right_sum

    return max_of_three(left_sum,right_sum,center_sum)


def insertionSort(arr):                 """Insertion Sort Func"""

n = len(arr)
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= and key < arr[j]
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = key


def shellSort(arr):                     """Shell Sort Func"""

n = len(arr)
gap = n // 2
while gap > 0:
    for i in range(gap, n):
        temp = arr[i]
        j = i
        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j = j - gap
            arr[j] = temp
            gap //= 2



Dizi_1 = [64, 25, 12, 22, 11]            """Selection Sort Func"""

for i in range(len(Dizi_1)):

    min_value = i
    for j in range(i + 1, len(Dizi_1)):
        if Dizi_1[min_value] > Dizi_1[j]:
            min_value = j

    Dizi_1[i], Dizi_1[min_value] = Dizi_1[min_value], Dizi_1[i]

print("Sıralanmış Dizi")
for i in range(len(Dizi_1)):
    print("%d" % Dizi_1[i])