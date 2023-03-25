import connect as con


def register_user(name, email, age, usertype, plan):
    sql = f"INSERT INTO user (nameUser, emailUser, ageUser, typeUser, planUser) " \
          f"VALUES ('{name}','{email}','{age}','{usertype}','{plan}')"
    con.cursor.execute(sql)
    con.db.commit()


def register_movie(name, age, category, plan):
    sql = f"INSERT INTO movie (nameMovie, ageGroup, category, planMovie) " \
          f"VALUES ('{name}','{age}','{category}','{plan}')"
    con.cursor.execute(sql)
    con.db.commit()


# register_user('Raphael', 'rap@', 18, 'adm', 'basic')
# register_movie('Die Hard', 16, 'action', 'basic')

con.cursor.execute('SELECT * from movie')
for i in con.cursor:
    print(i)
