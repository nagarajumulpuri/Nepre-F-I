#### Nepre-I ####
Scoring Function based on Neighborhood Preference Statistics based on Interfacial residues. 

#### Usage ####  
The running folder should contain:\
bio_Nepre_I.py (Main program) \
{cutoff}.npy (Energy matrix) \
fb_grid.txt (Fibonacci grid points parameter file)

In this program two cutoff values shoul be provided, one cutoff value for neighborhood residue cutoff \
value (cutoff) and another cutoff value for interfacial residue cutoff value (in_cutoff). \
Interfacial residue distance threshold (in_cutoff) value from **4** to **6** and neighborhood residue distance threshold value \
(cutoff) from **4** to **10** (recommended value is **6**). We provided three energy matrix files (in_cutoff.npy) in_cutoff \
options **4, 5,** and **6** angstroms in all cases neighborhood cutoff value are **6** angstroms.

You can see help information by typing:\
![image](https://user-images.githubusercontent.com/92762541/140528886-4bdebeac-3d7b-4181-a7e0-b9309a0f4e5b.png)

Nepre@liulab:~$python bio_Nepre_I.py -h 

usage: \
bio_Nepre_I.py  [-h] [-s|-m] [-o]   path cutoff  fb_grid  in_cutoff 

Nepre-I Scoring Function Created by CSRC \
Positional arguments: 
  * path		PDB file path of folder path 
  * cutoff		neighborhood cutoff parameter for Nepre-I 
  * fb_grid		Fibonacci grid point file 
  * in_cutoff  interfacial residue cutoff parameter for Nepre-I 

Optional arguments: \
   -h,  --help  show this help message and exit \
   -s,  --single  calculate single PDB \
   -m,  --multi  calculate a series of PDB \
   -o,  --output  save the results as a text file in running folder 

For single protein potential energy calculate, choose a cutoff (**6** angstrom eg.) and turn on **-s ** flag:

#### Print results to the termial ####

Nepre@liulab:~$ python bio_Nepre_I.py  -s  ../Example/PDB/native.pdb 6 fibonacci-400-grid-points.txt 6 \
The calculation results are shown as:
Nepre Potential Energy \
Using Cutoff: 6 \
Examples/PDB/native_rcsb_xleap.pdb [2.0297539] 
#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
Nepre@liulab:~$ python bio_Nepre_I.py  -s  -o  ../Example/PDB/native.pdb 6 fibonacci-400-grid-points.txt  6

For **multi-object** calculation, you can use **-m** flag:
#### Print results to the terminal ####
Nepre@liulab:~$ python bio_Nepre_I.py -m ./Example/PDB 6   fibonacci-400-grid-points.txt  6

The results are:
The Nepre Potential Energy
Using Cutoff: 6 \
complex_52.pdb      0.27934136604604937 \
complex_84.pdb      1.8803398177673987 \
complex_63.pdb      5.742218874905891 \
complex_93.pdb      7.670267668752434 \
complex_1.pdb      6.241319865719331 \
complex_89.pdb      -0.8186528883958015 \
complex_71.pdb      0.6496764412344058 \
complex_58.pdb      -2.267308879299487 \
complex_39.pdb      5.5758194614664776 \
complex_44.pdb      3.1516186555669496 \
complex_88.pdb      3.5200277838108156 \
complex_87.pdb      1.2497834709575772 \
complex_95.pdb      2.320245849947439 \
complex_75.pdb      3.6924455881211395 \
complex_38.pdb      3.7544312892695335 \
complex_72.pdb      0.6010132860002849 \
complex_99.pdb      1.6180529208542567 \
complex_98.pdb      2.0761606192423954 \
complex_78.pdb      2.5191994495276866 \
complex_9.pdb      3.3723615033395746 \
complex_77.pdb      1.7191631029661258 \
complex_3.pdb      6.1443260630890615 \
complex_53.pdb      2.186657890001272 \
complex_57.pdb      4.520796080525149 \
complex_6.pdb      6.764836214650217 \
complex_94.pdb      5.561301257761129 \
complex_59.pdb      1.856940618169138 \
complex_41.pdb      1.2290474054597225 \
complex_4.pdb      0.7827895058438374 \
complex_66.pdb      -2.9349699020536146 \
complex_42.pdb      7.294727064248496 \
complex_70.pdb      3.771035050346875 \
complex_55.pdb      5.107847639438728 \
complex_90.pdb      2.2481485110209927 \
complex_43.pdb      5.830793219454253 \
complex_92.pdb      11.161823578777422 \
complex_83.pdb      -3.818236031435426 \
complex_60.pdb      1.059792248210734 \
complex_37.pdb      4.178878814372677 \
complex_31.pdb      5.81094743073412 \
complex_32.pdb      -0.026419902355114405 \
complex_49.pdb      -0.6257575580187003 \
complex_30.pdb      -2.7208265609045297 \
complex_86.pdb      3.2450516926676425 \
complex_47.pdb      4.02105082352348 \
complex_33.pdb      7.252366782248512 \
complex_96.pdb      3.396854847864797 \
complex_91.pdb      5.4591617741689715 \
complex_64.pdb      2.2903115922677277 \
complex_46.pdb      1.989280419842381 \
complex_85.pdb      6.606965627435031 \
complex_7.pdb      3.780462118452803 \
complex_79.pdb      8.215875210497009 \
complex_61.pdb      4.886785541917205 \
complex_76.pdb      2.9447019798595644 \
complex_69.pdb 	    2.019392537388217 \
complex_67.pdb 		     2.576434284502398 \
complex_5.pdb      2.6867642860352134 \
complex_51.pdb      2.633940581396434 \
complex_34.pdb      1.132389611540802 \
complex_97.pdb      2.6953558018950727 \
complex_65.pdb      -2.0080791617394285 \
complex_8.pdb      2.635408600275485 \
native_rcsb_xleap.pdb      2.0297539006232377 \
complex_50.pdb      2.2194196356808367

#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
Nepre@liulab:~$ python bio_Nepre_I.py -m -o ./Example/PDB 6   fibonacci-400-grid-points.txt  6



