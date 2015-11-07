
"""
Utilisation de la librairie python pyephem pour verification des calculs

VOIR INSTALLATION et documentation la:

http://rhodesmill.org/pyephem/index.html

"""
import ephem

import math

# create a satelite object from NORAD Two-Line Element Set Format
# Obtained from Celestrak web site
# =>
# http://celestrak.com/NORAD/elements/tdrss.txt

# Here for INTELSAT 904
satellite = ephem.readtle('INTELSAT 904 (IS-904)',
                         '1 27380U 02007A   15310.12198263  .00000039  00000-0  00000+0 0  9992',
                         '2 27380   0.0328  79.5781 0003108 154.6653 274.7037  1.00272586 50235'
                         )


#creer un observateur
obs=ephem.Observer()

# definir sa position
# Toulouse 43.6 1.433333
obs.lat = 43.6
obs.lon = 1.433333
# definit la date d'observation
obs.date = '2015/11/07 15:40'

#calculer les coordonnees de l'objet pour cet observateur

satellite.compute(obs)


#calculer les coordonnees de l'objet pour cet observateur

satellite.compute(obs)

def text_and_float(angle_text):
    return ( str(angle_text) + ', ' + str( math.degrees(float(angle_text))))

print 'sublat=' + text_and_float(satellite.sublat)
print 'sublong=' + text_and_float(satellite.sublong) 
print 'elevation=',text_and_float(satellite.alt) # elevation and altitude exchanged
print 'az=',text_and_float(satellite.az)
print 'altitude', satellite.elevation #strange name for altitude in pyephem
