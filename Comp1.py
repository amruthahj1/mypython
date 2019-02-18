def comp(a,b,c):
    high,mid,lea=0,0,0
    if a>b and a>c:
        high=a
    if b>a and b>c:
        high=b
    if c>a and c>b:
        high=c
    if a>b and a<c or a<a and a>c:
        mid=a
    if b>a and b<c or b<a and b>c:
        mid=b
    if c>b and c<a or c<b and c>a:
        mid=a
    if a<b and a<c:
        lea=a
    if b<a and b<c:
        lea=b
    if c<a and c<b:
        lea=c
    print("%d>%d>%d",high,mid,lea)
    return high,mid,lea


