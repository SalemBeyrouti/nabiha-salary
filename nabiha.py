salary = float(input("Enter your salary for the month: "))

month = input("Enter the name of the month: ")

savings = float(input("Enter the percentage of savings: ")) 

rent = float(input("Enter the percentage of rent: "))

electricity = float(input("Enter the percentage of electricity: "))

totalsavings = (savings/100)*salary

totalrent = (rent/100)*salary

totalelectricity = (electricity/100)*salary

totalspending = totalrent + totalsavings + totalelectricity

remaindersalary = salary - totalspending

yearlyrent = totalrent*12

yearlyelectricity = totalelectricity*12

salarysquared = salary*salary

print("The amount allocated to savings: ", totalsavings  )
print("The amount allocated to electricity: ", totalelectricity)
print("The amount allocated to rent: ", totalrent)
print("The total amount spent on savings, rent and electricity: ", totalspending)
print("The remainder salary: ", remaindersalary)
print("Yearly rent: ", yearlyrent)
print("Yearly electricity: ", yearlyelectricity)
print("Salary squared just for fun: ", salarysquared)