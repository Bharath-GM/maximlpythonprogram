noofchar=256
def maxdistinctchar(str,n):
    count=[0]*noofchar
    for i in range(n):
        count[ord(str[i])] +=1
    maxdist=0
    for i in range(noofchar):
        if(count[i]!=0):
            maxdist+=1
    return maxdist
def substring_with_maxdistinctchar(str):
    n=len(str)
    maxd=maxdistinctchar(str,n)
    minlen=n
    for i in range(n):
        for j in range(n):
            substring=str[i:j]
            substringlen=len(substring)
            subdistchar=maxdistinctchar(substring,substringlen)
    if (substringlen <minlen and maxd==subdistchar):
        minlen=substringlen
    return minlen

str=input()
leng=substring_with_maxdistinctchar(str)
print(leng-1)