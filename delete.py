import connect as con


def delete_user_window(id):
    sql = f"DELETE FROM user WHERE id = '{id}'"
    con.cursor.execute(sql)
    con.db.commit()
