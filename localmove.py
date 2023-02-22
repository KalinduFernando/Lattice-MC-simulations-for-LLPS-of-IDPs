from LJ import append_energy
from LJ import calculate_energy
import random
import math
import matplotlib.pyplot as plt
"MC Movements"
"Local Movement"

def Local_MV(chain_no,length,lattice,chn_info,Nbox,EE):
    
    append_energy(lattice,Nbox,chn_info)
    E_old= calculate_energy(chn_info)
    
    set_chnLMV=random.randint(0,chain_no-1)
    set_bdLMV =random.randint(0,length-1)
    x,y,z = chn_info[set_chnLMV][set_bdLMV][2]
    #print(chn_info[set_chnLMV][set_bdLMV][2])
    #print(chn_info[set_chnLMV][set_bdLMV][1])
    posL=[]
    if x > 1 and x < Nbox-1 and y > 1 and y < Nbox-1 and z > 1 and z < Nbox-1 :
        
        if lattice[x-1][y][z] == 0:
            posL.append([x-1,y,z])
            
        if lattice[x+1][y][z] == 0:
            posL.append([x+1,y,z])
            
        if lattice[x][y-1][z] == 0:      
            posL.append([x,y-1,z])
            
        if lattice[x][y+1][z] == 0:
            posL.append([x,y+1,z])
            
        if lattice[x][y][z-1] == 0:
            posL.append([x,y,z-1])
            
        if lattice[x][y][z+1] == 0:
            posL.append([x,y,z+1])
    #print(posL)
            
    if len(posL)>0:
        set_no=random.randint(0,len(posL)-1)
        chn_info[set_chnLMV][set_bdLMV][2]= [posL[set_no][0],posL[set_no][1],posL[set_no][2]]
        #print(chn_info[set_chnLMV][set_bdLMV][2])
            
        lattice[x][y][z]=0
        if chn_info[set_chnLMV][set_bdLMV][1]=="SA01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=1
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SB01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=2
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SC01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=3
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SD01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=4
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SE01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=5
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SF01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=6
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SG01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=7
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SH01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=8
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SI01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=9
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SJ01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=10
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SK01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=11
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SL01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=12
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SM01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=13
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SN01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=14
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SO01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=15
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SP01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=16
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SQ01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=17
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SR01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=18
        elif chn_info[set_chnLMV][set_bdLMV][1]=="SS01":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=19
        elif chn_info[set_chnLMV][set_bdLMV][1][0]=="L":
            lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=20


            
        append_energy(lattice,Nbox,chn_info)
        E_new=calculate_energy(chn_info)

        dE = E_new-E_old
        if dE<0:
            #print("Movement accepted")
            EE.append(E_new)
        elif dE >=0:
            w = (len(posL)/6)*math.exp(dE)
            #print(w)
            r = random.randint(0,1)
            if w > r:
                #print("movement accepted")
                EE.append(E_new)
            else:
                #print("Movement rejected")
                EE.append(E_old)
                
                lattice[posL[set_no][0]][posL[set_no][1]][posL[set_no][2]]=0
                if chn_info[set_chnLMV][set_bdLMV][1]=="SA01":
                    lattice[x][y][z]=1
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SB01":
                    lattice[x][y][z]=2
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SC01":
                    lattice[x][y][z]=3
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SD01":
                    lattice[x][y][z]=4
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SE01":
                    lattice[x][y][z]=5
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SF01":
                    lattice[x][y][z]=6
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SG01":
                    lattice[x][y][z]=7
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SH01":
                    lattice[x][y][z]=8
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SI01":
                    lattice[x][y][z]=9
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SJ01":
                    lattice[x][y][z]=10
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SK01":
                    lattice[x][y][z]=11
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SL01":
                    lattice[x][y][z]=12
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SM01":
                    lattice[x][y][z]=13
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SN01":
                    lattice[x][y][z]=14
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SO01":
                    lattice[x][y][z]=15
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SP01":
                    lattice[x][y][z]=16
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SQ01":
                    lattice[x][y][z]=17
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SR01":
                    lattice[x][y][z]=18
                elif chn_info[set_chnLMV][set_bdLMV][1]=="SS01":
                    lattice[x][y][z]=19
                elif chn_info[set_chnLMV][set_bdLMV][1][0]=="L":
                    lattice[x][y][z]=20

    else:
        #print("Attempt not succesfull")
        EE.append(E_old)

    return chn_info



