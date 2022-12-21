#Question 2
#variables defined for different values:
Gross_income  = int (input ('Enter your Gross Income to the nearest penny:'))
Standard_deduction = 10000
Dependent_deduction = 3000
Number_of_dependents = int (input ('No. of Dependents:'))
#Formula for Taxable income:
Taxable_income = Gross_income  - Standard_deduction - (Dependent_deduction * Number_of_dependents )
#Formula for Tax:
Tax = Taxable_income * 20%Gross_income

print ('Person Income tax is = ', Tax)


