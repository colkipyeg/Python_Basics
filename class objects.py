
class Student:
    school_name = "ABC PRIMARY SCHOOL"
    station=5

    def __init__(self,math,eng,kis,sci,sst):
        self.M = math
        self.E = eng
        self.K = kis
        self.S = sci
        self.T = sst


    def total_marks(self):
        print(self.M + self.E + self.K + self.S + self.T)

        
    def average_score(self):
        print((self.M + self.E + self.K + self.S + self.T) /5)

sch=Student(56,67,87,89,78)
print(sch.station)
s1=Student(56,67,87,89,78)
sch.total_marks()
sch.average_score()
s1.average_score()
