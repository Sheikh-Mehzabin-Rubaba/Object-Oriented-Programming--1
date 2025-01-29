class student:
    grade=10
    name="Mitu"
    def intro(self):
        print("Hi I am a student")
    def details(self):
        print("My name is ", self.name, "and I study in", self.grade)
ol=student()#object creation
ol.intro()
ol.details()