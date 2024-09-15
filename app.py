from tkinter import ttk

import my_calendar
import tkinter as tk
import calendar
import datetime


def calculate_tax(nuber_days, tax, loan, days_in_year):
    tax = tax * (2/3) / 100
    benefit = round((loan * tax * (nuber_days / days_in_year)), 2)
    result = round(benefit * 0.35, 2)
    return benefit, result


def get_days_in_year(date):
    days_in_year = (datetime.date(date.year, 12, 31) - datetime.date(date.year, 1, 1)).days + 1
    return days_in_year

def get_tax():
    days_in_month_start = calendar.monthrange(ttkcal1.selection.year, ttkcal1.selection.month)[1]
    date = ttkcal1.selection
    loan = int(entry_loan.get())
    part = loan / int(entry_period.get())
    benefit, ndfl = calculate_tax((days_in_month_start - int(date.day) + 1), int(entry_tax.get()), loan, get_days_in_year(date))

    text = f"Месяц - {date.month},\nДней пользования заемными средствами: {days_in_month_start - int(date.day) + 1},"\
                 f"\nМатериальная выгода: {int(entry_tax.get()) / 100} * 2/3 * {loan} *"\
                 f" {days_in_month_start - int(date.day) + 1}/{get_days_in_year(date)} = {benefit}"\
                 f"\nНалог: {ndfl}"
    for next_month in range(int(entry_period.get()) - 1):
        if date.month != 12:
            date = date.replace(month=date.month + 1)
        else:
            date = date.replace(month=1, year=date.year + 1)

        if next_month == int(entry_period.get()) - 2:
            days_in_month = ttkcal1.selection.day
        else:
            days_in_month = calendar.monthrange(date.year, date.month)[1]

        loan -= part
        benefit, ndfl = calculate_tax((days_in_month), int(entry_tax.get()),
                                      loan, get_days_in_year(date))
        text += (f"\n\n"
                 f"Месяц - {date.month},\nДней пользования заемными средствами: {days_in_month},"
                       f"\nМатериальная выгода: {int(entry_tax.get()) / 100} * 2/3 * {loan} *'"
                       f"{days_in_month}/{get_days_in_year(date)} = {benefit}"
                       f"\nНалог: {ndfl}")



    info_root = tk.Tk()
    info_root.title("Расчет налога")
    info_root.geometry("520x600")
    editor = tk.Text(info_root, width=520, height=600)
    editor.pack()
    editor.insert(index="1.0", chars=text)
    info_root.mainloop()

    return



#окно
root = tk.Tk()
root.title("Расчет налога")
root.geometry("520x450")


label_tax = tk.Label(root, text="Ключевая ставка ЦБ")
entry_tax = tk.Entry(root,)
label_tax.pack(side='top')
entry_tax.pack(side='top')

label_loan = tk.Label(root, text="Сумма займа")
entry_loan = tk.Entry(root,)
label_loan.pack(side='top')
entry_loan.pack(side='top')

frame1 = tk.Frame(root)
# Add Calendar
label1 = tk.Label(frame1, text="Дата заключения договора заема")
label1.grid(row=0, column=0)
ttkcal1 = my_calendar.TtkCalendar(frame1)
ttkcal1.grid(row=1, column=0)

label_period = tk.Label(frame1, text="Срок займа")
entry_period = tk.Entry(frame1)
label_period.grid(row=2, column=0)
entry_period.grid(row=3, column=0)

frame1.pack()

button = tk.Button(root, text="Расчет", width=5, command=get_tax)
button.pack(pady=5)

root.mainloop()