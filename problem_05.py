# problem 5: largest subarray sum of k.
# 4,1,1,1,2,3,5 ->4,1 ->1,1,1,2 ->2,3, -> 5
#  ans: 4(1,1,1,2 array's length)

def sol(arr,k):
    i=j=0
    mx=0
    ans=0

    while j< len(arr):
        ans+=arr[j]
        if ans < k:
            j+=1
        elif ans==k:
            mx=max(mx,j-i+1)
            j+=1
        else: 
            while ans > k:
                ans-= arr[i]
                if ans== k:
                    ans=max(ans, j-i+1)
                i+=1
                
            j+=1
        
    return mx

print(sol([4,1,1,2,3,5],8))
