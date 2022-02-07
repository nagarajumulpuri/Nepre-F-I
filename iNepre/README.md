#### iNepre ####
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
![image](https://user-images.githubusercontent.com/92762541/140533023-353f9937-4dff-4b10-9bc9-a5fbd0f09f7c.png)

For single protein potential energy calculate, choose a cutoff (**6** angstrom eg.) and turn on **-s ** flag:

#### Print results to the termial ####
![image](https://user-images.githubusercontent.com/92762541/140532432-63d8b0d2-3995-41b9-a0f1-6a24700faef1.png)

#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
![image](https://user-images.githubusercontent.com/92762541/140532018-b2911493-5e99-4296-9f3f-7fcef26fe224.png)

For **multi-object** calculation, you can use **-m** flag:
#### Print results to the terminal ####
<img width="797" alt="image" src="https://user-images.githubusercontent.com/92762541/152834676-d0d716a1-b27e-4943-9901-45fcf8b16a41.png">

The results are:
<img width="946" alt="image" src="https://user-images.githubusercontent.com/92762541/152836268-a9e2999a-2fba-461f-be9c-64aecc7393bb.png">
<img width="945" alt="image" src="https://user-images.githubusercontent.com/92762541/152836517-903ad223-b70f-46c6-9e9d-22bb55f8a0ce.png">
<img width="943" alt="image" src="https://user-images.githubusercontent.com/92762541/152836711-afaa01ef-8e32-4d79-a7d2-dfebb22c995b.png">
<img width="943" alt="image" src="https://user-images.githubusercontent.com/92762541/152836957-85df515e-7656-4e5f-92df-2ed9df37b38f.png"> \
Note: Complete list of resutls of PDB1 protein complex was given in Example folder with file name "results_PDB1.txt"

#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
![image](https://user-images.githubusercontent.com/92762541/140536484-891f8d3b-2950-42a6-87c2-8c8c4b72d37a.png)



