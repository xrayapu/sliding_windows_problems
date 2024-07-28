#problem 3: count occuarance of anagram

# input:aabaabaa ,tar:aaba -> output:4
from collections import Counter
def sol(arr,tar):
    ans=0
    i,j=0,0
    x=Counter(tar)
    it=len(x)
    k=len(tar)
    while j<len(arr):
        if arr[j] in x:
            x[arr[j]] -=1
            if x[arr[j]]==0:
                it-=1

        if j-i+1 <k:
            j+=1

        else:
            if it==0:
                ans+=1
            if arr[i] in x:
                x[arr[i]] +=1
                if x[arr[i]]==1:
                    it+=1

            j+=1
            i+=1

    return ans

print(sol('aabaabaa','aaba'))
    
