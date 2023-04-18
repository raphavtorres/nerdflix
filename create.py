import connect as con


def register_user_window(name, email, age, usertype, plan):
    """
    Adds a new user in the database
    """
    sql = f"INSERT INTO user ( \
    nameUser, emailUser, ageUser, typeUser, planUser) \
    VALUES ('{name}','{email}','{age}','{usertype}','{plan}')"
    con.cursor.execute(sql)
    con.db.commit()


""" def register_movie():
    name, age, category, plan = input_reg_movie()
    sql = f"INSERT INTO movie (nameMovie, ageGroup, category, planMovie) " \
          f"VALUES ('{name}','{age}','{category}','{plan}')"
    con.cursor.execute(sql)
    con.db.commit() """
