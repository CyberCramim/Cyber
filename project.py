import glob as fileList
import os
import arc4

key = "ourkey1"
content = ""

def get_files():
    newlst = []
    files_list = fileList.glob("files\\*.txt")

    for file_name in files_list:
        file_name = file_name.replace("files\\", "")
        file_name = file_name.replace(".txt", "")
        newlst.append(file_name)
    return newlst


def does_exist():
    exists = get_files().__contains__(input("which file do you want to check?"))
    return exists


def write_file():
    file_name = input("enter file name: ")
    content = input("enter file content: ")

    with open(f'files\\{file_name}.txt', 'w') as f:
        f.write(content)


def read_file():
    file_name = input("the file you want to read:")

    with open(f'files\\{file_name}.txt', 'r') as f:
        content = f.read()
    return content


def menu():
    global content
    choice = 0
    print("welcome, what do you want to do?\n"
          "1 - Get files list\n"
          "2 - Check if a file exists\n"
          "3 - Write a new file\n"
          "4 - Reads the file\n"
          "5 - Decrypts a file\n"
          "6 - Exit")

    while choice != "7":
        choice = input("your choice is:")
        if choice == "1":
            print(get_files())

        if choice == "2":
            print(does_exist())

        if choice == "3":
            write_file()

        if choice == "4":
            print(read_file())

        if choice == "5":
            print(decrypt_content())



def signup():
    if not fileList.glob("login").__contains__("login"):
        os.mkdir(os.path.join("", "login"))
        os.mkdir(os.path.join("", "files"))
    with open("files\\file.txt", "a") as a:
        with open("login\\login.txt", "a") as w:
            with open("login\\login.txt", "r") as r:
                if r.read() == "":
                    w.write(input("what do you want to be your password?:"))


def login(password):
    with open("login\\login.txt", "r") as f:
        if password == f.read():
            menu()
        else:
            login(input("your password:"))

def encrypt_content():
    for file in get_files():
        with open(f"files\\{file}.txt", "r") as f:
            content = f.read()
            encryptor = arc4.ARC4(key)
            cipher = encryptor.encrypt(content)

            with open(f"files\\{file}.txt", "w") as w:
                w.write(str(cipher))
        return cipher


def decrypt_content():
    decryptor = arc4.ARC4(key)
    decrypted = decryptor.decrypt(encrypt_content())
    return decrypted


encrypt_content()

signup()
login(input('password: '))