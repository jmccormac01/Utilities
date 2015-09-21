#
# python script to make jpgs of 
# of all fits images in cwd
#

from astropy.io import fits
import glob as g
import matplotlib.pyplot as pl
import matplotlib.cm as cm
import numpy as np

t=g.glob('*.fits')

for i in range(0,len(t)):
	h=fits.open(t[i])[0].data
	name="%s.png" % (t[i].split('.')[0])
	med=np.median(h)
	fig = pl.figure()
	pl.imshow(h,cmap=cm.Greys_r,vmin=med-0.2*med,vmax=med+0.2*med)
	fig.savefig(name,dpi=fig.dpi)
	print "[%03d/%03d]" % (i+1,len(t))
	