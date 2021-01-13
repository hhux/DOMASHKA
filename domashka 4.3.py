a = 'Иванов Иван Иваныч'


class Name:
    def __init__(self, namename):
        if len(namename.split()) == 1:
            try:
                a.brief_name
            except:
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

    def brief_name(self):  # Возвращает строку "Фамилия Имя"
        return print(self.surname, self.name)

    def initials(
            self):  # Возвращает строку Фамилия И.О., если есть отчество / возвращает Фамилия И., если нет отчества"
        final_name = self.name[0] + '.'
        try:
            return print(self.surname, final_name, self.secondname[0] + '.')
        except:
            return print(self.surname, final_name, self.secondname)

    def strfname(self, format_):  # Преобразует строку по заданному формату с помощью костылей
        surname, name, secondname = a.split()[0], a.split()[1], a.split()[2]

        if '%и.' in format_:
            print(name.replace('ван', '.'), end='')
        if '%о.' in format_:
            print(secondname.replace(secondname[1::], '.'), end='')
        if '%ф.' in format_:
            print(surname.replace(surname[1::], '.'), end='')

        if '%Ф' in format_:
            print(surname, end=' ')
        if '%И' in format_:
            print(name, end=' ')
        if '%О' in format_:
            print(secondname, end=' ')

        return


x = Name(a)
x.brief_name()
x.initials()
x.strfname('%Ф %и. %о.')
