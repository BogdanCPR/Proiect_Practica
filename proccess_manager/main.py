import subprocess
import os
import tkinter as tk
import getpass

class ProcessManager:
    def __init__(self, master):
        self.master = master
        master.title("Manager de procese")

        # creăm o listă cu toate procesele disponibile
        self.proceses = self.get_proceses()

        # creăm un frame pentru lista de procese
        self.proceses_frame = tk.Frame(master)
        self.proceses_frame.pack(fill='both')

        # creăm un scrollbar pentru lista de procese
        self.proceses_scrollbar = tk.Scrollbar(self.proceses_frame)
        self.proceses_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # creăm o listbox pentru lista de procese
        self.proceses_listbox = tk.Listbox(self.proceses_frame, yscrollcommand=self.proceses_scrollbar.set, height=600, background='#656565', foreground='#C0FF6B')
        self.proceses_listbox.pack(fill=tk.BOTH, expand=True)
        self.proceses_listbox.bind("<Double-Button-1>", self.toggle_process)

        # adăugăm toate procesele în listbox
        for process in self.proceses:
            self.proceses_listbox.insert(tk.END, process)

        # configurăm scrollbarul pentru listbox
        self.proceses_scrollbar.config(command=self.proceses_listbox.yview)

    def get_proceses(self):
        # obținem o listă cu toate procesele disponibile
        result = subprocess.run(["/home/student/PycharmProjects/ToolsWindow/proceses.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proceses = []
        for line in result.stdout.decode().split("\n"):
                proceses.append(line)
        return proceses

    def toggle_process(self, event):
        # obținem procesul selectat din listbox
        selection = self.proceses_listbox.curselection()
        if len(selection) > 0:
            selected_process = self.proceses_listbox.get(selection[0]).split(":")
            pid = selected_process[0]
            subprocess.run(["kill","-9", pid])
            self.update_process_list()


    def update_process_list(self):
        # actualizăm lista de procese
        self.proceses = self.get_proceses()

        # ștergem toate elementele din listbox
        self.proceses_listbox.delete(0, tk.END)

        # adăugăm toate procesele actualizate în listbox
        for process in self.proceses:
            self.proceses_listbox.insert(tk.END, process)

    def update_process_status(self):
        selection = self.proceses_listbox.curselection()
        if len(selection) > 0:
            process_name = self.proceses_listbox.get(selection[0])

root = tk.Tk()
root.geometry('300x600+800+100')
process_manager = ProcessManager(root)
process_manager.update_process_status()
root.mainloop()