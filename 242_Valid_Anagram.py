'''242. Valid Anagram
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''
s = "anagram"
t = "nagaram"
# Output = true


# s = "rat"
# t = "car"

# Output: false


# s = "rat"
# t = "car"

# Output: false

# s = "aa"
# # t = "a"
# Output:False


# def isAnagram(s,t):
#     lst1 = []
#     lst2 = []
    
    
#     for i in s:
#         lst1.append(i)
#     x1 = set(lst1)

#     for k in t:
#         lst2.append(k)
#     x2 = set(lst2)


#     if x1 == x2:
#         return True
#     else:
#         return False
        

# print(isAnagram(s,t))


# s = 'aa'
# k = set(s)

# all_char = []

# for elem in s:
#     all_char.append(elem)

# k = set(all_char)

# new_char = str()
# for elem in k:
#     new_char.join(elem)

# print(new_char)

# s= 'cat'
# all_ekem = []
# for i in s:
#     all_ekem.append(i)
# # print(all_ekem)


# sum = str()
# for i in set(all_ekem):
#     sum = sum+i

# print(sum)

def isAnagram(s,t):
    all_char = [ i for i in s]
    all_char.sort()
    k = all_char[:]

    all_char2 = [j for j in t]
    all_char2.sort()
    l = all_char2[:]

    if k == l:
        return True
    else:
        return False
        

isAnagram(s,t)