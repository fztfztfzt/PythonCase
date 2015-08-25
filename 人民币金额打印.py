#coding:utf8
a=120000200009
wei = u'零壹贰叁肆伍陆柒捌玖'
hou = u'零拾佰仟'
con = u'零万亿'
def fuck(s1,count):
    s = u''
    for i in range(len(s1)):
        if s1[i] == u'0':
            s = wei[0]+s
        else :
            s = wei[int(s1[i])]+hou[i]+s
    while u'零零' in s:
        #print 's'
        s=s.replace(u'零零',u'零')
    if s[len(s)-1] == u'零':
        s = s[:-1]
    if count != 0 and s!='':
        s = s+con[count]
    return s
s = u''
count=0
start=0
end=4
s1 = str(abs(a))[::-1]
while start<len(s1):
    if end > len(s1):
        end = len(s1)
    s = fuck(s1[start:end],count)+s
    start+=4
    end +=4
    count +=1
if a<0:
    s=u'负'+s
if a == 0 :
    print u'零圆'
else :
    print  s+u'圆'
    
    
    