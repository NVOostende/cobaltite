import os
import os.path
import numpy as np
import netCDF4 as nc

class rewrite_data():

	def __init__(self):
		return None

	def rewrite_obs_data(self,fileobs='',timevalue=0,fileout='./out.nc'):
		fid  = nc.Dataset(fileobs)
		var1 = fid.variables['O2_bottom'][:]
		lat  = fid.variables['lat'][:]		
		lon  = fid.variables['lon'][:]		
		nx,ny = var1.shape
		spval = -9999.

		# reverse latitudes, they are upside down
		#lat = lat[::-1]

		#var1out = var1.transpose()
		var1out = var1.copy()
		var1out[np.where(np.isnan(var1out))] = spval
		#var1out = var1out[::-1,:]

		fout = nc.Dataset(fileout,'w',format='NETCDF3_64BIT_OFFSET')
		fout.description = 'DIVA interpolated near-bottom dissolved oxygen concentration measured by NOAA Nortwest Fisheries Science Center'
		#fout.whatever # global attribute
		fout.data_source = 'https://www.nwfsc.noaa.gov/data/api/v1/source/trawl.operation_haul_fact/selection.csv?defaults=expanded'
		fout.Latitude_Units = 'Decimal_degrees'
		fout.Longitude_Units = 'Decimal_degrees'
		fout.Contact_Name = 'Todd Hay NOAA Federal'
		fout.Contact_Email = 'todd.hay@noaa.gov'
		
		# dimensions
		fout.createDimension('time', None)
		fout.createDimension('lat', nx)
		fout.createDimension('lon', ny)
		# variables
		time       = fout.createVariable('time', 'f8', ('time',))
		latitudes  = fout.createVariable('lat', 'f8', ('lat',))
		latitudes.units = 'Degrees/Negative in S Hemisphere'
		longitudes = fout.createVariable('lon', 'f8', ('lon',))
		longitudes.units = 'Degrees/Negative in W Hemisphere'
		outdata1   = fout.createVariable('O2_bottom', 'f8', ('time','lat','lon',),fill_value=spval)
		outdata1.units = 'ml/l'

		time.units = 'none'

		time.calendar = '1-12'

		# data
		time[0] = timevalue
		latitudes[:]    = lat
		longitudes[:]   = lon
		outdata1[0,:,:] = var1out
		# close
		fout.close()
