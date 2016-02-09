# script to calculate the gain and read noise
# using the method in the CCD handbook of astronomy
# howell (2000)

from astropy.io import fits
import matplotlib.pyplot as pl
from matplotlib import cm
import glob as g
import numpy as np

biases=g.glob('bias*')
flats=g.glob('flat*')

# load images, exclude 20 pixel boarder around the edge
f1=np.array(fits.open(flats[0])[0].data[20:2028,40:2048]).astype(np.float)
f2=np.array(fits.open(flats[1])[0].data[20:2028,40:2048]).astype(np.float)
b1=np.array(fits.open(biases[0])[0].data[20:2028,40:2048]).astype(np.float)
b2=np.array(fits.open(biases[1])[0].data[20:2028,40:2048]).astype(np.float)

# exclude stars
df=f1-f2
db=b1-b2

g = ( (np.average(f1)+np.average(f2)) - (np.average(b1)+np.average(b2)) ) / (  np.std(df)**2 - np.std(db)**2  )
rn = ( g * np.std(db) ) / np.sqrt(2.)

print('Gain: %.3f' % (g))
print('ReadNoise: %.3f' % (rn))

fig = pl.figure(1,figsize=(20,10))
ax = fig.add_subplot(1, 2, 1, xticks=[], yticks=[])
ax.imshow(df,cmap=cm.afmhot,vmin=0.8*np.median(df),vmax=1.2*np.median(df),interpolation=None)
ax.set_title('F1 - F2')
ax = fig.add_subplot(1, 2, 2, xticks=[], yticks=[])
ax.set_title('B1 - B2')
ax.imshow(db,cmap=cm.afmhot,vmin=0.8*np.median(db),vmax=1.2*np.median(db),interpolation=None)
pl.show()

