#!/usr/bin/env python3
gs=0
gk=0
gg=[]
ngg={}
k=0
d=False
ps=[
        ['https://w.wiki/FqvQ',[[71,2,60,56,3,49,4,69,2,46,3,77],[56,1,66,46,5,44,3,77,49,4,68,2,46,3,77],[66,44,2,43,3,77,49,4,69,2,46,3,77]],3],
        ['https://w.wiki/FqvW',[[66,7,49,44,38,70,4,44,43,3,77],[68,46,32,70,4,44,43,41],[56,2,66,3,49,44,37,70,44,43,3,77]],1],
        ['https://w.wiki/Fqvo',[[50,1,49,66,8,70,3,76,46,19,51,48,38,70,3,43,1,66,7],[50,1,49,66,11,46,19,51,48,2,76,70,3,43,1,66,7],
                                [50,1,49,66,11,46,19,51,48,32,65,1,70,10,43,1,66,31]],2],
        ['https://w.wiki/Fqw4',[[47,2,51,3,61,37,47,19,48,1,74,5,70,51,3,44,48,1,66,7],[47,2,51,3,61,1,76,47,19,48,1,74,5,77,51,3,44,48,1,70,66,7],
                                [47,2,51,3,61,1,76,47,19,48,1,74,42,51,3,44,48,1,66,1,77]],3],
        ['https://w.wiki/FqwE',[[51,13,75,74,10,44,2,49,43,37,71,2,44,9,51,16,44,75,41],[51,13,75,74,10,44,2,77,51,16,44,75,2,43,39,44,13,71,2,44,9],
                                [51,13,75,74,10,44,2,43,39,44,13,71,2,44,9,51,16,44,75,2,77]],1],
        ['https://w.wiki/FqxQ',[[73,1,51,2,14,63,63,3,43,1,66,31],[51,4,44,1,65,63,1,46,2,14,63,63,3,43,1,66,31],[75,1,68,53,14,44,14,63,63,3,43,1,66,31]],1],
        ['https://w.wiki/FqyS',[[50,2,44,9,66,1,71,4,68,1,77],[70,11,45,3,71,4,68,1,77],[71,10,66,2,71,6,68,1,77]],3]
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
def tpk():
    import sys,p
    pk=0
    global k,ngg
    while True:
        print(('k',k+1),('ngg',ngg))
        t=sys.stdin.readline()
        if t=='\n':
            p.vk(ps[k][1][pk])
            pk=(pk+1)%len(ps[k][1])
        elif t=='n\n':break
        elif len(t)>=3:
            t=t.split(' ')
            gk=int(t[0])
            if not gk in ngg:ngg[gk]=0
            pt=int(t[1])
            if pt==ps[k][2]:
                ngg[gk]+=1
                k+=1
                pk=0
                if k==len(ps):break
            else: 
                ngg[gk]-=2
    print(('ngg',ngg))
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
        if d:dd(k)
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
