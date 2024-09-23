#!/usr/bin/python3 env

# def comparison(list1, list2):
#     for i in range(len(list1)):
#         for j in range(len(list2)):
#             if list1[i] == list2[j]:
#                 print(f"{list1[i]} is equal to {list2[j]}")
#                 return True
#     return False
#
# list1 = [1, 3, 5]
# list2 = [2, 4, 5]
# comp = comparison(list1, list2)
# print(comp)
def first_non_repeating_char(string):
    #print(string[0])
    if len(string) is None:
        return None
    for i in range(len(string)):
        if string[i] == string[i+1]:
          return None
    #elif
        else:
              return string[i]
print(first_non_repeating_char("leetcode"))
print( first_non_repeating_char('hello'))
print( first_non_repeating_char('aabbcc') )
print( first_non_repeating_char("") )
