# program to search element in circular sorted array using binary Search

def find_small_element(arr,length):
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

def binary_search_iterative(arr,start,end,element_to_find):
    while(start <= end):
        mid = (start+end)//2
        if(arr[mid] == element_to_find):
            return mid
        elif(element_to_find < arr[mid]):
            end = mid-1
        else:
            start = mid+1
    return -1

if __name__ == "__main__":
    arr = [15,22,23,28,31,38,5,6,8,10,12]
    #arr = [1,2,3,4,5,6,7,8,9,0]
    length = len(arr)
    low,high = 0, length-1
    smallest_element_index = find_small_element(arr,len(arr))
    element_to_find = int(input("Enter element : "))
    if(element_to_find == arr[smallest_element_index]):
        print(element_to_find,"Found at index : ",smallest_element_index)
    elif(element_to_find > arr[smallest_element_index] and element_to_find <= arr[high]):
        print(element_to_find,"Found at index : ",binary_search_iterative(arr,(smallest_element_index+1)%length,high,element_to_find))
    elif(element_to_find >= arr[smallest_element_index] and element_to_find >= arr[low]):
        print(element_to_find,"Found at index : ",binary_search_iterative(arr,low,(smallest_element_index-1+length)%length,element_to_find))