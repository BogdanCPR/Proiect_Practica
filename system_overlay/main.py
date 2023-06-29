import tkinter as tk
import subprocess
import threading
import os



os.environ['TERM'] = 'xterm'
root = tk.Tk()
root.overrideredirect(True)
root.configure(background="#656565")
root.geometry('{}x{}+{}+{}'.format(350, 350, root.winfo_screenwidth() - 400, 50))
root.attributes('-topmost', True)

output_spec = subprocess.check_output(['./spec.sh'])
label_spec = tk.Label(root, text=output_spec.decode(), font=('Arial', 10), fg='#C0FF6B')
label_spec.configure(background="#656565")
label_spec.pack()

label_time = tk.Label(root, text="Detalii Timp", font=('Arial', 10), fg='#C0FF6B')
label_time.configure(background="#656565")
label_time.pack()

label_sys = tk.Label(root, text="Detalii Sistem", font=('Arial', 10), fg='#C0FF6B')
label_sys.configure(background="#656565")
label_sys.pack()

label_net = tk.Label(root, text="Detalii Retea", font=('Arial', 10), fg='#C0FF6B')
label_net.configure(background="#656565")
label_net.pack()


def stop_process(PID):
    subprocess.run(["kill", "-9", PID])


def free_cpu(PID, process_name):
    question = tk.Toplevel(root)
    question.title("Stop process?")
    question.geometry('300x100+500+500')
    question.configure(background="#656565")

    label = tk.Label(question, text="Do you want to stop the process " + process_name + "?", font=('Arial', 10),
                     fg='#C0FF6B')
    label.configure(background="#656565")
    label.pack(pady=10)

    def yes():
        thread = threading.Thread(target=stop_process, args=PID)
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

def update_label_time():
    output_time = subprocess.check_output(['/home/student/PycharmProjects/System_overlay/time.sh'])
    label_time.config(text=output_time.decode())

    label_time.after(500, update_label_time)
    label_time.config()


def start_grafic():
    script_path = "/home/student/PycharmProjects/graficRetea/main.py"
    subprocess.Popen(['python', script_path])


def quit_app():
    root.quit()

def show_hardware():
    hardware_window = tk.Toplevel(root)
    hardware_window.title("Hardware Components")
    hardware_window.geometry("580x800")
    hardware_window.configure(background="#656565")

    output_hardware = subprocess.check_output(['/home/student/PycharmProjects/System_overlay/hardware.sh'])
    text_hardware = output_hardware.decode()

    frame = tk.Frame(hardware_window)
    frame.pack(fill="both", expand=True)
    text_hardware_widget = tk.Text(frame, font=('Arial', 10), fg='#C0FF6B',bg="#656565", wrap="word")
    text_hardware_widget.insert("1.0", text_hardware)
    scrollbar = tk.Scrollbar(frame, orient="vertical")
    text_hardware_widget.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_hardware_widget.yview)
    text_hardware_widget.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    hardware_window.mainloop()

def show_services():
    services_window = tk.Toplevel(root)
    services_window.title("Running Services")
    services_window.geometry("670x500")
    services_window.configure(background="#656565")

    output_services = subprocess.check_output(['/home/student/PycharmProjects/System_overlay/services.sh'])
    text_services = output_services.decode()

    frame = tk.Frame(services_window)
    frame.pack(fill="both", expand=True)
    text_services_widget = tk.Text(frame, font=('Arial', 10), fg='#C0FF6B', bg="#656565", wrap="word")
    text_services_widget.insert("1.0", text_services)
    scrollbar = tk.Scrollbar(frame, orient="vertical")
    text_services_widget.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_services_widget.yview)
    text_services_widget.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    services_window.mainloop()

def tools_page():
    script_path = "/home/student/PycharmProjects/ToolsWindow/main.py"
    subprocess.Popen(['python', script_path])


def install_tool():
    install_window = tk.Toplevel(root)
    install_window.title("Install app")
    install_window.geometry("400x250+900+100")
    install_window.configure(background="#656565")

    install_label = tk.Label(install_window, text="App Manager Tool", font=('Arial', 20), fg='#C0FF6B',
                             background="#656565")
    install_label.pack()

    app_entry = tk.Entry(install_window, width=30, show="")
    app_entry.insert(0, "Application Name...")
    app_entry.pack(pady=10)

    pass_entry = tk.Entry(install_window, width=30, show="")
    pass_entry.insert(0, "User Password...")
    pass_entry.pack(pady=10)

    def install_app():
        app_name = app_entry.get()
        password = pass_entry.get()
        command = ["sudo", "-S", "apt-get", "install", app_name]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   universal_newlines=True)
        stdout, stderr = process.communicate(input=password + "\n")

        if process.returncode != 0:
            print("Comanda a eșuat. Mesajul de eroare este:")
            print(stderr)
        else:
            print("Comanda a fost executată cu succes. Iată ieșirea:")
            print(stdout)

    def remove_app():
        app_name = app_entry.get()
        password = pass_entry.get()
        command = ["sudo", "-S", "apt-get", "remove", app_name]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   universal_newlines=True)
        stdout, stderr = process.communicate(input=password + "\n")

        if process.returncode != 0:
            print("Comanda a eșuat. Mesajul de eroare este:")
            print(stderr)
        else:
            print("Comanda a fost executată cu succes. Iată ieșirea:")
            print(stdout)

    install_frame = tk.Frame(install_window)
    install_frame.pack(side='bottom', pady=15)

    button_install = tk.Button(install_frame, text="Install", command=install_app, relief="groove", highlightbackground="#C0FF6B")
    button_install.pack(side='left')
    button_remove = tk.Button(install_frame, text="Remove", command=install_app, relief="groove",
                       highlightbackground="#C0FF6B")
    button_remove.pack(side='left')
    install_window.mainloop()

thread1 = threading.Thread(target=update_label_sys)
thread2 = threading.Thread(target=update_label_net)
thread3 = threading.Thread(target=update_label_time)


frame2 = tk.Frame(root)
frame2.pack(side='bottom')

frame1 = tk.Frame(root)
frame1.pack(side='bottom')



button_graph = tk.Button(frame2, text="Graph", command=start_grafic, relief="groove", highlightbackground="#C0FF6B")
button_graph.configure(background="#D5D5D5")
button_graph.pack(side='left')


button_hardware = tk.Button(frame1, text="Hardware", command=show_hardware, relief="groove", highlightbackground="#C0FF6B")
button_hardware.configure(background="#D5D5D5")
button_hardware.pack(side='left')

button_services = tk.Button(frame1, text="Services", command=show_services, relief="groove", highlightbackground="#C0FF6B")
button_services.configure(background="#D5D5D5")
button_services.pack(side='left')

button_processes = tk.Button(frame2, text="Processes", command=tools_page, relief="groove", highlightbackground="#C0FF6B")
button_processes.configure(background="#D5D5D5")
button_processes.pack(side='left')

button_install = tk.Button(frame2, text="Install", command=install_tool, relief="groove", highlightbackground="#C0FF6B")
button_install.configure(background="#D5D5D5")
button_install.pack(side='left')

button_quit = tk.Button(frame2, text="Quit", command=quit_app, relief="groove", highlightbackground="#C0FF6B")
button_quit.configure(background="#D5D5D5")
button_quit.pack(side='left')



thread1.start()
thread2.start()
thread3.start()

root.mainloop()
