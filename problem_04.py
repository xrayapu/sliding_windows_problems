#problem 4: find maximum of all subarray of size k

# input:[1,3,-1,5,3,6,7]

# output:[3,5,5,6,7]

def sol(arr,k):
    
    i=j=0
    ans,new=[],[]
    while j< len(arr):
        new.append(arr[j])
        if j-i+1< k:
            j+=1

        elif j-i+1==k:
            
            it=max(new)
            
            ans.append((it))
            new.pop(0)
            j+=1
            i+=1

        

    return ans

print(sol([1,3,-1,-3,5,3,6,7],3))
