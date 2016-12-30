import pymysql


class Database():
    def __init__(self):
        self.mysql_conn, self.mysql_cursor = self.connect_mysql()

    def connect_mysql(self):
        conn = pymysql.connect(read_default_file='connectors.cnf',
                               charset='utf8')
        cursor = conn.cursor()

        return (conn, cursor)

    def close_mysql(self):
        self.mysql_conn.close()
        self.mysql_collection.close()

    def query_from_mysql(self, sql):
        self.mysql_cursor.execute(sql)
        return self.mysql_cursor.fetchall()

    def insert_into_mysql(self, sql, param, isMany=False):
        try:
            if not isMany:
                self.mysql_cursor.execute(sql, param)
            else:
                self.mysql_cursor.executemany(sql, param)
            self.mysql_conn.commit()
        except Exception as e:
            print(e)
            self.mysql_conn.rollback()

    def update_mysql(self, sql):
        try:
            self.mysql_cursor.execute(sql)
            self.mysql_conn.commit()
        except Exception as e:
            print(e)
            self.mysql_conn.rollback()
