'''
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''
# x = -123
# Output =  -321

x = 123
Output: 321

# x = 120
# Output: 21

# x = 0
# # Output: 0

# x = -10
# Output: 0

# x = 324351
# Output: 0

# x = 153423
# Output: 0

# x = (-2147483648)
# Output: 0

# x = -8463847412
# Output: 0



def reverse(x): 
        nw_var = str(x)
        x2 = (nw_var[::-1])
        
        if x < -(2**31) or x > (2**31)-1: return 0
        elif x < -(2**31) or x > (2**31)-1: return 0
        elif x2[0] == '0': return int(x2[1:])
        elif x2[-1] == '-': return int('-' + x2[0:-1])
        elif len(x2) == 1: return int(x2[:])
        else : return int(x2)
        
        #     return 0
        
 
        





        
        # elif x2[-1] == '-':
        #     return int('-' + x2[0:-1])

        # elif x2[0] == '0':
        #     return int(x2[1:])

        # else:
        #     if int(x2) < -(2**31) or int(x2) > (2**31)-1:
        #         return 0
        #     else :
        #         return int(x2)












print(reverse(x))