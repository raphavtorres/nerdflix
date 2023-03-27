from menu import menu
from create import register_user, register_movie
"""
import update
import delete
import netflix
import read"""


while True:
    choice = menu()
    if choice == 'Sign in':
        ...
    elif choice == 'Sign Up':
        register_user()
    elif choice == 'Register Movie':
        register_movie()
    elif choice == 'List Movies':
        ...
    else:
        break
