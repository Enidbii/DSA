#!/usr/bin/python3 env

def reverse(s):
    result = ""
    for i in s:
        result = i + result

    return result

if __name__ == "__main__":
    s = 'complicated'
    print("Original string is ", s)
    print("Reversed string is ", reverse(s))
