'''
    bloom filter is a probabilistic data structure used to find an element is present or not
    It is more kind of a space efficient manner for searching
    The main drawback for this is false positives (some times we will get as an element is present even the element is not actually present)
    Deletion of element is not possible
'''

import pyhash
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

bit_vector = [0] * 30

# Non cryptographic hash functions (fnv and murmur)


def insert_element(element):
    fnv_elem_hash = fnv(element) % 30
    murmur_elem_hash = murmur(element) % 30

    bit_vector[fnv_elem_hash] = 1
    bit_vector[murmur_elem_hash] = 1


def find(element):
    fnv_elem_hash = fnv(element) % 30
    murmur_elem_hash = murmur(element) % 30

    if(bit_vector[fnv_elem_hash] == 1 and bit_vector[murmur_elem_hash] == 1):
        return True
    return False


print(bit_vector)
