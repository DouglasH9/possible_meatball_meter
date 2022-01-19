# a cursor is the object we use to interact with the database
import pymysql.cursors

# this class gives and instance of a connection to a database
class MySQLConnection:
    def __init__(self, db):
        # change the username and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root',
                                    password = 'FunkPanda86$@$$!',
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish connection to the database
        self.connection = connection
    
    # method that queries the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print('Running Query:', query)

                cursor.execute(query, data)
                if query.lower().find('insert') >= 0:
                    # insert queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find('select') >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result

                else:
                    # UPDATE and DELETE queries return nothing
                    self.connection.commit()

            except Exception as e:
                # if query fails, this method will return FALSE
                print('Something went wrong', e)
                return False

            finally:
                # closes connection
                self.connection.close()

# connectToMySQL receives the database we're using and uses it to create an instance of a MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)