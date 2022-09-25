
#!/usr/bin/python3
print("content-type: text/html")
print()

import os 
import getpass

os.system("tput setaf 1")
print("\t\tHello this is TUI project which will makes ur life simple")

os.system("tput setaf 7")
print("\t\t---------------------------------------------------------")

passwd = getpass.getpass("Enter ur password : ")
apass = "shruti"
if passwd != apass:
    print("authentication failure")
    exit()
    
while True:
    print("""
    Press 1  : To check connectivity
    Press 2  : To check date and time
    Press 3  : To check calander
    Press 4  : To long list all files and directories of current directory 
    Press 5  : To create file
    Press 6  : To remove file
    Press 7  : To create directory
    press 8  : To remove directory
    Press 9  : To copy files or directory
    Press 10  : To move files or directory
    Press 11 : To create user
    Press 12 : To delete user
    Press 13 : To download anything form google
    Press 14 : To configure web server
    Press 15 : To exit
    """)   

    print("enter ur choice : ",end="")
    ch=input()
    print(ch)
    if int(ch) == 1:
        os.system("ansible ansible_clients -m ping")
    elif int(ch) == 2:
        os.system("ansible ansible_clients -m command -a'date'")
    elif int(ch) == 3:
        os.system("ansible ansible_clients -m command -a'cal'")
    elif int(ch) == 4:
        os.system("ansible ansible_clients -m command -a'ls -l'")
    elif int(ch) == 5:
        os.system("ansible-playbook create_file.yml")
    elif int(ch) == 6:
        os.system("ansible-playbook remove_file.yml")
    elif int(ch) == 7:
        os.system("ansible-playbook create_dir.yml")
    elif int(ch) == 8:
        os.system("ansible-playbook remove_dir.yml")
    elif int(ch) == 9:
        os.system("ansible-playbook copy_file.yml")
    elif int(ch) == 10:
        os.system("ansible-playbook move_file.yml")
    elif int(ch) == 11:
        os.system("ansible-playbook create_user.yml")
    elif int(ch) == 12:
        os.system("ansible-playbook remove_user.yml")
    elif int(ch) == 13:
        os.system("ansible-playbook download.yml")
    elif int(ch) == 14:
        os.system("ansible-playbook configure_webserver.yml")
    elif int(ch) == 15:
        exit()
    else:
        print("Does not support")
