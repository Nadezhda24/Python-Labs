Задания для изучения Python
=====================
Лабораторная работа №1 
----------------
Исходный код находится в папке Lab1

Задание:
1) Вычислить математическое выражение. 
2) Работа со списком элементов разных типов.
      * Показать значения списка на экране.
      * Добавить новый элемент в конец списка.
      * Удалить указанный элемент.
      * Сформировать кортеж, состоящий из вещественных положительных элементов списка. Вывести содержимое кортежа на экран.
      * Найти произведение всех целочисленных элементов списка.
      * Сформировать  строку  из  значений  элементов  списка. Посчитать  сколько  раз встречается в строке указанное пользователем слово.
      * Задать с клавиатуры множество M1, сформировать множество M2 из списка. Вывести на экран симметричную разницумножеств M1 и M2.
      * Получить  из  списка  словарь,  ключом  каждого  элемента  сделать  позицию  элемента  в словаре. 
        Построчно  отобразить  на  экране  элементы  словаря  с  нечетными  значениями ключа.                                                           
3) Вычисление площади фигур.
      * Площадь квадрата.
      * Площадь трапеции.
      * Площадь параллелограмма.
      
Не разрабатывать GUI.      

Лабораторная работа №2 
----------------
Исходный код находится в папке Lab2

Задание:
1) Вычислить математическое выражение.
2) Вычисление площади фигур. Входные  данные  задать  в  виде  одного  списка.  Программа  должна  обеспечить возможность вычислять площадь фигур до тех пор, пока в списке есть входные данные. 
      * Площадь квадрата.
      * Площадь трапеции.
      * Площадь параллелограмма.
      
Замечание: при  разработке  программы  не  использовать  управляющие  конструкции. Использовать функции первого класса и высшего порядка  

Не разрабатывать GUI.

Лабораторная работа №3 
----------------
Исходный код находится в папке Lab3

Разработать класс "Преподаватель" с полями: табельный номер, фамилия, имя, отчество, пол, дата рождения, адрес, телефон, дисциплина, стаж

Меню программы:
1. добавление информации в список (разработать конструктор с произвольным количеством параметром);
2. удаление информации о выбранном объекте списка;
3. отображение информации обо всех объектах списка в удобном виде;
4. поиск преподавателей преподающих указанную дисциплину.

Не разрабатывать GUI.

Лабораторная работа №4
----------------
Исходный код находится в папке Lab4

Разработать и реализовать графический интерфейс для лабораторной №3 

Лабораторная работа №5
----------------
Исходный код находится в папке Lab5

В  программу  лабораторной  работы №4 добавить  главное  меню  с  пунктами «Файл», «Справка».

Пункт  главного  меню  «Файл»  должен  включать  подпункты:
* «Создать»  (очистка формы  для  ввода  новых  данных)
* «Открыть»  (считывание  из  файла информацииобобъектах  и  отображение  её  на  форме)
* «Сохранить»  (обновление  текущего  файла;  если файл не создан, то действия пункта «Сохранить как...»)
* «Сохранить как...» (сохранение информации об объектахв файл по указанному пути)
* «Выход» (дружественный выход из программы). 

Пункт главного меню «Справка» должен показывать информацию о разработчике программы.

Лабораторная работа №6
----------------
Исходный код находится в папке Lab6

Разработать клиент-серверное приложение для обработки текста.

Требования к клиенту:
1. отправка на сервер введенного пользователем текста;
2. получение обработанного сервером текста;
3. удобный графический интерфейс.

Требования к серверу:
1. обработка полученного текста по следующим правилам: 
     * перед запятой не может быть пробела;
     * после запятой должен стоять один пробел;
     * не могут стоять подряд две запятые;
     * текст не может начинаться с запятой.

Лабораторная работа №7
----------------
Исходный код находится в папке Lab7

Разработать приложение, взаимодействующее с базой данных. Приложение  должно  иметь  удобный  графический  интерфейс. Разработать БД "Преподаватели". База данных должна состоять из 2-3 связанных таблиц; одна таблица основная. 

Функционал приложения:
* добавление информации в основную таблица;
* удалении информации из основной таблицы;
* отображение информации из основнойтаблицы.

Добавление и отображение информации должно бытьреализованов читаемой для пользователяформе.

Лабораторная работа №8
----------------
Исходный код находится в папке Lab8

Разработать Web-приложение, взаимодействующее с базой данных. Приложение  должно  иметь  удобный  графический интерфейс. Разработать БД "Преподаватели". База данных должна состоять из 2-3 связанных таблиц; одна таблица основная. 

Функционал приложения:
* добавление информации в основную таблица;
* удалении информации из основной таблицы;
* отображение информации из основнойтаблицы.

Добавление и отображение информации должно бытьреализованов читаемой для пользователяформе.

Запуск :

* Скачать всю папку с проектом
* Перейти из консоли в папку lab8
* Выполнить команду `pip install Django==1.9.1.`
* Выполнить команду `pip install django-crispy-forms`
* Выполнить команду `python manage.py runserver`
* перейти по адресу ссылки 
