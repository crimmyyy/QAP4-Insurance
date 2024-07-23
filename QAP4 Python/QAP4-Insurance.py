# Title - One Stop Insurance Company
# Description - A program for One Stop Insurance Company that helps them enter and calculate new insurance policy information for customers.
# Author - Kyle / Scarlett Budgell

#import libraries
import math
import random
import datetime
import sys
import time
import DollarConvLib # Credit for library - ZACHARY COLLIER


# pull constants from "Const.dat"

with open('Const.dat', 'r') as f:
    POLICY_NUM = int(f.readline())
    BASIC_PREMIUM = float(f.readline())
    CAR_DISCOUNT = float(f.readline())
    EXTRA_LIABILITY_COVERAGE = float(f.readline())
    GLASS_COVERAGE = float(f.readline())
    LOANER_COVERAGE = float(f.readline())
    HST_RATE = float(f.readline())
    MONTHLY_PROCESS_FEE = float(f.readline())

VALID_PROV = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
PAY_METHODS = ["F", "M", "D"]

# program functions

def ErrMsg(Message):
    print(f"ERROR - {Message}")

def ListCheck(var, lst):
    return var in lst

def PostValid(post):
    if len(post) != 6:
        ErrMsg(" ERROR - Please ensure 6 characters are used for the postal code. ")
        return False
    
    postNums = post[1] + post[3] + post[5]
    postLetters = post[0] + post[2] + post[4]
    
    if not postNums.isdigit():
        ErrMsg(" ERROR - Please make sure numbers are the second, fourth, and sixth characters. ")
        return False
    elif not postLetters.isalpha():
        ErrMsg(" ERROR - Please make sure letters are the first, third, and fifth characters. ")
        return False
    
    return True

# this is where the main program begins.

# user inputs
FirstCust = input("Please enter the customer's first name: ").title()
LastCust = input("Please enter the customer's last name: ").title()
Addr = input("Enter the customer's address: ")
City = input("Enter the customer's city: ").title()

# put loops and validation checks here.
while True:
    Prov = input(" Enter the customer's province (ex. NL, NB, PE.): ").upper()
    if len(Prov) != 2:
        ErrMsg(" ERROR - You must use the abbreviated province name (ex. 'NL' for Newfoundland & Labrador.) Please try again. ")
    else:
        ProvVal = ListCheck(Prov, VALID_PROV)
        if ProvVal:
            break
        else:
            ErrMsg(" ERROR - invalid province. Please try again. ")

while True:
    Postal = input(" Enter customer's postal code (ex. A1AB2B): ").upper()
    if PostValid(Postal):
        break

while True:
    Phone = input("Enter customer's phone number (10-digit number): ")
    if len(Phone) != 10 or not Phone.isdigit():
        ErrMsg("Please ensure 10 numbers are used for the phone number.")
    else:
        PhoneDsp = f"({Phone[:3]}) {Phone[3:6]}-{Phone[6:]}"
        break

while True:
    try:
        CarsDsp = input(" Enter the number of cars the customer has insured: ")
        Cars = int(CarsDsp)
        break
    except ValueError:
        ErrMsg(" ERROR - only numbers may be used. Please try again. ")

while True:
    ExtraLiability = input(" OPTIONAL - Does the customer require extra liability up to $1,000,000..? (Y for Yes, N for No.): ").upper()
    if ExtraLiability in ["Y", "N"]:
        break
    else:
        ErrMsg(" ERROR - enter only Y or N. Please try again. ")

while True:
    GlassCover = input(" OPTIONAL - Does the customer require extra glass coverage..? (Y for Yes, N for No.): ").upper()
    if GlassCover in ["Y", "N"]:
        break
    else:
        ErrMsg(" ERROR - enter only Y or N. Please try again. ")

while True:
    Loaner = input(" OPTIONAL - Does the customer want a loaner car..? (Y for Yes, N for No): ").upper()
    if Loaner in ["Y", "N"]:
        break
    else:
        ErrMsg(" ERROR - enter only Y or N. Please try again. ")

while True:
    PayMethod = input(" What is the customer's chosen payment method..? (F for Full, M for Monthly, D for Down Pay): ").upper()
    if PayMethod in PAY_METHODS:
        break
    else:
        ErrMsg(" ERROR - invalid pay method. Please try again. ")



