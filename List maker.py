import random
import sys
import os
import time

os.system("clear")
os.system("figlet Attack Starting")
print("Author | arhaby")
time.sleep(2)
print("Telegram | @rhaby")
time.sleep(1)
print("ChannelTelegram | @ciku370")
time.sleep(1)




#================================================
#وفرت لكم اغلب النطاقات الي تحتاجها في التخمين
#(hotmail.com)
#(gmail.com)
#(outlook.sa)
#(Yahoo.com)
#================================================
uesr = '078' #اليوزر المراد التخمين عليه بين النقطتين اكتبه 
chars2 = '1234567890' #ارقام واحرف لو ترغب
email = ''#اختار نطاق معين مثل هوتميل او جميل 
print('=========================================')
amount = input('What is a number List: ')
amount = int(amount)
length2 = input('How many letters or numbers do you want to add?: ')
length2 = int(length2)

print('==================================')

for password in range(amount):
    password = ''
    
    
    for item in range(length2):
         password = ''
    for item in range(length2):
        password += random.choice(chars2)



    print (uesr+password+email)
    with open('password.txt', 'a') as x:
     x.write(uesr + password + email + '\n')
