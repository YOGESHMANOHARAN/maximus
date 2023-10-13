import datetime as dt
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
from ncdump import ncdump

nc_f = r"C:\Users\ymnharan\OneDrive - The University of Memphis\new_pc\documents\GitHub\github_repository\STOCHASTIC DATA\CDF2_files\sgparmbeatmC1.c1.19940101.000000.cdf"  # Your filename
nc_fid = Dataset(nc_f, 'r')  # Dataset is the class behavior to open the file
                             # and create an instance of the ncCDF4 class

nc_attrs, nc_dims, nc_vars = ncdump(nc_fid)

time = nc_fid.variables['time'][:]

###### converting cdf to csv#######
# import netCDF4
# nc_file = r'file_path\file_name.nc'
# nc = netCDF4.Dataset(nc_file, mode='r')
# cols = list(nc.variables.keys())
# list_nc = []
# for c in cols:
#     list_nc.append(list(nc.variables[c][:]))
# df_nc = pd.DataFrame(list_nc)
# df_nc = df_nc.T
# df_nc.columns = cols
# df_nc.to_csv("file_path.csv", index = False)