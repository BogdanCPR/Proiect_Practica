import tkinter as tk
import subprocess
import threading

root = tk.Tk()
root.overrideredirect(True)
label_sys = tk.Label(root, text="Detalii Sistem", font=('Arial', 11), fg='green')
label_sys.pack()
root.geometry('{}x{}+{}+{}'.format(210, 160, root.winfo_screenwidth() - 210, 50))
root.attributes('-topmost', True)

label_net = tk.Label(root, text="Detalii Retea", font=('Arial', 11), fg='green')
label_net.place(x=label_sys.winfo_x()+5, y=60)
def update_label_sys():

    output_sys = subprocess.check_output(['/home/bogdan/system_stats.sh'])
    label_sys.config(text=output_sys.decode())

    label_sys.after(500, update_label_sys)
    label_sys.config()
def update_label_net():
    output_net = subprocess.check_output(['/home/bogdan/network.sh'])
    label_net.config(text=output_net.decode())

    label_net.after(500, update_label_net)
    label_net.config()

thread1 = threading.Thread(target=update_label_sys)
thread2 = threading.Thread(target=update_label_net)


thread1.start()
thread2.start()

root.mainloop()
