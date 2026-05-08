
'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

'''



# nums = [2,2,1]


# Output: 1

# nums = [1]

# Output: 1


# nums = [4,1,2,1,2]
# Output: 4

# def singleNumber(nums):

#     all_elem = {}
#     for i in nums:
#         elem = nums.count(i)
#         all_elem.update({i:elem})
#         key = all_elem.keys()
#         val = all_elem.values()

#     print(all_elem)




# singleNumber(nums)          