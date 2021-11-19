from Bio.PDB import PDBParser
from Bio.PDB.PDBIO import PDBIO
from Bio.PDB.Chain import Chain
import numpy as np
import math
import argparse
import os
import sys


def EuclideanDistances(A, B):
    BT = B.transpose()
    vecProd = A * BT
    SqA =  A.getA()**2
    sumSqA = np.matrix(np.sum(SqA, axis=1))
    sumSqAEx = np.tile(sumSqA.transpose(), (1, vecProd.shape[1]))
    SqB = B.getA()**2
    sumSqB = np.sum(SqB, axis=1)
    sumSqBEx = np.tile(sumSqB, (vecProd.shape[0], 1))
    SqED = sumSqBEx + sumSqAEx - 2*vecProd
    #SqED = np.sqrt(SqED)
    return np.matrix(SqED)

def load_EnergyMatrix(in_cutoff):
    aaDict={"ALA":{},"VAL":{},"LEU":{},"ILE":{},"PHE":{},\
            "TRP":{},"MET":{},"PRO":{},"GLY":{},"SER":{},\
            "THR":{},"CYS":{},"TYR":{},"ASN":{},"GLN":{},\
            "HIS":{},"LYS":{},"ARG":{},"ASP":{},"GLU":{},}

    List = sorted(list(aaDict.keys()))
    f = open("./" + str(in_cutoff) + ".npy", 'rb')
    for amino1 in List:
        for amino2 in List:
            aaDict[amino1][amino2] = np.load(f)
    f.close()
    return aaDict

def load_fb_grid(fb_grid_file):
    print('To read fibonacci grid data from file ')
    fb_array = []
    fbr = open(fb_grid_file, 'r')
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
    return fb_array

