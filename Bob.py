import math


#
# Change these variables to tweak the problem:
#
plate = 1                   # weight in pounds
weight = 1                  # weight in pounds
airContainer = 1            # weight in pounds

maxWeightHeight = 50        # height in inches
chamberInnerDiameter = 4    # diameter in inches

waterDensity = 8.345404/128      # pounds per fluid ounce
airDensity = 0.0765/957.506      # pounds per fluid ounce

def buoyancy_volume(waterDensity,airDensity,plate,weight,airContainer,airVol):
    # Need to displace the volume of water that weighs MORE than
    #   the combined weight of the plate, weight, air container, and air.
    airVol = (plate+weight+airContainer+airVol*airDensity)/waterDensity
    return airVol

def work_from_fall(plate, weight, airContainer, maxWeightHeight, chamberInnerDiameter, waterDensity, airDensity, airVol):
    g = 384.0   # inches/sec^2
    weightWork = (plate+weight+airContainer+airVol*airDensity)*g*maxWeightHeight
    waterWork = g*waterDensity*math.pi*chamberInnerDiameter**2*maxWeightHeight**3/3
    return (weightWork + waterWork)/(12**2*25037*0.94782)

def pressure_head(mass, height):
        # mass (pounds)
        # g = 32 ft/sec^2
        #   = 384 in/sec^2
        # height (inches)
    return mass*384.0*height




def main():
    print('\n /$$$$$$$$ /$$                       /$$$$$$$            /$$')
    print('|__  $$__/| $$                      | $$__  $$          | $$')
    print('   | $$   | $$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$ | $$$$$$$')
    print('   | $$   | $$__  $$ /$$__  $$      | $$$$$$$  /$$__  $$| $$__  $$')
    print('   | $$   | $$  \ $$| $$$$$$$$      | $$__  $$| $$  \ $$| $$  \ $$')
    print('   | $$   | $$  | $$| $$_____/      | $$  \ $$| $$  | $$| $$  | $$')
    print('   | $$   | $$  | $$|  $$$$$$$      | $$$$$$$/|  $$$$$$/| $$$$$$$/')
    print('   |__/   |__/  |__/ \_______/      |_______/  \______/ |_______/\n\n')

    airVol0 = 1         # initial volume guess in fluid ounces
    airVol1 = 0
    count = 0
    while (abs(airVol1 - airVol0) > 1e-5):
        airVol1 = buoyancy_volume(waterDensity, airDensity, plate, weight, airContainer, airVol0)
        airVol0, airVol1 = airVol1, airVol0
        count += 1
        if count > 10:
            print('something is broken - tell Doug')
            continue

    workOut = work_from_fall(plate, weight, airContainer, maxWeightHeight, chamberInnerDiameter, waterDensity, airDensity, airVol1)



    print('There is a straight cylindrical chamber full of water with a weight on top.')
    print('We calculate:')
    print('   1) the volume of air required to float the weight (neglecting the pressure change)')
    print('   2) the work done by the weight and water falling to/out of the bottom\n\n')


    print('INPUTS:')
    print('\tWeight:\t\t\t{:.1f}\tpound(s)'.format(weight))
    print('\tPlate:\t\t\t{:.1f}\tpound(s)'.format(plate))
    print('\tAir Container:\t\t{:.1f}\tpound(s)'.format(airContainer))
    print('\tPlate height:\t\t{:.1f}\tinches'.format(maxWeightHeight))
    print('\tChamber ID:\t\t{:.1f}\tinches'.format(chamberInnerDiameter))

    print('\nOUTPUTS:')
    print('\tAir volume needed:\t\t{:.1f}\tfl. oz. ({:.1f} gal.)'.format(airVol1, airVol1/128))
    print('\tGross work out:\t\t\t{:.1f}\tkilo-Joules\n'.format(workOut))

main()
