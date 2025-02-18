salary = float(input("Enter your salary for the month: "))

month = input("Enter the name of the month: ")

savings = float(input("Enter the percentage of savings: ")) # type: ignore

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
