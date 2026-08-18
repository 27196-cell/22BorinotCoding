from datetime import datetime
import calendar
import winsound
import tkinter as tk
from tkinter import messagebox


# =========================
# Settings
# =========================

year = datetime.now().year
homework_list = []


# =========================
# Main Window
# =========================

root = tk.Tk()
root.title("StudyCal")
root.geometry("430x780")
root.resizable(False, False)
root.configure(bg="#F5F3FF")


# =========================
# Functions
# =========================

def add_homework():

    subject = subject_entry.get()
    month_text = month_entry.get()
    day_text = day_entry.get()

    if subject == "" or month_text == "" or day_text == "":
        messagebox.showerror(
            "Missing information",
            "Please enter the subject, month and day."
        )
        return

    try:

        month = int(month_text)
        target_day = int(day_text)

        # Check if date is valid
        target_time = datetime(
            year,
            month,
            target_day
        )

        homework = {
            "subject": subject,
            "month": month,
            "day": target_day,
            "date": target_time
        }

        homework_list.append(homework)

        subject_entry.delete(
            0,
            tk.END
        )

        month_entry.delete(
            0,
            tk.END
        )

        day_entry.delete(
            0,
            tk.END
        )

        update_calendar()
        update_homework()

        check_time(homework)

    except ValueError:

        messagebox.showerror(
            "Invalid date",
            "Please enter a valid month and day."
        )


def update_calendar():

    calendar_text.config(
        state=tk.NORMAL
    )

    calendar_text.delete(
        "1.0",
        tk.END
    )

    if homework_list:
        month = homework_list[-1]["month"]
    else:
        month = datetime.now().month

    month_name = calendar.month_name[month]

    calendar_text.insert(
        tk.END,
        f"{month_name} {year}\n\n"
    )

    calendar_text.insert(
        tk.END,
        " Mo   Tu   We   Th   Fr   Sa   Su\n"
    )

    calendar_text.insert(
        tk.END,
        "──────────────────────────────\n"
    )

    cal = calendar.monthcalendar(
        year,
        month
    )

    homework_days = []

    for homework in homework_list:

        if homework["month"] == month:
            homework_days.append(
                homework["day"]
            )

    for week in cal:

        for day in week:

            if day == 0:

                calendar_text.insert(
                    tk.END,
                    "     "
                )

            elif day in homework_days:

                calendar_text.insert(
                    tk.END,
                    f" [{day:2}]",
                    "deadline"
                )

            else:

                calendar_text.insert(
                    tk.END,
                    f" {day:2} "
                )

        calendar_text.insert(
            tk.END,
            "\n"
        )

    calendar_text.config(
        state=tk.DISABLED
    )


def update_homework():

    for widget in homework_container.winfo_children():
        widget.destroy()

    if len(homework_list) == 0:

        empty_label = tk.Label(
            homework_container,
            text="No homework yet 📚",
            font=("Arial", 13),
            bg="#F5F3FF",
            fg="#888888"
        )

        empty_label.pack(
            pady=15
        )

        return

    # Sort by date
    homework_list.sort(
        key=lambda x: x["date"]
    )

    for homework in homework_list:

        create_homework_card(
            homework
        )


def create_homework_card(homework):

    card = tk.Frame(
        homework_container,
        bg="white",
        height=75
    )

    card.pack(
        fill="x",
        pady=5
    )

    card.pack_propagate(False)


    # Icon
    icon = tk.Label(
        card,
        text="📚",
        font=("Arial", 20),
        bg="white"
    )

    icon.place(
        x=15,
        y=17
    )


    # Subject
    subject_label = tk.Label(
        card,
        text=homework["subject"],
        font=("Arial", 14, "bold"),
        bg="white",
        fg="#29263D"
    )

    subject_label.place(
        x=55,
        y=12
    )


    # Date
    date_label = tk.Label(
        card,
        text=f"Due: "
             f"{calendar.month_abbr[homework['month']]} "
             f"{homework['day']}",
        font=("Arial", 11),
        bg="white",
        fg="#888888"
    )

    date_label.place(
        x=55,
        y=40
    )


    # DUE badge
    badge = tk.Label(
        card,
        text="DUE",
        font=("Arial", 9, "bold"),
        bg="#E9E2FF",
        fg="#5B43E6",
        padx=8,
        pady=4
    )

    badge.place(
        relx=1.0,
        x=-15,
        y=25,
        anchor="e"
    )


def check_time(homework):

    now = datetime.now()

    if now >= homework["date"]:

        winsound.Beep(
            700,
            2000
        )

        messagebox.showinfo(
            "StudyCal Reminder",
            f"Your homework is due!\n\n"
            f"📚 {homework['subject']}"
        )

    else:

        root.after(
            60000,
            lambda: check_time(homework)
        )


