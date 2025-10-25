#!/usr/bin/env python3
def vk(v):
    pass
def pk(sn):
    k=0
    pk=0
    ps=[]
    sp=False
    import curses
    curses.initscr()
    while k<len(ps):
        p=sys.stdin.read(1)
        if ord(p)==4:break
        if p=='\n':
            sp=True
            pk+=1
            if pk==len(ps[k]):
                k+=1
                pk=0
    curses.endwin()
    open(sn,'a').write('')
if __name__=="__main__":
    import sys
    if len(sys.argv)>1:
        pk(sys.argv[1])
