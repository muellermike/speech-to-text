import pymysql.cursors
import configparser

def execute(sql, params, statement):
    """
    Runs an sql command on the database and returns result if there is one.
    """
    config = configparser.ConfigParser()
    config.read("config.ini")

    db_config = config["DATABASE"]

    result = None

    conn = pymysql.connect(host = db_config.get("DB_URI"),
                            port = 3306,
                            user = db_config.get("DB_USER"),
                            password = db_config.get("DB_PW"),
                            db = db_config.get("DB_NAME"),
                            charset = "utf8mb4",
                            cursorclass = pymysql.cursors.DictCursor)

    try:
        with conn.cursor() as cursor:
            if statement == "SELECT":
                cursor.execute(sql, params)
                result = cursor.fetchall()
            elif statement == "INSERT MANY":
                cursor.executemany(sql, params)
                print(f"INSERT MANY done")
                conn.commit()
            else:
                cursor.execute(sql, params)
                result = conn.insert_id()
                print(f"result NOT SELECT: {result}")
                conn.commit()
    finally:
        conn.close()
    
    return result
