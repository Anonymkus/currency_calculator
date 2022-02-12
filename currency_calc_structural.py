import tkinter as tk

# создаем окно - экземпляр Tk
window = tk.Tk()


def calculate_currency(rate):
    user_money = int(money_entry.get())
    rate = rate.get()
    result = round(user_money / rate, 2)
    result_label.config(text=result)


# параметры окна
window.title("Калькулятор валют")
window.geometry("500x200")

# радиокнопки принимают флоаты
rate = tk.DoubleVar()
rate.set(75.84)

# виджеты
money_label = tk.Label(window, text="введите сумму")
money_entry = tk.Entry(window)
cur_0 = tk.Radiobutton(window, text="доллар США", variable=rate, value=75.84)
cur_1 = tk.Radiobutton(window, text="евро", variable=rate, value=85.92)
cur_2 = tk.Radiobutton(
    window, text="кувейтский динар",
    variable=rate, value=250.82
)
cur_3 = tk.Radiobutton(
    window, text="иранский риал",
    variable=rate, value=0.0018
)
result_label = tk.Label(
    window,
    text="здесь появится результат"
)
calculate_button = tk.Button(
    window, text="посчитать",
    command=lambda: calculate_currency(rate)
)

# разместить все виджеты в окне
money_label.pack()
money_entry.pack()
cur_0.pack()
cur_1.pack()
cur_2.pack()
cur_3.pack()
calculate_button.pack()
result_label.pack()

# запустить главный цикл окна
window.mainloop()
