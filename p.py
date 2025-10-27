#!/usr/bin/env python3
def vk(v):
    pass
def pk(sn,dk=0):
    s=''
    k=dk
    pk=0
    ps=[]
    sp=False
    import curses
    curses.initscr()
    while k<len(ps):
        p=sys.stdin.read(1)
        if ord(p)==4:break
        if p=='\n':
            if sp:pk+=1
            if pk==len(ps[k][1]):
                k+=1
                pk=0
            if not sp:vk([71,44,4,49,1,55,53,7,51,2,75])
            sp=True
            vk(ps[k][1][pk])
        elif ord(p)>=ord('0') and ord(p)<=ord('9'):
            import time
            s+=str(int(time.time()))+' '+':'.join([str(l) for l in ps[k][0]])+' '+p+'\n'
            print(p+'\r')

    curses.endwin()
    open(sn,'a').write('')
if __name__=="__main__":
    import sys
    if len(sys.argv)>2:
        pk(sys.argv[1],sys.argv[2])
    elif len(sys.argv)>1:
        pk(sys.argv[1])

