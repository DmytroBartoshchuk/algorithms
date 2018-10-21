# binary search

our_list = [1,2,3,4,5,6,8,9,10,7]

sorted_list = sorted(our_list)
print(sorted_list)


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    print(low)
    print(high)

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        print('mid={}'.format(mid))
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1


print(binary_search(sorted_list, 1))