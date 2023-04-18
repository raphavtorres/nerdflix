import connect as con


def update(table, element, value, id_elem):
    sql = f"UPDATE {table} SET {element} = '{value}' WHERE id = '{id_elem}'"
    con.cursor.execute(sql)
    con.db.commit()
