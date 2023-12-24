#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import random

# All accounts data stored in a dictionary
all_accounts = {}

def welcome_message():
    print("*" * 50)
    print("Welcome to Bank of Bhavishnu")
    print("This is a welcome note with decoration.")
    print("*" * 50)

def create_account():
    print("\nCreating an account:")
    
    # Step 1: Get customer name
    while True:
        name = input("Enter your name (letters only): ")
        if name.isalpha():
            break
        else:
            print("Invalid name. Please enter only letters.")
    
    # Step 2: Get Aadhaar card number
    while True:
        aadhaar_number = input("Enter your Aadhaar card number (12 digits): ")
        if re.match(r'^\d{12}$', aadhaar_number):
            break
        else:
            print("Invalid Aadhaar number. Please try again.")
    
    # Step 3: Get PAN card number
    while True:
        pan_number = input("Enter your PAN card number (in PAN format): ")
        if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan_number):
            break
        else:
            print("Invalid PAN number. Please try again.")
    
    # Step 4: Get email ID
    email = input("Enter your email ID: ").lower()
    
    # Step 5: Get mobile number
    while True:
        mobile_number = input("Enter your mobile number (10 digits): ")
        if re.match(r'^\d{10}$', mobile_number):
            break
        else:
            print("Invalid mobile number. Please try again.")
    
    # Step 6: Send OTP
    otp = str(random.randint(100000, 999999))
    print(f"OTP sent to {mobile_number}: {otp}")
    
    # Validate OTP
    while True:
        entered_otp = input("Enter the OTP: ")
        if entered_otp == otp:
            print("Account created successfully!")
            break
        else:
            print("Incorrect OTP. Please try again or request a new OTP.")
            resend_otp = input("Do you want to resend OTP? (yes/no): ")
            if resend_otp.lower() != 'yes':
                break
    
    # Step 7: Get initial deposit
    while True:
        initial_deposit = int(input("Enter the initial deposit amount (minimum 5000): "))
        if initial_deposit >= 5000:
            break
        else:
            print("Minimum deposit amount is 5000. Please enter a valid amount.")
    
    # Generate account number
    account_number = random.randint(1000000000, 9999999999)
    
    # Store account details
    account_details = {
        'Name': name,
        'Aadhaar Number': aadhaar_number,
        'PAN Number': pan_number,
        'Email': email,
        'Mobile Number': mobile_number,
        'Account Number': account_number,
        'Balance': initial_deposit
    }
    
    all_accounts[account_number] = account_details
    
    # Display account details
    print("\nAccount Details:")
    for key, value in account_details.items():
        print(f"{key}: {value}")
    print("*" * 50)

def deposit_amount():
    print("\nDeposit Amount:")
    name = input("Enter your name: ")
    account_number = int(input("Enter your account number: "))
    
    # Check if the account exists
    if account_number in all_accounts and all_accounts[account_number]['Name'] == name:
        amount = int(input("Enter the amount to deposit: "))
        all_accounts[account_number]['Balance'] += amount
        print(f"Deposit successful. Available balance: {all_accounts[account_number]['Balance']}")
    else:
        print("Invalid name or account number. Please check and try again.")

def withdraw_amount():
    print("\nWithdraw Amount:")
    name = input("Enter your name: ")
    account_number = int(input("Enter your account number: "))
    
    # Check if the account exists
    if account_number in all_accounts and all_accounts[account_number]['Name'] == name:
        amount_to_withdraw = int(input("Enter the amount to withdraw: "))
        if amount_to_withdraw > all_accounts[account_number]['Balance'] - 5000:
            print("Insufficient balance. Available balance: ", all_accounts[account_number]['Balance'])
        else:
            all_accounts[account_number]['Balance'] -= amount_to_withdraw
            print(f"Withdrawal successful. Available balance: {all_accounts[account_number]['Balance']}")
    else:
        print("Invalid name or account number. Please check and try again.")

def close_account():
    print("\nClose Account:")
    name = input("Enter your name: ")
    account_number = int(input("Enter your account number: "))
    
    # Check if the account exists
    if account_number in all_accounts and all_accounts[account_number]['Name'] == name:
        del all_accounts[account_number]
        print("Account closed successfully.")
    else:
        print("Invalid name or account number. Please check and try again.")

# Main program
welcome_message()

while True:
    print("\nOptions:")
    print("1. Create Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Show Current Balance")
    print("5. Account Details")
    print("6. Close Account")
    print("7. Exit")
    
    choice = int(input("Enter your choice (1-7): "))
    
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit_amount()
    elif choice == 3:
        withdraw_amount()
    elif choice == 4:
        account_number = int(input("Enter your account number: "))
        if account_number in all_accounts:
            print(f"Current balance: {all_accounts[account_number]['Balance']}")
        else:
            print("Invalid account number. Please check and try again.")
    elif choice == 5:
        account_number = int(input("Enter your account number: "))
        if account_number in all_accounts:
            print("\nAccount Details:")
            for key, value in all_accounts[account_number].items():
                print(f"{key}: {value}")
            print("*" * 50)
        else:
            print("Invalid account number. Please check and try again.")
    elif choice == 6:
        close_account()
    elif choice == 7:
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")


# In[ ]:




