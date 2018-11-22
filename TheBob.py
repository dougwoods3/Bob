
plate = 1           # weight in pounds
weight = 10         # weight in pounds
airContainer = 3    # weight in pounds


def buoyancy_volume(plate,weight,airContainer,airVol):
    # Need to displace the volume of water that weighs MORE than
    #   the combined weight of the plate, weight, air container, and air.
    waterDensity = 8.345404/128      # pounds per fluid ounce
    airDensity = 0.0765/957.506      # pounds per fluid ounce

    airVol = (plate+weight+airContainer+airVol*airDensity)/waterDensity




    return airVol


def pressure_head():
    NaN


def main():

    print('\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('%%%%         The Bob          %%%')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')

    airVol0 = 1         # initial volume guess in fluid ounces
    airVol1 = 0
    count = 0
    while (abs(airVol1 - airVol0) > 1e-5):
        airVol1 = buoyancy_volume(plate,weight,airContainer,airVol0)
        airVol0, airVol1 = airVol1, airVol0
        count += 1
        if count > 10:
            print('something is broken - tell Doug')
            continue


    print('With a {:.1f} pound weight, you need {:.1f} ({:.1f}) fluid ounces (gal.) '.format(weight, airVol1, airVol1/128))
    print('    of air to have equal buoyancy with the weight.\n')

main()
