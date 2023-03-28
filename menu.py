import inquirer


def menu():
    """
    Shows a menu to the user
    :return:
    """
    opt_menu = [
        inquirer.List('opt',
                      message='---MENU---',
                      choices=['Sign in', 'Sign Up', 'Register Movie',
                               'List Movies', 'List Users', 'Update', 'Delete', 'Exit']
                      )
    ]
    choice = inquirer.prompt(opt_menu)
    return choice['opt']
