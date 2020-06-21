from Data import *

class Users:

    def __init__(self, name):
        self.name = name

    #Method to allow users to filter their selection
    def filter(self, keywords, radius=10000, location=None):
        businesses = Data.search(keywords, radius, location)
        return businesses
    
    #Method for users to manually report lines and estimated wait times
    def report_line(self, address, queue, eta):
        Data.setLines(address, queue, eta)

person = Users("Jason")
person.report_line('1234 Sesame St', 12345, 1234123410)
print(Data.getLines('1234 Sesame St'))
print("Hello World")
