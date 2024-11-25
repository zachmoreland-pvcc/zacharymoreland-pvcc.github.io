# Name: Zach Moreland
# Prog Purpose: This program computes the 6-month cost of Personal Property tax in Charlottesville, VA

import datetime
#define annual tax rate
ANNUAL_RATE = 0.044
RELIEF_DISCOUNT_RATE = 0.3

#define global variables
vehicle_value = 0
relief_discount = 0

########### define program functions ###########
def main():

    more = True
    
    while more: 
        get_user_data()
        perform_calculations()
        display_results()
    
        yesno = input("\nWould you like to calculate tax for another vehicle (Y or N)? ")
        if yesno.upper() == "N" :
            more = False
            print('Personal Property Tax Due JUNE 05')
    
def get_user_data():
    global vehicle_value, relief_eligibility
    vehicle_value = int(input("Assessed value of the vehicle: "))
    relief_eligibility = int(input("Is your vehicle eligible for tax relief? (1 for YES, 2 for NO): "))

def perform_calculations():
    global annual_amount, sixmonth_amount, relief_amount, total_due
    annual_amount = vehicle_value * ANNUAL_RATE
    sixmonth_amount = annual_amount / 2

    if relief_eligibility == 1:
        relief_amount = sixmonth_amount * RELIEF_DISCOUNT_RATE
    else:
        relief_amount = 0

    total_due = sixmonth_amount - relief_amount

def display_results():
    print('------------------------------------')
    print('**** PERSONAL PROPERTY TAX BILL ****')
    print('   Please Pay in a Timely Manner    ')
    print(str(datetime.datetime.now()))
    print('------------------------------------')
    print('Assessed Value        $ ' + format(vehicle_value, '8,.2f'))
    print('Relief Amount         $ ' + format(relief_amount, '8,.2f'))
    print('Full Annual Amount    $ ' + format(annual_amount, '8,.2f'))
    print('____________________________________')
    print('Total Due             $ ' + format(total_due, '8,.2f'))



########### call on main program to execute ###########
main()
