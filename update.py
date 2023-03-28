import connect as con
import inquirer
from read import read_movie, read_user
from create import test_alpha, test_user_type, test_plan


def choose_update():
    opt_table = [
        inquirer.List('opt',
                      message='---UPDATE---',
                      choices=['Update User', 'Update Movie'])
    ]
    choice_table = inquirer.prompt(opt_table)

    if choice_table['opt'] == 'Update User':
        update_user()
    else:
        update_movie()


def get_value_input():
    new_value = input('New value: ')
    test_alpha(new_value)
    id_table = int(input('ID User: '))
    return new_value, id_table


def update_user():
    read_user()
    opt_element = [
            inquirer.List('opt',
                          message='What do you want to update?: ',
                          choices=['Name', 'E-mail',
                                   'Age', 'Type', 'Plan']
                          )
    ]
    choice_element = inquirer.prompt(opt_element)
    while True:
        try:
            new_value, id_user = get_value_input()

            table = 'user'
            element = ''
            if choice_element['opt'] == 'Name':
                element = 'nameUser'
            elif choice_element['opt'] == 'E-mail':
                element = 'emailUser'
            elif choice_element['opt'] == 'Age':
                element = 'ageUser'
                int(new_value)
            elif choice_element['opt'] == 'Type':
                element = 'typeUser'
                test_user_type(new_value)
            elif choice_element['opt'] == 'Plan':
                element = 'planUser'
                test_plan(new_value)

            break
        except ValueError:
            print("Invalid input...")

    update(table, element, new_value, id_user)
    read_user()


def update_movie():
    read_movie()
    opt_element = [
            inquirer.List('opt',
                          message="What do you want to update?: ",
                          choices=['Name', 'Age group',
                                   'Category', 'Plan']
                          )
        ]
    choice_element = inquirer.prompt(opt_element)

    while True:
        try:
            new_value, id_movie = get_value_input()

            table = 'movie'
            element = ''
            if choice_element['opt'] == 'Name':
                element = 'nameMovie'
            elif choice_element['opt'] == 'Age group':
                element = 'ageGroup'
                int(new_value)
            elif choice_element['opt'] == 'Category':
                element = 'category'
            elif choice_element['opt'] == 'Plan':
                element = 'planMovie'
                test_plan(new_value)

            break
        except ValueError:
            print("Invalid input...")

    update(table, element, new_value, id_movie)
    read_movie()


def update(table, element, value, id_elem):
    sql = f"UPDATE {table} SET {element} = '{value}' WHERE id = {id_elem}"
    con.cursor.execute(sql)
    con.db.commit()
