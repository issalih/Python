import os
import subprocess

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add")
        print ("use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system ("sudo adduser " + username)

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input ("Enter the name of the user to remove: ")
        print ("Remove the user : '" + username + "'? (Y/N)")
        confirm = input().upper()
        os.system("sudo userdel -r " + username)

def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ")
    
    output = str(subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0])
    
    print("Enter a list of groups to add the user to")
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3")
    print(str(output))
    
    chosenGroups = input("Groups: ")
    
    output = output.split(" ")
    chosenGroups = chosenGroups.split(" ")
    
    print("Add To:")
    found = True
    groupString = ""
    
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print("- Existing Group : " + grp)
                groupString = groupString + grp + ","
        if found == False:
            print("- New Group : " + grp)
            groupString = groupString + grp + ","
        else:
            found = False
    
    groupString = groupString[:-1] + " "
    
    confirm = ""
    while confirm != "Y" and confirm != "N" :
        print("Add user '" + username + "' to these groups? (Y/N)")
        confirm = input().upper()
    
    if confirm == "N":
        print("User '" + username + "' not added")
    elif confirm == "Y":
        os.system("sudo usermod -aG " + groupString + username)
        print("User '" + username + "' added")

new_user()
add_user_to_group()
remove_user()


