class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id

    def common_method(self):
        print("This method runs for all")

    def summation(self, x, y=None, z=None):
        sum = 0
        if y != None and z != None:
            sum = x + y + z
        elif y != None:
            sum = x + y
        else:
            sum = sum + x
        print(sum)

    def description(self):
        print(f'Student name is "{self.name}" and id is {self.id}')


class CSEStudent(Student):
    def __init__(self, name, student_id, number_of_courses):
        super().__init__(name, student_id)
        self.number_of_courses = number_of_courses

    def common_method(self):
        print("This method runs for CSE Student")

    def cry(self):
        print(f'CSE student {self.name} is crying '
              f'because he/she has {self.number_of_courses} courses!')


class BBAStudent(Student):
    def party(self):
        print(f'All day party!! No study.')

    def common_method(self):
        print("This method runs for BBA Student")


class Fresher(CSEStudent, BBAStudent):

    def common_method(self):
        print("This method runs for Fresher Student")

    def orientation(self, take_orientation: bool):
        if take_orientation:
            print(f'The Fresher named {self.name} has taken orientation')
        else:
            print(f'The Fresher named {self.name} has NOT taken orientation')


student = Student("Student", 000)

cse1 = CSEStudent("Charles", 1001, 4)
cse1.description()
cse1.cry()
bba1 = BBAStudent("Smantha", 1003)
bba1.party()

fresher = Fresher("Mofiz", 2000, 2)
fresher.cry()
cse1.common_method()
bba1.common_method()
student.common_method()
fresher.common_method()

student.summation(10,12,100)
