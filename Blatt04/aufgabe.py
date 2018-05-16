import sys
import threading
import time


students = int(sys.argv[1])
waiting = int(sys.argv[2])
book1 = threading.Semaphore(3)
book2 = threading.Semaphore(2)
book3 = threading.Semaphore(2)



class Student(threading.Thread):
    id = 0
    times = 0
    hasAll = False

    def __init__(self, i):
        super(Student, self).__init__()
        self.id = i;
    def run(self):
        while True:
            book1.acquire()
            book2.acquire()
            book3.acquire()
            self.hasAll = True
            self.times += 1
            time.sleep(waiting)

            book1.release()
            self.hasAll = False
            book2.release()
            book3.release()
            time.sleep(0.0001)



if len(sys.argv) != 3:
    print("Wrong number of parameters")
    exit(1)

studentList = []

for i in range(students):
    studentList.append(Student(i))
    studentList[i].start()

while True:
    time.sleep(1)
    workingStudents = 0
    for idx, student in enumerate(studentList):
        print("Student " + str(student.id) + " has " + str(student.times))
        if student.hasAll:
            workingStudents += 1
    print("Working Students: " +  str(workingStudents))
    print()
