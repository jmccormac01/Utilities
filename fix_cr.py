#
# python script to swop \r for \n in a file
#

import sys

f=open(sys.argv[1]).readlines()
f2=f[0].split('\r')
q=open(sys.argv[1],'w')

for i in range(0,len(f2)):
	line="%s\n" % f2[i]
	q.write(line)
	
q.close()

