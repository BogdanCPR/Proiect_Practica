import tkinter as tk
import subprocess
import threading

root = tk.Tk()
root.overrideredirect(True)
label = tk.Label(root, text="Detalii Sistem", font=('Arial', 11), fg='green')
label.pack()
root.geometry('{}x{}+{}+{}'.format(210, 60, root.winfo_screenwidth() - 210, 50))
root.attributes('-topmost', True)


def update_label():

    output = subprocess.check_output(['/home/bogdan/system_stats.sh'])

    label.config(text=output.decode())

    label.after(500, update_label)
    label.config()

thread = threading.Thread(target=update_label)
thread.start()

root.mainloop()