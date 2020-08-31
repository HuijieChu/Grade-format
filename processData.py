from insertData import InsertData
from readData import ReadData
from connectSQL import ConnectSql

class ProcessData:

    def __init__(self,user,host):
        self.primaryKey = {"students":'id','courses': 'id', 'tests': "course_id","marks":"student_id",'StudentMark':"marks_test_id",'CourseTest':"tests_id"}
        self.user = user
        self.host = host

    def insert(self,fileRoot,project,file,arg):
        Read = ReadData(fileRoot + arg)
        DataClass, Data = Read.readCsvInput()
        Insert = InsertData(self.user, self.host)
        Insert.dataName = arg[:file]
        Insert.dataClass = DataClass
        Insert.data = Data
        Insert.createTable(project)
        Insert.insertData(project)
        return arg,DataClass

    def checkValid(self,tableName,selectLine,weightLine,project,groupName):
        s = 'select ' + selectLine +' from ' + tableName + ' group by '+groupName+' having ' + selectLine +' > ' + weightLine + ' or ' + selectLine + ' < ' + weightLine + ';'
        NewTable = ConnectSql(self.user, self.host)
        NewTable.project = project
        NewTable.selectCommand = s
        NewTable.chooseProject()
        return NewTable.selectData()

    def mergeData(self,preTable1,preTable2,mergeTableName,dataClassDict,project):
        mergeClass = []
        s = "create table "+ mergeTableName + " as select "
        for item in dataClassDict[preTable1]:
            s = s + preTable1+'.'+item+ " as "+preTable1+'_'+item+','
            mergeClass.append(preTable1+'_'+item)
        for item in dataClassDict[preTable2]:
            s = s + preTable2+'.'+item+" as "+preTable2+'_'+item+','
            mergeClass.append(preTable2 + '_' + item)
        s = s[:-1]
        s = s + ' from ' + preTable1 + ' inner join ' + preTable2 + ' on ' + preTable1+'.'+self.primaryKey[preTable1] + ' = ' + preTable2+'.'+self.primaryKey[preTable2]
        NewTable = ConnectSql(self.user,self.host)
        NewTable.project = project
        NewTable.tableName = mergeTableName
        NewTable.createCommand = s
        NewTable.chooseProject()
        NewTable.createTable()
        return mergeClass

    def processData(self,dataClass,sourceTable,calculateForm,groupClass,project,form):
        s = 'select '
        for i in range(len(dataClass)):
            s = s + dataClass[i] + ' as ' + form[i] + ','
        s = s + calculateForm + ' from ' + sourceTable + ' group by '
        for item in groupClass:
            s = s + item + ','
        s = s[:-1] + ';'
        NewTable = ConnectSql(self.user, self.host)
        NewTable.project = project
        NewTable.selectCommand = s
        NewTable.chooseProject()
        return NewTable.selectData()











