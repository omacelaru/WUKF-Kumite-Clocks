###########
#  author: Octavian - Andrei Macelaru
###########


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# setting tkinter window size
root.geometry("%dx%d" % (width, height))
root.title("WUKF Kumite Clocks")
root.iconbitmap("./images/logo.ico")

atenai = ["", "A", "ACH", "AH"]
atenai_white_string = StringVar()
atenai_red_string = StringVar()
atenai_white_number = 0
atenai_red_number = 0
kinshi = ["", "K1", "K2", "KCH", "KH"]
kinshi_white_string = StringVar()
kinshi_red_string = StringVar()
kinshi_white_number = 0
kinshi_red_number = 0
update_time = "after#0"
font_ = "Arial"
score_font = ("Arial", 320, 'bold')
button_root_font = ("Arial", 18, 'bold')
kumite_font = ("Arial", 13)
decision_font = (font_, 38, 'bold')


def decision(decis, operator, color, number):
    global atenai_red_number, atenai_white_number, atenai, kinshi_red_number, kinshi_white_number, kinshi, running
    ok = 1
    if decis == "atenai":
        if operator == "+":
            if number == 3:
                ok = 0
            number += 1
        elif operator == "-":
            if number == 0:
                ok = 0
            number -= 1
        if ok == 1:
            if color == "white":
                atenai_white_number = number
                atenai_white_string.set(atenai[number])

                if number == 3:
                    stopwatch_label.after_cancel(update_time)
                    stopwatch_label_second.after_cancel(update_time)
                    running = False
                    pygame.mixer.music.load("sound_end.mp3")
                    pygame.mixer.music.play()
                    messagebox.showinfo(title="End", message="Aka Wins")


            elif color == "red":
                atenai_red_number = number
                atenai_red_string.set(atenai[number])
                if number == 3:
                    stopwatch_label.after_cancel(update_time)
                    stopwatch_label_second.after_cancel(update_time)
                    running = False
                    pygame.mixer.music.load("sound_end.mp3")
                    pygame.mixer.music.play()
                    messagebox.showinfo(title="End", message="Shiro Wins")
    elif decis == "kinshi":
        if operator == "+":
            if number == 4:
                ok = 0
            number += 1
        elif operator == "-":
            if number == 0:
                ok = 0
            number -= 1
        if ok == 1:
            if color == "white":
                kinshi_white_number = number
                kinshi_white_string.set(kinshi[number])
                if number == 4:
                    stopwatch_label.after_cancel(update_time)
                    stopwatch_label_second.after_cancel(update_time)
                    running = False
                    pygame.mixer.music.load("sound_end.mp3")
                    pygame.mixer.music.play()
                    messagebox.showinfo(title="End", message="Aka Wins")
            elif color == "red":
                kinshi_red_number = number
                kinshi_red_string.set(kinshi[number])
                if number == 4:
                    stopwatch_label.after_cancel(update_time)
                    stopwatch_label_second.after_cancel(update_time)
                    running = False
                    pygame.mixer.music.load("sound_end.mp3")
                    pygame.mixer.music.play()
                    messagebox.showinfo(title="End", message="Shiro Wins")


white_score = 0
red_score = 0
point = [-1, 1, -2, 2]
Maxpoints = 6
str_white_score = StringVar()
str_white_score.set("0")
str_red_score = StringVar()
str_red_score.set("0")


def points(crt, color):
    global white_score, red_score, point, Maxpoints, running
    if color == "white":
        if white_score + point[crt] >= 0 and white_score + point[crt] <= Maxpoints + 1:
            white_score += point[crt]
            if white_score >= Maxpoints:
                white_score = Maxpoints
                str_white_score.set(str(white_score))

                stopwatch_label.after_cancel(update_time)
                stopwatch_label_second.after_cancel(update_time)
                running = False
                pygame.mixer.music.load("sound_end.mp3")
                pygame.mixer.music.play()
                messagebox.showinfo(title="End", message="Shiro Wins")
                reset()
            else:
                str_white_score.set(str(white_score))
    elif color == "red":
        if red_score + point[crt] >= 0 and red_score + point[crt] <= Maxpoints + 1:
            red_score += point[crt]
            if red_score >= Maxpoints:
                red_score = Maxpoints
                str_red_score.set(str(red_score))

                stopwatch_label.after_cancel(update_time)
                stopwatch_label_second.after_cancel(update_time)
                running = False
                pygame.mixer.music.load("sound_end.mp3")
                pygame.mixer.music.play()
                messagebox.showinfo(title="End", message="Aka Wins")
                reset()
            else:
                str_red_score.set(str(red_score))


