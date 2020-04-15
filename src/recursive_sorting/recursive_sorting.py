def merge_sort(arr):
    if len(arr) > 1:
        midpoint = len(arr)//2
        A = arr[:midpoint]
        B = arr[midpoint:]
        merge_sort(A)
        merge_sort(B)
        
        x=y=0
        
        for z in range(0, len(arr)):
            if x >= len(A):
                arr[z] = B[y]
                y+=1
            elif y >= len(B):
                arr[z] = A[x]
                x+=1
            elif A[x] < B[y]:
                arr[z] = A[x]
                x+=1
            elif A[x] >= B[y]:
                arr[z] = B[y]
                y+=1
                
    return arr 



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
