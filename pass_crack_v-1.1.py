import pyautogui as bot
import random as r
import time as t

first_name = ''' ''' # add the first names you want to use in the password list separated by space
symbols=''' ''' # add the symbols you want to use in the password list separated by space
numbers = ''' ''' # add the numbers you want to use in the password list separated by space

first_name_list = list(first_name.split(' '))
symbols_list = list(symbols.split(' '))
numbers_list = list(numbers.split(' '))

random_name = r.choice(first_name_list)
random_symbol = r.choice(symbols_list) 
random_number = r.choice(numbers_list)

pass_word = f'{random_name}{random_symbol}{random_number}' # you can change the order of the password as per your requirement    

t.sleep(5)
while True:
    bot.typewrite(pass_word)
    bot.press('enter')
    t.sleep(2)
    bot.click() # place the cursor where the password is to be entered and click to focus on the password field
    bot.hotkey('ctrl', 'a')
    bot.press('backspace')
    t.sleep(4)
    print(f'Attempted password: {pass_word}')
    random_name = r.choice(first_name_list)
    random_symbol = r.choice(symbols_list) 
    random_number = r.choice(numbers_list)
    pass_word = f'{random_name}{random_symbol}{random_number}' # you can change the order of the password as per your requirement
