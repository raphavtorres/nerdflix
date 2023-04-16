import connect as con
import inquirer
from read import read_movie, read_user


def delete_user():
    while True:
        try:
            userID = int(input('User ID to be deleted: '))
            break
        except TypeError:
            continue


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


def delete(id):
    sql = f"DELETE FROM name WHERE id = {id}"
    con.cursor.execute(sql)
    con.db.commit()
