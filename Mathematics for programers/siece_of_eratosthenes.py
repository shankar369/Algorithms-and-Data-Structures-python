# sieve of eratosthenes algorithm to print prime numbers in a given range
import math

def print_primes(input_list,l):
    for i in range(int(math.sqrt(l))):
        if(input_list[i] != -1):
            for j in range(input_list[i]*2-2,l,input_list[i]):
                input_list[j] = -1
    for i in input_list:
        if(i!= -1):
            print(i,end=" ")




if __name__ == "__main__":
    n = int(input("Enter the n value : "))
    input_list = list(range(2,n+1))
    print_primes(input_list,len(input_list))