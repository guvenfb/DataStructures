# first, the selection sort


# swapping function
def swap(arr, swap_i, with_j):
    temp = arr[swap_i]
    arr[swap_i] = arr[with_j]
    arr[with_j] = temp  # no need to return it, it's mutable


def selection_sort(array):
    N = len(array)

    for i in range(N):  # for each element in array
        min_val = array[i]  # temp for min value
        min_index = i
        for j in range(i+1, N, 1):  # start from i
            if array[j] < min_val:
                min_val = array[j]
                min_index = j

        swap(array, i, min_index)  # no need to return in array, as array is a list and hence it is mutable
    # return array not needed due to mutability

def insertion_sort(array):
    n = len(array)

    for i in range(1, n, 1):  # start from the second element
        for j in range(i, 0, -1):  # start from i and go back to 0
            if array[j] < array[j-1]:
                swap(array, j, j-1)
            else:
                pass
                #  break   # <-- breaking is better, because we know that the previous entries are already sorted; no need to go down to 0 on j

def bubble_sort(array):

    n = len(array)
    number_of_swaps = 0
    for i in range(n):
        number_of_inner_swaps = 0
        for j in range(n-1):
            if array[j] > array[j+1]:
                swap(array,j,j+1)
                # print(array)
                number_of_swaps += 1  # increment the swap count
                number_of_inner_swaps += 1

        if number_of_inner_swaps == 0:
            break
    return number_of_swaps

'''
my_arr = [1,2,4,5,3,7,6,11,9]
print(selection_sort(my_arr))
print(my_arr)
my_arr = [1,2,4,5,3,7,6,11,9]
insertion_sort(my_arr)
print(my_arr)
'''
my_arr = [3,2,1]
print(bubble_sort(my_arr))