DownPayAmt = 0
if PayMethod == "D":
        while True:
            try:
                DownPayDsp = input("Down Payment selected, please enter the down payment amount: ")
                DownPay = float(DownPayDsp)
            except:
                ErrMsg("Please enter only numbers.")
            else:
                DownPayDsp = DollarConvLib.dollarConv(DownPayAmt)
                break

ClaimNumList = []
ClaimDateList = []
ClaimAmtList = []


# this is where our program will store our PAST CLAIMS.

f = open('PastClaims.dat', 'r')
for i in f:
        PastClaims = i.split(',')
        ClaimNumList.append(PastClaims[0].strip())
        ClaimDateList.append(PastClaims[1].strip())
        ClaimAmt = PastClaims[2].strip()
        ClaimAmtList.append(DollarConvLib.dollarConv(ClaimAmt))
f.close()

# this is where the program will start performing calculations.

if PayMethod == 'F':
     PayMethod == 'FULL PAYMENT'
elif PayMethod == 'M':
     PayMethod == 'MONTHLY'
else: PayMethod == 'DOWN PAYMENT'

InsPremium = BASIC_PREMIUM + (Cars - 1) * BASIC_PREMIUM * (1 - CAR_DISCOUNT)

ExtLiabCost = 0
if ExtraLiability == "Y":
    ExtLiabCost = EXTRA_LIABILITY_COVERAGE * Cars


GlassCost = 0
if GlassCover == "Y":
    GlassCost = GLASS_COVERAGE * Cars

LoanCost = 0
if Loaner == "Y":
    LoanCost = LOANER_COVERAGE * Cars


TotalExtraCost = ExtLiabCost + GlassCost + LoanCost
TotPrem = TotalExtraCost + InsPremium
Taxes = TotPrem * HST_RATE
TotCost = TotPrem + Taxes

if PayMethod != 'Full':
        MonPay = (MONTHLY_PROCESS_FEE + TotCost - DownPayAmt) / 8
        MonPayDsp = DollarConvLib.dollarConv(MonPay)
else:
        MonPayDsp = 'N/A'


if DownPayAmt == 0:
        DownPayAmtDsp = 'N/A'


# define dates.

Today = datetime.datetime.now()

TodayStr = Today.strftime("%Y-%m-%d")

TodayMon = TodayStr[5:7]
TodayYr = TodayStr[:4]

if TodayMon == "12":
    FirstPayYr = int(TodayYr) + 1
    FirstPayMon = 1
else:
    FirstPayYr = int(TodayYr)
    FirstPayMon = int(TodayMon) + 1

    FirstPayDate = datetime.datetime(FirstPayYr, FirstPayMon, 1)
    FirstPayDateDsp = FirstPayDate.strftime("%Y-%m-%d")

    
    # time for outputs!

# calling upon the "DollarConvLib" library to convert anything that is a float / anything that has to do with money, and in return it saves us time by automatically putting in the ":.2f" instead of doing it for each f statement.
InsPremiumDsp = DollarConvLib.dollarConv(InsPremium)
ExtLiabCostDsp = DollarConvLib.dollarConv(ExtLiabCost)
GlassCostDsp = DollarConvLib.dollarConv(GlassCost)
LoanCostDsp = DollarConvLib.dollarConv(LoanCost)

TotalExtraCostDsp = DollarConvLib.dollarConv(TotalExtraCost)
TotPremDsp = DollarConvLib.dollarConv(TotPrem)
TaxesDsp = DollarConvLib.dollarConv(Taxes)
TotalCostDsp = DollarConvLib.dollarConv(TotCost)


