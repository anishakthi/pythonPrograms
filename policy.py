from datetime import datetime
from dateutil.relativedelta import relativedelta

name =  raw_input("Enter policy name ")
term = raw_input("Enter the term ")
startDate = datetime.now().strftime ("%Y-%m-%d")


endDate = startDate + relativedelta(years=1)
print ("Start date of policy is %s" %startDate)
print ("End date of policy is %s" %endDate)
