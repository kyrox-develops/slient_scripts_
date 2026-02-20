import pyautogui as bot
import time as t

possible_passwords = '''Sarankumarrio22@# Sarankumarrio2002@# Sarankumar@20022 Riokumarsaran22@# Saranriokumar2002@# Saranriokumar22@# Saranriokumar222002@# Sarankumar@22 Saranriokumar@2002 Kumarsaran2002@#'''

pass_list =list(possible_passwords.split(' '))
# for i in pass_list:
#     print(i)
t.sleep(5)
for i in pass_list:
    t.sleep(1)
    bot.write(f'{i}')
    bot.press('enter')
    t.sleep(4)
    bot.click(button='left')
    bot.hotkey('ctrl', 'a')
    bot.press('backspace')
    print(f'{i} is not the password')

print('All passwords are tried')