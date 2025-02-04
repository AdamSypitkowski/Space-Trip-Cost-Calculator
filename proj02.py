###############################################################################
#
#   CSE 231 Project02
#       Space trip cost calculator
#           Determines the amount of money to be billed to an astronaut
#           Takes a specific code of: XV, ET, or SI
#           Each code then has different calculations to calculate the cost
#               Measures are in place to determine if the code is valid
#
###############################################################################

import math

# Printing welcome message
print("""
Welcome to SpaceX Galactic Car Extravaganza!

Prepare for an interstellar joyride with our cosmic cruisers!
At the prompt, please enter:
- Galactic code (XV, ET, SI)
- Days of your interstellar joyride
- Odometer at liftoff
- Odometer at touchdown
    """)

# 1st prompt for yes/no
prompt = input("Ready for an out-of-this-world adventure (Y/X)? ")

# Determines if answered "Y"
while prompt == "Y":
    code = input("\nGalactic code (XV, ET, SI): ")

# Loop that only exits when the Customer Code Input is a valid code
    loop_check = 0
    while loop_check < 1:
        if code == "XV" or code == "ET" or code == "SI":
            # Leaves the loop
            break
        else:
            print("\n*** Invalid galactic code. Retry! ***")
            code = input("\nGalactic code (XV, ET, SI): ")

# Inputs for both the number of days and the odometer readings
    days_input = int(input("\nNumber of days (int): "))
    start_odometer = int(input("\nOdometer at liftoff (int): "))
    end_odometer = int(input("\nOdometer at touchdown (int):   "))

# Determines the total number of light years traveled
    if end_odometer >= start_odometer:
        light_years = (end_odometer/10) - (start_odometer/10)
    else:
        # Takes into account the possibility of the odometer carrying over
        light_years = ((end_odometer + 1000000) / 10) - (start_odometer / 10)

    trip_cost = float(0)

# Code "XV"
    if code == 'XV':
        trip_cost = float((40 * days_input) + (0.25 * light_years))

# Code "ET"
    elif code == 'ET':
        avg_light_years = (light_years / days_input)
        trip_cost = float(60 * days_input)

        if avg_light_years > 100:
            # Adds extra cost if avg light years is > 100
            trip_cost += float((light_years - (100*days_input)) * 0.25)

# Code "SI"
    elif code == 'SI':
        weeks = math.ceil(days_input / 7)
        trip_cost = float(weeks * 190)
        avg_light_years_week = light_years / weeks

        if avg_light_years_week > 1500:
            trip_cost += float((200*weeks) + (0.25*(light_years - (1500 * weeks))))

        elif avg_light_years_week > 900:
            trip_cost += float(100*weeks)

        else:
            trip_cost += float(0)

# Final print statement
    print(
    "\nGalactic traveler summary:\n"
    "   Code:", code, "\n",
    "   Days in orbit:", days_input, "\n",
    "   Liftoff odometer:", start_odometer, "\n",
    "   Touchdown odometer:", end_odometer, "\n",
    "   Light-years traveled:", round(light_years, 2), "\n",
    "   Cost in star credits: $", round(trip_cost, 2))
    prompt = input("Ready for an out-of-this-world adventure (Y/X)? ")

# When the initial prompt is answered as "X"
print("\nThank you for entrusting us with your joyride!")
