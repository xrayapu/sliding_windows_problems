# problem 8: give the minimum sliding window length (print it )
from collections import Counter
def sol(arr, t):
   x= Counter(t)
   
   k= len(x)
   ans=''
   res=float('inf')
   i=j=0
   while j<len(arr):
      if arr[j] in x:
         x[arr[j]]-=1

         if x[arr[j]]==0:
            k-=1

      while k==0: # condition is this ! 
         if j-i+1 < res:
            res=  j-i+1
            # start,end=i, i+res
            # ans= arr[start:end]

         if arr[i] in x:
            x[arr[i]]+=1
            if x[arr[i]]==1:
               k+=1

         i+=1

      j+=1

   return res # return ans 

print(sol("ADOBECODEBANC",'ABC')) # output: BANC( if added those code ! )

# this without ans gives the length of minimum sliding window . ( 4 ) 
