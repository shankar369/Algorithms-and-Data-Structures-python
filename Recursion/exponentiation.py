# program to calculate power of n 
import time
def power(n,p):
    if(p==0):
        return 1
    elif(p%2 == 0):
        v = power(n,p//2)
        return v*v
    else:
        return n*power(n,p-1)

if __name__ == "__main__":
    n = int(input("Enter the number : "))
    p = int(input("Enter the power value : "))
    start_time = time.time()
    print("Value is : ",power(n,p))
    print("time taken : ",time.time()-start_time)
