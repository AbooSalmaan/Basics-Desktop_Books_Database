import sqlite3

class Database:

    def __init__(self, DBName, TableName):
        self.TableName=TableName
        self.conn = sqlite3.connect(DBName)
        self.cur = self.conn.cursor()
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {TableName} (Id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
        self.conn.commit()

    def insert(self,Title, Author, Year, ISBN):
        self.cur.execute(f"INSERT INTO {self.TableName} VALUES(NULL, ?, ?, ?, ?)", (Title, Author, Year, ISBN))
        self.conn.commit()

    def view(self):
        self.cur.execute(f"SELECT * FROM {self.TableName}")
        record = self.cur.fetchall()
        return record

    def update(self,ID, Title, Author, Year,ISBN):
        self.cur.execute(f"UPDATE {self.TableName} SET Title=?, Author=?, Year=?, ISBN=? where ID=?", (Title, Author, Year, ISBN, ID))
        self.conn.commit()

    def search(self,Title="", Author="", Year="", ISBN=""):
        self.cur.execute(f"SELECT * FROM {self.TableName} WHERE Title=? OR Author=? OR Year=? OR ISBN=?", (Title, Author, Year, ISBN))
        found = self.cur.fetchall()
        return found

    def delete(self,id):
        self.cur.execute(f"DELETE FROM {self.TableName} WHERE ID=?",(id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
