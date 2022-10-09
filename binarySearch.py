
# Binary search algorithm 
# runtime complexity O(log n)


def binary_search(nums, target):
    first = 0
    last = len(nums) - 1
    while first <= last:
        middle = last + first // 2
        if nums[middle] == target:
            return middle
        else:
            if nums[middle] < target:
                first = middle + 1
            else:
                last = middle -1
    return -1
        

