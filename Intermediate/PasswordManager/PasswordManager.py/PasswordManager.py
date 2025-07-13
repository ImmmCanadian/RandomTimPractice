from cryptography.fernet import Fernet

def keyLoad():
    key = input("Please enter the key to access. ")
    with open("key.txt","r") as f:
        if key != f.read():
            print("Wrong key!")
        else:
            print("Logging in.")
    return key
    
x = keyLoad()       
f = Fernet(x)

def view(f):
    print("Here is a list of all of your current user names and passwords!")
    with open("passwords.txt","r") as f:
        for i in f.readlines():
            decrypted=f.decrypt(i)
            data=decrypted.rsplit()
            username,password = data.split(" ")
            print("Username: "+username+" and password: "+password+".")

def add(f):
    username = input("Please enter the username of the account: ")
    password = input("Please enter the password of the account: ")
    save = f.encrypt(username+" "+password+"\n")
    with open("passwords.txt","a") as f:
        f.write(save)
        
while True:

    mode = input("Would you like to enter a new password (new), view current passwords (view) or quit (q)? ").lower().strip()

    if mode == "new":
        add(f)
    elif mode =="view":
        view(f)
    elif mode == "q":
        break
