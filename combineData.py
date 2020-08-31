import json

def addCourse(courseList,data,averageScore):
    courseList.append({})
    courseList[-1]['id'] = data[2]
    courseList[-1]['name'] = data[3]
    courseList[-1]['teacher'] = data[4]
    courseList[-1]['courseAverage'] = float(str(data[5]))

    averageScore[0] += float(str(data[5]))
    averageScore[1] += 1
    return averageScore

def combineDict(totalData):
    total_result = {'student':[]}
    student_num = set()
    averageScore = [0,0]
    for i in range(len(totalData)):
        if totalData[i][0] not in student_num:
            if len(total_result["student"]) > 0:
                total_result['student'][-1]['totalAverage'] = round(averageScore[0]/averageScore[1],2)
                averageScore = [0,0]
            total_result['student'].append({'id':totalData[i][0],'name':totalData[i][1],'totalAverage': 0,'Courses':[]})
            student_num.add(totalData[i][0])
            addCourse(total_result["student"][-1]['Courses'],totalData[i],averageScore)
        else:
            addCourse(total_result["student"][-1]['Courses'],totalData[i],averageScore)
    return total_result

def saveJson(filePath,arg,data):
    with open(filePath+arg, 'w') as f:
        json.dump(data, f)