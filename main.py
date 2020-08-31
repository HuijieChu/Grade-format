import sys
from processData import ProcessData
from connectSQL import ConnectSql
import combineData

mysqlUser = 'root'
mysqlHost = '127.0.0.1'
fileRoot = 'Example1/'
projectName = 'Grades'
suffixFile = -4
dataClassDict = {}
selectItem = ["StudentMark_students_id","StudentMark_students_name","CourseTest_courses_id","CourseTest_courses_name","CourseTest_courses_teacher"]
deserveItem = ['student_id',"student_name","course_id","course_name","course_teacher"]
calculateForm = 'round(sum(StudentMark_marks_mark*(CourseTest_tests_weight+0.00)/100),1)'
groupClass = ["StudentMark_students_id","CourseTest_courses_id"]
courses = sys.argv[1]
students = sys.argv[2]
test = sys.argv[3]
marks = sys.argv[4]
mergeStudentMark = 'StudentMark'
mergeCourseTest = 'CourseTest'
mergeTotal = 'Total'

CreateProject = ConnectSql(mysqlUser,mysqlHost)
CreateProject.project = projectName
CreateProject.createProject()

def main():

    for i in range(1,len(sys.argv)-1):
        Insert = ProcessData(mysqlUser,mysqlHost)
        classType, dataClass = Insert.insert(fileRoot,projectName,suffixFile,sys.argv[i])
        dataClassDict[classType[:suffixFile]] = dataClass
        if sys.argv[i] == test:
            if len(Insert.checkValid(test[:suffixFile],'sum(weight)','100',projectName,"course_id")) > 0:
                combineData.saveJson(fileRoot, sys.argv[-1], {"error": "Invalid course weights"})
                return


    MergeStudentMark = ProcessData(mysqlUser,mysqlHost)
    dataClass = MergeStudentMark.mergeData(students[:suffixFile],marks[:suffixFile],mergeStudentMark,dataClassDict,projectName)
    dataClassDict[mergeStudentMark] = dataClass

    MergeCourseTest = ProcessData(mysqlUser,mysqlHost)
    dataClass = MergeCourseTest.mergeData(courses[:suffixFile],test[:suffixFile],mergeCourseTest,dataClassDict,projectName)
    dataClassDict[mergeCourseTest] = dataClass

    MergeTotal = ProcessData(mysqlUser,mysqlHost)
    MergeTotal.mergeData(mergeStudentMark,mergeCourseTest,mergeTotal,dataClassDict,projectName)


    GroupData = ProcessData(mysqlUser,mysqlHost)
    totalData = GroupData.processData(selectItem,mergeTotal,calculateForm,groupClass,projectName,deserveItem)

    finalDict = combineData.combineDict(totalData)
    combineData.saveJson(fileRoot,sys.argv[-1],finalDict)
    return

main()