print()
print("--------------------------------------------------------------------------------------------------")
print("                                       ONE STOP INSURANCE                                         ")
print()
print("                                       Store Num: 123456                                          ") # I put a fake store number here for fun, as it is typically found on receipts. particularly restaurants but also retail shops.
print(f"                                        Policy No. {str(POLICY_NUM)}                             ") # Policy number usually fits in this category of the receipt as well.
print("--------------------------------------------------------------------------------------------------")
print()
print()
print(f"Customer: {FirstCust}  {LastCust}                                                                ")
print()
print(f"Home Address: {Addr}                                           Phone Number: {PhoneDsp}          ")
print(f"City: {City}                                                                                     ")
print(f"Province: {Prov}                                                                                 ")
print(f"Postal Code: {Postal}                                                                            ")
print()
print()
print("--------------------------------------------------------------------------------------------------")
print()
print()
print("                                          Customer choices:                                       ")
print("                                         ------------------                                       ")
print(f"                                    Extra liability: {ExtraLiability}                            ")
print(f"                                    Glass coverage: {GlassCost}                                  ")
print(f"                                    Loaned car (if applicable): {Loaner}                         ")
print()
print()
print("--------------------------------------------------------------------------------------------------")
print()
print()
print(f"Method of Payment: {PayMethod}                                                                   ")
print("-------------------------------                                                                   ")
print(f"Number of vehicles: {CarsDsp}                                                                    ")
print()
print()
print("--------------------------------------------------------------------------------------------------")
print()
print("         ITEM / CHOICE                                                     AMOUNT                 ")
print("--------------------------------------------------------------------------------------------------")
print(f"      Insurance Premiums:                                                 {InsPremiumDsp}        ")
print(f"       Extra Liability:                                                   {ExtLiabCostDsp}       ")
print(f"       Glass Coverage:                                                    {GlassCostDsp}         ")
print(f"        Loaner Car/s:                                                     {LoanCostDsp}          ")
print(f"      Total Extra Cost:                                                   {TotalExtraCostDsp}    ")
print(f"       Total Premiums:                                                    {TotPremDsp}           ")
print(f"             HST:                                                         {TaxesDsp}             ")
print(f"          Total Cost:                                                     {TotalCostDsp}         ")
print(f"  Down Payment (if applicable):                                           {DownPayAmtDsp}        ")
print(f"       Monthly Payments:                                                  {MonPayDsp}            ")
print()
print()
print("--------------------------------------------------------------------------------------------------")
print()
print(f"                Invoice Date: {TodayStr}                                                         ")
print(f"          First Payment Date: {FirstPayDateDsp}                                                  ")
print()
print()
print("--------------------------------------------------------------------------------------------------")
print("                 CLAIM #                     CLAIM DATE                  AMOUNT                   ")
print("               -----------                  ------------                --------                  ")
for i in range(len(ClaimNumList)):
    print(f"        {ClaimNumList[i]}             {ClaimDateList}             {ClaimAmtList}             ")

    #time to write everything to the info file!

 
def SaveData(POLICY_NUM, FirstCust, LastCust, Addr, City, Prov, Postal, PhoneDsp, CarsDsp, ExtraLiability, GlassCover, Loaner, PayMethod, DownPayAmtDsp, TotPremDsp):
    with open("PastClaims.dat", "a") as f:
        f.write(f"{POLICY_NUM}, ")
        f.write(f"{FirstCust}, ")
        f.write(f"{LastCust}, ")
        f.write(f"{Addr}, ")
        f.write(f"{City}, ")
        f.write(f"{Prov}, ")
        f.write(f"{Postal}, ")
        f.write(f"{PhoneDsp}, ")
        f.write(f"{CarsDsp}, ")
        f.write(f"{ExtraLiability}, ")
        f.write(f"{GlassCover}, ")
        f.write(f"{Loaner}, ")
        f.write(f"{PayMethod}, ")
        f.write(f"{DownPayAmtDsp}, ")
        f.write(f"{TotPremDsp}\n")

# Define the function to display a blinking message
def BlinkingMsg(message, duration=5, interval=0.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f'\r{message}')
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write('\r' + ' ' * len(message))
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write(f'\r{message} - Complete\n')
    sys.stdout.flush()


    SaveData(POLICY_NUM, FirstCust, LastCust, Addr, City, Prov, Postal, PhoneDsp, CarsDsp, ExtraLiability, GlassCover, Loaner, PayMethod, DownPayAmtDsp, TotPremDsp)

# Display blinking message
BlinkingMsg("Saving Policy Data...", duration=3)

print("Policy information has been successfully saved to PastClaims.dat ...!")
print()

while True:
    Cont =  input("Do you want to process another claim..? (Y / N): ").upper()
    if Cont == "N":
        break
    elif Cont != "Y":
        print("Invalid input. Please enter 'Y' or 'N'.")



    


































    




                                                  



















                       





