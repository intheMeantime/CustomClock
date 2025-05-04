import tkinter as tk
import time
import random

# defult == clock
showing_clock = True
# random text set
quotes = [
    "\nTime is Gold",
    "\nSee you another life",
    "\nIn the Meantime?",
    "\nEvery passing minute..",
    "\nWake up!"
]

def update_time():
    if showing_clock:
        now = time.localtime()
        current_time = time.strftime("%H:%M:%S", now)
        current_date = time.strftime("%Y-%m-%d", now)
        
        clock_label.config(text=current_time,
            font=("Helvetica Neue", 40),
            fg="#FFFFFF"
        )
        date_label.config(
            text=current_date,
            font=("Helvetica Neue", 15),
            fg="#999999"
    )
    
    # update every 200ms (to be smooth..)
    clock_label.after(200, update_time)


def toggle_display(event):
    global showing_clock
    showing_clock = not showing_clock
    
    if not showing_clock:
        # random select
        random_quote = random.choice(quotes)
        clock_label.config(
            text=random_quote,
            font=("Courier New", 20, 'bold'),
            fg="#ba9604",
            wraplength=200,  # auto line-break
            justify="center"
        )
        date_label.config(text="")
    else:
        update_time()



'''
# Initial color brightness control variable
brightness = 0
increasing = True  # Whether the brightness is increasing?
def animate_blink():
    global brightness, increasing

    if increasing:
        brightness += 5
        if brightness >= 100:
            increasing = False
    else:
        brightness -= 5
        if brightness <= 0:
            increasing = True

    # Change text color according to brightness (mint color series)
    color_value = int(170 + (brightness * 0.85))  # 170~255
    hex_color = f"#{0:02X}{255:02X}{color_value:02X}"  # R=0, G=255, B={change}

    clock_label.config(fg=hex_color)

    clock_label.after(100, animate_blink)  # change every 0.1s
'''



# main window
root = tk.Tk()
root.title("Time is Gold?")

# window setting
root.geometry("250x110")
root.configure(bg="#323232")
root.resizable(False, False)

# TIME
clock_label = tk.Label(
    root,
    font=("Helvetica Neue", 40),
    fg="#FFFFFF"
)
clock_label.pack(pady=(10, 5))  # white space (up, down)

# DATE
date_label = tk.Label(
    root,
    font=("Helvetica Neue", 15),
    fg="#999999"
)
date_label.pack()

# click event binding
root.bind("<Button-1>", toggle_display)  # if click the left mouse, toggle_display called

update_time()
#animate_blink()
root.mainloop()