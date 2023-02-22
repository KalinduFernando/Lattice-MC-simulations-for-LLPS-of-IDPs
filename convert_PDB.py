# 1 -  6        Record name     "ATOM  "                                            
# 7 - 11        Integer         Atom serial number.                   
#13 - 16        Atom            Atom name.                            
#17             Character       Alternate location indicator.         
#18 - 20        Residue name    Residue name.                         
#22             Character       Chain identifier.                     
#23 - 26        Integer         Residue sequence number.              
#27             AChar           Code for insertion of residues.       
#31 - 38        Real(8.3)       Orthogonal coordinates for X in Angstroms.                       
#39 - 46        Real(8.3)       Orthogonal coordinates for Y in Angstroms.                            
#47 - 54        Real(8.3)       Orthogonal coordinates for Z in Angstroms.                            
#55 - 60        Real(6.2)       Occupancy.                            
#61 - 66        Real(6.2)       Temperature factor (Default = 0.0).                   
#73 - 76        LString(4)      Segment identifier, left-justified.   
#77 - 78        LString(2)      Element symbol, right-justified.      
#79 - 80        LString(2)      Charge on the atom.  

a=open("out_trj.txt","r")
#data=[]
f=open("out_trj.pdb","wt")
#bead_type={"A":"A","L":"L","B":"B"}

for line in a:
	temp=line.strip().split()
	if temp[0][0]=="[":
		#print(temp[0][0])
		temp2=line.strip().split("], [")
		#print(temp2)
		lines=[]
		MM=0
		res=1
		for j in range(len(temp2)):
			towrite=""
			temp3=temp2[j].split(",")
			atom_num=temp3[0].split("'")[1]
			#print(atom_num)
			bead_type=temp3[1].split("'")[1]
			xaxis=temp3[2].split("[")[1]
			yaxis=temp3[3].strip()
			zaxis=temp3[4].strip().split("]")[0]

			NN=str(MM)
			atomnum=((5-len(NN))*" "+NN)
			atomname=((5-len(bead_type))*" "+bead_type)
			res_num=(4-len(str(res)))*" "+str(res)
			#print(res_num)
			towrite+=("ATOM  "+atomnum+atomname+" RES  "+res_num+"    ")
			#column 31 
			x_axis=(8-len(xaxis))*" "+xaxis
			y_axis=(8-len(yaxis))*" "+yaxis
			z_axis=(8-len(zaxis))*" "+zaxis
			towrite+=x_axis+y_axis+z_axis+"\n"
			f.write(towrite)
			if atom_num=="67":
	 			#f.write("TER\n")
	 			res+=1
			MM+=1
			#print(MM)
		f.write("END\n")
		
                
			
