#### Nepre ####
Scoring Function based on Neighbourhood Preference Statistics. 
#### Usage ####
The running folder should contain: \
bio_Nepre_F.py (Main program) \
{cutoff}.npy (Energy matrix) \
fb_grid.txt (fibonacci grid points parameter file) \
where cutoff is a number from **4** to **10**, describing the distance threshold for the neighborhood. We provide one cutoff option with cutoff **6** angstrom, previous studies shows **6** angstrom is optimal choice for the calculation.

You can see help information by typing:
![image](https://user-images.githubusercontent.com/92762541/140542119-38eedc61-b0af-48a9-890f-9f9f30b66ace.png)

For single protein potential energy calculate, choose a cutoff (6 angstrom e.g) and turn on **-s** flag:
#### Print results to the terminal ####
<img width="944" alt="image" src="https://user-images.githubusercontent.com/92762541/152854353-a187ac18-47e8-4bd3-8d4e-72a1013bcf6a.png">

The calculation results are shown as:
<img width="944" alt="image" src="https://user-images.githubusercontent.com/92762541/152854867-acf152a6-dd7b-4fea-9784-eda78d057bee.png">
#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
<img width="944" alt="image" src="https://user-images.githubusercontent.com/92762541/152854632-341cd232-4f26-4dce-83f9-c75e3a30dd74.png">


For multi-object calculation, you can use **-m** flag:
#### Print results to the terminal ####
<img width="947" alt="image" src="https://user-images.githubusercontent.com/92762541/152855216-dba8962a-8ad6-4d48-bdf2-ceff8b23aa6e.png">
The results are: 
<img width="944" alt="image" src="https://user-images.githubusercontent.com/92762541/152859328-c84db744-033f-4427-bd45-2744d7c7673d.png">


#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
![image](https://user-images.githubusercontent.com/92762541/140547592-06278181-41b4-47b0-a632-06d6f92514f8.png)
<img width="943" alt="image" src="https://user-images.githubusercontent.com/92762541/152859461-2264a1cd-a3d8-4096-a969-74be89b9b8f7.png">

