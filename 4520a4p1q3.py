__author__ = 'Meghan'

import math

r = 0.3 /2                        #m
vol = 4.0*math.pi*r**3 /3.0     #m^3
mb = 5.0/1000                   #kg
P = 101325                      #Pa
R = 8.3144598                   #kPa L / K mol
T = 298                         #k
nHe = P*vol/(R*T)               #moles
MHe = 4.003                     #g/mol
mHe = MHe*nHe /1000.0           #kg
m = mb + mHe                    #kg
Mair = 28.97/1000               #kg/mol
g = 9.81                        #N/kg
Fb = Mair*nHe*g                 #N
Fg = m*g                        #N
pay = (Fb-Fg)/g                 #kg/balloon
desmass = 20.0                  #kg
ball = desmass/pay              #number of balloons


print "radius                           = {0} m".format(r)
print "volume                           = {0} m^3".format(vol)
print "moles of Helium                  = {0} moles".format(nHe)
print "mass of Helium                   = {0} kg".format(mHe)
print "total mass of balloon            = {0} kg".format(m)
print "gravitational force              = {0} N".format(Fb)
print "buoyant force                    = {0} N".format(Fg)
print "payload                          = {0} kg/balloon".format(pay)
print "number of balloons to lift 20 kg = {0} balloons".format(ball)


