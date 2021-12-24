import random
import string
import pandas as pd
from pandas import Series, DataFrame
from utils import *
#inserting card -> write card number

if __name__ == "__main__":
    while True:
        account_info = pd.read_csv("./account_infos.csv")
        card_id = int(input("please press your card id: "))
        card_pin, card_account = bring_info(card_id)
        idx = account_info[account_info['Card_ID'] == card_id].index
        pressed_pin = int(input("please enter the pin number: "))
        if card_pin == pressed_pin:
            show_account(card_account)
            selected_account = int(input("please select the account number(only the number): "))
            menu_num = show_menu()
            if menu_num == 1:
                print("Your Balance: {} $".format(card_account[selected_account-1][1]))

            elif menu_num == 2:
                deposit_num = int(input("how much would you like to deposit? "))
                deposit(selected_account, deposit_num, card_account)
                
            else:
                withdraw = int(input("how much would you like to withdraw? "))
                if card_account[selected_account - 1][1] >= withdraw:
                    card_account[selected_account - 1][1] = card_account[selected_account - 1][1] - withdraw
                else:
                    print("sorry, lack of balance")
            print("renewing account informations...")
            id_info = account_info[account_info['Card_ID'] == card_id]
            id_info['account_n_balance'] = str(card_account)
            account_info = account_info.drop(idx)
            new_info = pd.concat([account_info, id_info])
            new_info.to_csv('./account_infos.csv', sep = ',', index = False)
            print("done")
            print("bye")
            print("=========================================================")
                
        else:
            print("WRONG PIN NUMBER")
            
            
            
            
        
        
    
    