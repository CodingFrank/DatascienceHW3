import pandas as pd
import numpy as np
from netCDF4 import Dataset
 
#open a new netCDF file for writing
rootgrp = Dataset("C:\\Frankwork\\HomeWork\\DS_3\\ly_ds3.nc", "w", format="NETCDF4")
episode = rootgrp.createDimension("episode",10)
scripts = rootgrp.createDimension("scripts",10)

episode = rootgrp.createVariable("episode","S39000",("episode",))
scripts = rootgrp.createVariable("scripts","S39000",("scripts",))

rootgrp.description = "Game of Thrones scripts"
rootgrp.history = "Created by Yi Liu on 10/24/2016"

#write data to variable
df = pd.read_csv('C:\\Frankwork\\HomeWork\\DS_3\\scripts.csv', header=0)
#print(df['No#'].values)
episode[:] = df['episode'].values
scripts[:] = df['scripts'].values
rootgrp.close()

 
