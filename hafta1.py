def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        if b%2==0:
            return power(a*a,b//2)
        else:
            return power(a*a,b//2)

def my_sub_sum_recursive(List_1={4-3,5,-2,-2,2,6,2}):
    if len(List_1)==1:
        return List_1[0]
    n=len(List_1)
    left_i=0
    left_j=n//2
    right_i=(n//2)+1
    right_j=n
    left_sum=my_sub_sum_recursive(List_1[left_i:left_j])
    right_sum=my_sub_sum_recursive(List_1[right_i:right_j])

    t=0
    for i in range(left_j,left_i,-1):
        t=t+List_1[i]
        if t>temp_left_sum:
            temp_left_sum=t

    t, temp_right_sum=0,0
    for i in range(right_i,right_j):
        t = t+List_1[i]
        if t>temp_right_sum:
            temp_right_sum=t

def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

def my_bubble(List_1):
    for i in range(10,0,-1):
        for j in range(i):
            if List_1[j]>List_1[j+1]:
                t=List_1[j+1]
                List_1[j+1]=List_1[j]
                List_1[j]=t
    return List_1