""" To read PDB file and extract coordinates within 6 Angstroms from an Amino Acid"""
def calculate_Energy(f,matrix,cutoff,fb_array,in_cutoff):
    structure = f
    residues_i = list(structure.get_residues())
    residues_j = list(structure.get_residues())
    all_amino = ["ALA","VAL","LEU","ILE","PHE","TRP","MET","PRO","GLY","SER","THR","CYS","TYR","ASN","GLN",\
                    "HIS","LYS","ARG","ASP","GLU"]

    record_CA_coord = []
    record_N_coord = []
    record_side_coord = []
    record_Axis = []

    for model in structure.get_list():
        for chain in model.get_list():
            for residue in chain.get_list():
                N_coord = []
                CA_coord = []
                coord_i = []
                chain_name = ''
                if residue.is_disordered() and residue.get_resname() in all_amino:
                    res_id = residue.get_id()[1]
                    res_name = residue.get_resname()
                    for atom in residue.get_list():
                        if atom.is_disordered():
                            if atom.get_altloc() == 'A':
                                if atom.disordered_has_id("A"):
                                    atom.disordered_select("A")
                                    if(atom.get_id() not in ["N","CA","C","O","H"]) or (residue.get_resname() == 'GLY'):
                                        coord = atom.get_coord()
                                        coord_i.append(coord)
                                        chain_name = atom.get_full_id()[2]
                                    if(atom.get_id() == 'CA'):
                                        CA_coord = atom.get_coord()
                                    if(atom.get_id() == 'N'):
                                        N_coord = atom.get_coord()
                        else:
                            if(atom.get_id() not in ["N","CA","C","O","H"]) or (residue.get_resname() == 'GLY'):
                                coord = atom.get_coord()
                                coord_i.append(coord)
                                chain_name = atom.get_full_id()[2]
                            if(atom.get_id() == 'CA'):
                                CA_coord = atom.get_coord()
                            if(atom.get_id() == 'N'):
                                N_coord = atom.get_coord()

                else:
                    if residue.get_resname() in all_amino:
                        res_id = residue.get_id()[1]
                        res_name = residue.get_resname()
                        for atom in residue.get_list():
                            if(atom.get_id() not in ["N","CA","C","O","H"]) or (residue.get_resname() == 'GLY'):
                                coord = atom.get_coord()
                                coord_i.append(coord)
                                chain_name = atom.get_full_id()[2]
                            if(atom.get_id() == 'CA'):
                                CA_coord = atom.get_coord()
                            if(atom.get_id() == 'N'):
                                N_coord = atom.get_coord()


                if(len(CA_coord) == 0 or len(N_coord) == 0 or len(coord_i) == 0):
                    continue
                else:
                    CA_coord = np.array(CA_coord)
                    N_coord = np.array(N_coord)
                    coord_i = np.array(coord_i)
                    centroid_i = coord_i.sum(axis=0)
                    centroid_i = centroid_i / len(coord_i)

                    record_side_coord.append([chain_name, res_id, res_name])
                    record_side_coord[-1].extend(centroid_i)
                    record_CA_coord.append([chain_name, res_id, res_name])
                    record_CA_coord[-1].extend(CA_coord)
                    record_N_coord.append([chain_name, res_id, res_name])
                    record_N_coord[-1].extend(N_coord)

                    xAxis = N_coord - centroid_i
                    yAxis = CA_coord - centroid_i
                    xAxis = xAxis / np.sqrt(np.dot(xAxis, xAxis))
                    yAxis = yAxis - (np.dot(yAxis, xAxis)) * xAxis
                    yAxis = yAxis / np.sqrt((np.dot(yAxis, yAxis)))
                    zAxis = np.cross(xAxis, yAxis)
                    xyzAxis = [xAxis, yAxis, zAxis]
                    xyzAxis = np.array(xyzAxis, dtype=float)
                    record_Axis.append([chain_name, res_id, res_name])
                    record_Axis[-1].extend(xyzAxis)



            
    vector = []
    for k in record_side_coord:
        vector.append(k[3:6])

    vector=np.matrix(vector)
    distanceMatrix=np.asarray(EuclideanDistances(vector, vector))

    tot_res = len(record_side_coord)
    E = 0
    cutoff = cutoff**2
    inter_cutoff = in_cutoff * in_cutoff
    old_chain = []
    inter_residues = []

    for i1 in range(tot_res):
        for i2 in range(tot_res):
            if(record_side_coord[i1][0] != record_side_coord[i2][0]) and (record_side_coord[i2][0] not in old_chain):
                if distanceMatrix[i1][i2] < inter_cutoff:
                    tmp1 = record_side_coord[i1][0:2]
                    tmp2 = record_side_coord[i2][0:2]

                    #print(tmp1, tmp2)

                    x_axis_i1 = record_Axis[i1][3]
                    y_axis_i1 = record_Axis[i1][4]
                    z_axis_i1 = record_Axis[i1][5]

                    x_axis_i2 = record_Axis[i2][3]
                    y_axis_i2 = record_Axis[i2][4]
                    z_axis_i2 = record_Axis[i2][5]

                    ###********************************************###
                    ### to add interface residue energy to E       ###
                    ###********************************************###
                    center_i1 = record_side_coord[i1][3:6]
                    center_i2 = record_side_coord[i2][3:6]
                    center_i1 = np.array(center_i1)
                    center_i2 = np.array(center_i2)
                    x1 = np.dot((center_i2 - center_i1), x_axis_i1)
                    y1 = np.dot((center_i2 - center_i1), y_axis_i1)
                    z1 = np.dot((center_i2 - center_i1), z_axis_i1)
                    x2 = np.dot((center_i2 - center_i1), x_axis_i2)
                    y2 = np.dot((center_i2 - center_i1), y_axis_i2)
                    z2 = np.dot((center_i2 - center_i1), z_axis_i2)
                    rho1 = np.sqrt(x1**2+y1**2+z1**2)
                    theta1 = np.arccos(z1/rho1)
                    phi1 = np.arctan2(y1,x1)
                    rho2 = np.sqrt(x2**2+y2**2+z2**2)
                    theta2 = np.arccos(z2/rho2)
                    phi2 = np.arctan2(y2,x2)
                    
                    theta_phi_dist1 = np.sqrt((fb_array[:,0] - theta1 )**2 + (fb_array[:,1] - phi1)**2)
                    indexes1 = [i for i, x in enumerate(theta_phi_dist1) if x == np.min(theta_phi_dist1)]
                    indexes1 = np.array(indexes1)
                    E += matrix[record_side_coord[i1][2]][record_side_coord[i2][2]][indexes1] / rho1

                    theta_phi_dist2 = np.sqrt((fb_array[:,0] - theta2 )**2 + (fb_array[:,1] - phi2)**2)
                    indexes2 = [i for i, x in enumerate(theta_phi_dist2) if x == np.min(theta_phi_dist2)]
                    indexes2 = np.array(indexes2)
                    E += matrix[record_side_coord[i2][2]][record_side_coord[i1][2]][indexes2] / rho2
                    ###***************************************************************************************###


                    if tmp1 not in inter_residues:
                        inter_residues.append(tmp1)
                        for i3 in range(tot_res):
                            if(i1 == i3):
                                continue
                            else:
                                if distanceMatrix[i1][i3] < cutoff:
                                    center_i1 = record_side_coord[i1][3:6]
                                    center_i2 = record_side_coord[i3][3:6]
                                    center_i1 = np.array(center_i1)
                                    center_i2 = np.array(center_i2)

                                    x = np.dot((center_i2 - center_i1), x_axis_i1)
                                    y = np.dot((center_i2 - center_i1), y_axis_i1)
                                    z = np.dot((center_i2 - center_i1), z_axis_i1)
                                    rho = np.sqrt(x**2+y**2+z**2)
                                    theta = np.arccos(z/rho)
                                    phi = np.arctan2(y,x)

                                    theta_phi_dist = np.sqrt((fb_array[:,0] - theta )**2 + (fb_array[:,1] - phi)**2)
                                    indexes = [i for i, x in enumerate(theta_phi_dist) if x == np.min(theta_phi_dist)]
                                    indexes = np.array(indexes)
                                    E += matrix[record_side_coord[i1][2]][record_side_coord[i3][2]][indexes] / rho

                    
                    if tmp2 not in inter_residues:
                        inter_residues.append(tmp2)
                        for i4 in range(tot_res):
                            if(i2 == i4):
                                continue
                            else:
                                if distanceMatrix[i2][i4] < cutoff :
                                    center_i1 = record_side_coord[i2][3:6]
                                    center_i2 = record_side_coord[i4][3:6]
                                    center_i1 = np.array(center_i1)
                                    center_i2 = np.array(center_i2)

                                    x = np.dot((center_i2 - center_i1), x_axis_i2)
                                    y = np.dot((center_i2 - center_i1), y_axis_i2)
                                    z = np.dot((center_i2 - center_i1), z_axis_i2)
                                    rho = np.sqrt(x**2+y**2+z**2)
                                    theta = np.arccos(z/rho)
                                    phi = np.arctan2(y,x)

                                    theta_phi_dist = np.sqrt((fb_array[:,0] - theta )**2 + (fb_array[:,1] - phi)**2)
                                    indexes = [i for i, x in enumerate(theta_phi_dist) if x == np.min(theta_phi_dist)]
                                    indexes = np.array(indexes)
                                    E += matrix[record_side_coord[i2][2]][record_side_coord[i4][2]][indexes] / rho

        old_chain.append(record_side_coord[i1][0])
        #print(inter_residues)

    return E



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Nepre-F Scoring Function Created by CSRC")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s","--single",help="calculate single PDB",action="store_true")
    group.add_argument("-m","--multi",help="calculate a series of PDB",action="store_true")
    parser.add_argument("-o","--output",help="save the results as a text file in running folder",action="store_true")
    parser.add_argument("path",help="PDB file path of folder path")
    parser.add_argument("cutoff",type=int,help="cutoff parameter for Nepre-F")
    parser.add_argument("fb_grid" , help="fibonacci grid parameter file")
    parser.add_argument("in_cutoff",type=int, help="cutoff parameter for interfacial residues")
    args = parser.parse_args()

    if(args.single == True):
        c = args.cutoff
        in_c = args.in_cutoff
        fb_grid_file = args.fb_grid
        fb_array = load_fb_grid(fb_grid_file)
        matrix = load_EnergyMatrix(in_c)
        p = args.path
        #parser = PDBParser(PERMISSIVE=True, QUIET=False)
        pdb_id = p[(-len('.pdb')-4):-len('.pdb')]
        f = PDBParser(QUIET=True).get_structure(pdb_id, p)
        #f = parser.get_structure(pdb_id, p)
        E = calculate_Energy(f,matrix,c, fb_array, in_c)
        print("Nepre Potential Energy")
        print("Using Cutoff:",c)
        print(p,E)
        if(args.output == True):
            with open("./latest_restults.txt", "w") as fwout:
                fwout.write("Nepre Potential Energy")
                fwout.write('\n')
                fwout.write("Using Cutoff: " + str(c))
                fwout.write('\n')
                fwout.write(p + '\t' + str(E))
                fwout.write('\n')
    
    if(args.multi == True):
        c = args.cutoff
        in_c = args.in_cutoff
        fb_grid_file = args.fb_grid
        fb_array = load_fb_grid(fb_grid_file)
        matrix = load_EnergyMatrix(in_c)
        folder_path = args.path
        file_list = []
        for pdb_file in os.listdir(folder_path):
            file_list.append(pdb_file)
        E = []
        if(folder_path[-1] != '/'):
            folder_path += '/'
        for pdb_file in file_list:
            pdb_path = folder_path + pdb_file
            #parser = PDBParser(PERMISSIVE=True) 
            pdb_id = pdb_path[(-len('.pdb')-4):-len('.pdb')]
            f = PDBParser(QUIET=True).get_structure(pdb_id, pdb_path)
            #f = parser.get_structure(pdb_id, pdb_path)
            E.append(calculate_Energy(f,matrix,c,fb_array,in_c))
        if(args.output == True):
            with open("./latest_restults.txt", "w") as fwout:
                fwout.write("Nepre Potential Energy")
                fwout.write('\n')
                fwout.write("Using Cutoff: " + str(c))
                fwout.write('\n')
                for i in range(len(E)):
                    dd = str(file_list[i]) + '\t\t' + str(float(E[i]))
                    fwout.write(dd)
                    #fwout.write(file_list[i] + '\t' + str(E[i]))
                    fwout.write('\n')

            #save_file = open("./modeller-results/1bbh.txt","wb")
            #save_file.write("Nepre Potential Energy" + '\n')
            #save_file.write("Using Cutoff:" + str(c) + '\n')
            #for i in range(len(E)):
            #    save_file.write(file_list[i] + '\t' + str(E[i]))
            #    save_file.write('\n')
            #save_file.close()

        print("Nepre Potential Energy")
        print("Using Cutoff:",c)
        for i in range(len(E)):
            output = str(file_list[i]) + '\t\t' + str(float(E[i]))
            print(output)
    



