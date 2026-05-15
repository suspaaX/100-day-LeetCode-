'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
# nums =[3,3,4]
# Output =  3

# nums = [3,2,3]
# Output = 3

nums = [2,2,1,1,1,2,2]
Output =  2

# nums = [2,4,4,3]
# Output = 3



def majorityElement(nums) :
    my_dict = {}
    for i in nums:
        x = nums.count(i)
        my_dict.update({i:x})

    print(my_dict)
    # majority = max(my_dict,key=my_dict.get)
    # return (majority)
 

print(majorityElement(nums))