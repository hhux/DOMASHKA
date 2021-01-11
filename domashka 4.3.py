a = ('Иванов Иван Иваныч')


class Name:
    def __init__(self, namename):
        if len(namename.split()) == 1:
            #TODO посмотреть как правильно raise Error?
            print('Введите ФИ или ФИО')

        elif 2 == len(namename.split()):
            surname, name = namename.split()[0], namename.split()[1]
            self.name = name
            self.surname = surname
            self.secondname = ''

        elif 3 == len(namename.split()):
            surname, name, secondname = namename.split()[0], namename.split()[1], namename.split()[2]
            self.name = name
            self.surname = surname
            self.secondname = secondname


    def brief_name(self): #Возвращает строку "Фамилия Имя"
        return print(self.surname, self.name)


    def initials(self): #Возвращает строку Фамилия И.О., если есть отчество / возвращает Фамилия И., если нет отчества"
        final_name = self.name[0] + '.'
        try:
            return print(self.surname, final_name, self.secondname[0] + '.')
        except:
            return print(self.surname, final_name, self.secondname)


    def strfname(format): # Преобразует строку по заданному формату
        little_name = format.name[0]
        big_name = format.name
        little_surname = format.surname[0]
        big_surname = format.surname
        little_secondname = format.secondname[0]
        big_secondname = format.secondname
        return print('%x. %y %Z' % (little_name, little_surname, big_secondname))



x = Name(a)
x.brief_name()
x.initials()
x.strfname('%x. %y %Z')