#!/usr/bin/env python

import pyroms
from brushcutter import *

#for kt in np.arange(12):
#	mm = str(kt+1).zfill(2) # month number
mm = '01'
cfile = '/Users/nicolasvanoostende/runs_coastaldiatoms/seawifs/chl_clim' + mm + '_seawifs.nc'
#cfile = '/Users/nicolasvanoostende/runs_coastaldiatoms/seawifs/Smo' + mm + '.L3m_MC_CHL_chlor_a_9km.nc'
#cfile = '/Volumes/ESM-ADMIN/data-nico/out.nc'
romsgrd  = '/Users/nicolasvanoostende/runs_coastaldiatoms/CCS_7k_0-360_fred_grd.nc'
grd      = pyroms.grid.get_ROMS_grid('CCS1')
landmask = grd.hgrid.mask_rho.copy()

# ---------- define segments on MOM grid -----------------------
domain = obc_segment('CCS', romsgrd, istart=0, iend=181, jstart=0, jend=481, target_model='ROMS')

# ---------- define variables on each segment ------------------
chl_seawifs1_domain = obc_variable(domain,'chl',geometry='line',obctype='radiation')
#chl_seawifs2_domain = obc_variable(domain,'lat',geometry='line',obctype='radiation')
#chl_seawifs3_domain = obc_variable(domain,'lon',geometry='line',obctype='radiation')

# ---------- interpolate remote sensing variable from SeaWiFS file -------------------
interp_t2s = chl_seawifs1_domain.interpolate_from(cfile,'chlor_a',frame=0,depthname='',method='bilinear')
#C_biomass2_domain.interpolate_from(cfile,'Composite_standard_deviation_PSD_slope',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)

# ---------- mask spurious interpolations over land ------------

# data_domain = data * landmask
 
# ---------- list segments and variables to be written -------
list_segments = [domain]

list_variables = [chl_seawifs1_domain]

list_vectvariables = []

#----------- time --------------------------------------------
time = chl_seawifs1_domain.timesrc

# ---------- write to file -----------------------------------
lib_ioncdf.write_obc_file(list_segments,list_variables,list_vectvariables,time,output='chl_clim_seawifs_CCS_' + mm + '.nc')
