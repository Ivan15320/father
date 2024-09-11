import my_calendar
import tkinter as tk


#окно
root = tk.Tk()
root.title("Расчет налога")
root.geometry("520x450")


label_ = tk.Label(root, text="Ставка налога")
entry = tk.Entry(root,)
label.pack(side='top')
entry.pack(side='top')

frame1 = tk.Frame(root)
# Add Calendar
label1 = tk.Label(frame1, text="Дата заключения договора заема")
label1.grid(row=0, column=0)
ttkcal1 = my_calendar.TtkCalendar(frame1)
ttkcal1.grid(row=1, column=0)

label2 = tk.Label(frame1, text="Дата завершения договора заема")
label2.grid(row=0, column=1)
ttkcal2 = my_calendar.TtkCalendar(frame1)
ttkcal2.grid(row=1, column=1)

frame1.pack()




button = tk.Button(root, text="ок", width=50)
button.pack()

root.mainloop()