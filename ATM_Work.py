
import random
customers_database = {}
def init():

  print('Welcome to Zuri Bank! \n')

  import datetime
  current_time = datetime.datetime.now()
  print(f"Today's date and current time is: {current_time.strftime('%c')} \n")

  have_account = int(input('Do you have an account with us? 1(yes) 2(no) \n'))

  if(have_account == 1):
    login()

  elif(have_account == 2):
    register()

  else:
    print('You have selected an invalid option \n')
    init()
    
acc_balance = float(1000)

def register():
  print('Create your unique bank account with us. \n')
  email = input('What is your email address? \n')
  global first_name
  first_name = input('What is your first name? \n')
  global last_name
  last_name = input('What is your last name? \n')
  password = input('Create your unique password. \n')

  account_number = account_number_generator()

  user_details = [email, first_name, last_name, password]


  customers_database[account_number] = [first_name, last_name, email, password]

  print('Your account has been created.')
  print(' == ==== ==== ==== ==== ==== ==')
  print(f'This is your account number: {account_number}.')
  print(' == ==== ==== ==== ==== ==== == ')
  print('Make sure to keep it safe. \n')

  login()

def login():
  print('Login to your account. \n')
  user_account_number = int(input('What is your account number? \n'))
  password = input('What is your password? \n')

  for account_number,user_details in customers_database.items():
    if account_number == user_account_number:
      if user_details[3] == password:
        bank_operations(user_details)

  print('Invalid account number or password')
  login()

def bank_operations(user):
  print(f'Dear {first_name} {last_name}. \n')
  selected_option = input('What would you like to do? (1)Deposit (2)Withdrawal (3)Logout (4)Exit: ')
  try:
    selected_option = int(selected_option)
  except:
    print('Error, please try again and enter a numeric value')
    quit()
  
  if selected_option == 1:
    cash_deposit()

  elif selected_option == 2:
    withdrawal_ops()

  elif selected_option == 3:
    logout()

  elif selected_option == 4:
    exit()

  else:
    print('Invalid option selected.')
    bank_operations()


def withdrawal_ops():
  cash_amount = float(input('How much would you like to withdraw? '))
  if cash_amount > acc_balance:
    print('Insufficient fund. Please make a deposit into your account. \n')

  else:
    print(f'Please take your NGN{cash_amount} cash. \n')
    remaining_balance = acc_balance - cash_amount
    print(f'Your remaining balance is: NGN{remaining_balance}. \n')

  print('Thank you for banking with us.')
  exit()
  

def cash_deposit():
  deposit = float(input('How much would you like to deposit? '))
  current_balance = acc_balance + deposit
  print('Deposit was successfully...')
  print(f'You made a deposit of NGN{deposit}')
  print(f'Your account balance is NGN{current_balance} \n')
  print('Thank you for banking with us.')
  exit()


def complaints():
  complaint = str(input('What issue will you like to report? \n'))
  print('Thank you for contacting us. \n')
  print(f'This is your complaint: {complaint}. \n')
  print('Please kindly note that your complaint will be resolved within five(5) working days.')
  print('However if it is an emergency, you can visit any nearest branch. \n')
  print('Thank you for banking with us.')
  exit()


def account_number_generator():
  return random.randrange(1000111111,9999999999)

def logout():
  login()

init()
