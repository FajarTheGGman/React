# Copright© 2019 By Fajar Firdaus
# Please Don't Recode My Program Because I Take A long Time To Complete This Project :)
import requests as r 

class Editor:
    def banner():
        print(" ??    [React Text Editor]  ")
        print("[  ]          [By]       ")
        print(" []     [Fajar Firdaus]")
        print("\n\n[!] Report Error To My Social Media")


    def http():
        user = str(input("[Site] >_ "))
        send = r.get(user)
        f = open("result.txt")
        f.write(str(send.text))
        print("--------------------------")
        print("[Status] > " + send.status_code)
        print("[Encoding] > " + send.encoding)
        print("[Header] > " + send.headers)
        print("[Content] > result.txt")
        print("--------------------------")

    def edit():
        print("[!] Click Space button + enter to save the file")
        file = str(input("[?] File Name >_ "))
        file = open(file, "w+")
        while True:
            user = str(input("- "))
            file.write(user + "\n")
            if user == " ":
                break

def help():
    print("[Commands Help]")
    print("- http (http request)")
    print("- edit (text editor)")
    print("- help (see all commands)")
    print("- about (developer information)")

def about():
    print("{")
    print(" Coder : Fajar Firdaus")
    print(" FB : Fajar Firdaus")
    print(" IG : fajar_firdaus_7")
    print(" YT : iTech7732")
    print("}")

b = Editor.banner()
menu = str(input("\n\n[R] >_ "))
if menu == "edit":
    edit = Editor.edit()
elif menu == "http":
    http = Editor.http()
elif menu == "help":
    help()
elif menu == "exit":
    print("[+] Exit...")
    print("Bye.. :(")
elif menu == "about":
    about()
else:
    print("[!] Wrong Commands !\n")
    help()