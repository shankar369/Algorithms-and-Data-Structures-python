# Binary search recursive implementation

def binary_search_recursion(arr,start,end,element_to_find):

    if(start>end):
        return -1
    mid = start+(end-start)//2
    if(arr[mid] == element_to_find):
        return mid
    elif(element_to_find < arr[mid]):
        return binary_search_recursion(arr,start,mid-1,element_to_find)
    else:
        return binary_search_recursion(arr,mid+1,end,element_to_find)



if __name__ == "__main__":
    
    arr = [2,3,44,45,59,66,544,940,966,999,1009]  # should be sorted

    element_to_find = input("\n\nEnter element to find : ")
    while(element_to_find != "stop"):
        try:
            result =  binary_search_recursion(arr,0,len(arr),int(element_to_find))
            if(result != -1):
                print(element_to_find,"found at index : ",result)
            else:
                print(element_to_find,"not found !!!")
        except:
            print("Invalid input !!!")
        element_to_find = input("\n\nEnter element to find : ")
