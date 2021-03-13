class Employee:
    # name="Ivan"
    # zp_day=100

    def __init__(self, name, zp_day, day):
        self.name = name
        self.zp_day= zp_day
        self.day= day

    def work(self):
        return "I come to the office"

    def cheak_salary(self, zp_day, days):
        return zp_day * days

    # def

class Recruiter(Employee):
    def work(self):
        return 'I come to the office and start to coding.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


class Programmer(Employee):
    def work(self):
        return 'I come to the office and start to hiring.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


a=Recruiter("Ivan", 100, 20)
print(a)


b=Programmer("Alex", 200, 20)
print(b)