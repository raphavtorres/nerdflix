import connect as con
import inquirer


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
    """ choice_element = inquirer.prompt(opt_element) """


def update_movie(id, info):
    opt_element = [
            inquirer.List('opt',
                          message="What do you want to update?: ",
                          choices=['Name', 'Age group',
                                   'Category', 'Plan']
                          )
        ]
    choice_element = inquirer.prompt(opt_element)

    update(element, info)


def update_user(id, info):
    opt_element = [
            inquirer.List('opt',
                          message='What do you want to update?: ',
                          choices=['Name', 'Email',
                                   'Age', 'Type', 'Plan']
                          )
        ]
    choice_element = inquirer.prompt(opt_element)
    if choice_element['opt'] == 'Name':
        element = 'nameUser'

    update(element, info)

    choice_table, choice_element = update()


def update(element, info):
    sql = f"UPDATE user SET {element} = '{info}' WHERE id = '{id}'"
    con.cursor.execute(sql)
    con.db.commit()


con.cursor.execute('SELECT * from user')
for i in con.cursor:
    print(i)
