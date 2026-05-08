'''

268. Missing Number

Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

'''

# nums = [3,0,1]

# Output: 2

nums = [9,6,4,2,3,5,7,0,1]

# Output: 8

# nums = [0,1]

# Output: 2

# nums = [3]

Output: 0
        
# nums = [2]

# Output: 1

# nums = [1,2]

# Output: 0

def missingNumber(nums):
    if len(nums) == 1 and nums[0] == 0:
        return 1

    elif len(nums) == 1 and nums[0]>=1:
        desr_num = nums[0]
        # print(desr_num)
        result = []
        for elem in range(0,desr_num):
            result.append(elem)
   
        for el in result:
            return el
        
    elif len(nums)>=2:
        (nums.sort())
        fnum = nums[0]
        lnum = len(nums)

        num2 = []
        for i in range(0,lnum+1):
            num2.append(i)
        x = set(num2)-set(nums)
        
        for k in x:
            return k

print(((missingNumber(nums))))

