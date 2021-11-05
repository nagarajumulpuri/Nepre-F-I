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
![image](https://user-images.githubusercontent.com/92762541/140533023-353f9937-4dff-4b10-9bc9-a5fbd0f09f7c.png)

For single protein potential energy calculate, choose a cutoff (**6** angstrom eg.) and turn on **-s ** flag:

#### Print results to the termial ####
![image](https://user-images.githubusercontent.com/92762541/140532432-63d8b0d2-3995-41b9-a0f1-6a24700faef1.png)

![image](https://user-images.githubusercontent.com/92762541/140530281-0ad2dfcb-82ce-441c-9edc-83007ec18315.png)

#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
![image](https://user-images.githubusercontent.com/92762541/140532018-b2911493-5e99-4296-9f3f-7fcef26fe224.png)

For **multi-object** calculation, you can use **-m** flag:
#### Print results to the terminal ####
![image](https://user-images.githubusercontent.com/92762541/140534786-998de96a-1103-46ee-aef7-c4d8b08d1d08.png)

The results are:
![image](https://user-images.githubusercontent.com/92762541/140535772-8ead68bb-0147-4e91-bf50-d95a4417192c.png)
![image](https://user-images.githubusercontent.com/92762541/140535902-34b1fbc4-e94c-4bb7-b39e-6d42037c319f.png)
![image](https://user-images.githubusercontent.com/92762541/140536056-3940c592-08b3-423e-af29-82f4a4f3c036.png)

#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
![image](https://user-images.githubusercontent.com/92762541/140536484-891f8d3b-2950-42a6-87c2-8c8c4b72d37a.png)



