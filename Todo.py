import tkinter as tk
from tkinter import messagebox, font

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.root.configure(bg="#ffffff")
        self.tasks = []

        #fonts
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.task_font = font.Font(family="Helvetica", size=12)

        #label
        self.title_label = tk.Label(root, text="To-Do", font=self.title_font, fg="#222222", bg="#ffffff")
        self.title_label.pack(pady=(15, 5))

        #listbox and scrollbar
        self.list_frame = tk.Frame(root, bg="#ffffff")
        self.list_frame.pack(padx=15, pady=5)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(
            self.list_frame, width=40, height=10, font=self.task_font,
            bg="#ffffff", fg="#222222", bd=1, selectbackground="#e0e0e0",
            yscrollcommand=self.scrollbar.set, highlightthickness=1, selectforeground="#222222"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.config(command=self.listbox.yview)

        #entry and buttons
        self.input_frame = tk.Frame(root, bg="#ffffff")
        self.input_frame.pack(pady=10)

        self.entry = tk.Entry(
            self.input_frame, width=28, font=self.task_font,
            bg="#f7f7f7", fg="#222222", insertbackground="#222222", bd=1, relief=tk.FLAT
        )
        self.entry.pack(side=tk.LEFT, padx=(0, 8), ipady=4)

        self.add_button = tk.Button(
            self.input_frame, text="Add Task", command=self.add_task,
            bg="#ffffff", fg="#222222", font=self.task_font, bd=0, relief=tk.FLAT,
            activebackground="#e0e0e0", activeforeground="#222222", highlightthickness=0
        )
        self.add_button.pack(side=tk.LEFT, padx=2)

        self.remove_button = tk.Button(
            self.input_frame, text="Remove Task", command=self.remove_task,
            bg="#ffffff", fg="#222222", font=self.task_font, bd=0, relief=tk.FLAT,
            activebackground="#e0e0e0", activeforeground="#000000", highlightthickness=0
        )
        self.remove_button.pack(side=tk.LEFT, padx=2)

        #icon
        try:
            icon_img = tk.PhotoImage(file="todo_icon.png")
            self.root.iconphoto(False, icon_img)
        except Exception as e:
            pass  

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.tasks.pop(idx)
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()