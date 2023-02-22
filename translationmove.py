##from LLPS import lattice
##from LLPS import chain_no
##from LLPS import Nbox
##from LLPS import chn_info
import random as rd
import LJ as lj
import math


def search_translation(chn_info,set_chnTMV,lattice,IndexT,Nbox,E_old,EE,x1,y1,z1):
    
    con = True
    count=0
    for i in range(len(IndexT)):
        x,y,z=IndexT[i][0],IndexT[i][1],IndexT[i][2]
        if x > 1 and x < Nbox-1 and y > 1 and y < Nbox-1 and z > 1 and z < Nbox-1:
            if lattice[x+x1][y+y1][z+z1]==0 :
                chn_info[set_chnTMV][i][2][0]=x+x1
                chn_info[set_chnTMV][i][2][1]=y+y1
                chn_info[set_chnTMV][i][2][2]=z+z1
            
                con = True
                count+=1
            else:
                con= False

    if len(IndexT)==count:
        #print("ok")
        for bdT in range(len(IndexT)):
            lattice[x][y][z]=0
            if chn_info[set_chnTMV][bdT][1]=="SA01":
                lattice[x+x1][y+y1][z+z1]=1
            elif chn_info[set_chnTMV][bdT][1]=="SB01":
                lattice[x+x1][y+y1][z+z1]=2
            elif chn_info[set_chnTMV][bdT][1]=="SC01":
                lattice[x+x1][y+y1][z+z1]=3
            elif chn_info[set_chnTMV][bdT][1]=="SD01":
                lattice[x+x1][y+y1][z+z1]=4
            elif chn_info[set_chnTMV][bdT][1]=="SE01":
                lattice[x+x1][y+y1][z+z1]=5
            elif chn_info[set_chnTMV][bdT][1]=="SF01":
                lattice[x+x1][y+y1][z+z1]=6
            elif chn_info[set_chnTMV][bdT][1]=="SG01":
                lattice[x+x1][y+y1][z+z1]=7
            elif chn_info[set_chnTMV][bdT][1]=="SH01":
                lattice[x+x1][y+y1][z+z1]=8
            elif chn_info[set_chnTMV][bdT][1]=="SI01":
                lattice[x+x1][y+y1][z+z1]=9
            elif chn_info[set_chnTMV][bdT][1]=="SJ01":
                lattice[x+x1][y+y1][z+z1]=10
            elif chn_info[set_chnTMV][bdT][1]=="SK01":
                lattice[x+x1][y+y1][z+z1]=11
            elif chn_info[set_chnTMV][bdT][1]=="SL01":
                lattice[x+x1][y+y1][z+z1]=12
            elif chn_info[set_chnTMV][bdT][1]=="SM01":
                lattice[x+x1][y+y1][z+z1]=13
            elif chn_info[set_chnTMV][bdT][1]=="SN01":
                lattice[x+x1][y+y1][z+z1]=14
            elif chn_info[set_chnTMV][bdT][1]=="SO01":
                lattice[x+x1][y+y1][z+z1]=15
            elif chn_info[set_chnTMV][bdT][1]=="SP01":
                lattice[x+x1][y+y1][z+z1]=16
            elif chn_info[set_chnTMV][bdT][1]=="SQ01":
                lattice[x+x1][y+y1][z+z1]=17
            elif chn_info[set_chnTMV][bdT][1]=="SR01":
                lattice[x+x1][y+y1][z+z1]=18
            elif chn_info[set_chnTMV][bdT][1]=="SS01":
                lattice[x+x1][y+y1][z+z1]=19
            elif chn_info[set_chnTMV][bdT][1][0]=="L":
                lattice[x+x1][y+y1][z+z1]=20

        #print(chn_info[set_chnTMV])

        lj.append_energy(lattice,Nbox,chn_info)
        E_new = lj.calculate_energy(chn_info)
        
        dE = E_new-E_old
        if dE<0:
            #print("Movement accepted")
            EE.append(E_new)
        elif dE >=0:
            w = (1/6)*math.exp(dE)
            #print(w)
            r = rd.randint(0,1)
            if w > r:
                #print("movement accepted")
                EE.append(E_new)
            else:
                #print("Movement rejected")
                EE.append(E_old)

                for bdT in range(len(chn_info[set_chnTMV])):
                    lattice[x+x1][y+y1][z+z1]=0
                    if chn_info[set_chnTMV][bdT][1]=="SA01":
                        lattice[x][y][z]=1
                    elif chn_info[set_chnTMV][bdT][1]=="SB01":
                        lattice[x][y][z]=2
                    elif chn_info[set_chnTMV][bdT][1]=="SC01":
                        lattice[x][y][z]=3
                    elif chn_info[set_chnTMV][bdT][1]=="SD01":
                        lattice[x][y][z]=4
                    elif chn_info[set_chnTMV][bdT][1]=="SE01":
                        lattice[x][y][z]=5
                    elif chn_info[set_chnTMV][bdT][1]=="SF01":
                        lattice[x][y][z]=6
                    elif chn_info[set_chnTMV][bdT][1]=="SG01":
                        lattice[x][y][z]=7
                    elif chn_info[set_chnTMV][bdT][1]=="SH01":
                        lattice[x][y][z]=8
                    elif chn_info[set_chnTMV][bdT][1]=="SI01":
                        lattice[x][y][z]=9
                    elif chn_info[set_chnTMV][bdT][1]=="SJ01":
                        lattice[x][y][z]=10
                    elif chn_info[set_chnTMV][bdT][1]=="SK01":
                        lattice[x][y][z]=11
                    elif chn_info[set_chnTMV][bdT][1]=="SL01":
                        lattice[x][y][z]=12
                    elif chn_info[set_chnTMV][bdT][1]=="SM01":
                        lattice[x][y][z]=13
                    elif chn_info[set_chnTMV][bdT][1]=="SN01":
                        lattice[x][y][z]=14
                    elif chn_info[set_chnTMV][bdT][1]=="SO01":
                        lattice[x][y][z]=15
                    elif chn_info[set_chnTMV][bdT][1]=="SP01":
                        lattice[x][y][z]=16
                    elif chn_info[set_chnTMV][bdT][1]=="SQ01":
                        lattice[x][y][z]=17
                    elif chn_info[set_chnTMV][bdT][1]=="SR01":
                        lattice[x][y][z]=18
                    elif chn_info[set_chnTMV][bdT][1]=="SS01":
                        lattice[x][y][z]=19
                    elif chn_info[set_chnTMV][bdT][1][0]=="L":
                        lattice[x][y][z]=20 
          
    else:
        #print("Attempt not succesfull")
        EE.append(E_old)
        
    return chn_info

