import matplotlib.pyplot as plt
import matplotlib.animation as animation
import subprocess

fig, ax = plt.subplots()


download_rates, upload_rates = [], []


download_line, = ax.plot([], [], label='Download')
upload_line, = ax.plot([], [], label='Upload')


def update_data(num):
    output = subprocess.check_output(['/home/student/PycharmProjects/graficRetea/network.sh']).decode('utf-8').strip().split('\t')

    output[0] = output[0].replace(',', '.')
    output[1] = output[1].replace(',', '.')
    download_rate = float(output[0])
    upload_rate = float(output[1])


    download_rates.append(download_rate)
    upload_rates.append(upload_rate)


    download_line.set_data(range(len(download_rates)), download_rates)
    upload_line.set_data(range(len(upload_rates)), upload_rates)


    ax.set_xlim(0, len(download_rates))
    ax.set_ylim(0, 100)
    return download_line, upload_line


ani = animation.FuncAnimation(fig, update_data, interval=1000, blit=True, cache_frame_data=False)

plt.title("Trafic retea")
ax.set_title('Rate de download și upload')
ax.set_xlabel('Timp')
ax.set_ylabel('Rate (Mbps)')


ax.legend()
plt.show()