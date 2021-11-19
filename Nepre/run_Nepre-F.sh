#!/bin/bash
cutoff=6
pdb_file='./Examples/PDB/native_rcsb_xleap.pdb'
fb_grid='fibonacci-400-grid-points.txt'
pdb_folder='./Examples/PDB'

echo 'Calculating energy for PDB structure' $pdb_file 'with cutoff=6'

python bio_Nepre_F.py -s $pdb_file 6 fibonacci-400-grid-points.txt

echo 'Calculating energy for PDB structures in a folder  ' $pdb_folder 'with cutoff=6'

python bio_Nepre_F.py -m $pdb_folder/ $cutoff $fb_grid

