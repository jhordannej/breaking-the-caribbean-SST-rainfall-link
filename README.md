# Render figures for "Breaking the Link: Warming disrupts early-season rainfall predictability in the Caribbean"
This repository contains the data and jupyter notebooks used to render Figures 1-4 for the Clarke et al. manuscript "Breaking the Link: Warming disrupts early-season rainfall predictability in the Caribbean". 

## How to run the notebooks
#### Alternative 1: Download repository to your computer
- From your command line, run the following code to create a virtual environment. The virtual environment contains all packages used to generate the plots. 
```
conda env create -f environment.yml
conda activate breaking-env

python -m ipykernel install --user --name=breaking-env
```
- From the virtual environment, run `jupyter-notebook`. Then, navgivate to `/code` folder and run notebooks. 

#### Alternative 2: View in Binder
Notebooks can be viewed at [https://mybinder.org/v2/gh/jhordannej/breaking-the-caribbean-SST-rainfall-link/HEAD](https://mybinder.org/v2/gh/jhordannej/breaking-the-caribbean-SST-rainfall-link/HEAD). 
- Navigate to the `/code` folder and run the notebooks. No need to create a virtual environment since the `/binder` folder does this for you at build.
  
## Credits
The notebooks were created by Dr. Jhordanne Jones, and is written in Python. 

### License
MIT License 
