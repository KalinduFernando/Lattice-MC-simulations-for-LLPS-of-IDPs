##from LJ import append_energy
##from LJ import calculate_energy
import LJ as lj
import random
import math
import matplotlib.pyplot as plt
"slithering Snake movement"

def SlitheringSnake_MV(chain_no,chn_info,lattice,Nbox,EE):

    lj.append_energy(lattice,Nbox,chn_info)
    E_old = lj.calculate_energy(chn_info)
    
    set_chnSMV=random.randint(0,chain_no-1)
    chnSMV =chn_info[set_chnSMV]
    #print(chnSMV)

    IndexSS=[]
    for i in range(len(chnSMV)):
        IndexSS.append(chn_info[set_chnSMV][i][2])
    #print(IndexSS)
    x,y,z = chn_info[set_chnSMV][0][2]
    posSS=[]
    if x > 1 and x < Nbox-1 and y > 1 and y < Nbox-1 and z > 1 and z < Nbox-1 :
        
        if lattice[x-1][y][z] == 0:
            posSS.append([x-1,y,z])
            lattice[x-1][y][z]= 1
            
        if lattice[x+1][y][z] == 0:
            posSS.append([x+1,y,z])
            lattice[x-1][y][z]= 1
            
        if lattice[x][y-1][z] == 0:      
            posSS.append([x,y-1,z])
            lattice[x-1][y][z] = 1
            
        if lattice[x][y+1][z] == 0:
            posSS.append([x,y+1,z])
            lattice[x-1][y][z] = 1
            
        if lattice[x][y][z-1] == 0:
            posSS.append([x,y,z-1])
            lattice[x-1][y][z]= 1
            
        if lattice[x][y][z+1] == 0:
            posSS.append([x,y,z+1])
            lattice[x-1][y][z] = 1

    if len(posSS)>0:
        set_no=random.randint(0,len(posSS)-1)
        IndexSS.insert(0,posSS[set_no])
        IndexSS.remove (IndexSS[-1])
        #print (IndexSS)
        for bdSMV in range (len(chnSMV)):               
            x,y,z=chn_info[set_chnSMV][bdSMV][2]
            lattice[x][y][z]=0           
            chn_info[set_chnSMV][bdSMV][2]=IndexSS[bdSMV]

        if chn_info[set_chnSMV][bdSMV][1]=="SA01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=1
        elif chn_info[set_chnSMV][bdSMV][1]=="SB01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=2
        elif chn_info[set_chnSMV][bdSMV][1]=="SC01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=3
        elif chn_info[set_chnSMV][bdSMV][1]=="SD01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=4
        elif chn_info[set_chnSMV][bdSMV][1]=="SE01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=5
        elif chn_info[set_chnSMV][bdSMV][1]=="SF01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=6
        elif chn_info[set_chnSMV][bdSMV][1]=="SG01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=7
        elif chn_info[set_chnSMV][bdSMV][1]=="SH01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=8
        elif chn_info[set_chnSMV][bdSMV][1]=="SI01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=9
        elif chn_info[set_chnSMV][bdSMV][1]=="SJ01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=10
        elif chn_info[set_chnSMV][bdSMV][1]=="SK01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=11
        elif chn_info[set_chnSMV][bdSMV][1]=="SL01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=12
        elif chn_info[set_chnSMV][bdSMV][1]=="SM01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=13
        elif chn_info[set_chnSMV][bdSMV][1]=="SN01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=14
        elif chn_info[set_chnSMV][bdSMV][1]=="SO01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=15
        elif chn_info[set_chnSMV][bdSMV][1]=="SP01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=16
        elif chn_info[set_chnSMV][bdSMV][1]=="SQ01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=17
        elif chn_info[set_chnSMV][bdSMV][1]=="SR01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=18
        elif chn_info[set_chnSMV][bdSMV][1]=="SS01":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=19
        elif chn_info[set_chnSMV][bdSMV][1][0]=="L":
            lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=20
            
        #print(chnSMV)

        lj.append_energy(lattice,Nbox,chn_info)
        E_new = lj.calculate_energy(chn_info)
        
        dE = E_new-E_old
        if dE<0:
            #print("Movement accepted")
            EE.append(E_new)
        elif dE >=0:
            w = (len(posSS)/6)*math.exp(dE)
            #print(w)
            r = random.randint(0,1)
            if w > r:
                #print("movement accepted")
                EE.append(E_new)
            else:
                #print("Movement rejected")
                EE.append(E_old)

                for bdSMV in range(len(chnSMV)):
                    lattice[IndexSS[bdSMV][0]][IndexSS[bdSMV][1]][IndexSS[bdSMV][2]]=0

                    if chn_info[set_chnSMV][bdSMV][1]=="SA01":
                        lattice[x][y][z]= 1
                    elif chn_info[set_chnSMV][bdSMV][1]=="SB01":
                        lattice[x][y][z]=2
                    elif chn_info[set_chnSMV][bdSMV][1]=="SC01":
                        lattice[x][y][z]=3
                    elif chn_info[set_chnSMV][bdSMV][1]=="SD01":
                        lattice[x][y][z]=4
                    elif chn_info[set_chnSMV][bdSMV][1]=="SE01":
                        lattice[x][y][z]=5
                    elif chn_info[set_chnSMV][bdSMV][1]=="SF01":
                        lattice[x][y][z]=6
                    elif chn_info[set_chnSMV][bdSMV][1]=="SG01":
                        lattice[x][y][z]=7
                    elif chn_info[set_chnSMV][bdSMV][1]=="SH01":
                        lattice[x][y][z]=8
                    elif chn_info[set_chnSMV][bdSMV][1]=="SI01":
                        lattice[x][y][z]=9
                    elif chn_info[set_chnSMV][bdSMV][1]=="SJ01":
                        lattice[x][y][z]=10
                    elif chn_info[set_chnSMV][bdSMV][1]=="SK01":
                        lattice[x][y][z]=11
                    elif chn_info[set_chnSMV][bdSMV][1]=="SL01":
                        lattice[x][y][z]=12
                    elif chn_info[set_chnSMV][bdSMV][1]=="SM01":
                        lattice[x][y][z]=13
                    elif chn_info[set_chnSMV][bdSMV][1]=="SN01":
                        lattice[x][y][z]=14
                    elif chn_info[set_chnSMV][bdSMV][1]=="SO01":
                        lattice[x][y][z]=15
                    elif chn_info[set_chnSMV][bdSMV][1]=="SP01":
                        lattice[x][y][z]=16
                    elif chn_info[set_chnSMV][bdSMV][1]=="SQ01":
                        lattice[x][y][z]=17
                    elif chn_info[set_chnSMV][bdSMV][1]=="SR01":
                        lattice[x][y][z]=18
                    elif chn_info[set_chnSMV][bdSMV][1]=="SS01":
                        lattice[x][y][z]=19
                    elif chn_info[set_chnSMV][bdSMV][1][0]=="L":
                        lattice[x][y][z]=20
                    
                  
    else:
        #print("Attempt not succesfull")
        EE.append(E_old)

    return chn_info




