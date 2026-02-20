import pyautogui as bot
import time as t

possible_passwords = '''Sarankumar@200222# Sarankumar#200222@ Sarankumar2002@# Sarankumar22@# Sarankumar2002@# Sarankumar222002@# Sarankumar200222@# Saran@22kumar2002# Sarankumar@2002#22 Sarankumar#22@2002 Kumarsaran@200222 Sarankumarsaran@200222 Sarankumar&2002&'''

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