import tkinter as tk
from tkinter import ttk, messagebox

PALETTE={
    "bg":"#ECF0F2",
    "1":"#5370B7",
    "2":"#3DA5D1",
    "3":"#3D53D1"
}

students = [
    {"name": "Alex", "science1": 85, "science2": 90, "science3": 88},
    {"name": "Sam", "science1": 98, "science2": 92, "science3": 95},
    {"name": "Jordan", "science1": 78, "science2": 85, "science3": 80},
    {"name": "Taylor", "science1": 91, "science2": 89, "science3": 93},
    {"name": "Riley", "science1": 88, "science2": 94, "science3": 90}
]


def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"


def find_topper():
    if not students:
        messagebox.showwarning("No Students", "No student records found.")
        return

    topper = max(students,key=lambda s: (sum([s["science1"], s["science2"], s["science3"]]) / 3,sum([s["science1"], s["science2"], s["science3"]]),s["name"]))

    for item in tree.get_children():
        tree.item(item, tags=())

    for item in tree.get_children():
        values = tree.item(item, "values")

        if values[0] == topper["name"]:
            tree.selection_set(item)
            tree.focus(item)
            tree.see(item)
            tree.item(item, tags=("topper",))

    total = topper["science1"] + topper["science2"] + topper["science3"]
    average = total / 3
    grade = letter_grade(average)

    total_label.config(text=f"Total Score: {total}")
    average_label.config(text=f"Average: {average:.2f}")
    grade_label.config(text=f"Grade: {grade}")

    messagebox.showinfo(
        "Science Topper!",
        f"Congratulations, {topper['name']}!\n\n"
        f"Science Average: {average:.2f}\n"
        f"Total Score: {total}\n"
        f"Average: {average:.2f}\n"
        f"Grade: {grade}\n\n"
        "Excellent work!"
    )


root = tk.Tk()
root.title("Science Score Topper")
root.geometry("550x500")
root.configure(bg=PALETTE["bg"])

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background=PALETTE["bg"],
    foreground=PALETTE["1"],
    fieldbackground=PALETTE["bg"],
    font=("Arial", 10),
    rowheight=30
)

style.configure(
    "Treeview.Heading",
    background=PALETTE["1"],
    foreground="white",
    font=("Arial", 10, "bold")
)

style.map(
    "Treeview",
    background=[("selected", PALETTE["2"])],
    foreground=[("selected", "white")]
)

tree = ttk.Treeview(root, columns=("Name", "Science 1", "Science 2", "Science 3"), show="headings", height=8)

for column in ("Name", "Science 1", "Science 2", "Science 3"):
    tree.heading(column, text=column)
    tree.column(column, anchor="center", width=120)

tree.tag_configure("topper", background=PALETTE["2"], foreground="white")
tree.pack(pady=10)

for student in students:
    tree.insert(
        "",
        tk.END,
        values=(
            student["name"],
            student["science1"],
            student["science2"],
            student["science3"]
        )
    )

total_label = tk.Label(root,text="Total Score: --",font=("Arial", 12, "bold"),bg=PALETTE["bg"],fg=PALETTE["1"])
total_label.pack(pady=3)

average_label = tk.Label(root,text="Average: --",font=("Arial", 12, "bold"),bg=PALETTE["bg"],fg=PALETTE["1"])
average_label.pack(pady=3)

grade_label = tk.Label(root,text="Grade: --",font=("Arial", 12, "bold"),bg=PALETTE["bg"],fg=PALETTE["1"])
grade_label.pack(pady=3)

topper_button = tk.Button(root,text="Find Science Topper",font=("Arial", 12, "bold"),bg=PALETTE["3"],fg="white",activebackground=PALETTE["2"],activeforeground="white",command=find_topper,relief="flat")
topper_button.pack(pady=15)

root.mainloop()