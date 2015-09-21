# python script to change fts --> fits
import glob as g
import os
t=g.glob('*.fts')
for i in t:	
	os.system('mv %s %s.fits' % (i,i.split('.')[0]))
	
	