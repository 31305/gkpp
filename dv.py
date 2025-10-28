#!/usr/bin/env python3
gs=0
gk=0
gg=[]
ps=[
        ['https://w.wiki/FqF8',[[56,1,70,68,44,1,43,5,70,3,75],[75,1,55,53,1,45,1,43,5,70,3,75]],2]
    ]
def pk():
    from os import system
    import os.path
    system("mkdir -p ds")
    for k in range(0,len(ps)):
        if os.path.isfile('ds/'+str(k+1)+'.jpg') or ps[k][0]=='':continue
        dn=ps[k][0]
        dn='"'+dn+'"'
        system('wget -O ds/'+str(k+1)+'.jpg '+dn)
def gss(p):
    global gs,gg
    gs=p
    gg=[0]*gs
def dd(k):
    from os import system
    system('explorer.exe ds\\\\'+str(k+1)+'.jpg')
def pp(k):
    print('pp')
    import sys,p
    pk=0
    while pk<len(ps[k][1]):
        t=sys.stdin.readline()
        if t=='\n':
            p.vk(ps[k][1][pk])
            pk=(pk+1)%len(ps[k][1])
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
        st=False
        tgk=gk
        pg=[False]*gs
        pgs=0
        dd(k)
        while True:
            print('gg '+str(gg))
            print('k ' +str(k+1))
            print('tgk '+str(tgk+1))
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
    print('gg '+str(gg))
if __name__=="__main__":
    pmk()
