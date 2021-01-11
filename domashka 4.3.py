class Name:
    def __init__(self, surname, name, secondname):
        self.name = name
        self.surname = surname
        self.secondname = secondname


    def brief_name(self): #Возвращает строку "Фамилия Имя"
        return print(surname, name)

    def initials(self): #Возвращает строку "Фамилия И.О."
        return print(surname, name[0], secondname[0])


    #def strfname(format): #СЛОЖНА


# Проверяю количество введенных символов и в зависимости от результата вызываю класс
while True:
    a = ("Иванов Иван Иванович")
    b = a.split()

    if len(b) < 2:
        print("Введите Фамилия + Имя или полностью ФИО")
        continue
    elif 2 == len(b):
        surname, name = a.split()[0], a.split()[1]
        x = Name(surname, name)
        x.brief_name()
        break
    elif 3 == len(b):
        surname, name, secondname = a.split()[0], a.split()[1], a.split()[2]
        x = Name(surname, name, secondname)
        x.initials()
        break

