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
    def __init__(self, *, name: str, gender: str, date_of_birth: date, phone_num: str = '', address: str = '', job: str, salary: float, school_graduated: str):
        super().__init__(name=name, gender=gender, date_of_birth=date_of_birth, phone_num=phone_num, address=address)
        self._job = job
        self._salary = salary
        self._school_graduated = school_graduated

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value: str):
        if not value:
            raise ValueError("Invalid! Empty input field for job.")
        self._job = value
    
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
        return f"{base_info}, Job: {self.job}, Salary: {self.salary}, School Graduated: {self.school_graduated}"

class Child(Person):
    def __init__(self, *, name: str, gender: str, date_of_birth: date, phone_num: str = '', address: str = '', school: str):
        super().__init__(name=name, gender=gender, date_of_birth=date_of_birth, phone_num=phone_num, address=address)
        self._school = school

    @property
    def school(self):
        return self._school
    
    @school.setter
    def school(self, value: str):
        if not value:
            raise ValueError("Invalid! Empty input field for school.")
        self._school = value

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, School: {self.school}"

def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            return date.fromisoformat(date_str)
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def create_adult():
    name = input("Enter Adult name: ")
    gender = input("Enter gender: ")
    date_of_birth = get_date_input("Enter date of birth (YYYY-MM-DD): ")
    phone_num = input("Enter phone number: ")
    address = input("Enter address: ")
    job = input("Enter job: ")
    salary = float(input("Enter salary: "))
    school_graduated = input("Enter school graduated: ")
    return Adult(name=name, gender=gender, date_of_birth=date_of_birth, phone_num=phone_num, address=address, job=job, salary=salary, school_graduated=school_graduated)

def create_child():
    name = input("Enter Children name: ")
    gender = input("Enter gender: ")
    date_of_birth = get_date_input("Enter date of birth (YYYY-MM-DD): ")
    phone_num = input("Enter phone number: ")
    address = input("Enter address: ")
    school = input("Enter school: ")
    return Child(name=name, gender=gender, date_of_birth=date_of_birth, phone_num=phone_num, address=address, school=school)

# Example usage:
adult = create_adult()
child = create_child()

print(adult.get_info())
print(child.get_info())
