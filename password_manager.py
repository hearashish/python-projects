from cryptography.fernet import Fernet

def load_key():
    f = open('key.key','rb')
    key = f.read()
    f.close()
    return key

'''def write_key():
    with open('key.key','wb') as f:
        key = Fernet.generate_key()
        f.write(key)'''

fobj = Fernet(load_key())

def add():
    username = input("Enter username : ")
    user_pass = input("Enter password : ")

    with open('passwords.txt','a') as f:
        f.write(username+'|'+ fobj.encrypt(user_pass.encode()).decode()+"\n")

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            uname, upass = line.split("|")
            print('Username : ',uname, '| Password : ', fobj.decrypt(upass.encode()).decode().rstrip())

master_pass = input("What is the Master Password : ")

while True:
    user_input = input("Select add or view to add or view password or type Q to quit: ").lower()
    if user_input == "q":
        break
    elif user_input == 'add':
        add()
    elif user_input == 'view':
        view()
    else:
        print("Wrong input")