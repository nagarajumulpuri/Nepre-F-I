**Nepre-I** \
Scoring Function based on Neighborhood Preference Statistics based on Interfacial residues. 

**Usage**  \
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
Nepre@liulab:~$python bio_Nepre_I.py -h 

usage: \
bio_Nepre_I.py  [-h] [-s|-m] [-o]   path cutoff  fb_grid  in_cutoff 

Nepre-I Scoring Function Created by CSRC \
positional arguments: 
  * path   PDB file path of folder path 
  * cutoff  neighborhood cutoff parameter for Nepre-I 
  * fb_grid  Fibonacci grid point file 
