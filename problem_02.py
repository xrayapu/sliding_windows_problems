# problem 2: 1st -ve number in every window size of k.

def sol(arr, k):
    i=j=0
    new=[]
    ans=[]
    while j< len(arr):
        if arr[j] < 0: # 1st collect the -ve number on a list to use later
            new.append(arr[j])

        if j-i+1< k:
            j+=1 # if not hit the size(k), only increase window's area ! 
        elif j-i+1==k:
            if len(new)==0:
                ans.append(0) # [30, 18, 28],no -ve number,so ans will be 0 
               # print(ans)
            else:
                ans.append(new[0])#[12, -1, -7,...] ->new will be [-1,-7] ,ans will be -1
                if arr[i]== new[0]:#kick off method !!! 
                    new.pop(0)
                
                
            j+=1
            i+=1
    return ans

print(sol([12, -1, -7, 8, -15, 30, 18, 28],3))
