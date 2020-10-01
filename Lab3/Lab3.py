class Teacher:

    def __init__(self, record, name, first_name,
                 second_name, gender, birthday,
                 telephone, discipline,experience = 1):
        self.record = record
        self.name = name
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.birthday = birthday
        self.telephone = telephone
        self.discipline = discipline
        self.experience = experience


    def showInfo(self):
        print("|%-7s|%-15s|%-15s|%-15s|%-6s|%-10s|%-11s|%-15s|%-10s|" % (str(self.record), self.name, self.first_name , self.second_name ,  self.gender, str(self.birthday), str(self.telephone), self.discipline , str(self.experience)))


person = [Teacher(1, "Person1", "Person1", "Person1", "w", "12/12/12", "88005553535", "math", 25),
Teacher(2, "Person2", "Person2", "Person2", "w", "12/12/12", "88005553535", "math", 10)]

while True:
    try:
        k = int(input("==========================\n"
                      "1. Добавление информации.\n"
                      "2. Удаление информации.\n"
                      "3. Отображение информации.\n"
                      "4. Поиск по дисциплине.\n"
                      "Для выхода введите 0.\n"
                      "Введите номер задания: "))
    except:
        print("Ошибка, введен не верный номер задания. Попробуйте снова.")
        continue
    break

while k != 0:
    if k == 1:
        while True:
            try:
                record = int(input("Табельный номер: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        name = (input("Имя: "))
        first_name = (input("Фамилия: "))
        second_name = (input("Отчество: "))
        gender = (input("Пол: "))
        birthday = (input("День рождение: "))
        while True:
            try:
                telephone = int(input("Номер телефона: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        discipline = (input("Дисциплина: "))

        while True:
            try:
                experience = int(input("Стаж: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        if (experience < 0):
         person.append(Teacher(record, name, first_name,
                 second_name, gender, birthday,
                 telephone, discipline))
        else:
            person.append(Teacher(record, name, first_name,
                                  second_name, gender, birthday,
                                  telephone, discipline, experience ))
    elif k == 2:
        while True:
            try:
                x = int(input("Номер для удаления: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        for i in range(len(person)):
            if(i == x):
                person.pop(i)
    elif k == 3:
        print("|%-7s|%-15s|%-15s|%-15s|%-6s|%-10s|%-11s|%-15s|%-10s|" % ("record", "name", "first_name", "second_name", "gender", "birthday","telephone","discipline","experience"))
        for i in range(len(person)):
            person[i].showInfo()
    elif k == 4:
        while True:
            try:
                x = (input("Дисциплина: "))
            except:
                print("Ошибка. Попробуйте снова.")
                continue
            break
        f = False
        for i in range(len(person)):
            if (person[i].discipline == x):
                f = True
                person[i].showInfo()
        if not(f):
            print("Преподавателей, которые ведут эту дисциплину нет.")
    else: print("Ошибка, введен не верный номер задания. Попробуйте снова.")

    while True:
        try:
            k = int(input("==========================\n"
                      "1. Добавление информации.\n"
                      "2. Удаление информации.\n"
                      "3. Отображение информации.\n"
                      "4. Поиск по дисциплине.\n"
                      "Для выхода введите 0.\n"
                      "Введите номер задания: "))
        except:
            print("Ошибка, введен не верный номер задания. Попробуйте снова.")
            continue
        break