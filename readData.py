import csv
class ReadData:
    def __init__(self,inputPath):
        self.inputPath = inputPath
    def readCsvInput(self):
        csvFile = open(self.inputPath)
        reader = csv.reader(csvFile)
        dataClass = []
        data = []
        for item in reader:
            if reader.line_num == 1:
                for it in item:
                    dataClass.append(it)
            else:
                tempData = []
                for it in item:
                    tempData.append(it)
                data.append(tempData)
        return dataClass,data
