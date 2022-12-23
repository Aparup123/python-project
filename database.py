import csv
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

def courseDb():
    choice=0
    while(choice!=5):
        choice=int(input("Enter 1)CREATE A COURSE, 2)VIEW PERFORMANCE, 3)COURSE STATISTICS, 4)VIEW 5)DONE!"))
        match choice:
            case 1:
                addCourse()
            case 2:
                updateStudent()
            case 3:
                removeStudent()
            case 4:
                viewStudent()


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
                removeStudent()
            case 4:
                viewStudent()
choice()