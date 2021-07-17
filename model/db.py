import sqlite3

def connect():
    # this will return a connection to the db
    conn = sqlite3.connect("main.db") # connection code
    cur = conn.cursor() 
    return conn, cur

def init_db():
    with open(r"./model/tables.sql", "r") as sql:
        conn, cur = connect()
        for query in sql.readlines():
            cur.execute(query) # execute the query
            # by doing this normal execute you cannot see the changes in the database
            # you have commit these to see the changes on the database
            conn.commit() # committing things
        conn.close() 


def check_user_email(email):
    try:
        conn, cur = connect()
        res = cur.execute("SELECT email FROM user WHERE email=?", (email,))
        data = res.fetchone()
        if data is None:
            return True
        return False
    except:
        return False
    finally:
        conn.close()

def register_user(data:tuple):
    try:
        conn, cur = connect()
        
        cur.execute(
            "INSERT INTO user(name,email,password, date_time) VALUES(?,?,?,?)",
            data
        )
        conn.commit()
        return True
    except:
        conn.rollback()
        return False
    finally:
        conn.close()