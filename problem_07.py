#problem 7: longest substring >> without repeating characters.= all unique chatacters
#len(m) = windows size= all unique characters
#leetcode:3

# pwwekw  -> output:3
#p ->1 , w->1,wek->3,ekw->3 so,ans is 3

 
def sol(arr):
    m={}
    i=j=0
    mx=0
    while j< len(arr):
        if arr[j] in m:
            m[arr[j]] +=1

        else: m[arr[j]]=1

        if len(m) < j-i+1: #pww p:1,w:2, here element(window) 3 but len->2, so not unique word ! 
            while len(m) < j-i+1:
                it= arr[i] # cut elements from 1st >>p,w,w,...
                m[it]-=1
                i+=1
                if m[it] ==0:
                    m.pop(it)

            j+=1

        elif len(m)== j-i+1:
            mx=max(mx,j-i+1)
            j+=1

    return mx

print(sol('pwwkew'))
