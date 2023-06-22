import tkinter as tk
import subprocess
import threading
import os

os.environ['TERM'] = 'xterm'
root = tk.Tk()
root.overrideredirect(True)

#LABEL SPECIFICATII SISTEM
output_spec = subprocess.check_output(['./spec.sh'])
label_spec = tk.Label(root, text=output_spec.decode(), font=('Arial', 10), fg='green')
label_spec.pack()


label_sys = tk.Label(root, text="Detalii Sistem", font=('Arial', 10), fg='green')
label_sys.pack()

root.geometry('{}x{}+{}+{}'.format(350, 260, root.winfo_screenwidth() - 350, 50))
root.attributes('-topmost', True)




label_net = tk.Label(root, text="Detalii Retea", font=('Arial', 10), fg='green')
label_net.pack()
def update_label_sys():

    output_sys = subprocess.check_output(['./system_stats.sh'])
    label_sys.config(text=output_sys.decode())

    label_sys.after(500, update_label_sys)
    label_sys.config()
def update_label_net():
    output_net = subprocess.check_output(['./network.sh'])
    label_net.config(text=output_net.decode())

    label_net.after(500, update_label_net)
    label_net.config()

thread1 = threading.Thread(target=update_label_sys)
thread2 = threading.Thread(target=update_label_net)


thread1.start()
thread2.start()

root.mainloop()
