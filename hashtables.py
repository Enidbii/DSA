#!/usr/bin/python3 env
from itertools import count


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            #returns an address on the hash table
            my_hash = (my_hash + ord(letter) * 17) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        #get index first of the address of the key
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False

# def find_duplicates(nums):
#     my_dict = {}
#
#     for num in nums:
#         if num in my_dict:
#             my_dict[num] += 1
#         else:
#             my_dict[num] = 1
#
#     duplicates = []
#
#     for num, count in my_dict.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates


# def find_duplicates(nums):
#     my_dict = {}
#     for i, val in enumerate(nums):
#         my_dict[i] = val
#     #print(my_dict)
#     duplicates = []
#     for num, count in my_dict.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates













# my_hashtable = HashTable()
# my_hashtable.set_item("bolts", 30)
# my_hashtable.set_item("washers", 50)
# my_hashtable.set_item("lumber", 70)
# #my_hashtable.print_table()
# print(my_hashtable.get_item("bolts"))
# print(my_hashtable.keys())
#
# list1 = [1, 2, 5]
# list2 = [2, 4, 6]
#
#print(item_in_common(list1,list2))
print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )
