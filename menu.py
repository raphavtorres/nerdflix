import inquirer


def menu():
    """
    Shows a menu to the user
    :return:
    """
    opt_menu = [
        inquirer.List('opt',
                      message=f'---MENU---',
                      choices=['Sign in', 'Sign Up', 'Register Movie', 'List Movies', 'Exit']
                      )
    ]
    choice = inquirer.prompt(opt_menu)
    return choice['opt']

menu()
