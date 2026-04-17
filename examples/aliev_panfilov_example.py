import numpy as np
import matplotlib.pyplot as plt

from implementation.aliev_panfilov_0d import AlievPanfilov0D, Stimulation


stimulations = [Stimulation(t_start=0.0, duration=0.1, amplitude=9),
                Stimulation(t_start=50.0, duration=0.1, amplitude=9),
                Stimulation(t_start=100.0, duration=0.1, amplitude=9),]
t_max = 130.0

model = AlievPanfilov0D(dt=0.01, stimulations=stimulations)
model.run(t_max=t_max)

time = np.arange(0, t_max, model.dt)
plt.plot(time, model.history['u'])
plt.plot(time, model.stim_history, label='Stimulus Current', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Membrane Potential (u)')
plt.title('0D Aliev-Panfilov Simulation')
plt.grid()
plt.show()

