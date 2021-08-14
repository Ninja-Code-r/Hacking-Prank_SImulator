
import time
import random

# Showing Headline

print(" ")
print(" ")
print(" ")
print(" *** Welcome to Trilok Arya's Personal Hacking Database ***")
time.sleep(5)

#giving Option to user

print('''
1. Wifi Password
2. Mobile pin 4 digit
3. Mobile password 6 digit
4. Mobile Pattern Unlock
5. Instagram Password Cracker
6. Facebook Password Cracker
7. Exit''')

 # Taking Input from User
a = int(input(" Enter Your Choice Trilok :\n"))

# For Wifi Password
if a == 1 :
    print(" Wait a Minute Sir !!! ")
    time.sleep(3)
    ab=input("Enter the Name of wifi Network :\n")
    print(f" The Password of ",ab," is '123Bhupesh456' ")


# For Mobile pin 4 digit
if a == 2 :
    print(" Connect your Mobile...")
    time.sleep(3)
    print(" vivo 1820 connected successfuly !!!")
    time.sleep(5)
    i=1000
    while i<=2003:
        print(i)
        i=i+1
    print(" password of vivo 1820 is '2003' ")

# For mobile password 6 digit
if a == 3 :
    print(" Connect your Mobile...")
    time.sleep(3)
    print(" vivo 1820 connected successfully !!!")
    i=100001
    while i<=123456:
        print(i)
        i=i+1
    print(" Password is '123456' ")


# For Mobile  Pattern Lock
if a == 4 :
   print("Trying Different combinations...")
   time.sleep(10)
   print(" Password is Cracked Successfuly !!!")


# For Instagram password
if a == 5 :
    z=input(" Please Enter a Username :")
    print(" Fetching Details From DataBases...")
    time.sleep(8)
    print(f" Password of username",z," is '123TRILOK2006'")


# Facebook Password
if a == 6 :
    z=input("Enter the Name of Your Friend:\n")
    print(" Fetching Details From DataBases...")
    time.sleep(8)
    print(f" Password of your friend",z," is '9111Dinesh'")

# For Exit the Programm
if a == 7 :
    print(" Thank you , Trilok Sir ")

if a > 7 :
    print(" Please ,Choose Correctly")



