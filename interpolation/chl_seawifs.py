#!/usr/bin/env python

from brushcutter import *

romsgrd  = '/Users/nicolasvanoostende/runs_coastaldiatoms/CCS_7k_0-360_fred_grd.nc'

import numpy as np

for kt in np.arange(12):
	mm = str(kt+1).zfill(2) # month number
	cfile = '/Users/nicolasvanoostende/runs_coastaldiatoms/seawifs/chl_clim' + mm + '_seawifs.nc'

	# ---------- define segments on MOM grid -----------------------
	domain = obc_segment('CCS', romsgrd, istart=0, iend=181, jstart=0, jend=481, target_model='ROMS')
	
	# ---------- define variables on each segment ------------------
	chl_seawifs1_domain = obc_variable(domain,'chl',geometry='line',obctype='radiation')
	
	# ---------- interpolate remote sensing variable from SeaWiFS file -------------------
	interp_t2s = chl_seawifs1_domain.interpolate_from(cfile,'chlor_a',frame=0,depthname='',method='bilinear')
	#C_biomass2_domain.interpolate_from(cfile,'Composite_standard_deviation_PSD_slope',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
	
	# ---------- list segments and variables to be written -------
	list_segments = [domain]
	
	list_variables = [chl_seawifs1_domain]
	
	list_vectvariables = []
	
	#----------- time --------------------------------------------
	time = chl_seawifs1_domain.timesrc
	
	# ---------- mask spurious interpolations over land ------------
	
	import pyroms
	
	grd = pyroms.grid.get_ROMS_grid('CCS1')
	lsm = grd.hgrid.mask_rho
	
	#for kz in np.arange(grd.vgrid.N):
	chl_seawifs1_domain.data[:,:] = chl_seawifs1_domain.data[:,:] * lsm
	
	# ---------- write to file -----------------------------------
	lib_ioncdf.write_obc_file(list_segments,list_variables,list_vectvariables,time,output='chl_clim_seawifs_CCS_' + mm + '.nc')

#---- concatenate monthly nc files --------
#ncrcat chl_clim_seawifs_CCS_01.nc chl_clim_seawifs_CCS_02.nc chl_clim_seawifs_CCS_03.nc chl_clim_seawifs_CCS_04.nc chl_clim_seawifs_CCS_05.nc chl_clim_seawifs_CCS_06.nc chl_clim_seawifs_CCS_07.nc chl_clim_seawifs_CCS_08.nc chl_clim_seawifs_CCS_09.nc chl_clim_seawifs_CCS_10.nc chl_clim_seawifs_CCS_11.nc chl_clim_seawifs_CCS_12.nc -o chl_clim_seawifs_CCS_monthly.nc
