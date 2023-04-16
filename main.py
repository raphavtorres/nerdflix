from menu import menu
from create import register_user, register_movie
from read import read_movie, read_user
from login import login, adm_warning
from update import choose_update
from delete import delete_choice

user_type = ''
while True:
    choice = menu()
    if choice == 'Sign in':
        user_type = login()
    elif choice == 'Sign Up':
        register_user()
    elif choice == 'Register Movie':
        adm_warning(user_type, register_movie)
    elif choice == 'List Movies':
        read_movie()
    elif choice == 'List Users':
        adm_warning(user_type, read_user)
    elif choice == 'Update':
        adm_warning(user_type, choose_update)
    elif choice == 'Delete':
        adm_warning(user_type, delete_choice)
    else:
        break
