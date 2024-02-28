import oracledb

connection = None
cursor = None


def toConnect(user="admin", password="adminpw", dsn="localhost/ORCL"):
    global connection
    global cursor
    if connection is not None:
        print("Connection already exists.")
        return True
    try:
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        cursor = connection.cursor()
        print("Connection established")
        return True
    except oracledb.DatabaseError as error:
        print(f"Connection error: {error}")
        return False


def disconnect():
    global cursor
    global connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Disconnected successfully")


def execute_query(query, *args):
    global cursor
    global connection
    try:
        cursor.execute(query, args)
        connection.commit()  # Add this line to commit changes for INSERT, UPDATE, DELETE
        return True  # Indicate success
    except oracledb.DatabaseError as error:
        print(f"Query execution error: {error}")
        return False  # Indicate failure


def fetchall(query, *args):
    global cursor
    try:
        cursor.execute(query, args)
        return cursor.fetchall()
    except oracledb.DatabaseError as error:
        print(f"Query execution error: {error}")
        return None
