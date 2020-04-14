# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    i = 0 
    for i in range(0, len(arr)):
        j = 1
        for j in range(0, len(arr)):
            if j > 0 and arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            j -= 1 
        i += i 
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a 

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr