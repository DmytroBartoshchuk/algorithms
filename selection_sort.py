# selection sort

our_list = [1,2,3,4,5,6,8,9,10,7]


def find_smallest(array):
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        # print(i)
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i

    return smallest_index


def selection_sort(array):
    newArr = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        newArr.append(array.pop(smallest))
    return newArr


print(selection_sort(our_list))
