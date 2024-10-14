import Savefile as sf
import time as t
import asfunc
import os




print("Astroverge: The Void" +" \n")

try:
    while True:
        print(f"Welcome back {sf.name}")
        enter_pass = input("Enter Your Password:")

        if enter_pass == sf.password:
            print("Welcome Back", sf.name)
            t.sleep(3)
            break

        else:
            print("wrong password")
            t.sleep(1)
            os.system('clear')
    asfunc.gameplay()
except AttributeError as a:
    new_name = input("what is your username going to be?")
    new_pass = input("input a password on your save file to secure it:")
    os.system('clear')

    name = new_name
    password = new_pass

    f = open("Savefile.py", "w")

    f.write("name = "+ "'" + str(name) + "'" + "\n")
    f.write("password = " + "'" + str(password) + "'" + "\n")

    f.close()

    print("your file has been created!")
    t.sleep(3)
    asfunc.tutorial()
    print("we hope you enjoy the astroverge, and make sure, dont die, good night!")
    t.sleep(3)
    os.system('clear')
    t.sleep(3)
    asfunc.gameplay()
