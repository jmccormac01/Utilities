###############################################################################
#                                                                             #
#                     nfits.py - count the no. of fits files in .             #
#                                    v1.0                                     #
#                               James McCormac                                #
#                                                                             #
# Version History:                                                            #
#	20150919	v1.0	Code written and tested                               # 
#                                                                             #
###############################################################################
#
# utility for listing number of fits images 
# in the current directory 
#
# to do:
#

import glob as g
t=g.glob('*.f*')
print("%d *.f* images\n" % len(t))
