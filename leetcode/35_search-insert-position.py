'''
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

nums = [1, 3, 5]
target = 3

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if target == nums[mid]:
        print(mid)
        break
    if target > nums[mid]:
        left = mid + 1
    if target < nums[mid]:
        right = mid - 1
else:
    print(left)

