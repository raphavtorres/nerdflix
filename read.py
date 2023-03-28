import connect as con
import prettytable


def table(table_bd, list_columns):
    con.cursor.execute(f'SELECT * from {table_bd}')
    table_view = prettytable.PrettyTable()
    table_view.field_names = list_columns
    for line in con.cursor:
        table_view.padding_width = 1
        table_view.add_row(line)
    print(table_view)


def read_user():
    table_bd = 'user'
    list_columns = ["ID", "NAME", "E-MAIL", "AGE", "TYPE", "PLAN"]
    table(table_bd, list_columns)


def read_movie():
    table_bd = 'movie'
    list_columns = ["ID", "NAME", "AGE GROUP", "CATEGORY", "PLAN"]
    table(table_bd, list_columns)
