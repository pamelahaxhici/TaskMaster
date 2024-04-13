import tkinter as tk
from tkinter import ttk, messagebox
import json

class TaskMasterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("TaskMaster")
        self.geometry("400x400")

        # Create input field for adding tasks
        self.task_input = ttk.Entry(self, font=(
            "TkDefaultFont", 16), width=30)
        self.task_input.pack(pady=10)

        # Create button for adding tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        # Create listbox to display added tasks
        self.task_list = tk.Listbox(self, font=(
            "TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create buttons for marking tasks as done or deleting them
        ttk.Button(self, text="Done", command=self.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)

        # Create button for displaying task statistics
        ttk.Button(self, text="View Stats", command=self.view_stats).pack(side=tk.BOTTOM, pady=10)

        self.load_tasks()

    def view_stats(self):
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    def add_task(self):
        task = self.task_input.get()
        if task.strip():
            self.task_list.insert("end", task)
            self.task_list.itemconfig("end", foreground="orange")
            self.task_input.delete(0, "end")
            self.save_tasks()

    def mark_done(self):
        selection = self.task_list.curselection()
        if selection:
            self.task_list.itemconfig(selection, foreground="green")
            self.save_tasks()

    def delete_task(self):
        selection = self.task_list.curselection()
        if selection:
            self.task_list.delete(selection)
            self.save_tasks()

    def load_tasks(self):
        try:
            with open("taskmaster_tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert("end", task["text"])
                    self.task_list.itemconfig("end", foreground=task["color"])
        except FileNotFoundError:
            pass

    def save_tasks(self):
        data = [{"text": self.task_list.get(i), "color": self.task_list.itemcget(i, "fg")} for i in range(self.task_list.size())]
        with open("taskmaster_tasks.json", "w") as f:
            json.dump(data, f)

if __name__ == '__main__':
    app = TaskMasterApp()
    app.mainloop()

