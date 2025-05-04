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
    
    # update per 200ms (for smooth..)
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
            wraplength=200,  # 가로 200px 넘으면 자동으로 줄바꿈 함
            justify="center"  # 가운데 정렬
        )
        date_label.config(text="")
    else:
        # 다시 시계 보여주기
        update_time()



'''
# 초기 색깔 밝기 조절 변수
brightness = 0
increasing = True  # 밝기 증가 중인지 여부
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

    # 밝기에 따라 글자 색 변경 (민트색 계열)
    color_value = int(170 + (brightness * 0.85))  # 170~255 범위
    hex_color = f"#{0:02X}{255:02X}{color_value:02X}"  # R=0, G=255, B=변화

    clock_label.config(fg=hex_color)

    clock_label.after(100, animate_blink)  # 0.1초마다 변경
'''



# main window
root = tk.Tk()
root.title("Time is Gold?")

# window setting
root.geometry("250x110")
root.configure(bg="#323232")
root.resizable(False, False)

# CLOCK
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

# 클릭 이벤트 바인딩
root.bind("<Button-1>", toggle_display)  # if click the left mouse, toggle_display called

update_time()
#animate_blink()
root.mainloop()