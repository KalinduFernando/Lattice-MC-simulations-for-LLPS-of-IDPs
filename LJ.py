import math
import numpy as np
"Initial energy introduction to the lattice molecules"
energy_mat = []
with open ('in_param.txt') as param_file:
    line_no = 1
    for line in param_file:
         info = line.split()

         if line_no >6:
             energy_mat.append(info[2:])
         line_no +=1
        


##def search_partner(lattice,chn_info,x,y,z,x1,y1,z1,chn,bd,no_1,no_2,Pr_E):
##    
##    if lattice[x][y][z]==no_1 and lattice[x1][y1][z1]==no_2:
##      lattice[x1][y1][z1]=(lattice[x1][y1][z1])*-1
##      lattice[x][y][z]=(lattice[x][y][z])*-1
##      if len(chn_info[chn][bd])==3:
##          chn_info[chn][bd].append(Pr_E)
##      else:
##          chn_info[chn][bd].pop()
##          chn_info[chn][bd].append(Pr_E)
##          
##    return lattice
          
def search_partner(lattice,chn_info,x,y,z,x1,y1,z1,chn,bd,energy_mat):
    
    for eg_ln in range(0,len(energy_mat)):
        for eg_tm in range(0,len(energy_mat)):
            
            if lattice[x][y][z]==eg_ln and lattice[x1][y1][z1]==eg_tm:
              lattice[x1][y1][z1]=(lattice[x1][y1][z1])*-1
              lattice[x][y][z]=(lattice[x][y][z])*-1
              if len(chn_info[chn][bd])==3:
                  chn_info[chn][bd].append(float(energy_mat[eg_ln][eg_tm][1:]))
              else:
                  chn_info[chn][bd].pop()
                  chn_info[chn][bd].append(float(energy_mat[eg_ln][eg_tm][1:]))
                           
    return lattice
    
              
def append_energy(lattice,Nbox,chn_info):

    for chn in range(0,len(chn_info)):
        for bd in range(0,len(chn_info[chn])):
            
            x,y,z = chn_info[chn][bd][2]
            if x > 1 and x < Nbox-1 and y > 1 and y < Nbox-1 and z > 1 and z < Nbox-1 :
                
                if lattice[x][y][z]> 0 and lattice[x-1][y][z]> 0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x][y-1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x,y-1,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x][y][z-1]>0:
                    search_partner(lattice,chn_info,x,y,z,x,y,z-1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x][y+1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x,y+1,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x][y][z+1]>0:
                    search_partner(lattice,chn_info,x,y,z,x,y,z+1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x-1][y-1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y-1,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y-1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y-1,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x-1][y+1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y+1,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y+1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y+1,z,chn,bd,energy_mat)

                if lattice[x][y][z] > 0 and lattice[x-1][y][z-1]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y,z-1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x-1][y][z+1]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y,z+1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y][z+1]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y,z+1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y][z-1]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y,z-1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x-1][y-1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y-1,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x-1][y+1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y+1,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y-1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y-1,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y+1][z]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y+1,z,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x-1][y-1][z-1]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y-1,z-1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y-1][z-1]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y-1,z-1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x-1][y+1][z-1]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y+1,z-1,chn,bd,energy_mat)

                if lattice[x][y][z] > 0 and lattice[x-1][y+1][z-1]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y-1,z+1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x-1][y+1][z+1]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y+1,z+1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x-1][y-1][z+1]>0:
                    search_partner(lattice,chn_info,x,y,z,x-1,y-1,z+1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y-1][z+1]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y-1,z+1,chn,bd,energy_mat)
                        
                if lattice[x][y][z] > 0 and lattice[x+1][y+1][z+1]>0:
                    search_partner(lattice,chn_info,x,y,z,x+1,y+1,z+1,chn,bd,energy_mat)

    for i in range (0,Nbox):
        for j in range (0,Nbox):
            for k in range (0,Nbox):
                if lattice[i][j][k]<0:
                    lattice[i][j][k]=-1*(lattice[i][j][k])
    return chn_info
                    


def calculate_energy(chn_info):
    E =0
    for chn in range(0,len(chn_info)):
        for bd in range(0,len(chn_info[chn])):
        
            if len(chn_info[chn][bd])==4:
                E += chn_info[chn][bd][3]
    return E





