# Binary search to find first and last occurance of a element

def binary_search_first_occurrence(arr,length,element_to_find):
    start,end = 0,length-1
    result = -1
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid] == element_to_find):
            end = mid-1 # changes here
            result = mid
        elif(element_to_find < arr[mid]):
            end = mid-1
        else:
            start = mid+1
    return result


def binary_search_last_occurrence(arr,length,element_to_find):
    start,end = 0,length-1
    result = -1
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid] == element_to_find):
            start = mid+1 #changes here
            result = mid
        elif(element_to_find < arr[mid]):
            end = mid-1
        else:
            start = mid+1
    return result




if __name__ == "__main__":
    
    arr = [2,3,44,45,59,59,59,59,66,544,940,966,999,999,1009]  # should be sorted

    element_to_find = input("\n\nEnter element to find : ")
    while(element_to_find != "stop"):
        try:
            result = -1
            choice = input("F for first occurrence\nL for last occurrencce\n")
            if(choice == "F"):
                result =  binary_search_first_occurrence(arr,len(arr),int(element_to_find))
            else:
                result =  binary_search_last_occurrence(arr,len(arr),int(element_to_find))
            if(result != -1):
                print(element_to_find,"found at index : ",result)
            else:
                print(element_to_find,"not found !!!")
        except:
            print("Invalid input !!!")
        element_to_find = input("\n\nEnter element to find : ")