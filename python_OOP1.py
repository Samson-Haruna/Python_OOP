class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

   # def get_grade(self):
        #return self.grade
    

class Course:
    def __init__(self,course_name,max_students):
        self.course_name = course_name
        self.max_students = max_students 
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
        

s1 = Student('sam',18,78)
s2 = Student('sadiq',19,70)
s3 = Student('ahmed',21,60)

course = Course('Mathematics',3)
course.add_students(s1)
course.add_students(s2)
course.add_students(s3)

print(course.get_average_grade())



