from connectSQL import ConnectSql
class InsertData:
    def __init__(self,user,host):
        self.user = user
        self.host = host
        self.dataName = ''
        self.data = None
        self.dataClass = None
        self.TypeDict = {'name': "VARCHAR(255)", "teacher" : "VARCHAR(255)","id":'INT',"course_id": "INT",'test_id':"INT","student_id":"INT","weight":"INT","mark":"INT"}
        self.NewTable = ConnectSql(self.user,self.host)

    def createTable(self,project):
        self.NewTable.project = project
        self.NewTable.chooseProject()
        s = "CREATE TABLE" + ' ' + self.dataName + ' ('
        for item in self.dataClass:
            s = s + item + " " + self.TypeDict[item] + ','
        s = s[:-1] + ');'
        self.NewTable.tableName = self.dataName
        self.NewTable.createCommand = s
        self.NewTable.createTable()

    def insertData(self,project):
        self.NewTable.project = project
        self.NewTable.chooseProject()
        s = 'insert into ' + self.dataName + " values("
        for item in self.data:
            for it in item:
                s = s + '%s'+ ','
            break
        s = s[:-1] + ');'
        self.NewTable.insertCommand = s
        for item in self.data:
            self.NewTable.insertArgs = tuple(item)
            self.NewTable.insertData()







