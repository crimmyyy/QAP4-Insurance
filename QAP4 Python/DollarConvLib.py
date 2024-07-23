def dollarConv(dollarValue):
    dollarValueStr = "${:,.2f}".format(dollarValue)
    return dollarValueStr

# CREDIT : ZACHARY COLLIER

def dollarConv(dollarValue):
    try:
        # Ensure dollarValue is converted to float
        dollarValue = float(dollarValue)
        dollarValueStr = "${:,.2f}".format(dollarValue)
        return dollarValueStr
    except ValueError:
        return "Invalid value"
# A function that I have added to the program, otherwise it would not work and give a syntax error. It helps convert a string to a float.


