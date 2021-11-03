import os
import math
import numpy as np
import sys

ccDict={"ALA":{},"VAL":{},"LEU":{},"ILE":{},"PHE":{},\
        "TRP":{},"MET":{},"PRO":{},"GLY":{},"SER":{},\
        "THR":{},"CYS":{},"TYR":{},"ASN":{},"GLN":{},\
        "HIS":{},"LYS":{},"ARG":{},"ASP":{},"GLU":{},}


cdDict={"ALA":{},"VAL":{},"LEU":{},"ILE":{},"PHE":{},\
        "TRP":{},"MET":{},"PRO":{},"GLY":{},"SER":{},\
        "THR":{},"CYS":{},"TYR":{},"ASN":{},"GLN":{},\
        "HIS":{},"LYS":{},"ARG":{},"ASP":{},"GLU":{},}


if __name__ == "__main__":
    
    args = sys.argv[1:]
    if(len(args) != 4):
      print ("\n usage: python ExtractEnergyDistribute.py <local_coord.txt> <cutoff> <fb_grid_file.txt> <pairing_frequency_file>")
      exit()

    coord_file = args[0]
    cutoff = int(args[1])
    fb_grid_data = args[2]
    neighboring_frequency_data = args[3]
   
    List = ccDict.keys()
    List.sort()
    fr = open(neighboring_frequency_data)
    i = 0
    for line in fr.readlines():
        line=line.strip().split()
        for j in range(20):
            ccDict[List[i]][List[j]]=float(line[j])
        i += 1
    fr.close()

    emptyarea = {}
   
    print("Start to read coordinate.txt")
    fr=open(coord_file, 'r')
    amino1=''
    amino2=''
    
    #line = fr.readline()
    for line in fr.readlines():
        line=line.rstrip('\n')
        if line=='':
            continue

        if len(line)==3:
            if amino2=='VAL' or amino1=='':
                amino1=line
                amino2=''
            else:
                amino2=line
        else:
            line=line.split()
            if amino2 not in cdDict[amino1]:
                cdDict[amino1][amino2]=[[float(line[0]),float(line[1]),float(line[2])]]
            else:
                cdDict[amino1][amino2].append([float(line[0]),float(line[1]),float(line[2])])
    fr.close()

    print('To read fibonacci grid data from file ')
    fb_array = []
    fbr = open(fb_grid_data, 'r')
    for line in fbr.readlines():
        line = line.rstrip('\n')
        if line == '':
           continue
        else:
            line=line.split()
            fb_array.append(line)

    fb_array=np.array(fb_array)
    fb_array = fb_array.astype(np.float)
    fb_array = np.round(fb_array, 3)
    N_fb_grids = len(fb_array)
        
    for amino1 in cdDict:
        for amino2 in cdDict[amino1]:
            emp = 0
            dualArray=np.zeros((N_fb_grids))
            for coor in cdDict[amino1][amino2]:
                coor = np.array(coor)
                rho = sum(coor**2)**0.5
                theta = np.arccos(coor[2]/rho)
                theta = round(theta, 3)
                phi = np.arctan2(coor[1],coor[0])
                phi = round(phi, 3)

                theta_phi_dist = np.sqrt((fb_array[:,0] - theta )**2 + (fb_array[:,1] - phi)**2)
                indexes = [i for i, x in enumerate(theta_phi_dist) if x == np.min(theta_phi_dist)]
                indexes = np.array(indexes)
                #phi_diff = np.abs(fb_array[indexes, 1] - phi)
                #phi_min_index = [i for i, x in enumerate(phi_diff) if x == np.min(phi_diff)]
                #phi_min_index = np.array(phi_min_index)


                #fb_point = indexes[phi_min_index]
                fb_theta = fb_array[indexes, 0]
                fb_phi = fb_array[indexes, 1]
                fb_point = indexes
                """
                with open('theta-phi-values.txt', 'a') as ftheta:
                    #ind = str(indexes) + '\t' + str(phi_min_index)
                    ind = str(indexes)
                    ftheta.write(ind)
                    ftheta.write('\n')
                    ftheta.write('above are theta, phi indexes')
                    ftheta.write('\n')
                    #tmp = str(theta) + '\t' + str(phi) + '\t' + str(fb_theta) + '\t' + str(fb_phi)
                    tmp = str(theta) + '\t' + str(phi)  + '\t' + str(fb_theta) + '\t' + str(fb_phi)
                    ftheta.write(tmp)
                    ftheta.write('\n')
                """

                if(rho < cutoff):
                    dualArray[fb_point] += 1.0


            #print("Start to find min data")
            mindata = None
            for fb_point in range(N_fb_grids):
                if(mindata == None and dualArray[fb_point] != 0):
                     mindata = dualArray[fb_point]
                if(mindata > dualArray[fb_point] and dualArray[fb_point] != 0):
                     mindata = dualArray[fb_point]
            #print("Start to check empty area")
            for fb_point in range(N_fb_grids):
                if dualArray[fb_point] == 0:
                     dualArray[fb_point] = mindata
                     emp += 1
            dualArray = dualArray / dualArray.sum()

            '''
            Integral = np.ones((N_fb_grids))
            for j in range(N_fb_grids):
                k = fb_array[j, 0]
                
                
                if j+1 == N_fb_grids:
                    l = 0
                else:
                    l = fb_array[j+1, 0]
                Integral[j] = Integral[j]*(np.cos(k)-np.cos(l))

            Integral = Integral / Integral.sum()
            '''
            Integral = 1.0 / N_fb_grids
            dualArray = dualArray / Integral

            cdDict[amino1][amino2] = ccDict[amino1][amino2]-np.log(dualArray)
            emptyarea[amino1+'-'+amino2] = emp

    f = file(str(cutoff) + ".npy",'wb')
    for amino1 in List:
        for amino2 in List:
            np.save(f, cdDict[amino1][amino2])

       
