# Register
Импорт необходимых библиотек:

import tkinter as tk
from tkinter import messagebox
import sqlite3
Здесь мы импортируем библиотеку tkinter для создания графического интерфейса, messagebox для отображения сообщений пользователю и sqlite3 для работы с базой данных SQLite.

Создание базы данных и таблицы пользователей:

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
Функция create_db создает базу данных users.db и таблицу users, если она еще не существует. Таблица имеет три поля: id, username и password.

Регистрация нового пользователя:

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
Функция register_user принимает имя пользователя и пароль, добавляет их в базу данных и обрабатывает возможные ошибки, такие как попытка зарегистрировать пользователя с уже существующим именем.

Авторизация пользователя:

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
Функция authorize_user проверяет, существует ли пользователь с введенными логином и паролем. Если да, отображается сообщение об успешной авторизации, иначе — сообщение об ошибке.

Окно регистрации:

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
Эта функция создает новое окно для регистрации, где пользователь может ввести свои данные. Кнопка "Регистрация" вызывает функцию register_user.

Основное окно приложения:

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
Здесь создается основное окно приложения, в котором пользователь может вводить свои данные для авторизации или открыть окно регистрации. root.mainloop() запускает главный цикл приложения, позволяя ему реагировать на действия пользователя.
