from astropy.coordinates import get_sun
from datetime import datetime as dt
import numpy as np
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

# script to get current sun alt
# observatory set up
olat=-24.-(37./60.)-(38./3600.)
olon=-70.-(24./60.)-(15./3600.)
elev=2418.
paranal=EarthLocation(lat=olat*u.deg,lon=olon*u.deg,height=elev*u.m)

# work in UTC - add 1 day as cron runs at 4pm
time=Time(dt.utcnow(),scale='utc')
altazframe = AltAz(obstime=time, location=paranal)
sunaltaz = get_sun(time).transform_to(altazframe)

print sunaltaz.alt.deg[0]