# =========================
# Header
# =========================

header = tk.Frame(
    root,
    bg="#F5F3FF"
)

header.pack(
    fill="x",
    padx=25,
    pady=(25, 0)
)


logo = tk.Label(
    header,
    text="StudyCal",
    font=("Arial", 27, "bold"),
    bg="#F5F3FF",
    fg="#5B43E6"
)

logo.pack(
    side="left"
)


add_button = tk.Button(
    header,
    text="+",
    font=("Arial", 20, "bold"),
    bg="#5B43E6",
    fg="white",
    activebackground="#4933C5",
    activeforeground="white",
    bd=0,
    width=3,
    height=1,
    command=lambda: subject_entry.focus()
)

add_button.pack(
    side="right"
)


subtitle = tk.Label(
    root,
    text="Never miss a homework due date",
    font=("Arial", 11),
    bg="#F5F3FF",
    fg="#888888"
)

subtitle.pack(
    anchor="w",
    padx=27,
    pady=(0, 15)
)


# =========================
# Calendar Card
# =========================

calendar_card = tk.Frame(
    root,
    bg="white",
    bd=0
)

calendar_card.pack(
    padx=20,
    fill="x"
)


calendar_text = tk.Text(
    calendar_card,
    height=10,
    width=35,
    font=("Consolas", 13),
    bg="white",
    fg="#29263D",
    bd=0,
    highlightthickness=0
)

calendar_text.pack(
    padx=15,
    pady=15
)


calendar_text.tag_config(
    "deadline",
    foreground="#6847E8",
    font=("Consolas", 13, "bold")
)


# =========================
# Add Homework
# =========================

form_title = tk.Label(
    root,
    text="Add Homework",
    font=("Arial", 17, "bold"),
    bg="#F5F3FF",
    fg="#29263D"
)

form_title.pack(
    anchor="w",
    padx=25,
    pady=(18, 8)
)


subject_entry = tk.Entry(
    root,
    font=("Arial", 12),
    bg="white",
    fg="#29263D",
    relief="flat",
    bd=8
)

subject_entry.insert(
    0,
    ""
)

subject_entry.pack(
    padx=25,
    fill="x"
)


# Date inputs

date_frame = tk.Frame(
    root,
    bg="#F5F3FF"
)

date_frame.pack(
    padx=25,
    pady=10,
    fill="x"
)


month_entry = tk.Entry(
    date_frame,
    font=("Arial", 12),
    width=8,
    justify="center",
    relief="flat",
    bd=8
)

month_entry.pack(
    side="left"
)


day_entry = tk.Entry(
    date_frame,
    font=("Arial", 12),
    width=8,
    justify="center",
    relief="flat",
    bd=8
)

day_entry.pack(
    side="left",
    padx=10
)


add_homework_button = tk.Button(
    date_frame,
    text="Add",
    font=("Arial", 11, "bold"),
    bg="#5B43E6",
    fg="white",
    activebackground="#4933C5",
    activeforeground="white",
    bd=0,
    padx=20,
    pady=8,
    command=add_homework
)

add_homework_button.pack(
    side="right"
)


# =========================
# Upcoming Homework
# =========================

upcoming_title = tk.Label(
    root,
    text="Upcoming Homework",
    font=("Arial", 17, "bold"),
    bg="#F5F3FF",
    fg="#29263D"
)

upcoming_title.pack(
    anchor="w",
    padx=25,
    pady=(5, 5)
)


homework_container = tk.Frame(
    root,
    bg="#F5F3FF"
)

homework_container.pack(
    padx=20,
    fill="both",
    expand=True
)


# =========================
# Bottom Navigation
# =========================

bottom = tk.Frame(
    root,
    bg="white",
    height=65
)

bottom.pack(
    padx=20,
    pady=10,
    fill="x"
)


calendar_button = tk.Button(
    bottom,
    text="📅\nCalendar",
    font=("Arial", 9),
    bg="white",
    fg="#5B43E6",
    bd=0
)

calendar_button.pack(
    side="left",
    expand=True
)


tasks_button = tk.Button(
    bottom,
    text="✓\nTasks",
    font=("Arial", 9),
    bg="white",
    fg="#888888",
    bd=0
)

tasks_button.pack(
    side="left",
    expand=True
)


grades_button = tk.Button(
    bottom,
    text="★\nGrades",
    font=("Arial", 9),
    bg="white",
    fg="#888888",
    bd=0
)

grades_button.pack(
    side="left",
    expand=True
)


profile_button = tk.Button(
    bottom,
    text="●\nProfile",
    font=("Arial", 9),
    bg="white",
    fg="#888888",
    bd=0
)

profile_button.pack(
    side="left",
    expand=True
)


# =========================
# Start
# =========================

update_calendar()
update_homework()

root.mainloop()
