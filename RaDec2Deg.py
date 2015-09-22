#
# script to convert deg to hms/dms and vice versa
#

import sys
from astropy.coordinates import SkyCoord
from astropy import units as u

def RaDec2Deg(x,y):

	# deg to hex
	if len(x.split(':'))== 1 and len(y.split(':')) == 1:
		c=SkyCoord(x,y,unit="deg")
		print c.to_string('hmsdms')
			
	# hex to deg
	if len(x.split(':'))== 3 and len(y.split(':')) == 3:
		c=SkyCoord(x,y,unit=(u.hourangle, u.deg))
		print c.to_string('decimal')

if len sys.argv != 2:
	print "USAGE: python RaDec2Deg.py RA DEC"
	
RaDec2Deg(sys.argv[1],sys.argv[2])