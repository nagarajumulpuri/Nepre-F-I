In this folder:

	cc-10-Energy.txt


The pariwise energy derived based on observed frequency over expected frequency.


	preprocess.py


converts a set of PDB files to local coordinates centered around each amino acid, and save the data to coordinate.txt


	ExtractEnergyDistribute.py


compiles Nepre statistical potentials based on the data in coordinate.txt file

There is an example script in the example folder. Note that a sufficient number of structures with low redundancy are required to compile a good potential energy.


