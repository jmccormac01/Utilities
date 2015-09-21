#
# script to grab the median value of 
# all fits files in the current directory
#
from astropy.io import fits
import glob as g
import numpy as np

t=g.glob('*.fits')
med=np.empty(len(t))
for i in range(0,len(t)):
	data=fits.open(t[i])[0].data
	med[i]=np.median(data)
	print "[%d/%d] %s %.2f" % (i+1,len(t),t[i],med[i])

	