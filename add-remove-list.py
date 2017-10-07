userlist = ['bob']
user_input = ''

#menu function
def menu():
    print('''
=====================
|    Main Menu      |
|===================|
|   1.Add User      |
|   2.Remove User   |
|   3.List Users    |
=====================   
    ''')
    return input('choices(1-3)?: ')

def addingUser():
    global user_input
    user_input = input('please enter username: ')
    if user_input not in userlist:
        userlist.append(user_input)
        print('user',user_input,'is now added to the list')
    elif user_input in userlist:
        print(user_input,' is already on the list,')


def removingUser():
    global user_input
    user_input = input('please enter username to remove: ')
    if user_input in userlist:
        userlist.remove(user_input)
        print('user',user_input,'is now removed to the list')
    elif user_input in userlist:
        print(user_input,' was removed or not in list,')


def listUser():
    print('users are: ',userlist)

while True:
    choices = menu()
    if choices == '1':
        addingUser()
    elif choices == '2':
        removingUser()
    elif choices == '3':
        listUser()
    else:
        menu()