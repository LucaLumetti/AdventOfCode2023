import sys

x = sys.stdin.read().strip().replace('\n','').split(',')

def hash(s):
    current_value = 0

    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256

    return current_value


x = sum([hash(s) for s in x])
print(x)
