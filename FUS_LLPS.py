import numpy as np
import random as rd
import matplotlib.pyplot as plt
import time
import pickle
import localmove as lm
import slitheringsnakemove as ssm
import translationmove as tm
import endrotationmove as erm
#import visualization as vsu

start = time.time()

Nbox = 20             						# Number of lattice sites in the main lattice
lattice = np.zeros((Nbox,Nbox,Nbox),dtype = int) 			# Generation of lattice
chain_no = 4
MC_steps = 10
bd_info = []


with open ('in_structure.txt', 'r') as structure:
     line_no = 1
     for line in structure:
         info = line.split()

         if line_no >3:
             bd_info.append(info[1:])
         line_no +=1
length = len(bd_info)        
#print(bd_info)
#print(chn_length)

chn_info=[]
for no in range(chain_no):
    coord_list=[]
    
    x,y,z = (rd.randint(0,Nbox-1),rd.randint(0,Nbox-1),rd.randint(0,Nbox-1))
    for i in range(length):
         coord=[]
         list2 = []
         #if x > 1 and x < Nbox-1 and y > 1 and y < Nbox-1 and z > 1 and z < Nbox-1:
         if x > 0: 
            if lattice[x-1][y][z] == 0:
                list2.append([x-1,y,z]) 

         if x < Nbox-1:
            if lattice[x+1][y][z] == 0:
                list2.append([x+1,y,z])
                
##         if x == 0:
##             if lattice[Nbox-1][y][z] == 0:
##                list2.append([Nbox-1,y,z])
##                
##         if x == Nbox-1:
##             if lattice[0][y][z] == 0:
##                list2.append([0,y,z])

         if y > 0:
            if lattice[x][y-1][z] == 0:                                             # Checking availability to place next monomer of the chain
                list2.append([x,y-1,z])

         if y < Nbox-1:  
            if lattice[x][y+1][z] == 0:
                list2.append([x,y+1,z])

##         if y == 0:
##             if lattice[x][Nbox-1][z] == 0:
##                list2.append([x,Nbox-1,z])
##                
##         if y == Nbox-1:
##             if lattice[x][0][z] == 0:
##                list2.append([x,0,z])

         if z > 0:  
            if lattice[x][y][z-1] == 0:
                list2.append([x,y,z-1])

         if z < Nbox-1:  
            if lattice[x][y][z+1] == 0:
                list2.append([x,y,z+1])

##         if z == 0:
##             if lattice[x][y][Nbox-1] == 0:
##                list2.append([x,y,Nbox-1])
##                
##         if z == Nbox-1:
##             if lattice[x][y][0] == 0:
##                list2.append([x,y,0])

         #print(list2)          
         if(len(list2)>0):
            rand = rd.randint(0,len(list2)-1) 
            x,y,z = list2[rand][0],list2[rand][1],list2[rand][2]
            coord = list.copy(bd_info[i])
            coord.append([x,y,z])
            coord_list.append(coord)
            #print(list2)
            #print(coord)
               
            if bd_info[i][1]=="SA01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=1
            elif bd_info[i][1]=="SB01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=2
            elif bd_info[i][1]=="SC01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=3
            elif bd_info[i][1]=="SD01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=4
            elif bd_info[i][1]=="SE01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=5
            elif bd_info[i][1]=="SF01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=6
            elif bd_info[i][1]=="SG01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=7
            elif bd_info[i][1]=="SH01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=8
            elif bd_info[i][1]=="SI01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=9
            elif bd_info[i][1]=="SJ01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=10
            elif bd_info[i][1]=="SK01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=11
            elif bd_info[i][1]=="SL01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=12
            elif bd_info[i][1]=="SM01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=13
            elif bd_info[i][1]=="SN01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=14
            elif bd_info[i][1]=="SO01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=15
            elif bd_info[i][1]=="SP01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=16
            elif bd_info[i][1]=="SQ01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=17
            elif bd_info[i][1]=="SR01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=18
            elif bd_info[i][1]=="SS01":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=19
            elif bd_info[i][1][0]=="L":
               lattice[list2[rand][0]][list2[rand][1]][list2[rand][2]]=20
         else:
             for coordinates in coord_list:
                 coordinate = coordinates[-1]
                 #print(coordinate)
                 lattice[coordinate[0]][coordinate[1]][coordinate[2]] = 0
                
             coord_list=[]
             print("Assignment Rejected")                                                   # The chain assignments are rejected due to self disturbing walks 
             #x,y,z = (rd.randint(0,Nbox-1),rd.randint(0,Nbox-1),rd.randint(0,Nbox-1))
             break
    #print(len(coord_list))         
    chn_info.append(coord_list)

#vsu.draw_plot(chn_info)
#plt.savefig("Startingfig.png", dpi=1000)
print(chn_info[1][-1])
  
with open("out_trj.txt",'w') as fh:
    
    fh.write(str(chn_info)+"\n")
    
    EE=[]
    step=[]
    ssc=0
    lmc=0
    tmc=0
    erc=0
    for i in range(MC_steps):
        
        rn = rd.randint(0,3)
        if rn==0:
            ssm.SlitheringSnake_MV(chain_no,chn_info,lattice,Nbox,EE)
            fh.write(str(chn_info)+"\n")
            ssc+=1
            with open('out_lastconf', 'wb') as f:
                pickle.dump(chn_info, f)
            
        elif rn==1:
            lm.Local_MV(chain_no,length,lattice,chn_info,Nbox,EE)
            fh.write(str(chn_info)+"\n")
            lmc+=1
            with open('out_lastconf', 'wb') as f:
                pickle.dump(chn_info, f)
            
        elif rn==2:
            tm.Translation_MV(chain_no,Nbox,lattice,chn_info,EE)
            fh.write(str(chn_info)+"\n")
            tmc+=1
            with open('out_lastconf', 'wb') as f:
                pickle.dump(chn_info, f)
                
        elif rn==3:
            erm.Endrotation_MV(chain_no,length,lattice,chn_info,Nbox,EE)
            fh.write(str(chn_info)+"\n")
            erc+=1
            with open('out_lastconf', 'wb') as f:
                pickle.dump(chn_info, f)
                
        step.append(i+1)
        with open("out_cuntstep.txt",'wt') as stf:
            stf.write("Final MC step performed"+" : "+str(step[i]))
        with open("out_step.txt",'wt') as stef:
            stef.write(str(step))
        with open("out_energy.txt",'wt') as eef:
            eef.write(str(EE))
            
fig, ax = plt.subplots(1, 1)

ax.plot(step[:], EE[:], 'r-', lw=1, label='Energy')
ax.set_xlabel("No of Monte Carlo Movements")
ax.set_ylabel("Potential Energy of the System")
ax.set_title("Potential Energy vs.Monte Carlo Movements")
ax.legend()
#plt.show()
#plt.savefig("Energy.png" ,dpi =1000)

#vsu.draw_plot(chn_info)
#plt.savefig("Endingfig.png", dpi=1000)

end = time.time()

with open("out_summary.txt",'w') as fd:

    fd.write("No of IPH chains in the lattice             %f\n" %(chain_no))
    fd.write('\n')
    fd.write("Fraction of Slithering Snake Movements      %f\n" %(ssc/MC_steps))
    fd.write("Fraction of Local Movements                 %f\n" %(lmc/MC_steps))
    fd.write("Fraction of Translation Movements           %f\n" %(tmc/MC_steps))
    fd.write("Fraction of Endrotation Movements           %f\n" %(erc/MC_steps))
    fd.write("Time taken for execution:                   %f\n" %round(end-start,2))



