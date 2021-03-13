import datetime

class Employee:
    # name=" "
    # zp_day=1
    # days=1
    # zp_mo=zp_day*days

    def __init__(self, name, zp_day, days):
        self.name = name
        self.zp_day= zp_day
        self.days= days

    def work(self):
        return "I come to the office"

    def cheak_salary(self):
        def zp(zp_day):
            data_now=datetime.date.today().day
            working_day=0
            while data_now>0:
                if data_now > 5:
                    working_day+=5
                else:
                    working_day+=data_now
                data_now-=7
            return zp_day * working_day
        zp_now=zp(self.zp_day)
        zp_month= self.zp_day * self.days
        return f"Зарплата за месяц: {zp_month}. Зарплата на текущий рабочий день: {zp_now}"

    def __gt__(self, other):
        return self.cheak_salary() > other.cheak_salary()

    def __ge__(self, other):
        return self.cheak_salary() >= other.cheak_salary()

    def __lt__(self, other):
        return self.cheak_salary() < other.cheak_salary()

    def __le__(self, other):
        return self.cheak_salary() <= other.cheak_salary()

    def __eq__(self, other):
        return self.cheak_salary() == other.cheak_salary()

    def __ne__(self, other):
        return self.cheak_salary() != other.cheak_salary()


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


a=Recruiter("Ivan", 100, 23)
print(a.work())
print(a.cheak_salary())
print(a)

print()

b=Programmer("Alex", 200, 23)
print(b.work())
print(b.cheak_salary())
print(b)

print(a<b)