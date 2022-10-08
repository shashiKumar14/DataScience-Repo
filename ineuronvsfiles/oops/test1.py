# class Person:
#     def __init__(self,name,surname,emailid,year_of_birth):
#         self.name=name
#         self.surname=surname
#         self.emailid=emailid
#         self.year_of_birth=year_of_birth

# shashi=Person('shashi','ega','mailid@gmail.com',1995)
# print(shashi.name)
# print(shashi.surname)
# print(shashi.emailid)
class Dress:
   cloth = "silk"
   type = "shirt"
   def details(self):
       return f"A {self.cloth} {self.type}"
shirt = Dress()
print(shirt.details())