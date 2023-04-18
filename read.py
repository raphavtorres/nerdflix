import connect as con


def read_user_window():
    con.cursor.execute('SELECT * from user')
    result = con.cursor.fetchall()
    return result


def search_user_window(id):
    con.cursor.execute(f"SELECT * from user WHERE id = '{id}'")
    result = con.cursor.fetchall()
    return result


def read_movie_window():
    con.cursor.execute('SELECT * from movie')
    result = con.cursor.fetchall()
    return result
