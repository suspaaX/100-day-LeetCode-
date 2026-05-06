'''
q1.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''
nums  = [2,7,11,15]
target = 9
Output = [0,1]

# nums = [3,2,4]
# target = 6
# Output =  [1,2]

# nums = [3,3]
# target  = 6
# Output = [0,1]

def twoSum(nums,target) :
    nw_lst = []
    for i in nums:
        if i<target:
            nw_lst.append(i)

    idx = []
    total_sum = sum(nw_lst)
    if total_sum == target:
        for i in nw_lst:
            x = nw_lst.index(i)
            idx.append(x)
    print(idx)


# twoSum(nums,target)
