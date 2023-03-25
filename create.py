import connect as con


def input_reg_user():
    def test_alpha(value):
        if value.isalpha() is not True:
            raise ValueError
    while True:
        try:
            name = input("Name: ")
            test_alpha(name)
            email = input("E-mail: ")
            age = int(input("Age: "))
            usertype = input("User type (Adm | Regular): ").lower().strip()
            test_alpha(usertype)
            if usertype != 'adm' and usertype != 'regular':
                raise ValueError
            plan = input("Plan (Basic | Medium | Premium): ").lower().strip()
            test_alpha(plan)
            if plan != 'basic' and plan != 'medium' and plan != 'premium':
                raise ValueError
            return name, email, age, usertype, plan
        except ValueError:
            print('Invalid value')
            continue


def register_user():
    """
    Adds a new user in the database
    """
    name, email, age, usertype, plan = input_reg_user()
    sql = f"INSERT INTO user ( \
    nameUser, emailUser, ageUser, typeUser, planUser) \
    VALUES ('{name}','{email}','{age}','{usertype}','{plan}')"
    con.cursor.execute(sql)
    con.db.commit()


def register_movie(name, age, category, plan):
    """
    Adds a new user in the database
    """
    sql = f"INSERT INTO movie (nameMovie, ageGroup, category, planMovie) " \
          f"VALUES ('{name}','{age}','{category}','{plan}')"
    con.cursor.execute(sql)
    con.db.commit()


# register_user('Raphael', 'rap@', 18, 'adm', 'basic')
# register_movie('Die Hard', 16, 'action', 'basic')

register_user()
con.cursor.execute('SELECT * from user')
for i in con.cursor:
    print(i)
