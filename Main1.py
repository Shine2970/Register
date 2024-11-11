import tkinter as tk
from tkinter import messagebox
import sqlite3


# Создание базы данных и таблицы пользователей
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


# Регистрация нового пользователя
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


# Авторизация пользователя
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


# Окно регистрации
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


# Основное окно
root = tk.Tk()
root.title("Авторизация")

create_db()

tk.Label(root, text="Логин").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Пароль").pack(pady=5)
entry_password = tk.Entry(root, show='*')
entry_password.pack(pady=5)

tk.Button(root, text="Авторизация", command=lambda: authorize_user(entry_username.get(), entry_password.get())).pack(
    pady=10)
tk.Button(root, text="Регистрация", command=open_registration_window).pack(pady=5)

root.mainloop()
