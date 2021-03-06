#부모 클래스 정의 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format( 
            self.name, self.phoneNumber))
    def methodA(self):
        pass
    def methodB(self):
        pass 
    
#자식 클래스 정의 
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모 클래스 생성자 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받아서 마음에 안들면 재정의(override)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format( 
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format( 
            self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "201111")
p.printInfo()
s.printInfo()



