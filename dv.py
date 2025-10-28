#!/usr/bin/env python3
gs=0
gk=0
gg=[]
ps=[]
def pk():
    from os import system
    import os.path
    system("mkdir -p ds")
    for k in range(0,len(ps)):
        if os.path.isfile('ds/'+str(k+1)+'.jpg'):continue
        dn=ps[k][0]
        dn='"'+dn+'"'
        system('wget -O ds/'+str(k+1)+'.jpg '+dn)
def gss(p):
    global gs,gg
    gs=p
    gg=[0]*gs
def dd(k):
    pass
def pp(k):
    import sys
    while True:
        for v in ps[k][1]:
            sys.stdin.readline()
            p.vk(v)
        print('t')
        t=sys.stdin.readline()
        if t!='\n':t=t[0]
        if t=='n':
            return t
        elif ord(t)>=ord('0') and ord(t)<=ord('9'):
            return int(t)
def pmk():
    pk()
    import p,sys
    p.vk([51,2,66,7,53,2,65,6,77])
    gss(int(sys.stdin.readline()))
    global gk
    for k in range(0,len(ps)):
        print('gg '+str(gg))
        st=False
        tgk=gk
        pg=[False]*gs
        pgs=0
        dd(k)
        while True:
            t=pp(k)
            pg[tgk]=True
            pgs+=1
            if t=='n' or t!=ps[k][2]:
                if t!=ps[k][2]:
                    gg[tgk]-=2
                if pgs==gs:break
                while True:
                    import random
                    n=random.randint(1,gs-1)
                    if not pg[(tgk+n)%gs]:
                        tgk=(tgk+n)%gs
                        break
            if t==ps[k][2]:
                gg[tgk]+=1
                break
        gk+=1
        if gk==gs:gk=0

if __name__=="__main__":
    pmk()
