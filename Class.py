class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def details(self):
        print(self.name, self.age, self.address)

    def u_name(self,uname):
        self.name = uname

    def u_age(self,uage):
        self.age = uage

    def u_address(self,uaddress):
        self.address = uaddress
        

x = Person("Ram", 25, "ABC Street")

print("Before Updation:\n")
x.details()

x.u_name("Shyam")
x.u_age(23)
x.u_address("XYZ street")

print("\nAfter Updation:\n")

x.details()