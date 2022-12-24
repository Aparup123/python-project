import csv
import matplotlib.pyplot as plt
fields=["Student ID", "Name", "Class Roll Number", "Batch Name"]
c=None

def addStudent():
    with open ("student.csv", "r") as fhand:
        c=fhand.read()
        print(c)
    if c=="":
        with open ("student.csv", "a") as fhand:
            csvWriter=csv.writer(fhand)
            csvReader=csv.reader(fhand)
            csvWriter.writerow(fields)
    else:
        print("fdfs")
        sid=input("STUDENT ID: ")
        sname=input("STUDENT NAME: ")
        sroll=input("Class ROll Number: ")
        sbatch=input("BATCH NAME: ")
        sdetails=[sid,sname,sroll,sbatch]
        with open ("student.csv","a") as fhand:
            csvWriter=csv.writer(fhand)
            csvWriter.writerow(sdetails)

def viewStudent():
    with open ("student.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        print("--------------------------------------------------------------------------------------------")
        for row in csvReader:
            print(row[0]+" "*(12-len(row[0]))+row[1]+" "*(30-len(row[1]))+str(row[2])+" "*(25-len(str(row[2])))+row[3])
        print("--------------------------------------------------------------------------------------------")
def removeStudent():
    delID=input("Enter the ID of the student to be deleted: ")
    editedData=[]
    with open ("student.csv","r") as fhandin:
        csvReader=csv.reader(fhandin)
        for row in csvReader:
            if(row[0]!=delID):
                editedData.append(row)
    with open ("student.csv","w") as fhandout:
        csvWriter=csv.writer(fhandout)
        csvWriter.writerows(editedData)
def updateStudent():
    updateddata=[]
    updateid=input("Enter the id of the student to be updated: ")
    updateChoice=int(input("1)Update Student Name, 2)Update Student Roll Number, 3)Update Student Batch"))
    with open ("student.csv","r") as fhandin:
        csvReader=csv.reader(fhandin)
        for row in csvReader:
            if(row[0]!=updateid):
                updateddata.append(row)
            else:
                match updateChoice:
                    case 1:
                        newName=input("Enter the new name: ")
                        row=[row[0],newName,row[2],row[3]]
                    case 2:
                        newRoll=int(input("Enter the new roll number: "))
                        row=[row[0],row[1],newRoll,row[3]]
                    case 3:
                        newBatch=input("Enter new batch: ")
                        row=[row[0],row[1],row[2],newBatch]
                updateddata.append(row)
    with open ("student.csv","w") as fhandout:
        csvWriter=csv.writer(fhandout)
        csvWriter.writerows(updateddata)
def studentDb():
    choice=0
    while(choice!=5):
        choice=int(input("Enter 1)CREATE A STUDENT, 2)UPDATE STUDENT DETAILS, 3)REMOVE A STUDENT FROM THE DATABASE, 4)VIEW 5)DONE!"))
        match choice:
            case 1:
                addStudent()
            case 2:
                updateStudent()
            case 3:
                removeStudent()
            case 4:
                viewStudent()


#Course Database

def addCourse():
    courseField=["id","name","marks"]
    with open ("course.csv", "r") as fhand:
        c=fhand.read()
        print(c)
    if c=="":
        with open ("course.csv", "a") as fhand:
            csvWriter=csv.writer(fhand)
            csvReader=csv.reader(fhand)
            csvWriter.writerow(courseField)
    else:
        print("fdfs")
        cid=input("Course ID: ")
        cname=input("Course name: ")
        marksLength=int(input("Enter the number of student u want to add marks: "))
        cmarks=dict(input("Enter student id and marks: ").split() for i in range (marksLength))
        cdetails=[cid,cname,cmarks]
        with open ("course.csv","a") as fhand:
            csvWriter=csv.writer(fhand)
            csvWriter.writerow(cdetails)
def viewCourse():
    with open ("course.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        print("--------------------------------------------------------------------------------------------")
        for row in csvReader:
            print(row[0]+" "*(12-len(row[0]))+row[1]+" "*(30-len(row[1]))+str(row[2]))
        print("--------------------------------------------------------------------------------------------")
def viewPerformance():
    courseId=input("Enter the course id: ")
    reqDic={}
    with open("course.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[0]==courseId):
                reqDic=eval(row[2])
        with open("student.csv","r") as fhand:
            csvReader=csv.reader(fhand)
            print("--------------------------------------------------------------------------------------------")
            print("NAME                          ROLL        MARKS")
            for key,value in reqDic.items():
                for row in csvReader:
                    # print(row)
                    # print(key)
                    if(key==row[0]):
                        print(row[1]+" "*(30-len(row[1]))+row[2]+" "*(12-len(row[2]))+value)
                        break
            print("--------------------------------------------------------------------------------------------")       
def histogram():
    courseId=input("Enter the course id: ")
    marksList=[]
    marksDict={}
    with open("course.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
          if(row[0]==courseId):
                marksDict=eval(row[2])
                for key,value in marksDict.items():
                    marksList.append(int(value))
                print(marksList)
                plt.hist(marksList)
                plt.xlabel("Grades")
                plt.ylabel("Number of students")
                plt.show()
            
    

def courseDb():
    choice=0
    while(choice!=5):
        choice=int(input("Enter 1)CREATE A COURSE, 2)VIEW PERFORMANCE, 3)COURSE STATISTICS, 4)VIEW 5)DONE!"))
        match choice:
            case 1:
                addCourse()
            case 2:
                viewPerformance()
            case 3:
                histogram()
            case 4:
                viewCourse()

#BATCH DATABASE
def addBatch():
    batchField=["Batch ID","Batch Name","Department Name", "List of Courses", "list of students"]
    with open ("batch.csv", "r") as fhand:
        c=fhand.read()
        print(c)
    if c=="":
        with open ("batch.csv", "a") as fhand:
            csvWriter=csv.writer(fhand)
            # csvReader=csv.reader(fhand)
            csvWriter.writerow(batchField)
    
    print("fdfs")
    bid=input("Batch ID: ")
    bname=input("Batch name: ")
    dname=input("Department name: ")
    courseLength=int(input("Enter the number of courses in this batch: "))
    courseList=[input("Enter courses in this batch: ") for i in range(courseLength)]
    studentList=[]
    with open ("student.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[3]==bid):
                studentList.append(row[0])
    # studentLength=int(input("Enter number of students in the batch: "))
    # studentList=[input("Enter student id: ") for i in range(studentLength)]
    bdetails=[bid,bname,dname,courseList,studentList]
    with open ("batch.csv","a") as fhand:
        csvWriter=csv.writer(fhand)
        csvWriter.writerow(bdetails)
def viewBatch():
    with open ("batch.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        print("--------------------------------------------------------------------------------------------")
        for row in csvReader:
            print(row[0]+" "*(12-len(row[0]))+row[1]+" "*(20-len(row[1]))+str(row[2])+" "*(20-len(row[2]))+str(row[3])+" "*(30-len(str(row[3])))+str(row[4]))
        print("--------------------------------------------------------------------------------------------")
def viewStudentList():
    batchId=input("Enter batchId: ")
    with open ("batch.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[0]==batchId):
                studentList=eval(row[4])
                for element in studentList:
                    print(element)
                    with open ("student.csv", "r") as fhand:
                        csvReader=csv.reader(fhand)
                        for row in csvReader:
                            if(row[0]==element):
                                print(row[0]+" "*(12-len(row[0]))+row[1]+" "*(20-len(row[1]))+str(row[2])+" "*(20-len(row[2]))+str(row[3]))

def batchDb():
    choice=0
    while(choice!=5):
        choice=int(input("Enter 1)CREATE A NEW BATCH, 2)VIEW LIST OF ALL STUDENT IN A BATCH, 3)VIEW LIST OF ALL COURSES TAUGHT IN A BATCH, 4)VIEW 5)DONE!"))
        match choice:
            case 1:
                addBatch()
            case 2:
                viewStudentList()
            case 3:
                histogram()
            case 4:
                viewBatch()
#Database choice
def choice():
    choice=0
    while(choice!=6):
        choice=int(input("Enter 1)STUDENT DB, 2)COURSE DB, 3)BATCH DB, 4)DEPARTMENT DB 5)EXAMINATION DB 6)DONE!"))
        match choice:
            case 1:
                studentDb()
            case 2:
                courseDb()
            case 3:
                batchDb()
            case 4:
                viewStudent()
choice()