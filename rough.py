# num = [5]

# def all_num(num):
#     for i in range(0,num[0]):
#         yield i

# print(all_num(num))


# num = [1,4,7,9]
# target  = 1

# if target not in num:
#     print('yes')

# else:
#     print('no')

# num = [0,1,3,5]

# num = [0,0,0]

# for i,v in enumerate(num):
#     print(i)


nums = [1,2,3,4]

for i in range(len(nums)-1):
    print(nums[i:i+2])
