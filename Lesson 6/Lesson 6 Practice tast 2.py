# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах. Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

all_stydents = {'Ivanov Sergei', 'Petrov Andrei', "Simonenko Anton", 'Kizil Egor', 'Vorobei Ivan', 'Zolotarev Vladimir',
                'Samsonov Emil', 'Babich Dmitrii', "Dimon )))))"}
Python = {'Ivanov Sergei', 'Vorobei Ivan', "Dimon )))))", 'Petrov Andrei'}
FrontEnd = {'Petrov Andrei', "Dimon )))))", 'Zolotarev Vladimir', }
FullStack = {'Simonenko Anton', 'Samsonov Emil', "Dimon )))))", 'Kizil Egor'}
Java = {'Kizil Egor', 'Babich Dmitrii', "Dimon )))))"}

print('Stydents who study in two or more group: ' + str(
    (Python & FrontEnd) | (Python & FullStack) | (Python & Java) | (FrontEnd & FullStack) | (FrontEnd & Java) | (
            FullStack & Java)))
print('Students not studying FrontEnd: ' + str(all_stydents - FrontEnd))
print('Students who study Python and Java: ' + str(Python | Java))
