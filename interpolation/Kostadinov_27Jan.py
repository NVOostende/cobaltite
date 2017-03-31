#!/usr/bin/env python

from brushcutter import *

mm = '08'
cfile = '/Users/nicolasvanoostende/runs_coastaldiatoms/phytoC_Kostadinov/PSD_PFT_C_MO_clim_CCS_SeaWiFS_' + mm + '.nc'
#cfile = '/Volumes/ESM-ADMIN/data-nico/out.nc'
romsgrd = '/Users/nicolasvanoostende/runs_coastaldiatoms/CCS_7k_0-360_fred_grd.nc'

# ---------- define segments on MOM grid -----------------------
domain = obc_segment('domain', romsgrd,istart=0,iend=181,jstart=0,  jend=481,target_model='ROMS')

# ---------- define variables on each segment ------------------
C_biomass1_domain  = obc_variable(domain,'PSD_slope',geometry='line',obctype='radiation')
C_biomass2_domain  = obc_variable(domain,'Composite_standard_deviation_PSD_slope',geometry='line',obctype='radiation')
C_biomass3_domain  = obc_variable(domain,'Particle_differential_number_concentration_log10',geometry='line',obctype='radiation')
C_biomass4_domain  = obc_variable(domain,'Composite_standard_deviation_Particle_differential_number_concentration_log10',geometry='line',obctype='radiation')
C_biomass5_domain  = obc_variable(domain,'C_biomass_total',geometry='line',obctype='radiation')
C_biomass6_domain  = obc_variable(domain,'Composite_standard_deviation_C_biomass_total',geometry='line',obctype='radiation')
C_biomass7_domain  = obc_variable(domain,'picoplankton_C_fraction',geometry='line',obctype='radiation')
C_biomass8_domain  = obc_variable(domain,'Composite_standard_deviation_picoplankton_C_fraction',geometry='line',obctype='radiation')
C_biomass9_domain  = obc_variable(domain,'nanoplankton_C_fraction',geometry='line',obctype='radiation')
C_biomass10_domain = obc_variable(domain,'Composite_standard_deviation_nanoplankton_C_fraction',geometry='line',obctype='radiation')
C_biomass11_domain = obc_variable(domain,'microplankton_C_fraction',geometry='line',obctype='radiation')
C_biomass12_domain = obc_variable(domain,'Composite_standard_deviation_microplankton_C_fraction',geometry='line',obctype='radiation')
C_biomass13_domain = obc_variable(domain,'Number_of_months_participating_in_composite_calculation',geometry='line',obctype='radiation')

# ---------- interpolate each biomass variable from Kostadinov file -------------------
interp_t2s = C_biomass1_domain.interpolate_from(cfile,'PSD_slope',frame=0,depthname='',method='bilinear')
C_biomass2_domain.interpolate_from(cfile,'Composite_standard_deviation_PSD_slope',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass3_domain.interpolate_from(cfile,'Particle_differential_number_concentration_log10',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass4_domain.interpolate_from(cfile,'Composite_standard_deviation_Particle_differential_number_concentration_log10',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass5_domain.interpolate_from(cfile,'C_biomass_total',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass6_domain.interpolate_from(cfile,'Composite_standard_deviation_C_biomass_total',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass7_domain.interpolate_from(cfile,'picoplankton_C_fraction',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass8_domain.interpolate_from(cfile,'Composite_standard_deviation_picoplankton_C_fraction',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass9_domain.interpolate_from(cfile,'nanoplankton_C_fraction',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass10_domain.interpolate_from(cfile,'Composite_standard_deviation_nanoplankton_C_fraction',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass11_domain.interpolate_from(cfile,'microplankton_C_fraction',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass12_domain.interpolate_from(cfile,'Composite_standard_deviation_microplankton_C_fraction',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)
C_biomass13_domain.interpolate_from(cfile,'Number_of_months_participating_in_composite_calculation',frame=0,depthname='',method='bilinear',interpolator=interp_t2s)

# ---------- list segments and variables to be written -------
list_segments = [domain]

list_variables = [C_biomass1_domain,C_biomass2_domain,C_biomass3_domain,C_biomass4_domain,C_biomass5_domain,C_biomass6_domain,\
		  C_biomass7_domain,C_biomass8_domain,C_biomass9_domain,C_biomass10_domain,C_biomass11_domain,C_biomass12_domain,\
		  C_biomass13_domain] 

list_vectvariables = []

#----------- time --------------------------------------------
time = C_biomass1_domain.timesrc

# ---------- write to file -----------------------------------
lib_ioncdf.write_obc_file(list_segments,list_variables,list_vectvariables,time,output='Carbon_phytosizeclass_CCS_' + mm + '.nc')
