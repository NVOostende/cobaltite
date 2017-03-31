import os
import os.path
import numpy as np
import netCDF4 as nc

class rewrite_data():

	def __init__(self):
		return None

	def rewrite_obs_data(self,fileobs='',timevalue=0,fileout='./out.nc'):
		fid  = nc.Dataset(fileobs)
		var1 = fid.variables['PSD_slope'][:]
		var2 = fid.variables['Composite_standard_deviation_PSD_slope'][:]
		var3 = fid.variables['Particle_differential_number_concentration_log10'][:]
		var4 = fid.variables['Composite_standard_deviation_Particle_differential_number_concentration_log10'][:]
		var5 = fid.variables['C_biomass_total'][:]
		var6 = fid.variables['Composite_standard_deviation_C_biomass_total'][:]
		var7 = fid.variables['picoplankton_C_fraction'][:]
		var8 = fid.variables['Composite_standard_deviation_picoplankton_C_fraction'][:]
		var9 = fid.variables['nanoplankton_C_fraction'][:]
		var10 = fid.variables['Composite_standard_deviation_nanoplankton_C_fraction'][:]
		var11 = fid.variables['microplankton_C_fraction'][:]		
		var12 = fid.variables['Composite_standard_deviation_microplankton_C_fraction'][:]
		var13 = fid.variables['Number_of_months_participating_in_composite_calculation'][:]		
		lat  = fid.variables['Grid_Latitudes'][:]		
		lon  = fid.variables['Grid_Longitudes'][:]		
		nx,ny = var1.shape
		spval = -9999.

		# reverse latitudes, they are upside down
		lat = lat[::-1]

		var1out = var1.transpose()
		var1out[np.where(np.isnan(var1out))] = spval
		var1out = var1out[::-1,:]
		var2out = var2.transpose()
		var2out[np.where(np.isnan(var2out))] = spval
		var2out = var2out[::-1,:]
		var3out = var3.transpose()
		var3out[np.where(np.isnan(var3out))] = spval
		var3out = var3out[::-1,:]
		var4out = var4.transpose()
		var4out[np.where(np.isnan(var4out))] = spval
		var4out = var4out[::-1,:]
		var5out = var5.transpose()
		var5out[np.where(np.isnan(var5out))] = spval
		var5out = var5out[::-1,:]
		var6out = var6.transpose()
		var6out[np.where(np.isnan(var6out))] = spval
		var6out = var6out[::-1,:]
		var7out = var7.transpose()
		var7out[np.where(np.isnan(var7out))] = spval
		var7out = var7out[::-1,:]
		var8out = var8.transpose()
		var8out[np.where(np.isnan(var8out))] = spval
		var8out = var8out[::-1,:]
		var9out = var9.transpose()
		var9out[np.where(np.isnan(var9out))] = spval
		var9out = var9out[::-1,:]
		var10out = var10.transpose()
		var10out[np.where(np.isnan(var10out))] = spval
		var10out = var10out[::-1,:]
		var11out = var11.transpose()
		var11out[np.where(np.isnan(var11out))] = spval
		var11out = var11out[::-1,:]
		var12out = var12.transpose()
		var12out[np.where(np.isnan(var12out))] = spval
		var12out = var12out[::-1,:]
		var13out = var13.transpose()
		var13out[np.where(np.isnan(var13out))] = spval
		var13out = var13out[::-1,:]

		fout = nc.Dataset(fileout,'w',format='NETCDF3_64BIT_OFFSET')
		fout.description = 'Carbon-based phytoplankton size classes retrieved via ocean color estimates of the particle size distribution'
		#fout.whatever # global attribute
		fout.data_source = 'https://doi.pangaea.de/10.1594/PANGAEA.859005?format=html#download'
		fout.SeaWiFS_version = 'R2010.0'
		fout.Processing_level = 'L3_Mapped'
		fout.Temporal_resolution = 'Monthly'
		fout.Year = '1998;1999;2000;2001;2002;2003;2004;2005;2006;2007;2008;2009;2010;'
		fout.Month = 'June'
		fout.Map_Projection = 'Equidistant_Cylindrical/Unprojected'
		fout.Latitude_Units = 'Decimal_degrees'
		fout.Longitude_Units = 'Decimal_degrees'
		fout.Northernmost_Latitude = 90.
		fout.Southernmost_Latitude = -90.
		fout.Westernmost_Longitude = -180.
		fout.Easternmost_Longitude = 180.
		fout.Latitude_Step = 0.0833333
		fout.Longitude_Step = 0.0833333
		fout.SW_Point_Latitude_center_of_pixel = -89.95833335
		fout.SW_Point_Longitude_center_of_pixel = -179.95833335
		fout.Grid_Registration = 'Latitude and Longitude values refer to centers of pixels'
		fout.Lat_Lon_Convention = 'Latitude and Longitude vectors begin at upper right (Northwest) corner of image'
		fout.PSD_Processing_script_name = 'calc_monthly_climatology_xi_v2016'
		fout.PFT_Processing_script_name = 'calc_monthly_climatology_PFTC_v2015'
		fout.Organization = 'University of Richmond'
		fout.Contact_Name = 'Tihomir S. Kostadinov'
		fout.Contact_Email = 'kostadinov.t@gmail.com'
		fout.Reference_1 = 'Kostadinov, T. S., Milutinovic, S., Marinov, I., and Cabre, A. (2015), Carbon-based phytoplankton size classes retrieved via ocean color estimates of the particle size distribution, Ocean Sci. Discuss., 12, 573-644, doi:10.5194/osd-12-573-2015'
		fout.Reference_2 = 'Kostadinov, T. S., D. A. Siegel, and S. Maritorena (2009), Retrieval of the particle size distribution from satellite ocean color observations, J. Geophys. Res., 114, C09015, doi:10.1029/2009JC005303'
		
		# dimensions
		fout.createDimension('time', None)
		fout.createDimension('lat', ny)
		fout.createDimension('lon', nx)
		# variables
		time       = fout.createVariable('time', 'f8', ('time',))
		latitudes  = fout.createVariable('lat', 'f8', ('lat',))
		latitudes.units = 'Degrees/Negative in S Hemisphere'
		longitudes = fout.createVariable('lon', 'f8', ('lon',))
		longitudes.units = 'Degrees/Negative in W Hemisphere'
		outdata1   = fout.createVariable('PSD_slope', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata1.units = 'dimensionless'
		outdata1.Variable_details = 'Power-law slope of the particle size distribution; For details, see Kostadinov et al. (2009), DOI: 10.1029/2009JC005303'
		outdata2   = fout.createVariable('Composite_standard_deviation_PSD_slope', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata2.units = 'dimensionless'
		outdata3   = fout.createVariable('Particle_differential_number_concentration_log10', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata3.units = 'log10 of (1/m^4)'
		outdata3.Variable_details = 'Differential number concentration of particles at the reference diameter of 2 microns (um). Unit is number of particles per m^3 seawater per m size bin width, so 1/m^4; The decimal logarithm of the value is given. For details, see Kostadinov et al. (2009), DOI: 10.1029/2009JC005303'
		outdata4   = fout.createVariable('Composite_standard_deviation_Particle_differential_number_concentration_log10', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata4.units = 'log10 of (1/m^4)'
		outdata5   = fout.createVariable('C_biomass_total', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata5.units = 'mg/m^3'
		outdata5.Size_range = '0.5-50 um (micrometers) in diameter'
		outdata6   = fout.createVariable('Composite_standard_deviation_C_biomass_total', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata6.units = 'mg/m^3'
		outdata6.Size_range = '0.5-50 um (micrometers) in diameter'
		outdata7   = fout.createVariable('picoplankton_C_fraction', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata7.units = 'Fraction of carbon biomass'
		outdata7.Size_range = '0.5-2 um (micrometers) in diameter'
		outdata8   = fout.createVariable('Composite_standard_deviation_picoplankton_C_fraction', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata8.units = 'Fraction of carbon biomass'
		outdata8.Size_range = '0.5-2 um (micrometers) in diameter'
		outdata9   = fout.createVariable('nanoplankton_C_fraction', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata9.units = 'Fraction of carbon biomass'
		outdata9.Size_range = '2-20 um (micrometers) in diameter'
		outdata10   = fout.createVariable('Composite_standard_deviation_nanoplankton_C_fraction', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata10.units = 'Fraction of carbon biomass'
		outdata10.Size_range = '2-20 um (micrometers) in diameter'
		outdata11   = fout.createVariable('microplankton_C_fraction', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata11.units = 'Fraction of carbon biomass'
		outdata11.Size_range = '20-50 um (micrometers) in diameter'
		outdata12   = fout.createVariable('Composite_standard_deviation_microplankton_C_fraction', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata12.units = 'Fraction of carbon biomass'
		outdata12.Size_range = '20-50 um (micrometers) in diameter'
		outdata13   = fout.createVariable('Number_of_months_participating_in_composite_calculation', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata13.units = 'Number of months'

		time.units = 'month'
		time.calendar = '1-12'

		# data
		time[0] = timevalue
		latitudes[:]    = lat
		longitudes[:]   = lon
		outdata1[0,:,:] = var1out
		outdata2[0,:,:] = var2out
		outdata3[0,:,:] = var3out
		outdata4[0,:,:] = var4out
		outdata5[0,:,:] = var5out
		outdata6[0,:,:] = var6out
		outdata7[0,:,:] = var7out
		outdata8[0,:,:] = var8out
		outdata9[0,:,:] = var9out
		outdata10[0,:,:] = var10out
		outdata11[0,:,:] = var11out
		outdata12[0,:,:] = var12out
		outdata13[0,:,:] = var13out
		# close
		fout.close()
