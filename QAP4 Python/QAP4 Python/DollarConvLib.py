

# CREDIT : ZACHARY COLLIER

def dollarConv(dollarValue):
    try:
        # Ensure dollarValue is converted to float
        dollarValue = float(dollarValue) # Converts a string into a float.
        dollarValueStr = "${:,.2f}".format(dollarValue)
        return dollarValueStr
    except ValueError:
        return "Invalid value"



