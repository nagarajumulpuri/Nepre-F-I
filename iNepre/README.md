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
<img width="800" alt="image" src="https://user-images.githubusercontent.com/92762541/152829715-351ddbaa-ef73-44d0-ace2-ee28344e8959.png">
![image](https://user-images.githubusercontent.com/92762541/140534786-998de96a-1103-46ee-aef7-c4d8b08d1d08.png)

The results are:


#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
![image](https://user-images.githubusercontent.com/92762541/140536484-891f8d3b-2950-42a6-87c2-8c8c4b72d37a.png)