# KINSHI WHITE
kinshi_white_button_plus = Button(root, text="K+", font=button_root_font, width=6, height=3,
                                  command=lambda: decision("kinshi", "+", "white", kinshi_white_number)).grid(row=0,
                                                                                                              column=0)
kinshi_white_button_minus = Button(root, text="K-", width=6, height=3, font=button_root_font,
                                   command=lambda: decision("kinshi", "-", "white", kinshi_white_number)).grid(row=1,
                                                                                                               column=0)

kinshi_white_label = Label(root, width=4, height=3, bg="lightgray", font=decision_font,
                           textvariable=kinshi_white_string).grid(row=0, column=1, rowspan=2, padx=5)

# ATENAI WHITE
atenai_white_button_plus = Button(root, text="A+", width=6, height=3, font=button_root_font,
                                  command=lambda: decision("atenai", "+", "white", atenai_white_number)).grid(
    row=2, column=0)
atenai_white_button_minus = Button(root, text="A-", width=6, height=3, font=button_root_font,
                                   command=lambda: decision("atenai", "-", "white", atenai_white_number)).grid(
    row=3, column=0)
atenai_white_label = Label(root, width=4, height=3, bg="lightgray", font=decision_font,
                           textvariable=atenai_white_string).grid(row=2, column=1, rowspan=2)

# SCOR WHITE
score_white_label = Label(root, font=score_font, textvariable=str_white_score).grid(row=0, column=3, rowspan=4,
                                                                                    columnspan=4)
score_white_minus_1 = Button(root, text="-1", width=4, height=2, font=button_root_font,
                             command=lambda: points(0, "white")).grid(row=4, column=3, padx=5)
score_white_plus_1 = Button(root, text="+1", width=4, height=2, font=button_root_font,
                            command=lambda: points(1, "white")).grid(row=4, column=4, padx=5)
score_white_minus_2 = Button(root, text="-2", width=4, height=2, font=button_root_font,
                             command=lambda: points(2, "white")).grid(row=4, column=5, padx=5)
score_white_plus_2 = Button(root, text="+2", width=4, height=2, font=button_root_font,
                            command=lambda: points(3, "white")).grid(row=4, column=6, padx=5)

# LOGO
image1 = Image.open("./images/logo.jpg")
image1 = image1.resize((250, 250))
test = ImageTk.PhotoImage(image1)
img = Label(root, image=test).grid(row=0, column=7, rowspan=4)

# KINSHI RED
kinshi_red_button_plus = Button(root, text="K+", width=6, height=3, font=button_root_font,
                                command=lambda: decision("kinshi", "+", "red", kinshi_red_number)).grid(row=0,
                                                                                                        column=13,
                                                                                                        padx=(0, 270))
kinshi_red_button_minus = Button(root, text="K-", width=6, height=3, font=button_root_font,
                                 command=lambda: decision("kinshi", "-", "red", kinshi_red_number)).grid(row=1,
                                                                                                         column=13,
                                                                                                         padx=(0, 270))

kinshi_red_label = Label(root, width=4, height=3, bg="lightgray", fg="red", font=decision_font,
                         textvariable=kinshi_red_string).grid(row=0, column=12, rowspan=2)

# ATENAI RED
atenai_red_button_plus = Button(root, text="A+", width=6, height=3, font=button_root_font,
                                command=lambda: decision("atenai", "+", "red", atenai_red_number)).grid(
    row=2,
    column=13, padx=(0, 270))
atenai_red_button_minus = Button(root, text="A-", width=6, height=3, font=button_root_font,
                                 command=lambda: decision("atenai", "-", "red", atenai_red_number)).grid(
    row=3,
    column=13, padx=(0, 270))

atenai_red_label = Label(root, width=4, height=3, bg="lightgray", fg="red", font=decision_font,
                         textvariable=atenai_red_string).grid(row=2, column=12, rowspan=2)

# SCOR RED
score_red_label = Label(root, font=score_font, fg="red", textvariable=str_red_score).grid(row=0, column=8, rowspan=4,
                                                                                          columnspan=4)
score_red_minus_1 = Button(root, text="-1", width=4, height=2, font=button_root_font,
                           command=lambda: points(0, "red")).grid(row=4, column=8, padx=5)
score_red_plus_1 = Button(root, text="+1", width=4, height=2, font=button_root_font,
                          command=lambda: points(1, "red")).grid(row=4, column=9, padx=5)
score_red_minus_2 = Button(root, text="-2", width=4, height=2, font=button_root_font,
                           command=lambda: points(2, "red")).grid(row=4, column=10, padx=5)
score_red_plus_2 = Button(root, text="+2", width=4, height=2, font=button_root_font,
                          command=lambda: points(3, "red")).grid(row=4, column=11, padx=5)

