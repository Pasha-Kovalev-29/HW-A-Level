import models as mod

a = mod.Recruiter("Ivan", 100, 23)
print(a)
print(a.work())
print(a.cheak_salary())

print()

b = mod.Programmer("Alex", 200, 23, {'knowledge of English ', 'Python', 'JS', 'Git', 'html&css'})
print(b)
print(b.work())
print(b.cheak_salary())
print(b.tech_stack)

print()
print(a == b)  # comparison by salary
print()

c = mod.Programmer("Alesha", 200, 23, {'knowledge of English ', 'Python', 'Flask', 'Django'})
print(c)
print(c.work())
print(c.cheak_salary())
print(c.tech_stack)

print()
print(b > c)  # comparison by skills
print()

alfa = b + c  # creature alfa-programmer
print(alfa)
print(alfa.work())
print(alfa.cheak_salary())
print(alfa.tech_stack)