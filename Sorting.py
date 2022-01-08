def exch(list,i,j):
    (list[i],list[j]) = (list[j],list[i])
    return list

def selection_sort(list,compare):
    for i in range(len(list)):
        minimum = i
        for j in range(i+1,len(list)):
            if compare(list[minimum],list[j]) > 0:
                minimum = j
        list = exch(list,i,minimum)
    return list

def insertion_sort(list,compare):
    for i in range(len(list)):
        for j in range(i,0,-1):
            if compare(list[j-1],list[j]) > 0:
                list = exch(list,j-1,j)
    return list

def merge_sort(arr,compare):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid],compare)
    high_arr = merge_sort(arr[mid:],compare)
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if compare(low_arr[l],high_arr[h])<=0:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def quick_sort(arr,compare):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if compare(num,pivot)<0:
            lesser_arr.append(num)
        elif compare(num,pivot)>0:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)