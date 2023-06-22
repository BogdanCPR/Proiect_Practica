import matplotlib.pyplot as plt
import matplotlib.animation as animation
import subprocess

# crearea figurii și axei
fig, ax = plt.subplots()

# inițializarea datelor
download_rates, upload_rates = [], []

# crearea liniei de grafic
download_line, = ax.plot([], [], label='Download')
upload_line, = ax.plot([], [], label='Upload')

# funcția de actualizare a datelor
def update_data(num):
    # citirea datelor de la subproces
    output = subprocess.check_output(['./network.sh']).decode('utf-8').strip().split('\t')[-1].split()

    # extragerea ratei de download și upload
    download_rate = float(output[0])
    upload_rate = float(output[1])

    # adăugarea unei noi valori pentru ratele de download și upload
    download_rates.append(download_rate)
    upload_rates.append(upload_rate)

    # actualizarea datelor liniilor de grafic
    download_line.set_data(range(len(download_rates)), download_rates)
    upload_line.set_data(range(len(upload_rates)), upload_rates)

    # setarea limitelor axei x
    ax.set_xlim(0, len(download_rates))
    ax.set_ylim(0, 8000)
    return download_line, upload_line

# crearea animației
ani = animation.FuncAnimation(fig, update_data, interval=1000, blit=True, cache_frame_data=False)
# adăugarea unui titlu și a etichetelor axelor
ax.set_title('Rate de download și upload')
ax.set_xlabel('Timp')
ax.set_ylabel('Rate (Mbps)')

# afișarea legendei
ax.legend()

# afișarea graficului
plt.show()