n=3
m=3
MAX = 999999999
maxcon = MAX
visit = [([False]*(n+2)) for i in range(m+2)]
def fun(a,b,co):
    global m,n,MAX,visit,maxcon
    if a>n or b>m or a<0 or b<0:
        return MAX
    print a,b
    if visit[a][b]:
        return MAX
    else:
        visit[a][b]=True
    if (a==n and b==m) or (a==m and b==n):
        maxcon = co
        return co
    if co<maxcon:
        mmin = fun(a+1,b+2,co+1)
        mmin = min(mmin,fun(a+2,b+1,co+1))
        mmin = min(mmin,fun(a-1,b+2,co+1))
        mmin = min(mmin,fun(a-2,b+1,co+1))
        mmin = min(mmin,fun(a+1,b-2,co+1))
        mmin = min(mmin,fun(a+2,b-1,co+1))
        mmin = min(mmin,fun(a-1,b-2,co+1))
        mmin = min(mmin,fun(a-2,b-1,co+1))
        return mmin
    else :
        return MAX
mm=fun(0,0,0)
if 999999999==mm:
    print -1
else :
    print mm
