class Student:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def details(self):
        print(f'Student name is: "{self.name}" and id is: "{self.id}"')


class CSEStudent(Student):
    def __init__(self, number_of_course, name: str, id: int):
        super().__init__(name, id)
        self.number_of_course = number_of_course

    def cry(self):
        print(f'CSE Student {self.name} is crying because of {self.number_of_course} courses!')


class BBAStudent(Student):
    def party(self):
        print(f'BBA Student {self.name} is partying all night!')


class Freshers(CSEStudent, BBAStudent):
    def orientation(self, take_orientation: bool):
        if take_orientation:
            print(f'The Fresher student named: {self.name} has taken orientation')
        else:
            print(f'The Fresher student named: {self.name} has NOT taken orientation')


student = Student("Student", 000)
cse1 = CSEStudent(4, "Bob", 50)
bba1 = BBAStudent("Charlie", 100)
bba1.details()
cse1.details()

fresher = Freshers(3, "Sam", 500)
fresher.details()
fresher.cry()

student.details()