#Amin Hagos
#18-11-2014
#Calculate Pay

def calculate_basic_pay(hours,pay):
    total = hours * pay
    return total

def calculate_overtime_pay(hours,pay):
    overtime_pay = pay * 1.5
    overtime_hours = hours - 40
    overtime_total = overtime_pay * overtime_hours
    basic_total = pay * 40
    total = basic_total + overtime_total
    return total
    
def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_overtime_pay(hours,pay)
    return total

def input_work_details():
    hours = int(input("please enter the amount of hours you have worked:" ))
    pay = int(input("please enter your hourly pay rate: "))
    return hours,pay
    
def calculate_pay():
    hours,pay = input_work_details()
    total = calculate_total_pay(hours,pay)
    return hours,pay,total
    
def display_total_pay(total):
    total = calculate_pay()
    return total

work_details = input_work_details()
print(work_details)

basic_pay = calculate_basic_pay(total)
print(basic_pay)

overtime_pay = claculate_overtime_pay(hours,pay)
print(overtime_pay)

total_pay = calculate_total_pay(hours,pay)
print(total_pay)

display = display_total_pay(total)
print(display)
