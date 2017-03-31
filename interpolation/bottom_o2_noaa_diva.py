#!/usr/bin/env python

from brushcutter import *

cfile = '/Users/nicolasvanoostende/runs_coastaldiatoms/WOA13/O2_bottom_noaa_diva.nc'
#cfile = '/Volumes/ESM-ADMIN/data-nico/out.nc'
romsgrd = '/Users/nicolasvanoostende/runs_coastaldiatoms/CCS_7k_0-360_fred_grd.nc'

# ---------- define segments on MOM grid -----------------------
domain = obc_segment('domain', romsgrd, istart=0, iend=181, jstart=0, jend=481, target_model='ROMS')

# ---------- define variables on each segment ------------------

bottom_o2_noaa_domain = obc_variable(domain,'O2_bottom', geometry='line', obctype='radiation')

# ---------- interpolate each variable from nc file -------------------
interp_t2s = bottom_o2_noaa_domain.interpolate_from(cfile,'O2_bottom',frame=0,depthname='',method='bilinear')
#C_biomass13_domain.interpolate_from(cfile,'Number_of_months_participating_in_composite_calculation',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)

# ---------- list segments and variables to be written -------
list_segments = [domain]

list_variables = [bottom_o2_noaa_domain]

list_vectvariables = []

#----------- time --------------------------------------------
time = bottom_o2_noaa_domain.timesrc

# ---------- write to file -----------------------------------
lib_ioncdf.write_obc_file(list_segments,list_variables,list_vectvariables,time,output='brushcutter_O2_diva_results.nc')
