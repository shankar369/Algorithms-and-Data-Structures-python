# slots are very useful for improving time and especially memory in classes

class Abc:
    pass


abc = Abc()

abc.first = "hello"
abc.second = "world"

'''
 in python we can add dynamic attributes to class and those
 will be stored in dictionary 
 abc.__dict__

'''
print(abc.__dict__, "attributes stored in dictionary format")
print(abc.first, abc.second)


class Def:
    __slots__ = ("first", "second")


de = Def()


de.first = "hello"
de.second = "world"

# de.third = "some value" throw us error as Def class has no third attribute

# print(de.__dict__, "attributes stored in dictionary format") will throw error as we are using slots

print(de.__slots__, "slots we have in our class")
print(de.first, de.second)


class Efg:
    __slots__ = ("first", "second", "__dict__")


ef = Efg()


ef.first = "hello"
ef.second = "world"

ef.third = "some value"  # this will work as we specified __dict__ in slots tuple

# print(ef.__dict__, "attributes stored in dictionary format") will throw error as we are using slots

print(ef.__slots__, "slots we have in our class")
print(ef.__dict__, "dict which stored dynamic attributes")
print(ef.first, ef.second, ef.third)
