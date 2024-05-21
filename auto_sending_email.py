#  sending e-mail automation 

import pyautogui

from time import sleep

import webbrowser

import pyperclip

import psutil



webbrowser.get('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
webbrowser.open('http://gmail.com')


# maximize windows if it restore down and open text box

pyautogui.hotkey('win', 'up')


sleep(10)

pyautogui.click(x=99, y=196)

sleep(3)



# Now we will transform our poeple those whome we will send email
emails = ['email1@mail.com','email2@mail.com', 'email3@mail.com', 'email4@mail.com']

for email in emails:
   
        pyperclip.copy(email)
        pyautogui.hotkey("ctrl", "v")
        sleep(1)

# add the subject and content of email

pyautogui.press('tab')
sleep(1)

pyautogui.write('Meeting Reminder ')
pyperclip.copy('📢')
pyautogui.hotkey("ctrl", "v")
sleep(1)

pyautogui.press('tab')
sleep(1)

pyautogui.write('Dear Team, \nFriendly reminder that we have a meeting booked for today at 8 am to discuss the latest project updates and align our strategies. \nYour presence is crucial')
pyperclip.copy('!')
pyautogui.hotkey("ctrl", "v")

sleep(2)

#  send email 
# pyautogui.hotkey('ctrl', 'enter')


