import sqlite3

def commit_close(func):
    def decorator(*args):
        data = sqlite3.connect('database.db')
        cursor = data.cursor()
        sql = func(*args) 
        cursor.execute(sql)    
        data.commit()
        data.close()
    return decorator


def db_create_table(name_database, name_table):
    data = sqlite3.connect('{}.db'.format(name_database))
    cursor = data.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS {} ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'desc_long TEXT' 
            ')'.format(name_table))    
    data.commit()
    data.close()

@commit_close
def db_insert(table_name, field, value):
    return """
        INSERT INTO {} ({})
        VALUES('{}')   
    """.format(table_name, field, value)

@commit_close
def db_update(name_table, field, value, idnum):
    return """
        UPDATE {} 
        SET {} = '{}' 
        WHERE id = '{}'
    """.format(name_table, field, value, idnum)

@commit_close
def db_delete(idnum):
    return """
        DELETE FROM true_table 
        WHERE id='{}'
    """.format(idnum)

def db_select_all(name_database, name_table):
    data = sqlite3.connect('{}.db'.format(name_database))
    cursor = data.cursor()
    sql = """
            SELECT * FROM {}
        """.format(name_table)
    cursor.execute(sql)    
    result = cursor.fetchall()
    data.commit()
    data.close()
    return result