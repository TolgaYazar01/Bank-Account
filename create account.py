import hashlib
import os.path

salts = []

def get_salt():
    file = open("salts.txt", "r")
    for line in file:
        salts.append(line)

def salt_password(password):
    indexA = ord('a')
    password = password.lower()
    last_letter = password[-1]
    if not last_letter.isalnum():
        index = 0
    elif last_letter.isnumeric():
        index = int(last_letter)
    else:
        indexL = ord(last_letter)
        index = indexL - indexA
    salt = salts[index]
    return salt
    
def read_file():
    if not os.path.isfile("accounts.txt"):
        return
    f = open("accounts.txt", "r")
    for line in f:
        print(line)
        words = line.split(" ")
        words.pop()
        f = open("accounts.txt", "r")
        words = line.split(" ")
        words.pop()
        #code to .update() your dictionary using
        #words[0], words[1]
        username = words[0]
        password = words[1]
        PIN = words[2]
        balance = int(words[3])
        accounts.update({words[0] : [password, PIN, 0]})
    f.close()
    
def write_file():
    f = open("accounts.txt", "w")
    for item in accounts:
            f.write(username + " ")
            info = accounts[username]
            for item in info:
                f.write(str(item) + " ")
            f.write("\n")
    f.close()

def hasher(password):
    b = bytes(password, 'utf-8')
    m = hashlib.sha256(b)
    m = m.hexdigest()
    return m

accounts = {}

def login ():
    print("Logging in")
    username = input("Please enter your username: ")
    if not accounts.get(username):
            print("Please enter a valid username")
            return
    password = input("Please enter your password")
    actual_password = accounts[username][0]
    for i in range (0, 6):
        if i == 5:
            print("locked out")
            break
        elif password == actual_password:
            print("Welcome, " + username + "!")
            opt = input("Press 'V' to view account or 'T' to transfer: ")
            balance = accounts[username][2]
            if opt == 'V':
                print(balance)
            elif opt == 'T':
                amt = input("How much would you like to transfer?: ")
                friend = input("Who would you like to transfer to?")
                if amt > balance:
                    print("You cannot transfer this much money from your account")
                continue
            opt =  input("Press 'W' to withdraw money or 'D' to deposit: ")
            if opt == 'W':
                amt = input("How much would you like to withdraw?")
                if amt > balance:
                    print("You cannot withdraw that much from your account")
                    continue
                else:
                    accounts[username][2] -= amt
            elif opt == 'D':
                amt = input("How much would you like to deposit?")
                accounts[username][2] += amt
            if message ==  'C':
                info = accounts[username]
                del accounts[username]
                username = input("Create a new username: ")
                password = input("Create a new password: ")
                accounts[username] = info
    else:
        print("Wrong password- try again")
        password = input("Please enter your password")
        
#write_salts()
get_salt()
salt_password("tac")
read_file()
message = input("Enter 'C' to create a new bank account, or press 'L' to login: ")

while message != 'Q':
    if message == 'C':
        username = input("Create a username: ")
        while accounts.get(username):
            username = input("Username taken- please pick a different username: ")
        password = input("Create a password: ")
        password = password + salt_password(password)
        password =  hasher(password)
        PIN = input("Please enter a PIN to secure your info: ")
        accounts.update({username : [password, PIN, 0]})      
    elif message == 'L':
        print("Logging in")
        username = input("Please enter your username: ")
        if not accounts.get(username):
            print("Please enter a valid username")
            continue
    else:
        print("Please enter a valid option: ")
    message = input("Enter 'C' to create a new bank account, or press 'L' to login: ")
