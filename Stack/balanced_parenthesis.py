'''
using stack to check a string is a balanced paranthesis or not

Example:
    (), ()(),(({[]})) are Balanced
    ((), {{}}],][ are unbalanced
    special case: ))]   -- starts with closing paranthesis
'''
from stack import Stack


def is_match(top, paren):
    if(top == '[' and paren == ']'):
        return True
    elif(top == "(" and paren == ")"):
        return True
    elif(top == '{' and paren == '}'):
        return True
    return False


def is_parenthesis_balanced(paranthesis_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paranthesis_string) and is_balanced:
        paren = paranthesis_string[index]
        if(paren in "([{"):
            s.push(paren)
        else:
            if(s.is_empty()):
                is_balanced = False
            else:
                top = s.pop()
                if(not is_match(top, paren)):
                    is_balanced = False
        index += 1

    if(s.is_empty() and is_balanced):
        return True
    return False

print(is_parenthesis_balanced("(({[]}))"))
print(is_parenthesis_balanced("()()"))
print(is_parenthesis_balanced("}}}(){{{"))
print(is_parenthesis_balanced("(){}[]"))