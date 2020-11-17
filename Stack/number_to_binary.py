'''
Convert a decimal number into binary string

ex: 242 = 11110010 in binary format
'''

from stack import Stack


def convert_to_binary(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num //= 2
    # print(s.get_stack())
    binary_format = ""
    while not s.is_empty():
        binary_format += str(s.pop())
    return binary_format


print(convert_to_binary(2))
print(convert_to_binary(242))
print(convert_to_binary(10000))
