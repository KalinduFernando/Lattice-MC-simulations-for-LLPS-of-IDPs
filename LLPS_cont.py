import FUS_LLPS as LS
import localmove as lm
import slitheringsnakemove as ssm
import translationmove as tm
import random as rd
import endrotationmove as erm

MC_steps_done = 4
with open("Results.txt",'a') as fh:
    
    
    i=0
    EE=[]
    step=[]
    ssc=0
    lmc=0
    tmc=0
    erc=0
    for i in range(LS.MC_steps-MC_steps_done):
         
        rn = rd.randint(0,2)
        if rn==0:
            ssm.SlitheringSnake_MV(LS.chain_no,LS.chn_info,LS.lattice,LS.Nbox,EE)
            fh.write(str(LS.chn_info)+"\n")
            ssc+=1
        elif rn==1:
            lm.Local_MV(LS.chain_no,LS.length,LS.lattice,LS.chn_info,LS.Nbox,EE)
            fh.write(str(LS.chn_info)+"\n")
            lmc+=1
        elif rn==2:
            tm.Translation_MV(LS.chain_no,LS.Nbox,LS.lattice,LS.chn_info,EE)
            fh.write(str(LS.chn_info)+"\n")
            tmc+=1
        elif rn==3:
            erm.Endrotation_MV(chain_no,length,lattice,chn_info,Nbox,EE)
            fh.write(str(chn_info)+"\n")
            erc+=1
            
        step.append(i)
        with open("steps.txt",'w') as stf:
            stf.write(str(step[i]))
        
       






