## ATM machine project that allows user to withdraw, deposit, or make a complaint.
name = input("What is your username?  \n")
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']
balance = 0
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
if(name in allowedUsers):
    password = input("Your password?  \n")
    userId = allowedUsers.index(name)

    while password == allowedPassword[userId]:
        
        print('\nWelcome %s!' % name)
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        print("Current date and time:", dt_string)        
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))
        if(selectedOption == 1):
            print('You selected %s.' % selectedOption)
            withdrawalAmt = int(input('How much do you want to withdraw? '))
            if withdrawalAmt > balance:
                print('The amount requested is greater than the balance. ')
            else:
                balance = balance - withdrawalAmt
                print('Take your cash. Your balance is $%s.' % balance) 

        elif(selectedOption == 2):
            print('You selected %s.' % selectedOption)
            depositAmt = int(input('How much do you want to deposit? '))
            balance = depositAmt + balance
            print('Your deposit was successful. Balance: $%d.' % balance)
            
        elif(selectedOption == 3):
            print('You selected %s.' % selectedOption)
            complaint = input('What issue will you like to report: ')
            print('Thank you for contacting us.')
            
        else:
            print('Invalid Option selected, please try again.')
    else:

        print('Password Incorrect, please try again.')  

else:

    print('Name not found, please try again.')             
