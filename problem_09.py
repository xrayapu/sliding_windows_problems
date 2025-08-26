# print the longest substring with k unique characters 

# same as problem 6, just return the array

def sol(arr, k):
    m={}
    ans=0
    i=j=0
    while j<len(arr):
        if arr[j] in m:
            m[arr[j]]+=1

        else: 
            m[arr[j]] =1

        if len(m) <k:
            j+=1

        elif len(m)== k:
            ans= max(ans, j-i+1)
            j+=1

        else:
            while len(m)> k:
                it= arr[i]
                
                m[it]-=1
                if m[it] ==0:
                    m.pop(it)

                i+=1

            j+=1

    return arr[i:]


print(sol('aabacbebebe',3))
