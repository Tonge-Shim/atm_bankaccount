import random
import string
import pandas as pd
from pandas import Series, DataFrame
import ast 

def show_account(card_account):
    for i in range(1, len(card_account) + 1):
        print("{}. {}".format(i,card_account[i-1][0]))
        
def show_menu():
    print("------------------")
    print("1. balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("------------------")
    menu = int(input("Please choose one: "))
    return menu

def deposit(selected_account, money, card_account):
    card_account[selected_account -1][1] = card_account[selected_account-1][1] + money
    
    
    
    

def bring_info(id_num, account_info):
    id_info = account_info[account_info['Card_ID'] == id_num]
    pin = id_info['PIN']
    account = ast.literal_eval(id_info['account_n_balance'][0])
    return pin, account

    
def make_acc_name(L):
    name_len = L
    name_candidate = string.ascii_letters
    name = ''
    for i in range(name_len):
        name += random.choice(name_candidate)
    return name


def make_balance(L):
    bal_len = L
    bal_candidate = string.digits
    balance = str(random.randrange(1, 10))
    for i in range(bal_len - 1):
        balance += random.choice(bal_candidate)
    return int(balance)