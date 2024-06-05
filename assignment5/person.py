class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        

class AttributeDisplayMixin:
    def display_attributes(self):
      
        attribute_strings = []

        for key in self.__dict__:
            value = getattr(self, key)
            attribute_string = "{}: {}".format(key, value)
            attribute_strings.append(attribute_string)

        result = ', '.join(attribute_strings)
        return result
    
class Student(Person, AttributeDisplayMixin):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university
        
        
