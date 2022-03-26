# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment_amount = int(input("Enter the number for investment amount without \",\" please: "))
interest_rate = int(input("Enter the interest rate in percentage without %: "))
num_years_invest = int(input("How long is the number of years to invest?: "))

future_value = (investment_amount * (1 + interest_rate/100)) * num_years_invest

print(future_value)