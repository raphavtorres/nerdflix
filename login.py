import connect as con


def login():
    while True:
        try:
            email_input = input("Enter your e-mail: ")
            break
        except ValueError:
            print("Invalid e-mail...")
    sql = f"SELECT nameUser, typeUser FROM user WHERE emailUser = '{email_input}'"
    con.cursor.execute(sql)
    response = ''
    for i in con.cursor:
        response = i
     
    if response != '':
        print(f"Hello, {i[0]}! | type: ({i[1]})")
    else:    
        print("No user found with this e-mail adress...")

    return response[1]


def adm_warning(response, function):
    if response == 'adm':
        function()
    else:
        print("Access restricted to administrators!")
