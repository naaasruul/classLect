print("-----------------------------------")
print("Loan Calculation System")

userName = input("enter your name: ")
loanAmount = float(input("enter your loan amount: ")) #100000
loanPeriod = int(input("enter your loan period 5 years or 7 years: ")) # 5 years

print("")
print("Name: ", userName)
print("Loan Amount: RM", loanAmount)
print("Loan period (years): ", loanPeriod)

print("-----------------------------------")

if loanAmount < 30000: # loan amout less than 300000
    # if 5 years
    if loanPeriod == 5:
        interest = 3.23/100
        totalInterest = loanAmount * interest
        print("interest rate: 3.23%")

        # output total interest paid
        print("total interest paid: RM",totalInterest)
        # output total interest paid

        # output total loan
        totalLoan = loanAmount + totalInterest
        print("total loan amout: RM", totalLoan)

        # output montly payment
        monthlyPayment = (totalInterest + loanAmount) / (loanPeriod * 12)
        print("monthly payment: RM", round(monthlyPayment,2))

     # if 7 years
    else: 
        interest = 3.15/100
        totalInterest == loanAmount * interest
        print("interest rate: 3.15%")
        print("total interest paid: RM",totalInterest)
        totalLoan = loanAmount + totalInterest
        print("total loan amout: RM", totalLoan)
        monthlyPayment = (totalInterest + loanAmount) / (loanPeriod * 12)
        print("monthly payment: RM", round(monthlyPayment,2))

elif loanAmount >= 30000 and loanAmount < 60000:
    # if 5 years
    if loanPeriod == 5:
        interest = 2.85/100
        totalInterest = loanAmount * interest
        print("interest rate: 2.85%")
        print("total interest paid: RM",round(totalInterest,2))
        
        totalLoan = loanAmount + totalInterest
        print("total loan amout: RM", totalLoan)
        monthlyPayment = (totalInterest + loanAmount) / (loanPeriod * 12)
        print("monthly payment: RM", round(monthlyPayment,2))

    # if 7 years
    else:
        interest = 2.93/100
        totalInterest = loanAmount * interest
        print("interest rate: 2.93%")
        print("total interest paid: RM", round(totalInterest,2))
        totalLoan = loanAmount + totalInterest
        print("total loan amout: RM", totalLoan)
        monthlyPayment = (totalInterest + loanAmount) / (loanPeriod * 12)
        print("monthly payment: RM", round(monthlyPayment,2))

elif loanAmount >= 60000  and loanAmount < 110000:
    # if 5 years
    if loanPeriod == 5:
        interest = 2.75/100
        totalInterest = loanAmount * interest
        print("interest rate: 2.75%")
        print("total interest paid: RM", totalInterest)
        totalLoan = loanAmount + totalInterest
        print("total loan amout: RM", totalLoan)
        monthlyPayment = (totalInterest + loanAmount) / (loanPeriod * 12)
        print("monthly payment: RM", round(monthlyPayment,2))
    
    # if 7 years
    else:
        interest = 2.83/100
        totalInterest = loanAmount * interest
        print("interest rate: 2.83%")
        print("total interest paid: RM", totalInterest)
        totalLoan = loanAmount + totalInterest
        print("total loan amout: RM", totalLoan)
        monthlyPayment = (totalInterest + loanAmount) / (loanPeriod * 12)
        print("monthly payment: RM", round(monthlyPayment,2))

else:
    # if 5 years
    if loanPeriod == 5:
        interest = 2.53/100
        totalInterest = loanAmount * interest
        print("interest rate: 2.53%")
        print("total interest paid: RM", totalInterest)
        totalLoan = loanAmount + totalInterest
        print("total loan amout: RM", totalLoan)
        monthlyPayment = (totalInterest + loanAmount) / (loanPeriod * 12)
        print("monthly payment: RM", round(monthlyPayment,2))

    # if 7 years
    else:
        interest = 2.52/100
        totalInterest = loanAmount * interest
        print("interest rate: 2.52%")
        print("total interest paid: RM",totalInterest)
        totalLoan = loanAmount + totalInterest
        print("total loan amout: RM", totalLoan)
        monthlyPayment = (totalInterest + loanAmount) / (loanPeriod * 12)
        print("monthly payment: RM", round(monthlyPayment,2))



