def find_smallist(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        #如果要大到小排序 就是> ;如果要小到大排序 就是<
        if arr[i] > smallest:      
           smallest = arr[i]
           smallest_index = i
    return smallest_index

def select_sort(arr):
    new_list = []
    for i in range(len(arr)):
        smallest_index = find_smallist(arr)
        new_list.append(arr.pop(smallest_index))
    return new_list
##########################
print(select_sort([3,5,87,95,42,46,2,48,6,21,8565,0]))