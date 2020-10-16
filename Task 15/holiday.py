

def hotelcost(numberOfNights):
    pricePerNight = 150
    return pricePerNight*numberOfNights

def planeCost(city):
    if(city == 'Pretoria'):
        return 350
    elif(city == 'Johnannesburg'):
        return 300
    elif(city == 'Nelspruit'):
        return 400
    elif(city == 'Polokwane'):
        return 600
    else: return 450

def carRental(numberOfDaysHired):
    return 120 * numberOfDaysHired

def holidayCost(numberOfNights, city, numberOfDaysHired):
    return numberOfNights + city + numberOfDaysHired

print("ZAR: ", holidayCost(hotelcost(2), planeCost('Polokwane'), carRental(2)))
