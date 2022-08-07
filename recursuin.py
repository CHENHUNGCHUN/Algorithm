#1.遞迴簡單將數字print出來
def countdown(i):
    print(i)
    if i <= 1:
        return
    countdown(i-1)
#####################
countdown(600)

#2.用遞迴寫出階層
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
##################################
print(fact(30))

#3.(自己) 用遞迴寫加總
def sum_recur(list):
    if list == []:
        return 0
    else:
        a= list.pop()
        return a + sum_recur(list)
###############################
print(sum_recur([1,2,68,41,56,2,4,5,3]))

#3.(書) 用遞迴寫加總
def sum_recur_book(list):
    if list == []:
        return 0
    else:
        return list[0]+sum_recur_book(list[1:])
###############################

#4.用遞迴寫每個階層的list長度
def lens_list(list):
    if list == []:
        return 0
    else:
        return 1+lens_list(list[1:])
###############################
print(lens_list([1,2,68,41,56,2,4,5,3]))
        
#5.用遞迴寫最大值
def max_list(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1] 
    else:
        return list[0] if list[0] > max_list(list[1:]) else max_list(list[1:])
##############################
print(max_list([1,2,68,41,56,2,4,5,3]))

#6.用遞迴排序(快速排序法)
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        povit = arr[0]
        greater = [i for i in arr[1:] if i > povit]
        less = [i for i in arr[1:] if i <= povit]
        return quicksort(less) + [povit] + quicksort(greater)
##############################
print(quicksort([1,2,68,41,56,2,4,5,3]))