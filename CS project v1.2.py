######################FUNCTIONS################################################    

import os
import math
import random
import smtplib
import json


#generates a random password containing alphabets numbers and special characters#
def create():
    

    import secrets
    import string

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd_length=12
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
        
    #copies the password generated to the users clipboard    
    import pyperclip
    pyperclip.copy(pwd)
        
    print("Your new Password is: ",pwd,"and has been copied to you clipboard")
   
    
        
#deletes an existing account        
def deleteacc():
           
    user = input("Enter the username of the account which you want to delete: ")
    passw = input("Enter the password of the given account: ")
    
    print("If this account is yours, please enter the security key to continue")
    sec_key = int(input(":"))
    
    
    
    import json
    with open(user) as f:
        data = f.read()
        js = json.loads(data)
        conf=js.get(user) 
                        
        if conf == passw:
            
            import json
            with open(user) as f:
                data = f.read()
                js = json.loads(data)
                security_conf = js.get("sec.key")
                print(security_conf)
                
                
                if sec_key == security_conf:
                
                    f.close()
                    import os
                    
                    try:
                        os.remove(user)
                        
                    except OSError as e: 
                        print("Error: %s - %s." % (e.filename, e.strerror))
            
            
                else:
                    print("----------------------")
                    print("Incorrect Security Key")
                    print("----------------------")    
            
        else:
            print(" ")
            print("Incorrect Password")



