"""
Coding Challenge #1: The Coupon Code

Challenge: Take an input of: enteredCode, correctCode, currentDate, expirationDate and
return True or False based on whether the Coupon Code is valid or not.

Example: 123, 123, January 1 2021, January 31 2021 = Valid

"""

import datetime

def check_coupon(enteredCode, correctCode, currentDate, expirationDate):
    current_date = currentDate.split(" ")
    current_date_updated = current_date[0][0:3] + current_date[1] + current_date[2]
    c_date = datetime.datetime.strptime(current_date_updated, '%b%d%Y').strftime('%Y-%m-%d')
    exp_date = expirationDate.split(" ")
    exp_date_updated = exp_date[0][0:3] + exp_date[1] + exp_date[2]
    e_date = datetime.datetime.strptime(exp_date_updated, '%b%d%Y').strftime('%Y-%m-%d')
    
    if enteredCode == correctCode and e_date > c_date:
        return True
        
    else:
        return False


if __name__ == '__main__':
        #Cheching with Valid input, should return True
        print("Coupon Validation result is :",check_coupon(123, 123, 'January 20 2020', 'January 18 2021'))
        #Cheching with Invalid input, should return False
        print("Coupon Validation result is :",check_coupon(123, 123, 'January 20 2021', 'January 18 2021'))
        #Cheching with Invalid input, should return False
        print("Coupon Validation result is :",check_coupon(123, 1234, 'January 20 2021', 'January 30 2021'))