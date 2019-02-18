def comp(a,b,c):
    high=a if a>b and a>c else b if b>a and b>c else c 
    mid=a if a>b and a<c or a>c and a<b else b if b>a and b<c or b>c and b<a else c
    low=a if a<b and a<c else b if b<a and b<c else c 
    return high,mid,low
    
