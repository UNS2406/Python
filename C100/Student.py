# C100--- python classes


class Student(object):
    """
      blueprint for Student
    """

    def __init__(self, nameInput, ageInput, genderInput, levelInput, gradesInput):
        self.name = nameInput
        self.age = ageInput
        self.gender = genderInput
        self.level = levelInput
        self.grades = gradesInput or {}

    def setGrade(self, courseInput, gradesInput):
        self.grades[courseInput] = gradesInput

    def getGrade(self, courseInput):
        return self.grades[courseInput]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)


# Define some students
john = Student("John", 12, "male", 6, {"math": 3.3})
jane = Student("Jane", 12, "female", 6, {"math": 3.5})

# calling/triggering functions
print("The grades of john are: "+john.getGPA())
print("The grades of john are: "+jane.getGPA())
