#!/bin/bash
cutoff=6
in_cutoff=6
pdb_file='./Examples/PDB/native_rcsb_xleap.pdb'
fb_grid='fibonacci-400-grid-points.txt'
pdb_folder='./Examples/PDB'

echo 'Calculating energy for PDB structure' $pdb_file 'with cutoff=6 and in_cutoff=6'

python bio_Nepre_I.py -s $pdb_file 6 fibonacci-400-grid-points.txt 6

echo 'Calculating energy for PDB structures in a folder  ' $pdb_folder 'with cutoff=6 and in_cutoff=6'

python bio_Nepre_I.py -m $pdb_folder/ $cutoff $fb_grid $in_cutoff

