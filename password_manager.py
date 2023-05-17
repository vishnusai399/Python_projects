master_password=input("what is the master password ")

def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split('|')
            print('user:',user,'password:',passw)


def add():
    name=input("Account Name: ")
    pwd=input("password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + '|' + pwd + '\n')


while True:
    mode=input("would you like to add a new password or view existing ones (view,add), q to exit? ").lower()
    if mode=='q':
        break
    if mode=="add":
        add()
    elif mode=="view":
        view()
    else:
        print("Invalid mode!")
        continue