# TIME
# ***** VARIABLES *****
# use a boolean variable to help control state of time (running or not running)
running = False
# time variables initially set to 0
minutes, seconds = 0, 0
str_minut_entry = StringVar()
str_second_entry = StringVar()
str_pause_play = StringVar()
str_pause_play.set("Pause")


# ***** NOTES ON GLOBAL *****
# global will be used to modify variables outside functions
# another option would be to use a class and subclass Frame

# ***** FUNCTIONS *****
# start, pause, and reset functions will be called when the buttons are clicked
# start function

def start(event):
    global minutes, seconds
    str_minut = str_minut_entry.get()
    str_second = str_second_entry.get()

    if str_minut.isdigit() and str_minut != '' and int(str_minut) >= 0 and int(
            str_minut) <= 59 and str_second.isdigit() and str_second != '' and int(
        str_second) >= 0 and int(str_second) <= 59:
        reset()
        minutes = int(str_minut_entry.get())
        seconds = int(str_second_entry.get())
        minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
        seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
        stopwatch_label.config(text=minutes_string + ':' + seconds_string)
        stopwatch_label_second.config(text=minutes_string + ':' + seconds_string)
        global running
        if not running:
            update()
            running = True


# pause function
def pause():
    global running, minutes, seconds, pause_inutil
    if minutes >= 0 and seconds > 0:
        if running:
            # cancel updating of time using after_cancel()
            stopwatch_label.after_cancel(update_time)
            stopwatch_label_second.after_cancel(update_time)
            str_pause_play.set("Play")
            running = False
        else:
            str_pause_play.set("Pause")
            running = True
            update()


# reset function
def reset():
    global running, str_white_score, str_red_score, kinshi_red_string, kinshi_white_string, atenai_white_string, atenai_red_string, white_score, red_score, atenai_white_number, atenai_red_number, kinshi_red_number, kinshi_white_number
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        stopwatch_label_second.after_cancel(update_time)
        running = False
    str_white_score.set("0")
    str_red_score.set("0")
    kinshi_white_string.set("")
    kinshi_red_string.set("")
    atenai_white_string.set("")
    atenai_red_string.set("")
    white_score = 0
    red_score = 0
    atenai_white_number = 0
    atenai_red_number = 0
    atenai_red_number = 0
    kinshi_white_number = 0
    str_pause_play.set("Pause")
    stopwatch_label.configure(fg="black")
    stopwatch_label_second.configure(fg="black")
    # set variables back to zero
    global minutes, seconds
    minutes, seconds = 0, 0
    # set label back to zero
    stopwatch_label.config(text='00:00')
    stopwatch_label_second.config(text='00:00')


pygame.mixer.init()


# update stopwatch function
def update():
    # update seconds with (addition) compound assignment operator
    global minutes, seconds, running
    seconds -= 1

    if minutes <= 0 and seconds <= 0:
        stopwatch_label.config(text='00:00')
        stopwatch_label_second.config(text='00:00')
        pygame.mixer.music.load("sound_end.mp3")
        pygame.mixer.music.play()
        messagebox.showerror(title="End", message="End of the match!")

        stopwatch_label.configure(fg="black")
        stopwatch_label_second.configure(fg="black")
        running = False
    else:
        if seconds == -1:
            minutes -= 1
            seconds = 59

        if minutes == 0 and seconds == 15:
            pygame.mixer.music.load("sound_atoshi.mp3")
            pygame.mixer.music.play()
            stopwatch_label.configure(fg="red")
            stopwatch_label_second.configure(fg="red")

        # format time to include leading zeros
        minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
        seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
        # update timer label after 1000 ms (1 second)
        stopwatch_label.config(text=minutes_string + ':' + seconds_string)
        stopwatch_label_second.config(text=minutes_string + ':' + seconds_string)

        # after each second (1000 milliseconds), call update function
        # use update_time variable to cancel or pause the time using after_cancel
        global update_time
        update_time = stopwatch_label.after(1000, update)


def kumitef(k):
    global Maxpoints, bg_color_sambon_kumite, bg_color_ippon_kumite, bg_color_nihon_kumite, minutes, seconds
    if minutes == 0 and seconds == 0:
        if k == 'ippon':
            Maxpoints = 2
            ippon_button.configure(bg="lightsalmon")
            sambon_button.configure(bg="lavender")
            nihon_button.configure(bg="lavender")
        elif k == "nihon":
            Maxpoints = 4
            ippon_button.configure(bg="lavender")
            sambon_button.configure(bg="lavender")
            nihon_button.configure(bg="lightsalmon")

        elif k == "sambon":
            Maxpoints = 6
            ippon_button.configure(bg="lavender")
            sambon_button.configure(bg="lightsalmon")
            nihon_button.configure(bg="lavender")


