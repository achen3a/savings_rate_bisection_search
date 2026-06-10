## intro and initializing house hunting variables
print("Let's go house hunting!")
print("With this program, we will determine what portion of your monthly salary to save to make the down payment on your dream house.")
annual_salary = float(input("To get started, please enter your starting annual salary."))
semi_annual_raise = float(input("What is your semi-annual raise? Please enter as a decimal."))
r = float(input("What is the annual return on your savings? Please enter as a decimal."))
months = int(input("In how many months would you like to make your down payment?"))
total_cost = float(input("Please enter the cost of your dream home."))
portion_down_payment = float(input("Finally, what portion of the cost of your dream house do you need for a down payment? Please enter as a decimal."))
savings_rate = 0.0
current_savings = 0.0
monthly_salary = annual_salary/12
down_payment = portion_down_payment*total_cost

## bisection variables
number_of_bisection_searches = 0
lower = 0
upper = 10000
middle = (lower + upper)/2
epsilon = 100

## finding savings rate
## making sure they're not too poor
savings_rate = middle/10000
for i in range(0, months):
    if (i+1) % 6 == 0 and (i+1) != 0:
        current_savings += current_savings*(r/12)
        current_savings += (monthly_salary*savings_rate)
        monthly_salary += monthly_salary*semi_annual_raise
    else:
        current_savings += current_savings*(r/12)
        current_savings += (monthly_salary*savings_rate)
if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    current_savings = 0
    monthly_salary = annual_salary/12
    ## finding savings rate fr
    while abs(current_savings - down_payment) > epsilon:
        current_savings = 0
        monthly_salary = annual_salary/12
        number_of_bisection_searches += 1
        savings_rate = middle/10000
        for i in range(0, months):
            if (i+1) % 6 == 0 and (i+1) != 0:
                current_savings += current_savings*(r/12)
                current_savings += (monthly_salary*savings_rate)
                monthly_salary += monthly_salary*semi_annual_raise
            else:
                current_savings += current_savings*(r/12)
                current_savings += (monthly_salary*savings_rate)
        if current_savings > down_payment:
            upper = middle
            middle = (lower + upper)/2
        else:
            lower = middle
            middle = (lower + upper)/2
    print("The recommended savings rate per month is " + str(savings_rate) + ".")
    print("The number of bisection searches performed is " + str(number_of_bisection_searches) + ".")