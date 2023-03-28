import connect as con
import inquirer
from read import read_movie, read_user


def delete_user():
    ...


def delete_movie():
    ...


def delete_choice():
    opt_table = [
        inquirer.List('opt',
                      message='---DELETE---',
                      choices=['Delete User', 'Delete Movie'])
    ]
    choice_table = inquirer.prompt(opt_table)

    if choice_table['opt'] == 'Delete User':
        delete_user()
    else:
        delete_movie()


def delete():
    sql = "DELETE FROM name WHERE id = 1"
    con.cursor.execute(sql)
    con.db.commit()
