#note:must sort first!!!
a,b,c = sorted([a,b,c])
r = ''
d = (a*a+b*b-c*c)
if d==0:
    r = 'Z'
elif d<0:
    r = 'D'
else:
    r = 'R'
if not (a+b>c and a-b<c):
    r='W'
print r
