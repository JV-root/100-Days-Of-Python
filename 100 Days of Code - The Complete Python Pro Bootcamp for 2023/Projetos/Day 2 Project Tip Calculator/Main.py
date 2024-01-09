# Name: Day 2 Project Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print('Welcome to the trip calculator')
bill = float(input('What was the total bill? '))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
how_many_people = int(input('How many people to split the bill? '))

bill_with_tip = bill + (bill * percentage / 100)
each_person_pay = bill_with_tip / how_many_people
final_amount = round(each_person_pay, 2)
final_amount = "{:.2f}".format(each_person_pay)

print(f'Each person should pay: ${final_amount}')

