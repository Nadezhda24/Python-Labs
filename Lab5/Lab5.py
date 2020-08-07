from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk
from tkinter import filedialog as fd
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

    lable_record = Label(frame, text="Табельный номер", font=("Comic Sans MS", 10), background="lavender", padx="20",
                         pady="8", width=12, height=1, borderwidth=2, relief="groove")
    lable_record.grid(row=1+i, column=1+j)

    lable_name = Label(frame, text="Имя", font=("Comic Sans MS", 10), background="lavender", padx="20", pady="8",
                       width=8, height=1, borderwidth=2, relief="groove")
    lable_name.grid(row=1+i, column=2+j)

    lable_first_name = Label(frame, text="Фамилия", font=("Comic Sans MS", 10), background="lavender", padx="20",
                             pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_first_name.grid(row=1+i, column=3+j)

    lable_second_name = Label(frame, text="Отчество", font=("Comic Sans MS", 10), background="lavender", padx="20",
                              pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_second_name.grid(row=1+i, column=4+j)

    lable_gender = Label(frame, text="Пол", font=("Comic Sans MS", 10), background="lavender", padx="20", pady="8",
                         width=8, height=1, borderwidth=2, relief="groove")
    lable_gender.grid(row=1+i, column=5+j)

    lable_birthday = Label(frame, text="День рождения", font=("Comic Sans MS", 10), background="lavender", padx="20",
                           pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_birthday.grid(row=1+i, column=6+j)

    lable_telephone = Label(frame, text="Телефон", font=("Comic Sans MS", 10), background="lavender", padx="20",
                            pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_telephone.grid(row=1+i, column=7+j)

    lable_discipline = Label(frame, text="Дисциплина", font=("Comic Sans MS", 10), background="lavender", padx="20",
                             pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_discipline.grid(row=1+i, column=8+j)

    lable_experience = Label(frame, text="Стаж", font=("Comic Sans MS", 10), background="lavender", padx="20",
                             pady="8", width=8, height=1, borderwidth=2, relief="groove")
    lable_experience.grid(row=1+i, column=9+j)

def body(i,k,h, frame):
    record = Label(frame, text=str(person[i].record), font=("Comic Sans MS", 10), background="lavender",
                   padx="20",
                   pady="8", width=12, height=1, borderwidth=2, relief="groove")
    record.grid(row=i + k, column=1+h)

    name = Label(frame, text=str(person[i].name), font=("Comic Sans MS", 10), background="lavender", padx="20",
                 pady="8",
                 width=8, height=1, borderwidth=2, relief="groove")
    name.grid(row=i + k, column=2+h)

    first_name = Label(frame, text=str(person[i].first_name), font=("Comic Sans MS", 10), background="lavender",
                       padx="20",
                       pady="8", width=8, height=1, borderwidth=2, relief="groove")
    first_name.grid(row=i + k, column=3+h)

    second_name = Label(frame, text=str(person[i].second_name), font=("Comic Sans MS", 10), background="lavender",
                        padx="20",
                        pady="8", width=8, height=1, borderwidth=2, relief="groove")
    second_name.grid(row=i + k, column=4+h)

    gender = Label(frame, text=str(person[i].gender), font=("Comic Sans MS", 10), background="lavender", padx="20",
                   pady="8",
                   width=8, height=1, borderwidth=2, relief="groove")
    gender.grid(row=i + k, column=5+h)

    birthday = Label(frame, text=str(person[i].birthday), font=("Comic Sans MS", 10), background="lavender",
                     padx="20",
                     pady="8", width=8, height=1, borderwidth=2, relief="groove")
    birthday.grid(row=i + k, column=6+h)

    telephone = Label(frame, text=str(person[i].telephone), font=("Comic Sans MS", 10), background="lavender",
                      padx="20",
                      pady="8", width=8, height=1, borderwidth=2, relief="groove")
    telephone.grid(row=i + k, column=7+h)

    discipline = Label(frame, text=str(person[i].discipline), font=("Comic Sans MS", 10), background="lavender",
                       padx="20",
                       pady="8", width=8, height=1, borderwidth=2, relief="groove")
    discipline.grid(row=i + k, column=8+h)

    experience = Label(frame, text=str(person[i].experience), font=("Comic Sans MS", 10), background="lavender",
                       padx="20",
                       pady="8", width=8, height=1, borderwidth=2, relief="groove")
    experience.grid(row=i + k, column=9+h)

def click_show(frame, window):
    r_var = IntVar()
    r_var.set(0)
    hat(0, 0, frame)
    radiobutton = []

    for i in range(len(person)):
        r = Radiobutton(frame, background="lavender", activebackground="lavender", variable=r_var, value=i)
        r.grid(row=i + 2, column=0)
        body(i, 2, 0, frame)
        radiobutton.append(r)

def click_save(frame_lable, str_record, str_name, str_first_name, str_second_name, str_telephone, str_calendar, str_experience, variable, r_var):
    gender = ""
    if (r_var.get()):
        gender = "w"
    else:
        gender = "m"
    person.append(
        Teacher(str(str_record.get()), str(str_name.get()), str(str_first_name.get()), str(str_second_name.get()),
                str(gender), str(str_calendar.get()), str(str_telephone.get()), str(variable.get()),
                str(str_experience.get())))

    hint = Label(frame_lable, text="Запись дабавлена", font=("Comic Sans MS", 8), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=0, column=0)

def click_delete(frame_table, window, r_var):
    if len(person) != 0:
        person.pop(r_var.get())
    click_show(frame_table, window)

def click_find(frame_table, variable):
    hat(0, 0, frame_table)
    for i in range(len(person)):
        if (person[i].discipline == variable.get()):
            body(i, 2, 0, frame_table)

def click_allexit():
    window.destroy()

def click_info():
    mb.showinfo("Информация", "Информация о разработчике")

def click_new_record():
    text_record.delete(0, tk.END)
    text_name.delete(0, tk.END)
    text_first_name.delete(0, tk.END)
    text_second_name.delete(0, tk.END)
    text_telephone.delete(0, tk.END)
    text_experience.delete(0, tk.END)
    calendar.delete(0, tk.END)
    r_var.set(0)
    variable.set(discipline[0])


def click_open(frame_table):
    person.clear()
    f = open('text.txt')
    for line in f:
        teacher =line.split(" ")
        person.append(Teacher(str(teacher[0]),teacher[1],teacher[2],teacher[3],teacher[4],str(teacher[5]),str(teacher[6]),teacher[7],str(teacher[8])))
    click_show(frame_table, window)

def click_save():
    try:
        f = open('text.txt', 'x')
        file_name = fd.asksaveasfilename()
        f = open(file_name, 'w')
        for i in range(len(person)):
            f.write(str(person[i].record) + " " + person[i].name + " " + person[i].first_name + " " + person[
                i].second_name + " " + person[i].gender + " " + str(person[i].birthday) + " " + str(
                person[i].telephone) + " " + person[i].discipline + " " + str(person[i].experience) + "\n")
        f.close()
    except:
        f = open('text.txt', 'w')
        for i in range(len(person)):
            f.write(str(person[i].record) + " " + person[i].name + " " + person[i].first_name + " " + person[
                i].second_name + " " + person[i].gender + " " + str(person[i].birthday) + " " + str(
                person[i].telephone) + " " + person[i].discipline + " " + str(person[i].experience) + "\n")
        f.close()

def click_saveas():
    file_name = fd.asksaveasfilename()
    f = open(file_name, 'w')
    for i in range(len(person)):
        f.write(str(person[i].record) + " " + person[i].name + " " + person[i].first_name + " " + person[i].second_name + " " + person[i].gender + " " + str(person[i].birthday) + " " + str(person[i].telephone) + " " + person[i].discipline + " " + str(person[i].experience)+ "\n")
    f.close()

window = Tk()
window.title("Преподаватели")
window.geometry('1100x600')
window["bg"] = "lavender"

mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
helpmenu = Menu(mainmenu, tearoff=0)

filemenu.add_command(label="Создать",command=lambda: click_new_record())
filemenu.add_command(label="Открыть",command=lambda: click_open(frame_table))
filemenu.add_command(label="Сохранить",command=lambda: click_save())
filemenu.add_command(label="Сохранить как...", command=lambda: click_saveas())
filemenu.add_command(label="Выход", command=lambda: click_allexit())
helpmenu.add_command(label="Информация", command=lambda: click_info())
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

frame_lable = Frame(window)
frame_lable["bg"] = "lavender"
hint = Label(frame_lable, text="", font=("Comic Sans MS", 8), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=0, column=0)
frame_btn = Frame(window)
frame_btn["bg"] = "lavender"

frame_table = Frame()
frame_table["bg"] = "lavender"
frame_new_record = Frame(window)
frame_new_record["bg"] = "lavender"
frame_lable.pack()
frame_btn.pack()
frame_new_record.pack()
frame_table.pack()

create = Button(frame_btn, text="Добавление записи", background="light steel blue", foreground="RoyalBlue4", padx="20", pady="8", font=("Comic Sans MS", 10), command=lambda: click_save(frame_lable,str_record, str_name, str_first_name, str_second_name, str_telephone, str_calendar, str_experience, variable, r_var)).grid(row=0, column=0)
delete = Button(frame_btn, text="Удаление записи", background="light steel blue", foreground="RoyalBlue4", padx="20", pady="8", font=("Comic Sans MS", 10), command=lambda: click_delete(frame_table, window,r_var)).grid(row=0, column=1)
show = Button(frame_btn, text="Отобразить записи", background="light steel blue", foreground="RoyalBlue4", padx="20", pady="8", font=("Comic Sans MS", 10),  command=lambda: click_show(frame_table, window)).grid(row=0, column=2)
find = Button(frame_btn, text="Найти запись", background="light steel blue", foreground="RoyalBlue4", padx="20", pady="8", font=("Comic Sans MS", 10),command=lambda: click_find(frame_table,variable)).grid(row=0, column=3)

lable_record = Label(frame_new_record, text="Табельный номер: ", font=("Comic Sans MS", 10), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=0, column=0)
str_record = StringVar()
text_record = Entry(frame_new_record, font=("Comic Sans MS", 10), textvariable = str_record)
text_record.grid(row=0, column=1)
lable_name = Label(frame_new_record, text="Имя: ", font=("Comic Sans MS", 10), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=1, column=0)
str_name = StringVar()
text_name = Entry(frame_new_record, font=("Comic Sans MS", 10), textvariable = str_name)
text_name.grid(row=1, column=1)
str_first_name = StringVar()
lable_first_name = Label(frame_new_record, text="Фамилия: ", font=("Comic Sans MS", 10), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=2, column=0)
text_first_name = Entry(frame_new_record, font=("Comic Sans MS", 10), textvariable = str_first_name )
text_first_name.grid(row=2, column=1)
str_second_name = StringVar()
lable_second_name = Label(frame_new_record, text="Отчество: ", font=("Comic Sans MS", 10), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=3, column=0)
text_second_name = Entry(frame_new_record, font=("Comic Sans MS", 10), textvariable = str_second_name)
text_second_name.grid(row=3, column=1)
lable_gender = Label(frame_new_record, text="Пол: ", font=("Comic Sans MS", 10), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=4, column=0)
r_var = BooleanVar()
r_var.set(0)
mаn = Radiobutton(frame_new_record, text="Мужчина", font=("Comic Sans MS", 10), background="lavender", activebackground="lavender",  variable=r_var, value=0).grid(row=4, column=1)
woman = Radiobutton(frame_new_record, text="Женщина", font=("Comic Sans MS", 10), background="lavender", activebackground="lavender", variable=r_var, value=1).grid(row=4, column=2)
lable_birthday = Label(frame_new_record, text="День рождения: ", font=("Comic Sans MS", 10), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=5, column=0)
str_calendar = StringVar()
calendar = DateEntry(frame_new_record, width=12,  background="RoyalBlue4", foreground="lavender", borderwidth=2,textvariable = str_calendar)
calendar.grid(row=5, column=1)
lable_telephone = Label(frame_new_record, text="Телефон: ", font=("Comic Sans MS", 10), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=0, column=2)
str_telephone = StringVar()
text_telephone = Entry(frame_new_record, font=("Comic Sans MS", 10), textvariable = str_telephone)
text_telephone.grid(row=0, column=3)
lable_experience = Label(frame_new_record, text="Стаж: ", font=("Comic Sans MS", 10), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=1, column=2)
str_experience = StringVar()
text_experience = Entry(frame_new_record, font=("Comic Sans MS", 10), textvariable = str_experience)
text_experience.grid(row=1, column=3)
lable_discipline = Label(frame_new_record, text="Дисциплина: ", font=("Comic Sans MS", 10), background="lavender",padx="20", pady="8", width=15, height=1).grid(row=2, column=2)
variable = StringVar(frame_new_record)
variable.set(discipline[0])
w = OptionMenu(frame_new_record, variable, *discipline)
w.grid(row=2, column=3)
window.mainloop()
