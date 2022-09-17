print("Welcome to XYZ Bank EMI Calculator!")
loanTypeInput = input("Enter the loan type for which EMI has to be calculated: ")
# User input for principal amount or loan amount
p = float(input("Enter the principal or loan amount: "))  
# User input for rate of interest per annum(per year)
R = float(input("Enter the rate of interest per annum: "))
# User input for loan tenure(in years)
N = int(input("Enter the loan tenure in year: "))
# The formula for calculation of emi is emi = (p * r * (1+r)**n)/((1 + r) ** n -1); where r is the rate of interest per month and n is the number of monthly 
# installments. n can be obtained by multiplying loan tenure in years by 12 and rate of interest per month can be obtained by R/12/100 or R/(12 *100)
# The formulas for conversion of R and N are computed and stored in variables n and r respectively
n = N * 12    
r = R/(12 * 100)
# The user is given the option to input the type of loan for which they want to calculate EMI. To make the input case insensitive, we have used .lower() and
# .upper() to check if the input is present in the list loanTypeInput is one out of personal, car and home loan. Else "Invalid Input" message will be printed
if loanTypeInput.lower() or loanTypeInput.upper() == 'Personal Loan':
    if (p >= 50000 and p <= 400000) and (R>=10.99 and R <=24) and (N>=1 and N<=5):
        emi = (p * r * (1+r)**n)/((1 + r) ** n -1)
        print(emi)
        totalAmountPayable = emi * n
        print(totalAmountPayable)
    else:
        print("Please enter a valid input of principal or rate of interest or loan tenure")
elif loanTypeInput.lower() or loanTypeInput.upper() == 'Home Loan':
    if (p >= 300000 and p <= 50000000) and (R>=6.9 and R <=11) and (N>=1 and N<=30):
        emi = (p * r * (1+r)**n)/((1 + r) ** n -1)
        print(emi)
        totalAmountPayable = emi * n
        print(totalAmountPayable)
    else:
        print("Please enter a valid input of principal or rate of interest or loan tenure")
elif loanTypeInput.lower() or loanTypeInput.upper() == 'Car Loan':
    if (p >= 100000 and p <= 10000000) and (R>=7 and R <=17.5) and (N>=1 and N<=7):
        emi = (p * r * (1+r)**n)/((1 + r) ** n -1)
        print(emi)
        totalAmountPayable = emi * n
        print(totalAmountPayable)
    else:
        print("Please enter a valid input of principal or rate of interest or loan tenure")
else:
        print("Invalid input")
