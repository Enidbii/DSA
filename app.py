#!/usr/bin/env python3
def rem_zero():
    d_list = [1,0,2,0,4,6]

    for item in d_list:
        if item == 0:
            d_list.remove(item)
            d_list.append(item)
    print(d_list)
print_out = rem_zero()
