#problem 6: longest substring with k unique characters.

# aabacbebebebe                  k=3
# output:7(cbebebebe)

#from collections import Counter
def sol(arr,k):
    i=j=0
    m={}
    mx=0
    # x=Counter(arr)
    # if len(x) <k: return -1  #for case like 'aavvcc'      k=4
    while j<len(arr):
        if arr[j] in m:
            m[arr[j]] +=1

        else: m[arr[j]] =1

        if len(m) < k:
            j+=1

        elif len(m) ==k:
            mx=max(mx, j-i+1)
            j+=1

        else:
            while len(m) > k:
                it=arr[i]
                m[it] -=1 #m[arr[i]] gives string index out of range ! although we did same work here ! 
                i+=1
                if m[it]==0:
                    m.pop(it)
            j+=1

    return mx

print(sol('aabbcc',2))
