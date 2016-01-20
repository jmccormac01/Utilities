import numpy as np
import matplotlib.pyplot as pl

# pressure correction
P=np.array([74.,75.,76.,77.]) #kPa
T=np.array([0.,10.,20.,30.]) # degC

pix_scale=4.96
pix_per_arcmin=60./pix_scale

dalt=2.8
alt=np.linspace(30,90,61)[::-1]
dR=np.empty(len(alt))

fig,ax=pl.subplots(1,4,figsize=(20,5))

for j in range(0,len(P)):
	pcor=(P[j]/101.)*(283./(273+T))
	for i in range(0,len(alt)):
		R1=1./np.tan(np.radians(alt[i]+(7.31/(alt[i]+4.4))))
		R2=1./np.tan(np.radians(alt[i]-dalt+(7.31/(alt[i]-dalt+4.4))))
		dR[i]=(R1-R2)*pix_per_arcmin
	ax[j].set_title('DR [%d kPa]' % (P[j]))
	ax[j].set_xlabel('Altitude of Highest Point (deg)')
	ax[j].set_ylabel('Differential Refraction (pix)')
	ax[j].set_xlim(25,90)
	ax[j].set_ylim(-2.5,0)
	ax[j].plot(alt,(dR*pcor[0]),'r-')
	ax[j].plot(alt,(dR*pcor[1]),'g-')
	ax[j].plot(alt,(dR*pcor[2]),'b-')
	ax[j].plot(alt,(dR*pcor[3]),'k-')
	ax[j].legend(('T=  0 C','T=10 C','T=20 C','T=30 C'),loc='upper left')

pl.show()