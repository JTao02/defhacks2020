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
print(Data.getLines('1234 Sesame St'))


person.report_line('1885 Univeristy Ave', 10, 30)

person.report_line('1234 Sesame St', 5, 15)
print(Data.getLines('1234 Sesame St'))

print(person.filter("Coffee"))

for biz in person.filter("Coffee")['businesses']:
    print(biz['name'])

