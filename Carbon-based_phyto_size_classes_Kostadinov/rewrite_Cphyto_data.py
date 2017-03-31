#!/usr/bin/env python

from lib_rewrite_data import rewrite_data

dirdatain='/Users/nicolasvanoostende/runs_coastaldiatoms/phytoC_Kostadinov/'
dirdataout='/Users/nicolasvanoostende/runs_coastaldiatoms/phytoC_Kostadinov/'

june = rewrite_data()
june.rewrite_obs_data(fileobs=dirdatain + 'PSD_PFT_C_MO_climatology_SeaWiFS_06.nc',fileout=dirdataout + 'PSD_PFT_C_MO_clim_CCS_SeaWiFS_06.nc')
july = rewrite_data()
july.rewrite_obs_data(fileobs=dirdatain + 'PSD_PFT_C_MO_climatology_SeaWiFS_07.nc',fileout=dirdataout + 'PSD_PFT_C_MO_clim_CCS_SeaWiFS_07.nc')
august = rewrite_data()
august.rewrite_obs_data(fileobs=dirdatain + 'PSD_PFT_C_MO_climatology_SeaWiFS_08.nc',fileout=dirdataout + 'PSD_PFT_C_MO_clim_CCS_SeaWiFS_08.nc')
