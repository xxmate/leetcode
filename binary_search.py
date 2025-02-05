def binary_search(list, item):
    left = 0
    right = len(list)-1

    while left <= right:
        mid = (left + right) // 2
        if item == list[mid]:
            return mid
        if item < list[mid]:
            right = mid - 1
        else:
            left = mid + 1

a = [1,5,7,8,9,11,17,29,30]
print(a)
print("I'm trying to get the index of value 17....so let's use binary_search algorithm binary_search(a, 17)")
result = binary_search(a, 17)
print(result)

