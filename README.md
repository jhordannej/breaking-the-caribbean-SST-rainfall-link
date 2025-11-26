# Render figures for "Breaking the Link: Warming disrupts early-season rainfall predictability in the Caribbean"
This repository contains the data and jupyter notebooks used to render Figures 1-5 for the Clarke et al. manuscript "Breaking the Link: Warming disrupts early-season rainfall predictability in the Caribbean". 

## How to run the notebooks
#### Alternative 1: Download repository to your computer
From your command line, run the following code to create a virtual environment. The virtual environment contains all packages used to generate the plots. 
```
conda env create -f environment.yml
conda activate breaking-env

python -m ipykernel install --user --name=breaking-env
```
Then, run `jupyter-notebook`. Navgivate to `/code` folder and run notebooks. 

#### Alternative 2: View in Binder
Notebooks can be viewed and run online at [https://mybinder.org/v2/gh/jhordannej/breaking-the-caribbean-SST-rainfall-link/HEAD](https://mybinder.org/v2/gh/jhordannej/breaking-the-caribbean-SST-rainfall-link/HEAD). Navigate to the `/code` folder and run the notebooks. No need to create a virtual environment since the Binder installs all required packages in `/binder/requirements.txt` for you at build.
  
## Additional Information
### Credits
The notebooks were created by Dr. Jhordanne Jones at the University of the West Indies Mona, and is written in Python. 

### License
MIT License :copyright: Jhordanne Jones
