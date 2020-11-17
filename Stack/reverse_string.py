from stack import Stack


def reverse_string(input_string):
    s = Stack()
    for ch in input_string:
        s.push(ch)
    rev_str = ""
    while not s.is_empty():
        rev_str += s.pop()
    return rev_str


print(reverse_string("shankar"))


# print(input_string[::-1])
