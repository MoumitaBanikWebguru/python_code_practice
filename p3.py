# class Parent:
#    def func1(self):
#        print("This function is in parent class.")
# class Child(Parent):
#    def func2(self):
#        print("This function is in child class.")
# object = Child()
# object.func1()
# object.func2()

# class Mother:
#    mothername = ""
#    def mother(self):
#        print(self.mothername)
# class Father:
#    fathername = ""
#    def father(self):
#        print(self.fathername)
# class Son(Mother, Father):
#    def parents(self):
#        print("Father name is :", self.fathername)
#        print("Mother :", self.mothername)
# s1 = Son()
# s1.fathername = "Mommy"
# s1.mothername = "Daddy"
# s1.parents()


# class Animal:
#    def __init__(self, name):
#        self.name = name
 
#    def show_details(self):
#        print("Name:", self.name)
 
# class Dog(Animal):
#    def __init__(self, name, breed):
#        Animal.__init__(self, name)
#        self.breed = breed
 
#    def show_details(self):
#        Animal.show_details(self)
#        print("Species: Dog")
#        print("Breed:", self.breed)
 
# class Cat(Animal):
#    def __init__(self, name, color):
#        Animal.__init__(self, name)
#        self.color = color
 
#    def show_details(self):
#        Animal.show_details(self)
#        print("Species: Cat")
#        print("Color:", self.color)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(f"hi {self.name}, your average is {sum/3}") 
obj1 = Student("Moumita", [50,80,85])
obj1.avg()


   


