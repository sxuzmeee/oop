#1
# class CPerson:
#     def __init__(self, first_name, last_name, middle_name, birth_day, birth_month, birth_year, gender):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#         self.birth_day = birth_day
#         self.birth_month = birth_month
#         self.birth_year = birth_year
#         self.gender = gender
#
#     def __del__(self):
#         print("Person object has been deleted")
#
#     def update_info(self, first_name, last_name, middle_name, birth_day, birth_month, birth_year, gender):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#         self.birth_day = birth_day
#         self.birth_month = birth_month
#         self.birth_year = birth_year
#         self.gender = gender
#
#     def get_info(self):
#         return f"Name: {self.first_name} {self.last_name} {self.middle_name}, Date of Birth: {self.birth_day}/{self.birth_month}/{self.birth_year}, Gender: {self.gender}"
#
#
#
# person1 = CPerson("John", "Doe", "Smith", 10, 5, 1990, "Male")
# print(person1.get_info())
# person1.update_info("Jane", "Doe", "Smith", 15, 8, 1985, "Female")
# print(person1.get_info())
# del person1

#2

# class Phone:
#     def __init__(self, number, model, weight):
#         self.number = number
#         self.model = model
#         self.weight = weight
#
#     def receiveCall(self, caller_name):
#         print(f"Звонит {caller_name}")
#
#     def getNumber(self):
#         return self.number
#
#
#
# phone1 = Phone("12345", "iPhone", 150)
# phone2 = Phone("67890", "Samsung", 180)
# phone3 = Phone("54321", "Nokia", 200)
#
#
# print("Phone 1 - Number:", phone1.number, "Model:", phone1.model, "Weight:", phone1.weight)
# print("Phone 2 - Number:", phone2.number, "Model:", phone2.model, "Weight:", phone2.weight)
# print("Phone 3 - Number:", phone3.number, "Model:", phone3.model, "Weight:", phone3.weight)
#
#
# phone1.receiveCall("John")
# print("Phone 1 Number:", phone1.getNumber())
#
# phone2.receiveCall("Alice")
# print("Phone 2 Number:", phone2.getNumber())
#
# phone3.receiveCall("Bob")
# print("Phone 3 Number:", phone3.getNumber())

#3

class Reader:
    def __init__(self, full_name, ticket_number, faculty, birth_date, phone_number):
        self.full_name = full_name
        self.ticket_number = ticket_number
        self.faculty = faculty
        self.birth_date = birth_date
        self.phone_number = phone_number

    def takeBook(self, sum_of_books):
        print(f"{self.full_name} взял книги в количестве '{sum_of_books}'")

    def returnBook(self, sum_of_books):
        print(f"{self.full_name} вернул книги в количестве:'{sum_of_books}'")



reader1 = Reader("Иванов Иван Иванович", "ABC12345", "Программирование Python", "01.01.2007", "123-45-67")
reader2 = Reader("Петрова Мария Сергеевна", "BCAD54321", "Медтехника", "15.05.2007", "987-65-43")

reader1.takeBook("3")
reader2.returnBook("3")



