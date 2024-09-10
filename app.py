import my_calendar
import tkinter as tk


#окно
root = tk.Tk()
root.title("Расчет налога")
root.geometry("800x450")

label = tk.Label(text="Ставка налога")
entry = tk.Entry()
label.pack()
entry.pack()

# Add Calendar
ttkcal = my_calendar.TtkCalendar()
ttkcal.pack()

def callback():
    print(entry.get())
    print(ttkcal.selection)


button = tk.Button(text="ок", command=callback)
button.pack()

root.mainloop()