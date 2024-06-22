class Ward:
    def __init__(self, name=""):
        self.name = name
        self.people = []

    def describe(self):
        print(f"Ward Name: {self.name}")

    def add_person(self, person):
        self.people.append(person)

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people.sort(key=lambda x: x.yob)

    def compute_average(self):
        sum_age = 0
        count = 0
        for person in self.people:
            if isinstance(person, Teacher):
                sum_age += person.yob
                count += 1
        return sum_age / count


class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Student - Name : {self.name} - YoB : {self.yob} - Grade : {self.grade}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name : {self.name} - YoB : {self.yob} - Specialist: : {self.specialist}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name : {self.name} - YoB : {self.yob} - Subject : {self.subject}")


if __name__ == "__main__":
    student1 = Student(name=" studentA ", yob=2010, grade="7")
    teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
    teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
    doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1 = Ward(name=" Ward1 ")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    print(ward1.count_doctor())
