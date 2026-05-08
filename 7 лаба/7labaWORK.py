import tkinter as tk
from tkinter import scrolledtext, messagebox
import itertools
import random
import time

# Функция запуска программы

def run_program():
    output.delete(1.0, tk.END)

    try:
        K = int(entry_k.get())
        T = int(entry_t.get())

        if K < 3:
            messagebox.showerror("Ошибка", "Количество музыкантов должно быть не меньше 3")
            return

        if T <= 0:
            messagebox.showerror("Ошибка", "Количество типов инструментов должно быть больше 0")
            return

    except ValueError:
        messagebox.showerror("Ошибка", "Введите целые числа")
        return

    musicians = []

    
    for i in range(K):
        instrument_type = (i % T) + 1
        skill = random.randint(1, 10)

        musicians.append((i + 1, instrument_type, skill))

    output.insert(tk.END, "=== Музыканты ===\n\n")

    for m in musicians:
        output.insert(
            tk.END,
            f"Музыкант {m[0]} — тип {m[1]} — мастерство {m[2]}\n"
        )
    
    filtered_musicians = []

    for m in musicians:
        if m[2] >= 5:
            filtered_musicians.append(m)

    output.insert(tk.END, "\n=== Прошедшие отбор ===\n\n")

    for m in filtered_musicians:
        output.insert(tk.END, f"Музыкант {m[0]}\n")

    # Алгоритмический способ

    start1 = time.perf_counter()

    trios_algo = []

    N = len(filtered_musicians)

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):

                trio = (
                    filtered_musicians[i],
                    filtered_musicians[j],
                    filtered_musicians[k]
                )

                trios_algo.append(trio)

    end1 = time.perf_counter()

    output.insert(tk.END, "\n=== Алгоритмический способ ===\n\n")

    for trio in trios_algo:
        output.insert(tk.END, f"{trio}\n")

    output.insert(
        tk.END,
        f"\nКоличество трио: {len(trios_algo)}\n"
    )

    output.insert(
        tk.END,
        f"Время выполнения: {end1 - start1:.6f} сек\n"
    )

    # Способ itertools
   
    start2 = time.perf_counter()

    trios_func = list(itertools.combinations(filtered_musicians, 3))

    end2 = time.perf_counter()

    output.insert(tk.END, "\n=== Способ itertools ===\n\n")

    for trio in trios_func:
        output.insert(tk.END, f"{trio}\n")

    output.insert(
        tk.END,
        f"\nКоличество трио: {len(trios_func)}\n"
    )

    output.insert(
        tk.END,
        f"Время выполнения: {end2 - start2:.6f} сек\n"
    )

    # Сравнение времени

    output.insert(tk.END, "\n=== Сравнение ===\n\n")

    if (end1 - start1) < (end2 - start2):
        output.insert(tk.END, "Алгоритмический способ быстрее.\n")
    elif (end1 - start1) > (end2 - start2):
        output.insert(tk.END, "Способ itertools быстрее.\n")
    else:
        output.insert(tk.END, "Время выполнения одинаковое.\n")


# Создание окна

root = tk.Tk()
root.title("Генератор музыкальных трио")
root.geometry("900x700")

# Поля ввода

label_k = tk.Label(root, text="Количество музыкантов:")
label_k.pack()

entry_k = tk.Entry(root)
entry_k.pack()

label_t = tk.Label(root, text="Количество типов инструментов:")
label_t.pack()

entry_t = tk.Entry(root)
entry_t.pack()

# Кнопка

run_button = tk.Button(
    root,
    text="Запустить программу",
    command=run_program
)

run_button.pack(pady=10)

# Окно вывода со скроллингом

output = scrolledtext.ScrolledText(
    root,
    width=110,
    height=35
)

output.pack(padx=10, pady=10)

# Запуск GUI

root.mainloop()
