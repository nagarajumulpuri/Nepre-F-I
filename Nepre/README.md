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
![image](https://user-images.githubusercontent.com/92762541/140543143-e5a166d4-d4af-4619-b558-9f27d708ff97.png)
<img width="944" alt="image" src="https://user-images.githubusercontent.com/92762541/152854143-b4e5d7ba-e6e6-48fb-9303-c25f447c58f9.png">

The calculation results are shown as:
![image](https://user-images.githubusercontent.com/92762541/140543268-61894b1e-3ad9-41a6-991e-ec1d6d8600e7.png)
#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
![image](https://user-images.githubusercontent.com/92762541/140543529-17e2501a-4b35-4cde-a5c3-d74a87271886.png)

For multi-object calculation, you can use **-m** flag:
#### Print results to the terminal ####
![image](https://user-images.githubusercontent.com/92762541/140543951-6647e487-3ff5-4308-923f-a43ca6b64983.png)
The results are:
![image](https://user-images.githubusercontent.com/92762541/140547048-2cb423d4-15a9-428c-9a18-9bc83417d246.png)
![image](https://user-images.githubusercontent.com/92762541/140547202-0f9cde14-7e2a-4e69-8af8-08a3414ad458.png)
![image](https://user-images.githubusercontent.com/92762541/140547298-17b44c2c-f515-4827-8dde-32415aaf7a9d.png)

#### Save the results in a text file (Same folder with Nepre.py with name “latest_results.txt”) ####
![image](https://user-images.githubusercontent.com/92762541/140547592-06278181-41b4-47b0-a632-06d6f92514f8.png)

