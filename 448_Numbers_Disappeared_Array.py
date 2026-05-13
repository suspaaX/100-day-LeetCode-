'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

'''


# nums = [1,1]
# Output =  [2]

# nums = [2,2]
# Output =  [1]


# nums = [3,4]
# Output =  [1,2]

# nums = [1,1,2,2]
# output = [3,4]

nums = [4,3,2,7,8,2,3,1]
Output =  [5,6]



def findDisappearedNumbers(nums):
    fnum = nums[0]
    lnum = nums[-1]
    nums_len = len(nums)

    if nums_len == 2 and 1 not in nums and nums[0] == fnum and nums[-1] == fnum:
        return [1]
    
    elif nums_len == 2 and nums[0] == 1 and nums[-1] == 1:
        return [2]
    
    elif nums_len>2 :
        nums.sort()
        new_nums = []
    
        for i in range(1,nums_len+1):
            new_nums.append(i)
            result = set(new_nums) - set(nums)
            return (list(result))
     
    # nums.sort()
    # new_nums = []
    # for i in range(1,nums[-1]+1):
    #     new_nums.append(i)
    # result = set(new_nums) - set(nums)

    return (list(result))



print(findDisappearedNumbers(nums))