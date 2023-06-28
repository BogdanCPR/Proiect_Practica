import subprocess
import tkinter as tk


class ProcessManager:
    def __init__(self, master):
        self.master = master
        master.title("Manager de procese")

        self.processes = self.get_proceses()
        self.processes_frame = tk.Frame(master)
        self.processes_frame.pack(fill='both')

        self.processes_scrollbar = tk.Scrollbar(self.processes_frame)
        self.processes_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.processes_listbox = tk.Listbox(self.processes_frame, yscrollcommand=self.processes_scrollbar.set,
                                            height=600,
                                            background='#656565', foreground='#C0FF6B')
        self.processes_listbox.pack(fill=tk.BOTH, expand=True)
        self.processes_listbox.bind("<Double-Button-1>", self.toggle_process)

        for process in self.processes:
            self.processes_listbox.insert(tk.END, process)

        self.processes_scrollbar.config(command=self.processes_listbox.yview)

    def get_proceses(self):
        result = subprocess.run(["/home/student/PycharmProjects/ToolsWindow/proceses.sh"], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        processes = []
        for line in result.stdout.decode().split("\n"):
            processes.append(line)
        return processes

    def toggle_process(self, event):
        selection = self.processes_listbox.curselection()
        if len(selection) > 0:
            selected_process = self.processes_listbox.get(selection[0]).split(":")
            pid = selected_process[0]
            subprocess.run(["kill", "-9", pid])
            self.update_process_list()

    def update_process_list(self):
        self.processes = self.get_proceses()
        self.processes_listbox.delete(0, tk.END)
        for process in self.processes:
            self.processes_listbox.insert(tk.END, process)


root = tk.Tk()
root.geometry('300x600+800+100')
process_manager = ProcessManager(root)
root.mainloop()
