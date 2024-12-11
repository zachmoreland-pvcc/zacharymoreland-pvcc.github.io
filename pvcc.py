# Name: Zach Moreland
# Prog Purpose: This program finds the cost of movie tickets, popcorn, & drinks
#   The output is sent to an .html file

import datetime

##############  define global variables ############
RATE_TUITION_IN = 164.40
RATE_TUITION_OUT = 353.00
RATE_CAPITAL_FEE = 26.00
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
ship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

# create output file
outfile = 'pvccweb.html'


##############  define program functions ################
def main():
    
    open_outfile()
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()
        
        yesno = input("\nwould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == 'N':
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-pvcc.jpg); color: #f8dd61;">\n')
    
def get_user_data():
    global inout, numcredits, scholarship
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    ship_amt = int(input("Scholarship amount received: "))    

def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    inst_fee = numcredits * RATE_INSTITUTION_FEE
    act_fee = numcredits * RATE_ACTIVITY_FEE
    total = tuition + cap_fee + inst_fee + act_fee
    balance = tuition + cap_fee + inst_fee + act_fee - ship_amt

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #47161a;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>PVCC TUITION</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('**Tuition Amount at PVCC**\n')
    
    f.write(tr + 'Tuition' + endtd + format(tuition,currency) + endtr)
    f.write(tr + 'Capital Fee' + endtd + format(cap_fee,currency) + endtr)
    f.write(tr + 'Institution Fee' + endtd + format(inst_fee,currency) + endtr)

    f.write(tr + 'Activity Fee' +  endtd + format(act_fee,currency)  + endtr)     
    f.write(tr + 'Total' + endtd + format(total,currency) + endtr)
    f.write(tr + 'Balance' +  endtd + format(balance,currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')


##########  call on main program to execute ############
main()              

