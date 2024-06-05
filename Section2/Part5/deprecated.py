import warnings
from datetime import date

class Person:
    def __init__(self, *, name: str, gender: str, date_of_birth: date, phone_num: str = '', address: str = ''):
        self.name = name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self._phone_num = phone_num
        self._address = address
        
    @property 
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
    @property
    def phone_num(self):
        return self._phone_num
    
    @phone_num.setter
    def phone_num(self, value: str):
        if not value:
            raise ValueError("Invalid! Empty input field for phone number.")
        self._phone_num = value

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value: str):
        if not value:
            raise ValueError("Invalid! Empty input field for address.")
        self._address = value

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Phone: {self.phone_num}, Address: {self.address}"

class Adult(Person):
    def __init__(self, *, name: str, gender: str, date_of_birth: date, phone_num: str = '', address: str = '', occupation: str, salary: float, school_graduated: str):
        super().__init__(name=name, gender=gender, date_of_birth=date_of_birth, phone_num=phone_num, address=address)
        self._occupation = occupation
        self._salary = salary
        self._school_graduated = school_graduated

    @property
    def occupation(self):
        return self._occupation
    
    @occupation.setter
    def occupation(self, value: str):
        if not value:
            raise ValueError("Invalid! Empty input field for occupation.")
        self._occupation = value
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value: float):
        if value < 0:
            raise ValueError("Invalid! Salary cannot be negative.")
        self._salary = value
    
    @property
    def school_graduated(self):
        return self._school_graduated
    
    @school_graduated.setter
    def school_graduated(self, value: str):
        if not value:
            raise ValueError("Invalid! Empty input field for school graduated.")
        self._school_graduated = value

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Occupation: {self.occupation}, Salary: {self.salary}, School Graduated: {self.school_graduated}"
    
     # Added a deprecation warning to the job property and setter, advising to use occupation instead.
     # The job property and setter are updated to provide a deprecation warning and forward compatibility with occupation.
    @property
    def job(self):
        """
        Deprecated. Use `occupation` instead.
        """
        warnings.warn("The 'job' attribute is deprecated, use 'occupation' instead", DeprecationWarning, stacklevel=2)
        print("\n")
        return self._occupation
    
    @job.setter
    def job(self, value: str):
        """
        Deprecated. Use `occupation` instead.
        """
        warnings.warn("The 'job' attribute is deprecated, use 'occupation' instead", DeprecationWarning, stacklevel=2)
        print("\n")
        self._occupation = value

class Child(Person):
    # Renamed the 'school' parameter to 'school_name'
    def __init__(self, *, name: str, gender: str, date_of_birth: date, phone_num: str = '', address: str = '', school_name: str):
        super().__init__(name=name, gender=gender, date_of_birth=date_of_birth, phone_num=phone_num, address=address)
        #made the school_name attribute private
        self._school_name = school_name

    @property
    def school_name(self):
        return self._school_name
    
    @school_name.setter
    def school_name(self, value: str):
        if not value:
            raise ValueError("Invalid! Empty input field for school name.")
        self._school_name = value

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, School: {self.school_name}"

    @property
    def school(self):
        """
        Deprecated. Use `school_name` instead.
        """
        warnings.warn("The 'school' attribute is deprecated, use 'school_name' instead", DeprecationWarning, stacklevel=2)
        print("\n")
        return self._school_name
    
    @school.setter
    def school(self, value: str):
        """
        Deprecated. Use `school_name` instead.
        """
        warnings.warn("The 'school' attribute is deprecated, use 'school_name' instead", DeprecationWarning, stacklevel=2)
        print("\n")
        self._school_name = value

def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            return date.fromisoformat(date_str)
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

adult = Adult(name="Tejas",
             gender="Male", 
             date_of_birth=date(2005, 1, 6), 
             occupation="SDE I", 
             salary=3500000, 
             school_graduated="KVGK")

# Triggering the deprecation warning by setting and getting the 'job' attribute
adult.job = "SDE"
print(adult.job)

child = Child(name="Samiksha",
             gender="Female",
             date_of_birth=date(2019, 5, 15),
             school_name="Springfield Elementary")

# Triggering the deprecation warning by setting and getting the 'school' attribute
child.school = "Westfield Elementary"
print(child.school)