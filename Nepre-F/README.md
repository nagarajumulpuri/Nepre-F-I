Nepre-F
Scoring Function based on Neighbourhood Preference Statistics
Usage
The running folder should contain:
bio_Nepre_F.py (Main program)
{cutoff}.npy (Energy matrix)
fb_grid.txt (fibonacci grid points parameter file)
where cutoff is a number from 4 to 10, describing the distance threshold for the neighborhood. We provide one cutoff option with cutoff 6 angstrom, previous studies shows 6 angstrom is optimal choice for the calculation.
You can see help information by typing:
Nepre@liulab:~$ python bio_Nepre_F.py -h
usage: bio_Nepre_F.py [-h] [-s | -m] [-o] path  cutoff  fb_grid
Nepre-F Scroing Function Created by CSRC
positional arguments:
	path		PDB file path of folder path
	cutoff		cutoff parameter for Nepre-F
	fb_grid	fibonacci grid point file
optional arguments:
	-h, --help	show this help message and exit
	-s, --single	calculate single PDB
	-m, --multi	calculate a series of PDB
	-o, --output	save the results as a text file in running folder
For single protein potential energy calculate, choose a cutoff (6 angstrom e.g) and turn on -s flag:
Print results to the terminal
Nepre@liulab:~$ python bio_Nepre_F.py  -s  ../Example/PDB/native.pdb 6 fibonacci-400-grid-points.txt 
The calculation results are shown as:
Nepre Potential Energy
Using Cutoff: 6
Examples/PDB/native_rcsb_xleap.pdb [-110.28253686]
Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”)
Nepre@liulab:~$ python bio_Nepre_F.py  -s  -o  ../Example/PDB/native.pdb 6 fibonacci-400-grid-points.txt
For multi-object calculation, you can use -m flag:
Print results to the terminal
Nepre@liulab:~$ python bio_Nepre_F.py -m ./Example/PDB 6   fibonacci-400-grid-points.txt
The results are:
The Nepre Potential Energy
Using Cutoff: 6
complex_52.pdb      -156.66099826942005
complex_84.pdb      -158.0044423052302
complex_63.pdb      -155.9438907768273
complex_93.pdb      -155.95475506730966
complex_1.pdb      -156.82338377461892
complex_89.pdb      -154.96428317287447
complex_71.pdb      -153.5850382154521
complex_58.pdb      -159.10003855302227
complex_39.pdb      -156.18677049006274
complex_44.pdb      -155.47124069110575
complex_88.pdb      -158.53428340438603
complex_87.pdb      -157.48164109487107
complex_95.pdb      -157.77492732976154
complex_75.pdb      -157.26005135001122
complex_38.pdb      -154.29905825268108
complex_72.pdb      -157.8001746956553
complex_99.pdb      -157.97463892576644
complex_98.pdb      -155.92422746451126
complex_78.pdb      -155.40287920818082
complex_9.pdb      -159.4286923471188
complex_77.pdb      -154.47395322767247
complex_3.pdb      -152.8204066181026
complex_53.pdb      -157.03754227817072
complex_57.pdb      -153.97738937130597
complex_6.pdb      -156.25382180445695
complex_94.pdb      -154.8124032801678
complex_59.pdb      -157.92255987860185
complex_41.pdb      -157.41279467762945
complex_4.pdb      -158.0775707949723
complex_66.pdb      -156.99022398220544
complex_42.pdb      -155.1154529487947
complex_70.pdb      -157.4831078819987
complex_55.pdb      -156.06358311925476
complex_90.pdb      -156.75928334885506
complex_43.pdb      -154.45318642535833
complex_92.pdb      -153.09347013930974
complex_83.pdb      -158.360887066984
complex_60.pdb      -158.78001615031724
complex_37.pdb      -157.0190753151134
complex_31.pdb      -157.213236054839
complex_32.pdb      -158.43425603201413
complex_49.pdb      -156.82229463765148
complex_30.pdb      -155.89288157651708
complex_86.pdb      -156.26562349693788
complex_47.pdb      -157.3351909199175
complex_33.pdb      -154.10811996726252
complex_96.pdb      -155.24724413451654
complex_91.pdb      -157.3750267398701
complex_64.pdb      -156.64351615283218
complex_46.pdb      -157.8914498632306
complex_85.pdb      -156.9077180967203
complex_7.pdb      -155.09379693453707
complex_79.pdb      -154.61505929328504
complex_61.pdb      -155.1103805825779
complex_76.pdb      -158.40749367125596
complex_69.pdb      -156.72986661140487
complex_67.pdb      -154.9385399211609
complex_5.pdb      -157.50301309868394
complex_51.pdb      -157.5949106940575
complex_34.pdb      -155.82936101623216
complex_97.pdb      -157.66619997364674
complex_65.pdb      -159.92729009650228
complex_8.pdb      -157.50760112868684
native_rcsb_xleap.pdb      -110.28253685770267
complex_50.pdb      -155.02878812529258 

Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”)
Nepre@liulab:~$ python bio_Nepre_F.py  -m  -o  ./Example/PDB 6   fibonacci-400-grid-points.txt