# ***** WIDGETS *****
time = Frame(root)
time.grid(row=5, column=3, columnspan=9)
# label to display time
stopwatch_label = Label(time, text='00:00', font=('Arial', 165))
stopwatch_label.grid(row=5, column=0, columnspan=13)
# start, pause, reset, quit button

setting = Frame(root, borderwidth=1, relief="solid")
setting.grid(row=5, column=9, columnspan=6, padx=20)
# L = Label(setting, text="  fdfsf").grid(row=5,column=15)
minut_entry = Entry(setting, textvariable=str_minut_entry, width=3, font=("Arial", 18)).grid(row=6, column=0, padx=5)
colon_label = Label(setting, text=":", font=("Arial", 16)).grid(row=6, column=1)
second_entry = Entry(setting, textvariable=str_second_entry, width=3, font=("Arial", 18)).grid(row=6, column=2, padx=5)

start_button = Button(setting, text='Start', font=('Arial', 20))
start_button.grid(row=6, column=4, padx=5, pady=10)
start_button.bind('<Double-Button-1>', start)
pause_button = Button(setting, textvariable=str_pause_play, width=5, font=('Arial', 20), command=pause)
pause_button.grid(row=6, column=5, padx=5)
reset_button = Button(setting, text='Reset', font=('Arial', 20), command=reset)
reset_button.grid(row=6, column=6, padx=5)
quit_button = Button(setting, text='Quit', font=('Arial', 20), command=root.quit)
quit_button.grid(row=6, column=7, padx=5)

bg_color_nihon_kumite = StringVar()
bg_color_sambon_kumite = StringVar()
bg_color_ippon_kumite = StringVar()
bg_color_ippon_kumite = "lavender"
bg_color_sambon_kumite = "lightsalmon"
bg_color_nihon_kumite = "lavender"
kumite = Frame(setting)
kumite.grid(row=8, column=0, columnspan=14)
nihon_button = Button(kumite, text="Nihon Kumite", font=kumite_font, bg=bg_color_nihon_kumite,
                      command=lambda: kumitef("nihon"))
nihon_button.grid(row=7, column=1, padx=5, pady=40)
sambon_button = Button(kumite, text="Sambon Kumite", font=kumite_font, bg=bg_color_sambon_kumite,
                       command=lambda: kumitef("sambon"))
sambon_button.grid(row=7, column=2, padx=5, pady=40)
ippon_button = Button(kumite, text="Ippon Kumite", font=kumite_font, bg=bg_color_ippon_kumite,
                      command=lambda: kumitef("ippon"))
ippon_button.grid(row=7, column=3, padx=5, pady=40)

###########
#  author: Octavian - Andrei Macelaru
###########
root_second = Toplevel()
root_second.geometry("%dx%d" % (width, height))
root_second.title("WUKF Kumite Clocks")
root_second.iconbitmap("./images/logo.ico")

score_font_second = ("Arial", 320, 'bold')
decision_font_second = (font_, 38, 'bold')

Label_space = Label(root_second, width=36).grid(row=0, column=0, rowspan=2)
kinshi_red_label_second = Label(root_second, width=4, height=3, bg="lightgray", fg="red", font=decision_font_second,
                                textvariable=kinshi_red_string).grid(row=0, column=1, padx=5)
atenai_red_label_second = Label(root_second, width=4, height=3, bg="lightgray", fg="red", font=decision_font_second,
                                textvariable=atenai_red_string).grid(row=1, column=1)
score_red_second = Label(root_second, font=score_font, fg="red", textvariable=str_red_score).grid(row=0, column=2,
                                                                                                  rowspan=2)
image2 = Image.open("logo_second.jpg")
image2 = image2.resize((250, 250))
test2 = ImageTk.PhotoImage(image2)
logo_second = Label(root_second, image=test2).grid(row=0, column=3, rowspan=2)
score_white_second = Label(root_second, font=score_font, textvariable=str_white_score).grid(row=0, column=4, rowspan=2)
kinshi_white_label_second = Label(root_second, width=4, height=3, bg="lightgray", font=decision_font_second,
                                  textvariable=kinshi_white_string).grid(row=0, column=5)
atenai_white_label_second = Label(root_second, width=4, height=3, bg="lightgray", font=decision_font_second,
                                  textvariable=atenai_white_string).grid(row=1, column=5)

time_second = Frame(root_second).grid(row=2, column=1, columnspan=5)
stopwatch_label_second = Label(root_second, text='00:00', font=('Arial', 165))
stopwatch_label_second.grid(row=2, column=1, columnspan=5)

root.mainloop()
