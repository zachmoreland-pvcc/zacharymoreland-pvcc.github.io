# Name: your name here
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

########## NEW LISTS for calculated amounts

gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret401k = []
net_pay = []

total_gross = 0
total_net = 0

############# TUPLES of constants #############
#          C     S    J    M
# indexes  0     1    2    3
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

#           fed  state  ss   med   ret
# indexes    0    1     2     3     4
DED_RATE = (.12, .03, .062, .0145, .04)

############ define program functions #############
def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):

    #calculate gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]

        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]

        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]

        else:
            pay = hours[i] * PAY_RATE[3]

    #calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        soc_sec_amt = pay * DED_RATE[2]
        medicare_amt = pay * DED_RATE[3]
        ret401k_amt = pay * DED_RATE[4]

        net = pay - fed - state - soc_sec_amt - medicare_amt - ret401k_amt
        
    #add to totals
        total_gross += pay
        total_net += net

    #append amounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(soc_sec_amt)
        medicare.append(medicare_amt)
        ret401k.append(ret401k_amt)
        net_pay.append(net)

def display_results():
    currency = '8,.2f'
    line = '------------------------------------------'
    tab = "\t"

    print(line)
    print('*********** FRESH FOODS MARKET***********')
    print('---------- WEEKLY PAYROLL REPORT --------')
    print(tab + str(datetime.datetime.now()))
    print(line)
    titles1 = "Emp Name" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + tab + "Medicare" + tab + "401k" + tab + tab + "Net"
    print(titles1 + titles2)

    for i in range(num_emps):
        data1 = emp[i] + " " + job[i] + format(gross_pay[i], currency) + tab + format(fed_tax[i], currency) + tab + format(state_tax[i], currency) + tab + format(soc_sec[i], currency) + tab + format(medicare[i], currency) + tab + format(ret401k[i], currency) + tab + format(net_pay[i], currency)
        print(data1)
    print(line)
    print("*************** TOTAL GROSS: $" + format(total_gross, currency))
    print("*************** TOTAL NET  : $" + format(total_net, currency))
    print(line)

########## call on main program to execute ##########
main()
