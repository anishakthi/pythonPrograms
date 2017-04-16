sun_diameter = 865400
earth_diameter = 7917.5
sun_radius = sun_diameter/2
earth_radius = earth_diameter/2
vol_sun = 4/3*3.14*sun_radius * sun_radius* sun_radius
vol_earth = 4/3*3.14*earth_radius * earth_radius * earth_radius
ratio = vol_sun/vol_earth
print "Volume of Sun is %.2f cubic miles" %vol_sun
print "Volume of earth is %.2f cubic miles" %vol_earth
print "Ratio of the volume of the Sun to the volume of the Earth is %.2f" %ratio