def Translation_MV(chain_no,Nbox,lattice,chn_info,EE):

    lj.append_energy(lattice,Nbox,chn_info)
    E_old = lj.calculate_energy(chn_info)
    
    set_chnTMV= rd.randint(0,chain_no-1)
    chnTMV =chn_info[set_chnTMV]
    #print(chnTMV)
    IndexT=[]
    for bdT in range(len(chnTMV)):
        IndexT.append(chn_info[set_chnTMV][bdT][2])
    
    rdt=rd.randint(0,5)
    if rdt==0:
        search_translation(chn_info,set_chnTMV,lattice,IndexT,Nbox,E_old,EE,1,0,0)
    elif rdt==1:
        search_translation(chn_info,set_chnTMV,lattice,IndexT,Nbox,E_old,EE,-1,0,0)
    elif rdt==2:
        search_translation(chn_info,set_chnTMV,lattice,IndexT,Nbox,E_old,EE,0,1,0)
    elif rdt==3:
        search_translation(chn_info,set_chnTMV,lattice,IndexT,Nbox,E_old,EE,0,-1,0)
    elif rdt==4:
        search_translation(chn_info,set_chnTMV,lattice,IndexT,Nbox,E_old,EE,0,0,1)
    else:
        search_translation(chn_info,set_chnTMV,lattice,IndexT,Nbox,E_old,EE,0,0,-1)
    
    
    
    
        

    #print(chnTMV)
                
            
        

