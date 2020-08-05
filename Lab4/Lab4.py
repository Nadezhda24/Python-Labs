from tkinter import *
from tkcalendar import DateEntry
class Teacher:

    def __init__(self, record, name, first_name,
                 second_name, gender, birthday,
                 telephone, discipline,experience ):
        self.record = record
        self.name = name
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.birthday = birthday
        self.telephone = telephone
        self.discipline = discipline
        self.experience = experience

person = [Teacher(1, "Person1", "Person1", "Person1", "w", "12/12/12", "88005553535", "math", 25),
Teacher(2, "Person2", "Person2", "Person2", "w", "12/12/12", "88005553535", "math", 10)]

discipline = ["math", "english", "python", "c++", "java"]

def hat(i, j, frame):
    r_var = IntVar()
    r_var.set(0)

    lable_record = Label(frame, text="Табельный номер", font=("Comic Sans MS", 12), background="lavender", padx="20",
                         pady="8", width=12, height=1, borderwidth=2, relief="groove")
    lable_record.grid(row=1+i, column=1+j)

    lable_name = Label(frame, text="Имя", font=("Comic Sans MS", 12), background="lavender", padx="20", pady="8",
                       width=8, height=1, borderwidth=2, relief="groove")
    lable_name.grid(row=1+i, column=2+j)

    lable_first_name = Label(frame, text="Фамилия", font=("Comic Sans MS", 12), background="lavender", padx="20",
                             pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_first_name.grid(row=1+i, column=3+j)

    lable_second_name = Label(frame, text="Отчество", font=("Comic Sans MS", 12), background="lavender", padx="20",
                              pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_second_name.grid(row=1+i, column=4+j)

    lable_gender = Label(frame, text="Пол", font=("Comic Sans MS", 12), background="lavender", padx="20", pady="8",
                         width=8, height=1, borderwidth=2, relief="groove")
    lable_gender.grid(row=1+i, column=5+j)

    lable_birthday = Label(frame, text="День рождения", font=("Comic Sans MS", 12), background="lavender", padx="20",
                           pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_birthday.grid(row=1+i, column=6+j)

    lable_telephone = Label(frame, text="Телефон", font=("Comic Sans MS", 12), background="lavender", padx="20",
                            pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_telephone.grid(row=1+i, column=7+j)

    lable_discipline = Label(frame, text="Дисциплина", font=("Comic Sans MS", 12), background="lavender", padx="20",
                             pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_discipline.grid(row=1+i, column=8+j)

    lable_experience = Label(frame, text="Стаж", font=("Comic Sans MS", 12), background="lavender", padx="20",
                             pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_experience.grid(row=1+i, column=9+j)

def body(i,k,h, frame):
    record = Label(frame, text=str(person[i].record), font=("Comic Sans MS", 12), background="lavender",
                   padx="20",
                   pady="8", width=12, height=1, borderwidth=2, relief="groove")
    record.grid(row=i + k, column=1+h)

    name = Label(frame, text=str(person[i].name), font=("Comic Sans MS", 12), background="lavender", padx="20",
                 pady="8",
                 width=8, height=1, borderwidth=2, relief="groove")
    name.grid(row=i + k, column=2+h)

    first_name = Label(frame, text=str(person[i].first_name), font=("Comic Sans MS", 12), background="lavender",
                       padx="20",
                       pady="8", width=8, height=1, borderwidth=2, relief="groove")
    first_name.grid(row=i + k, column=3+h)

    second_name = Label(frame, text=str(person[i].second_name), font=("Comic Sans MS", 12), background="lavender",
                        padx="20",
                        pady="8", width=8, height=1, borderwidth=2, relief="groove")
    second_name.grid(row=i + k, column=4+h)

    gender = Label(frame, text=str(person[i].gender), font=("Comic Sans MS", 12), background="lavender", padx="20",
                   pady="8",
                   width=8, height=1, borderwidth=2, relief="groove")
    gender.grid(row=i + k, column=5+h)

    birthday = Label(frame, text=str(person[i].birthday), font=("Comic Sans MS", 12), background="lavender",
                     padx="20",
                     pady="8", width=8, height=1, borderwidth=2, relief="groove")
    birthday.grid(row=i + k, column=6+h)

    telephone = Label(frame, text=str(person[i].telephone), font=("Comic Sans MS", 12), background="lavender",
                      padx="20",
                      pady="8", width=8, height=1, borderwidth=2, relief="groove")
    telephone.grid(row=i + k, column=7+h)

    discipline = Label(frame, text=str(person[i].discipline), font=("Comic Sans MS", 12), background="lavender",
                       padx="20",
                       pady="8", width=8, height=1, borderwidth=2, relief="groove")
    discipline.grid(row=i + k, column=8+h)

    experience = Label(frame, text=str(person[i].experience), font=("Comic Sans MS", 12), background="lavender",
                       padx="20",
                       pady="8", width=8, height=1, borderwidth=2, relief="groove")
    experience.grid(row=i + k, column=9+h)

def click_back(frame, window):
    frame.destroy()
    frame = Frame(window)
    frame["bg"] = "lavender"
    frame.pack()
    create = Button(frame, text="Добавление записи",
                    background="light steel blue",
                    foreground="RoyalBlue4",
                    padx="20",
                    pady="8",
                    font=("Comic Sans MS", 16),
                    command=lambda: click_create(frame, window))
    create.pack(pady="20")

    delete = Button(frame, text="Удаление записи",
                    background="light steel blue",
                    foreground="RoyalBlue4",
                    padx="20",
                    pady="8",
                    font="16",
                    command=lambda: click_delete(frame, window))
    delete.pack(pady="20")

    show = Button(frame, text="Отобразить записи",
                  background="light steel blue",
                  foreground="RoyalBlue4",
                  padx="20",
                  pady="8",
                  font=("Comic Sans MS", 16),
                  command=lambda: click_show(frame, window))
    show.pack(pady="20")

    find = Button(frame, text="Найти запись",
                  background="light steel blue",
                  foreground="RoyalBlue4",
                  padx="20",
                  pady="8",
                  font=("Comic Sans MS", 16),
                  command=lambda: click_find(frame, window))
    find.pack(pady="20")


def click_save(frame, str_record, str_name, str_first_name, str_second_name, str_telephone, str_calendar, str_experience, variable, r_var):
    gender = ""
    if (r_var.get()):
        gender = "w"
    else:
        gender = "m"
    person.append(Teacher(str(str_record.get()), str(str_name.get()), str(str_first_name.get()), str(str_second_name.get()), str(gender), str(str_calendar.get()), str(str_telephone.get()), str(variable.get()), str(str_experience.get())))

    hint = Label(frame, text="Запись добавлена", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    hint.grid(row=10, column=0)


def click_create(frame, window):
    frame.destroy()
    frame = Frame(window)
    frame["bg"] = "lavender"
    frame.grid(row=0, column=0)
    back = Button(frame, text="Назад",
                background="light steel blue",
                foreground="RoyalBlue4",
                padx="10",
                pady="8",
                font=("Comic Sans MS", 10),
                command=lambda: click_back(frame, window))
    back.grid(row=0, column=0)
    save = Button(frame, text="Добавить",
                  background="light steel blue",
                  foreground="RoyalBlue4",
                  padx="10",
                  pady="8",
                  font=("Comic Sans MS", 10),
                  command=lambda: click_save(frame, str_record, str_name, str_first_name, str_second_name, str_telephone, str_calendar, str_experience, variable, r_var))
    save.grid(row=0, column=1)

    lable_record = Label(frame, text="Табельный номер: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_record.grid(row=1, column=0)
    str_record = StringVar()
    text_record = Entry(frame, font=("Comic Sans MS", 10), textvariable = str_record)
    text_record.insert(0,"1")
    text_record.grid(row=1, column=1)

    lable_name = Label(frame, text="Имя: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_name.grid(row=2, column=0)
    str_name = StringVar()
    text_name = Entry(frame, font=("Comic Sans MS", 10), textvariable = str_name)
    text_name.grid(row=2, column=1)
    text_name.insert(0,"Person1")
    str_first_name = StringVar()
    lable_first_name = Label(frame, text="Фамилия: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_first_name.grid(row=3, column=0)

    text_first_name = Entry(frame, font=("Comic Sans MS", 10), textvariable = str_first_name )
    text_first_name.grid(row=3, column=1)
    text_first_name.insert(0, "Person1")
    str_second_name = StringVar()
    lable_second_name = Label(frame, text="Отчество: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_second_name.grid(row=4, column=0)

    text_second_name = Entry(frame, font=("Comic Sans MS", 10), textvariable = str_second_name)
    text_second_name.grid(row=4, column=1)
    text_second_name.insert(0, "Person1")
    lable_gender = Label(frame, text="Пол: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_gender.grid(row=5, column=0)

    r_var = BooleanVar()
    r_var.set(0)

    mаn = Radiobutton(frame, text="Мужчина", font=("Comic Sans MS", 10), background="lavender", activebackground="lavender",  variable=r_var, value=0)
    mаn.grid(row=5, column=1)

    woman = Radiobutton(frame, text="Женщина", font=("Comic Sans MS", 10), background="lavender", activebackground="lavender", variable=r_var, value=1)
    woman.grid(row=5, column=2)

    lable_birthday = Label(frame, text="День рождения: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_birthday.grid(row=6, column=0)

    str_calendar = StringVar()
    calendar = DateEntry(frame, width=12,  background="RoyalBlue4", foreground="lavender", borderwidth=2,textvariable = str_calendar)
    calendar.grid(row=6, column=1)

    lable_telephone = Label(frame, text="Телефон: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_telephone.grid(row=7, column=0)

    str_telephone = StringVar()
    text_telephone = Entry(frame, font=("Comic Sans MS", 10), textvariable = str_telephone)
    text_telephone.grid(row=7, column=1)
    text_telephone.insert(0, "88005553535")
    lable_discipline = Label(frame, text="Дисциплина: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_discipline.grid(row=8, column=0)

    variable = StringVar(frame)
    variable.set(discipline[0])

    w = OptionMenu(frame, variable, *discipline)
    w.grid(row=8, column=1)

    lable_experience = Label(frame, text="Стаж: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_experience.grid(row=9, column=0)
    str_experience = StringVar()
    text_experience = Entry(frame, font=("Comic Sans MS", 10), textvariable = str_experience)
    text_experience.grid(row=9, column=1)
    text_experience.insert(0, "1")


def click_save_delete(frame, window,r_var):
    if len(person)!=0:
        person.pop(r_var.get())
        click_delete(frame, window)


def click_delete(frame, window):
    frame.destroy()
    frame = Frame(window)
    frame["bg"] = "lavender"
    frame.grid(row=0, column=0)
    back = Button(frame, text="Назад",
                  background="light steel blue",
                  foreground="RoyalBlue4",
                  padx="10",
                  pady="8",
                  font=("Comic Sans MS", 10),
                  command=lambda: click_back(frame, window))
    back.grid(row=0, column=0)
    save_delete = Button(frame, text="Удалить",
                  background="light steel blue",
                  foreground="RoyalBlue4",
                  padx="10",
                  pady="8",
                  font=("Comic Sans MS", 10),
                  command=lambda: click_save_delete(frame, window,r_var))
    save_delete.grid(row=0, column=1)

    r_var = IntVar()
    r_var.set(0)
    hat(0, 0, frame)
    radiobutton = []

    for i in range(len(person)):
            r = Radiobutton(frame, background="lavender", activebackground="lavender", variable=r_var, value=i)
            r.grid(row=i+2, column=0)
            body(i, 2, 0, frame)
            radiobutton.append(r)


def click_show(frame, window):
    frame.destroy()
    frame = Frame(window)
    frame["bg"] = "lavender"
    frame.grid(row=0, column=0)
    back = Button(frame, text="Назад",
                  background="light steel blue",
                  foreground="RoyalBlue4",
                  padx="10",
                  pady="8",
                  font=("Comic Sans MS", 10),
                  command=lambda: click_back(frame, window))
    back.grid(row=0, column=0)
    hat(0, -1, frame)

    for i in range(len(person)):
        body(i, 2, -1, frame)



def click_save_find(frame, window,variable):
    frame.destroy()
    frame = Frame(window)
    frame["bg"] = "lavender"
    frame.grid(row=0, column=0)
    back = Button(frame, text="Назад",
                  background="light steel blue",
                  foreground="RoyalBlue4",
                  padx="10",
                  pady="8",
                  font=("Comic Sans MS", 10),
                  command=lambda: click_back(frame, window))
    back.grid(row=0, column=0)
    hat(1, -1, frame)


    for i in range(len(person)):
        if(person[i].discipline == variable.get()):
            body(i, 3, -1, frame)


def click_find(frame, window):
    frame.destroy()
    frame = Frame(window)
    frame["bg"] = "lavender"
    frame.grid(row=0, column=0)
    back = Button(frame, text="Назад",
                  background="light steel blue",
                  foreground="RoyalBlue4",
                  padx="10",
                  pady="8",
                  font=("Comic Sans MS", 10),
                  command=lambda: click_back(frame, window))
    back.grid(row=0, column=0)
    save_find = Button(frame, text="Найти",
                         background="light steel blue",
                         foreground="RoyalBlue4",
                         padx="10",
                         pady="8",
                         font=("Comic Sans MS", 10),
                         command=lambda: click_save_find(frame, window, variable))
    save_find.grid(row=1, column=2)

    lable_discipline = Label(frame, text="Выберете дисциплину: ", font=("Comic Sans MS", 12), background="lavender",padx="20", pady="8", width=15, height=1)
    lable_discipline.grid(row=1, column=0)

    variable = StringVar(frame)
    variable.set(discipline[0])

    w = OptionMenu(frame, variable, *discipline)
    w.grid(row=1, column=1)


window = Tk()
window.title("Преподаватели")
window.geometry('1300x600')
window["bg"] = "lavender"
frame = Frame(window)
frame["bg"] = "lavender"
frame.pack()
click_back(frame, window)
window.mainloop()