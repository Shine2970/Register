1. Импорт библиотек:
   
   import tkinter as tk
   from tkinter import messagebox
   import sqlite3
   
  tkinter: библиотека для создания графических интерфейсов в Python.
   messagebox: модуль из tkinter, который позволяет выводить всплывающие сообщения пользователю.
   sqlite3: библиотека для работы с базами данных SQLite.

2. Создание базы данных:
   
   def create_db():
       conn = sqlite3.connect('users.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               username TEXT UNIQUE,
               password TEXT
           )
       ''')
       conn.commit()
       conn.close()
   
   Функция создает базу данных users.db и таблицу users, если она не существует.
   Таблица имеет три колонки: id, username (логин, уникальный) и password (пароль).

3. Регистрация пользователя:

   def register_user(username, password):
       conn = sqlite3.connect('users.db')
       cursor = conn.cursor()
       try:
           cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
           conn.commit()
           messagebox.showinfo("Успех", "Пользователь успешно зарегистрирован!")
       except sqlite3.IntegrityError:
           messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует.")
       finally:
           conn.close()
   
   Функция принимает логин и пароль, добавляет их в базу данных.
   Если логин уже существует, пользователю выводится сообщение об ошибке.
   В случае успешной регистрации появляется всплывающее сообщение о результате.

4. Авторизация пользователя:

     def authorize_user(username, password):
       conn = sqlite3.connect('users.db')
       cursor = conn.cursor()
       cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
       user = cursor.fetchone()
       conn.close()

    if user:
           messagebox.showinfo("Успех", "Вы успешно авторизованы!")
       else:
           messagebox.showerror("Ошибка", "Неверный логин или пароль.")
   
   Функция проверяет наличие логина и пароля в базе данных.
   Если найден соответствующий пользователь, выводится сообщение об успешной авторизации.
   В противном случае показывается сообщение об ошибке.

6. Открытие окна регистрации:
   
   def open_registration_window():
    reg_window = tk.Toplevel(root)
    reg_window.title("Регистрация")

    tk.Label(reg_window, text="Логин").pack(pady=5)
    username_entry = tk.Entry(reg_window)
    username_entry.pack(pady=5)

    tk.Label(reg_window, text="Пароль").pack(pady=5)
    password_entry = tk.Entry(reg_window, show='*')
    password_entry.pack(pady=5)

    tk.Button(reg_window, text="Регистрация",
              command=lambda: register_user(username_entry.get(), password_entry.get())).pack(pady=10)

   Функция создает новое окно для регистрации пользователя.
   В этом окне находятся поля для ввода логина и пароля, а также кнопка для регистрации, которая вызывает функцию register_user().

8. Главное окно приложения:
   
   root = tk.Tk()
   root.title("Авторизация")

   create_db()

   tk.Label(root, text="Логин").pack(pady=5)
   entry_username = tk.Entry(root)
   entry_username.pack(pady=5)

   tk.Label(root, text="Пароль").pack(pady=5)
   entry_password = tk.Entry(root, show='*')
   entry_password.pack(pady=5)

   tk.Button(root, text="Авторизация", command=lambda: authorize_user(entry_username.get(), entry_password.get())).pack(pady=10)
   tk.Button(root, text="Регистрация", command=open_registration_window).pack(pady=5)

   root.mainloop()
 
Создается основное окно приложения, в котором размещены поля для ввода логина и пароля, а также кнопки для авторизации и открытия окна регистрации.
root.mainloop() запускает главный цикл приложения, позволяя ему ждать и обрабатывать пользовательский ввод.
