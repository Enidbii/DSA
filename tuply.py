#!/usr/bin/env python3

def sort_list():
    list_1 = [(2,5), (1,2), (4,4), (2,3), (2,1)]
    
    list2 = sorted(list_1, key=lambda j: j[1])

    print(list2)

if __name__ == "__main__":
    sort_list()
