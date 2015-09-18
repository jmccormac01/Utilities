###############################################################################
#                                                                             #
#                     pybz2 - un/zip many files with bzip2                    #
#                                    v1.0                                     #
#                               James McCormac                                #
#                                                                             #
# Version History:                                                            #
#	20150919	v1.0	Code written and tested                               # 
#                                                                             #
###############################################################################
#
# A script to make a telescoped.mesh file without pterrors
#
# process:
# 	subtract the TEL_RA from LST to get HA
# 	get field centre from astrometry and subtract the actual from the commanded
# 	make a file with:
# 		HA (decimal hours) DEC (decimal degrees) HA_err (arcmin) DEC_err (arcmin)
# 		
# 	apply the mesh
# 	repeat the spiral to see if it improves
#
# to do:
#

# pybz2
# python + glob wrapper for bunzip2
# When zipping or unzipping lots of files 
# Linux may complain about the list being too long,
# this will fix that. 


import argparse as ap
import glob as g
import os

# get command line args
def ArgParse():
	parser=ap.ArgumentParser()
	parser.add_argument('pattern',help='glob pattern, e.g. *.fits')
	parser.add_argument('ztype',help="operation type, e.g. 'zip' ", choices=['zip','unzip'])
	args=parser.parse_args()
	return args
	
args=ArgParse()
t=g.glob('%s' % (args.pattern))

if args.ztype=='zip':
	for i in range(0,len(t)):
		os.system('bzip2 %s' % (t[i]))
elif args.ztype=='unzip':
	for i in range(0,len(t)):
		os.system('bunzip2 %s' % (t[i]))
		
		