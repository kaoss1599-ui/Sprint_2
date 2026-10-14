from random import randint

class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8

        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f'{name}@email.com'

        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls):
        cls.hourly_payment = randint(300, 500)

    def salary(self):
        employee = self

        if self.hours is None:
            employee = EmployeeSalary.get_hours(self.name, self.hours, self.rest_days, self.email)

        return employee.hours * self.hourly_payment
