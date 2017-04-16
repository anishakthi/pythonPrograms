def calculate_bil_amt(amount, tax, tips) :
    return amount + amount * (tax+tips)/100
print "Total bill amount is Rs%r " % round(calculate_bil_amt(250.0,10,5))
