#!/usr/bin/env python

from lib_rewrite_O2_data import rewrite_data

dirdatain='/Users/nicolasvanoostende/runs_coastaldiatoms/WOA13/O2_diva_results.nc'
dirdataout='/Users/nicolasvanoostende/runs_coastaldiatoms/WOA13/'

O2_bottom = rewrite_data()
O2_bottom.rewrite_obs_data(fileobs=dirdatain, fileout=dirdataout + 'O2_bottom_noaa_diva.nc')


