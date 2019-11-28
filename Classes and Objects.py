class Person:
    species="Homo sapien"

    #init method/constructor method..It runs as soon you create an object
    def __init__(self, name, age):
        print("I am the contsructor method")
        self.jina=name
        self.miaka=age
    def walk(self):
        print("{} is walking".format(self.jina,))

p12=Person("collo",25)
print(p12.miaka)
print(p12.jina)
p12.walk()


#
# p1=Person()
# p2=Person()
# p1.name="collins"
# p2.name="jane"
# p1.age=20
# p2.age=21
# p1.citizenship="Kenyan"
# p1.marital_status="single"
# p1.walk()
# p2.walk()
# print(p1.walk)
#
# class Car:
#     make="Subaru"
#     wheels=4
#     YOM=2012
#
#     def park(self):
#         print("{} is being parked".format(self.make))
#
# C1=Car()
# print(C1.make)
# C1.park()
# print(C1.park)


class Student:
    school_name = "ABC PRIMARY SCHOOL"
    station=5
    def __init__(self,math,eng,kis,sci,sst,station):
        self.M = math
        self.E = eng
        self.K = kis
        self.S = sci
        self.T = sst
        self.ST = station

    def total_marks(self):
        print(self.M + self.E + self.K + self.S + self.T)
    def average_score(self):
        print((self.M + self.E + self.K + self.S + self.T) /5)

sch=Student("class 5:",56,67,87,89,78)
s1=Student("class 5:",56,67,87,89,78)
sch.total_marks()
sch.average_score()
s1.average_score()



#name
#subjects
#create a method to find totalmarks---TotalMarks()
#createa method to find the average score--AverageScore()
#create a method to grade the student--GradeS