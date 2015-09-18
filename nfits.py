# utility for listing number of fits images 
# in the current directory 

import glob as g
t=g.glob('*.f*')
print "%d *.f* images\n" % len(t)
