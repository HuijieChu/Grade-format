import mysql.connector
class ConnectSql:
    def __init__(self,user,host):
        self.connect = mysql.connector.connect(user = user, host = host)
        self.project = None
        self.createCommand = ''
        self.tableName = ''
        self.insertCommand = ''
        self.insertArgs = []
        self.selectCommand = ''

    def createProject(self):
        cur = self.connect.cursor()
        cur.execute("drop database if exists " + self.project + ';')
        cur.execute("create database " + self.project + ";")

    def chooseProject(self):
        cur = self.connect.cursor()
        cur.execute("use " + self.project)

    def createTable(self):
        cur = self.connect.cursor()
        cur.execute("begin;")
        cur.execute("drop table if exists " + self.tableName + ';')
        cur.execute(self.createCommand)
        cur.execute("commit;")

    def insertData(self):
        cur = self.connect.cursor()
        cur.execute("begin;")
        cur.execute(self.insertCommand,self.insertArgs)
        cur.execute("commit;")

    def selectData(self):
        cur = self.connect.cursor()
        cur.execute("begin;")
        cur.execute(self.selectCommand)
        temp = cur.fetchall()
        cur.execute("commit;")
        return temp