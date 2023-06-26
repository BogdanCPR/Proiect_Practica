import tkinter as tk
import subprocess
import threading
import os

os.environ['TERM'] = 'xterm'
root = tk.Tk()
root.overrideredirect(True)
root.configure(background="#656565")
# LABEL SPECIFICATII SISTEM
output_spec = subprocess.check_output(['./spec.sh'])
label_spec = tk.Label(root, text=output_spec.decode(), font=('Arial', 10), fg='#C0FF6B')
label_spec.configure(background="#656565")
label_spec.pack()

label_sys = tk.Label(root, text="Detalii Sistem", font=('Arial', 10), fg='#C0FF6B')
label_sys.configure(background="#656565")
label_sys.pack()


root.geometry('{}x{}+{}+{}'.format(350, 260, root.winfo_screenwidth() - 400, 50))
root.attributes('-topmost', True)

label_net = tk.Label(root, text="Detalii Retea", font=('Arial', 10), fg='#C0FF6B')
label_net.configure(background="#656565")
label_net.pack()


def stop_process(PID):
    subprocess.run(["pkill", "-P", PID])



def free_cpu(PID, process_name):
    question = tk.Toplevel(root)
    question.title("Stop process?")
    question.geometry("300x100")
    question.configure(background="#656565")

    label = tk.Label(question, text="Do you want to stop the process " + process_name + "?", font=('Arial', 10), fg='#C0FF6B')
    label.configure(background="#656565")
    label.pack(pady=10)

    def yes():
        thread = threading.Thread(target=stop_process, args=(PID,))
        thread.start()
        question.destroy()

    def no():
        question.destroy()

    yes_button = tk.Button(question, text="Yes", command=yes, relief="groove", highlightbackground="#C0FF6B")
    yes_button.pack(side='left', padx=40)
    no_button = tk.Button(question, text="No", command=no, relief="groove", highlightbackground="#C0FF6B")
    no_button.pack(side='left')
    question.wait_window()

def update_label_sys():
    output_sys = subprocess.check_output(['/home/student/PycharmProjects/System_overlay/system_stats.sh'])
    output_sys_vector = output_sys.decode('utf-8').strip().split('\t')
    cpu_usage = output_sys_vector[1].split("%")[0]
    cpu_usage = cpu_usage.replace(',', '.')
    if float(cpu_usage) > 95:
        output_free_proc = subprocess.check_output(['/home/student/PycharmProjects/System_overlay/free_cpu.sh']).decode(
            'utf-8').strip().split('\n')
        free_cpu(output_free_proc[0], output_free_proc[1])
    label_sys.config(text=output_sys.decode())

    label_sys.after(500, update_label_sys)
    label_sys.config()


def update_label_net():
    output_net = subprocess.check_output(['/home/student/PycharmProjects/System_overlay/network.sh'])
    label_net.config(text=output_net.decode())

    label_net.after(500, update_label_net)
    label_net.config()


def start_grafic():
    script_path = "/home/student/PycharmProjects/graficRetea/main.py"
    subprocess.Popen(['python', script_path])


def quit_app():
    root.quit()


thread1 = threading.Thread(target=update_label_sys)
thread2 = threading.Thread(target=update_label_net)

button_graph = tk.Button(root, text="Graph", command=start_grafic, relief="groove", highlightbackground="#C0FF6B")
button_graph.configure(background="#D5D5D5")
button_graph.pack(side='left', padx=80)

button_quit = tk.Button(root, text="Quit", command=quit_app, relief="groove", highlightbackground="#C0FF6B")
button_quit.configure(background="#D5D5D5")
button_quit.pack(side='left')

thread1.start()
thread2.start()

root.mainloop()
