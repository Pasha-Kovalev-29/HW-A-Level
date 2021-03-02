# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

students = {'Ivanov Sergey': [3, 5, 5], 'Sidorov Evgeniy': [5, 5, 2], 'Kravchenko Denis': [4, 4, 3],
            'Denisov Egor': [3, 2, 3], 'Kylakov Sergey': [3, 4, 3]}


def averagesum(numList):
    """
    input: list numbers
    return: average point
    """
    theSum = 0
    for i in numList:
        theSum = theSum + int(i)
    return theSum / len(numList)


def for_everybody(listSt):
    """ input: dictionary with student grades
     causes function averagesum for counting average point
     return dictionary with averagesum"""
    for i in listSt:
        students[i] = averagesum(students[i])
    return students


def academic_performance(d):
    """ a) input a list of the dict keys and values;
        b) return the key with the max and the min value
        c) print the most successful student and the lagging student"""
    average = for_everybody(d)
    v = list(average.values())
    k = list(average.keys())
    print('The most successful student ' + str(k[v.index(max(v))]) + '.' + "Average point " + str(max(v)))
    print('The lagging student ' + str(k[v.index(min(v))]) + '.' + "Average point " + str(min(v)))


academic_performance(students)
