# TO-DO: Complete the selection_sort() function below 

def selection_sort(arr):
    for i in range(0, len(arr) -1):
        cur_index = i
        smallest_index = cur_index
        for j in range (cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
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




""" selection sort """ 
# swap value at the smallest index with our starting index 

# [1, 2, 3, 4]       [6, 4, 8, 4, 2 , 1, 9]
# sorted side         ^current        ^smallest




""" find the index of the smallest value """
for j in range (cur_index, len(arr)):
    if arr[j] < arr[smallest_index]:
        smallest_index = j

""" swamp the current index with the smallest index """

for i in range(0, len(arr) -1):
    cur_index = i
    smallest_index = cur_index
    arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


""" bubble sort """



"""largest values "bubble to the top" one by one  """

def bubble_sort(arr):
    swaps_occured = True
    while swaps_occured:
        print(arr)
        swaps_occured = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i] # SWAP from the right 
                swaps_occured = True 