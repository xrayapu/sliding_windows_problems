#maximum sum of the subarray of size k in the array

# [2,5,2,7,9,1,3], k=3 -> 2,5,2 | 5,2,7| 2,7,9|9,1,3 ==== output => max(18 )

def sol(arr,k):
    i,j=0,0 # i=j=0 both same effect
    mx,add=0,0
    while j <len(arr):
      add+=arr[j]
      if j-i+1<k:
        j+=1
      elif j-i+1 ==k:
        mx=max(mx,add)
        add=add- arr[i] #type of kick off the used item ,to reuse rest of it again
        i+=1
        j+=1
  
    return mx

print(sol([2,5,1,8,2,9,1],3))

# output-> 19
