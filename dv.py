#!/usr/bin/env python3
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
if __name__=="__main__":
    pk()
