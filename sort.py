#!/usr/bin/python3 env
""" sorting algorithms """
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[j]
            my_list[j] = my_list[min_index]
            my_list[min_index] = temp

    return my_list
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    while i < len(list1):
        combined.append(list1[i])
        i+=1
    while j < len(list2):
        combined.append(list2[j])
        j+=1
    return combined

def merge_sort(my_list):
    if len(my_list) <= 1: #base case
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)
    # items = []
    # for item in my_list:
    #     items.append([item])

    # for i in range(len(items) - 1):
    #     mid_in






def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        for j in range(len(my_list[i:i+1:-1])):
            if my_list[j] < my_list[i]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list

def insertion_sort_two(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j>-1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j=-1
    return my_list

def swap(mylist, index1, index2):
    temp = mylist[index1]
    mylist[index1] = mylist[index2]
    mylist[index2] = temp

def partition(mlist,pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if mlist[i] < mlist[pivot_index]:
            swap_index+=1
            swap(mlist, swap_index, i)

    swap(mlist, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = partition(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)






mylist = [4,1,34,33,22,25,40,2]
# print(bubble_sort(mylist))
# print(selection_sort(mylist))
# print(insertion_sort_two(mylist))
# this_list = merge_sort(mylist)
# print(this_list)
# print()
print(quick_sort(mylist))
