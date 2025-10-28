#!/usr/bin/env python3
gs=0
gk=0
def pk():
    from os import system
    import os.path
    sysetm("mkdir -p ds")
    ps=[]
    for k in range(0,len(ps)):
        if os.path.isfile('ds/'+str(k+1)+'.jpg'):continue
        dn=ps[k][0]
        dn='"'+dn+'"'
        system('wget -O ds/'+str(k+1)+'.jpg '+dn)
def pmk():
    import p,sys
    p.vk([51,2,66,7,53,2,65,6,77])
    gs=int(sys.stdin.readline())
    print(gs)
if __name__=="__main__":
    pmk()