#creats a new profile#
def new_userfile():
    
    a=input("Username(Enter your name and 6 digit number in <first name> <last name> <xxxxxx> format):")
    c=input("Email ID:")
    b=input("Password:")
    
    import os.path
    d=a.replace(" ", "")
    file_exists = os.path.exists(d)
    if file_exists == True:
        print("-------------------")
        print("File already exists")
        print("-------------------")
        
        print(" ")
        print("If this account is yours, please enter the security key to get access")
        sec_key = input(": ")
        
        import json
        with open(a) as f:
            data = f.read()
            js = json.loads(data)
            passw = js.get(a)
            security_conf = js.get("sec.key")
        
        if sec_key == security_conf:
            print("The password of your account is: ", passw)
        
    else:    
        from random import randint
        
        def random_with_N_digits(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randint(range_start, range_end)
        
        securitykey = random_with_N_digits(10)
        
        print("This is your security key, which you will need in case you forget your password or user ID: ", securitykey)
        
        #copies the password generated to the users clipboard    
        import pyperclip
        pyperclip.copy(securitykey)
            
        print("copied to you clipboard")
        
    
        import json  
        details ={a:b, "email":c, "sec.key":securitykey}     
        with open(a, 'a+') as convert_file:
            convert_file.write(json.dumps(details))
            
            print(" ")
            print("******************************************************************************")
            print("*******Do not share this password with anyone under any cirmcumstances********")
            print("******************************************************************************")
        

 
       
#Adds a new password#
def appendNew():
    
    userName = input("Please enter the username: ")
    password = input("Please enter the password here: ")
    email = input("Please enter your email address here: ")
    website = input("Please enter the website address here: ")

    
    from csv import writer
    List = [userName,email,password,website]

    with open('passwords.csv', 'a', newline='') as f_object:

        writer_object = writer(f_object, lineterminator='\r')
        writer_object.writerow(List)
        f_object.close()
 
    
 
    

#deletes a existing record from the file
def delete_record():
    
    import csv
    updatedlist=[]
    with open("passwords.csv",'r') as f:
      reader=csv.reader(f)
      username=input("Enter the username of the record you wish to remove from file:")     
      for row in reader:
                if row[0] != username:
                    updatedlist.append(row) 
                    updatefile(updatedlist)
                     
        
  
    
def updatefile(updatedlist):
    
    from csv import writer
    with open("passwords.csv", 'w', newline='') as f:
        Writer= writer(f, lineterminator='\r')
        Writer.writerows(updatedlist)
        print("File has been updated")  
 
    

    
#searches for the email and returns all the passwords registered with it#    
def find_email():
    
    import csv
    email=input("Enter your Email address: ")
    header = ["User ID", "Email ID", "Password", "Website"]
    with open('passwords.csv') as csv_file:
        csv_read = csv.reader(csv_file)
        print(" ")
        print(header)
        print(" ")
        for row in csv_read:
    
            if email in row:

                print(row)
 
#searches for a partiular password through the username#
def app_pass():
    
    import csv
    app=input("Enter the user ID: ")
    header = ["User ID", "Email ID", "Password", "Website"]
    with open('passwords.csv') as csv_file:
        csv_read = csv.reader(csv_file)
        print(" ")
        print(header)
        print(" ")
        for row in csv_read:
    
            if app in row:

                print(row)

                          

 
#####################################################CODE####################################################################################################     




while True:     

    print("-"*30)
    print("-"*12 +"WELCOME TO PASSWARDEN"+"-"*12)
    print("Do you wish to create a new account or login with the existing one? ")
    print("Enter 1 to sign up or 2 to login into your existing account or 3 if you don't remember your password")
    ans=input(':')
    
    
    #SIGN UP
    if ans == "1":

        
        a=input("Username (Enter your name and a 6 digit number in <first name> <last name> <xxxxxx> format):")
        c=input("Email ID:")
        b=input("Password:")
        
        

        #checks if an account is already present and give the user its  password after verification through its security key
        import os.path

        file_exists = os.path.exists(a)
        if file_exists == True:
            print("The account already exists")
            
            print("Enter your choice to authorise this process (email/securitykey)")
            ans = input("")
            if ans == "email":
                email = input("Enter your Email ID in order to retrieve your password: ")
                with open(a) as f:
                    data = f.read()
                    js = json.loads(data)
                    passw = js.get(a)
                    conf=js.get("email")
                    
                if conf == email:
                    import os
                                        
                    digits="0123456789"
                    OTP=""
                    for i in range(6):
                        OTP+=digits[math.floor(random.random()*10)]
                    otp = OTP + " is your OTP"
                    msg= otp
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login("___________________@gmail.com", "_____________") #Enter the email you want to send mails with and type in the app password 
        
                    s.sendmail('&&&&&&&&&&&',email,msg)
                    
                    otp = input("Enter Your OTP >>: ")
                    if otp == OTP:
                        print("Verified")
                        
                    
                        from tkinter import *  
                        from PIL import ImageTk,Image  
                        root = Tk()  
                        canvas = Canvas(root, width = 300, height = 200)  
                        canvas.pack()  
                        img = ImageTk.PhotoImage(Image.open("CAPTCHA.png"))  
                        canvas.create_image(20, 40, anchor=NW, image=img) 
                        root.mainloop()
                        
                        b = input("Enter the captcha code: ")
                        if b == "PassWarden":
                            print("The password of your account is: ", passw)
                            
                            print("To create a new password, Press 0")
                            new=input(":  ")
                            if new == "0":
                                
                                oldpass = input("Enter the old password: ")
                                if oldpass == oldpass_conf:
                                    
                                    newpass = input("Enter new password: ")
                                    newpassc = input("confirm new password: ")
                                    if newpass == newpassc and newpass != oldpass_conf:
                                        
                                        import json  
                                        details ={user:newpass, "email":email}     
                                        with open(user,'w') as convert_file:
                                            convert_file.write(json.dumps(details))
                                                
                                    else:
                                        print("----------------------------------------------------------")
                                        print("-------------Error: Passwords do no match-----------------")
                                        print("------or the new password is same as the old password-----")
                                        print("----------------------------------------------------------")
                                        
                                else:
                                    print(" ---------------- ")
                                    print("Incorrect Password")
                                    print(" ---------------- ")                               
                                        
                            else:
                                print(" ------- ")
                                print("Thank you")
                                print(" ------- ")
                                
                        else:
                            print(" ----------------------------- ")
                            print("access denied, incorrect captcha")
                            print(" ------------------------------ ")
                                
                else:
                    print("Failed request: Incorrect EmailID")
            
                  
            
            elif ans == "securitykey": 
                
                print("Enter your security key")
                sec_key = input(": ")
                import json
                with open(a) as f:
                    data = f.read()
                    js = json.loads(data)
                    passw = js.get(a)
                    security_conf = js.get("sec.key")
                
                if sec_key == security_conf:
                    print("The password of your account is: ", passw)
            
                else:
                    print("----------------------")
                    print("Incorrect Security Key")
                    print("----------------------") 
                    
             
                    
        else:
                        
            digits="0123456789"
            OTP=""
            for i in range(6):
                OTP+=digits[math.floor(random.random()*10)]
            otp = OTP + " is your OTP for verification of your email ID"
            msg= otp
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("_________________@gmail.com", "_________________") #Enter the email you want to send mails with and type in the app password 
            emailid = input("Confirm your email: ")
            s.sendmail('&&&&&&&&&&&',emailid,msg)
            otp = input("Enter Your OTP >>: ")

            if otp == OTP:
                print("Verified")
            
            
                from random import randint
                
                def random_with_N_digits(n):
                    range_start = 10**(n-1)
                    range_end = (10**n)-1
                    return randint(range_start, range_end)
                
                print("This is your security key, which you will need in case you forget your password or user ID: ", random_with_N_digits(10))
                
                securitykey = random_with_N_digits(10)
            
                import json  
                details ={a:b, "email":c, "sec.key":securitykey}     
                with open(a, 'a+') as convert_file:
                    convert_file.write(json.dumps(details))
                    
                    print(" ")
                    print("******************************************************************************")
                    print("*******Do not share this password with anyone under any cirmcumstances********")
                    print("******************************************************************************")
                
            else:
                print("Please Check your OTP again")

           
    #LOGIN
    elif ans=="2":
        
        user=input("Enter your username:")
        passw=input("Enter your password:")
        import json
        file_exists = os.path.exists(user)
        if file_exists == True:
            with open(user) as f:
                data = f.read()
                js = json.loads(data)
                conf=js.get(user)
                email=js.get("email")
                        
                if conf == passw:

                        #CAPTCHA to increase security 
                         from tkinter import * 
                         from PIL import ImageTk,Image  
                         root = Tk()  
                         canvas = Canvas(root, width = 300, height = 200)  
                         canvas.pack()  
                         img = ImageTk.PhotoImage(Image.open("CAPTCHA.png"))  
                         canvas.create_image(20, 40, anchor=NW, image=img) 
                         root.mainloop()
                        
                
                         b=input("Enter the captcha code: ")
                         if b=="PassWarden":
                             
                             
                             print(" ------------- ")
                             print("access granted")
                             print(" ------------- ")
                             
                            
                             #MENU
                             while True:    
                                    print('-'*50)
                                    print(('-'*23) + 'Menu'+ ('-' *23))
                                    print('1. Delete an existing account')
                                    print('2. Create new password record')
                                    print('3. Delete a existing record')
                                    print('4. Find all sites and apps connected to an email')
                                    print('5. Find a specific password of an app')
                                    print('6. Generate a new password')
                                    print('Q. Exit')
                                    choice=input(': ')
                                    
                                    if choice == "1":
                                        deleteacc()
                                    
                                    if choice == "2":
                                        appendNew()
                                      
                                        
                                    elif choice == "3":
                                        delete_record()
                                           
                                        
                                    elif choice == "4":
                                        find_email()
                                        
                                        
                                    elif choice == "5":
                                        app_pass()
                                        
                                        
                                    elif choice == "6":
                                        create()
                                    
                                    elif choice == "Q" or "q":
                                        print("-"*20 +"THANK YOU" + "-"*20)
                                        break
                                        
                                    else:
                                        print("-"*20 +"Invalid Choice" + "-"*20)
                                        
                         
                         else:
                             
                             print(" ----------------------------- ")
                             print("access denied, incorrect captcha")
                             print(" ------------------------------ ")
                             
                             break           
                                           
                else:
                    print(" ------------------------------- ")                    
                    print("access denied, incorrect password")
                    print(" ------------------------------- ")
    
        else:
            print("No such file found, please enter the correct username")
    
    #forgot password    
    elif ans == "3":
        user = input("Enter your User ID, in order to retrieve your password: ")        
        
        import json
        with open(user) as f:
            data = f.read()
            js = json.loads(data)
            conf = js.get("email")
            oldpass_conf = js.get(user)
            security_conf = js.get("sec.key")
            
            print("Enter your choice to authorise this process (email/securitykey)")
            ans = input("")
            if ans == "email":
                email = input("Enter your Email ID in order to retrieve your password: ")
                if conf == email:

                        import os
                        import math
                        import random
                        import smtplib
                        
                        digits="0123456789"
                        OTP=""
                        for i in range(6):
                            OTP+=digits[math.floor(random.random()*10)]
                        otp = OTP + " is your OTP"
                        msg= otp
                        s = smtplib.SMTP('smtp.gmail.com', 587)
                        s.starttls()
                        s.login("_________________@gmail.com", "___________________") #Enter the email you want to send mails with and type in the app password 
            
                        s.sendmail('&&&&&&&&&&&',email,msg)
                        otp = input("Enter Your OTP >>: ")
                        if otp == OTP:
                            print("Verified")
                            from tkinter import *  
                            from PIL import ImageTk,Image  
                            root = Tk()  
                            canvas = Canvas(root, width = 300, height = 200)  
                            canvas.pack()  
                            img = ImageTk.PhotoImage(Image.open("CAPTCHA.png"))  
                            canvas.create_image(20, 40, anchor=NW, image=img) 
                            root.mainloop()
                            
                    
                            b=input("Enter the captcha code: ")
                            if b=="PassWarden":
                                
                                
                                print(" ------------- ")
                                print("access granted")
                                print(" ------------- ")
                            
                                print("Your password is: ", js.get(user))
                                
                                print("To create a new password, Press 0, or 1 to exit")
                                new=input(":  ")
                                if new == "0":
                                    
                                    oldpass = input("Enter the old password: ")
                                    if oldpass == oldpass_conf:
                                        
                                        newpass = input("Enter new password: ")
                                        newpassc = input("confirm new password: ")
                                        if newpass == newpassc and newpass != oldpass_conf:
                                            
                                            import json  
                                            details ={user:newpass, "email":email}     
                                            with open(user,'w') as convert_file:
                                                convert_file.write(json.dumps(details))
                                                    
                                        else:
                                            print("----------------------------------------------------------")
                                            print("-------------Error: Passwords do no match-----------------")
                                            print("------or the new password is same as the old password-----")
                                            print("----------------------------------------------------------")
                                            
                                    else:
                                        print(" ---------------- ")
                                        print("Incorrect Password")
                                        print(" ---------------- ") 
                                
                                elif new == "1":
                                        break
                                
                                else:
                                    print(" ------------ ")
                                    print("Invalid Choice")
                                    print(" ------------ ")
    
                            else:
                                print("-----------------")
                                print("incorrect captcha")
                                print("-----------------")
    
    
                        else:
                            print("If you don't have access to this email right now, you can retrieve your account using your security key")
                            anss = input("do you want to continue? (y/n)")
                            if anss == "y":
                                securitykey = input("Enter your 10 digit security key to authorise: ")
                                if securitykey == security_conf:
                                        
                                    from tkinter import *  
                                    from PIL import ImageTk,Image  
                                    root = Tk()  
                                    canvas = Canvas(root, width = 300, height = 200)  
                                    canvas.pack()  
                                    img = ImageTk.PhotoImage(Image.open("CAPTCHA.png"))  
                                    canvas.create_image(20, 40, anchor=NW, image=img) 
                                    root.mainloop()
                                    
                            
                                    b=input("Enter the captcha code: ")
                                    if b=="PassWarden":
                                        
                                        
                                        print(" ------------- ")
                                        print("access granted")
                                        print(" ------------- ")
                                    
                                        print("Your password is: ", js.get(user))
                                        
                                        print("To create a new password, Press 0")
                                        new=input(":  ")
                                        if new == "0":
                                            
                                            oldpass = input("Enter the old password: ")
                                            if oldpass == oldpass_conf:
                                                
                                                newpass = input("Enter new password: ")
                                                newpassc = input("confirm new password: ")
                                                if newpass == newpassc and newpass != oldpass_conf:
                                                    
                                                    import json  
                                                    details ={user:newpass, "email":email}     
                                                    with open(user,'w') as convert_file:
                                                        convert_file.write(json.dumps(details))
                                                            
                                                else:
                                                    print("----------------------------------------------------------")
                                                    print("-------------Error: Passwords do no match-----------------")
                                                    print("------or the new password is same as the old password-----")
                                                    print("----------------------------------------------------------")
                                                    
                                            else:
                                                print(" ---------------- ")
                                                print("Incorrect Password")
                                                print(" ---------------- ")                               
                                                    
                                        else:
                                            print(" ------- ")
                                            print("Thank you")
                                            print(" ------- ")
                                    
                                    else:
                                            print("-----------------")
                                            print("incorrect captcha")
                                            print("-----------------")
                                else:
                                    print("----------------------")
                                    print("Incorrect Security Key")
                                    print("----------------------")
    
                            elif anss == "n":
                                print("oops, try again")
    
                            else:
                                print("Incorrect choice")    
                        
                else:
                    print("------------------")
                    print("Incorrect Email ID")
                    print("------------------")                    
            
            elif ans == "securitykey": 
                if securitykey == security_conf:
                                    
                    from tkinter import *  
                    from PIL import ImageTk,Image  
                    root = Tk()  
                    canvas = Canvas(root, width = 300, height = 200)  
                    canvas.pack()  
                    img = ImageTk.PhotoImage(Image.open("CAPTCHA.png"))  
                    canvas.create_image(20, 40, anchor=NW, image=img) 
                    root.mainloop()
                    
            
                    b=input("Enter the captcha code: ")
                    if b=="PassWarden":
                        
                        
                        print(" ------------- ")
                        print("access granted")
                        print(" ------------- ")
                    
                        print("Your password is: ", js.get(user))
                        
                        print("To create a new password, Press 0")
                        new=input(":  ")
                        if new == "0":
                            
                            oldpass = input("Enter the old password: ")
                            if oldpass == oldpass_conf:
                                
                                newpass = input("Enter new password: ")
                                newpassc = input("confirm new password: ")
                                if newpass == newpassc and newpass != oldpass_conf:
                                    
                                    import json  
                                    details ={user:newpass, "email":email}     
                                    with open(user,'w') as convert_file:
                                        convert_file.write(json.dumps(details))
                                            
                                else:
                                    print("----------------------------------------------------------")
                                    print("-------------Error: Passwords do no match-----------------")
                                    print("------or the new password is same as the old password-----")
                                    print("----------------------------------------------------------")
                                    
                            else:
                                print(" ---------------- ")
                                print("Incorrect Password")
                                print(" ---------------- ")                               
                                    
                        else:
                            print(" ------- ")
                            print("Thank you")
                            print(" ------- ")
                    
                    else:
                            print("-----------------")
                            print("incorrect captcha")
                            print("-----------------")
                else:
                    print("----------------------")
                    print("Incorrect Security Key")
                    print("----------------------")             

            else:
                print("----------------------")
                print("____Invalid Choice____")
                print("----------------------")  

    else:
            print(" -------------------------------------------------------------------------- ")
            print("____________________________Thank you_______________________________________")
            print(" -------------------------------------------------------------------------- ")
        
   
    
                 
                    
    




