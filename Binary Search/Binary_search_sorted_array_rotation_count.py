# Program to find how many times the sorted array is rotated

def find_rotation_count(arr,length):
    first,last = 0,length-1
    while(first<=last):
        if(arr[first]<=arr[last]):
            return first #sorted #case:1
        mid = (first+last)//2
        prev,next = (mid+length-1)%length,(mid+1)%length
        if(arr[mid]<=arr[prev]  and arr[mid] <= arr[next]):
            return mid # case : 2
        elif(arr[mid] <= arr[last]):
            last = mid-1 # case : 3
        elif(arr[mid] >= arr[first]):
            first = mid+1 # case : 4
    return -1

if __name__ == "__main__":
    arr = [15,22,23,28,31,38,5,6,8,10,12]
    print("No of rotations of sorted arr is : ",find_rotation_count(arr,len(arr)))
