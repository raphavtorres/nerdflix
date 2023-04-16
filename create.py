import connect as con


def test_alpha(value):
    value = value.replace(' ', '')
    if value.isalpha() is not True:
        raise ValueError


def test_user_type(value):
    if value != 'adm' and value != 'regular':
        raise ValueError


def test_plan(value):
    if value != 'basic' and value != 'medium' and value != 'premium':
        raise ValueError


def input_reg_user():
    print(" | Sign Up | ")
    while True:
        try:
            name = input("Name: ")
            test_alpha(name)
            email = input("E-mail: ")
            age = int(input("Age: "))
            usertype = input("User type (Adm | Regular): ").lower().strip()
            test_alpha(usertype)
            test_user_type(usertype)
            plan = input("Plan (Basic | Medium | Premium): ").lower().strip()
            test_alpha(plan)
            test_plan(plan)
            return name, email, age, usertype, plan
        except ValueError:
            print('Invalid value')
            continue


def input_reg_movie():
    print(" | REGISTER MOVIE | ")
    while True:
        try:
            name = input("Movie Name: ")
            test_alpha(name)
            age = int(input("Age Group: "))
            category = input("Category: ")
            test_alpha(category)
            plan = input("Plan: (Basic | Medium | Premium): ").lower().strip()
            if plan != 'basic' and plan != 'medium' and plan != 'premium':
                raise ValueError
            return name, age, category, plan
        except ValueError:
            print('Invalid value')
            continue


def register_user():
    name, email, age, usertype, plan = input_reg_user()
    sql = f"INSERT INTO user ( \
    nameUser, emailUser, ageUser, typeUser, planUser) \
    VALUES ('{name}','{email}','{age}','{usertype}','{plan}')"
    con.cursor.execute(sql)
    con.db.commit()


def register_user_window(name, email, age, usertype, plan):
    """
    Adds a new user in the database
    """
    sql = f"INSERT INTO user ( \
    nameUser, emailUser, ageUser, typeUser, planUser) \
    VALUES ('{name}','{email}','{age}','{usertype}','{plan}')"
    con.cursor.execute(sql)
    con.db.commit()


def register_movie():
    """
    Adds a new user in the database
    """
    name, age, category, plan = input_reg_movie()
    sql = f"INSERT INTO movie (nameMovie, ageGroup, category, planMovie) " \
          f"VALUES ('{name}','{age}','{category}','{plan}')"
    con.cursor.execute(sql)
    con.db.commit()
