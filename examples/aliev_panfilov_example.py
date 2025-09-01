import numpy as np
import matplotlib.pyplot as plt

from implementation.aliev_panfilov_0d import AlievPanfilov0D, Stimulation


stimulations = [Stimulation(t_start=0.0, duration=0.1, amplitude=2.0),
                Stimulation(t_start=40.0, duration=0.1, amplitude=2.0),
                Stimulation(t_start=70.0, duration=0.1, amplitude=2.0),]
t_max = 100.0

model = AlievPanfilov0D(dt=0.01, stimulations=stimulations)
model.run(t_max=t_max)

time = np.arange(0, t_max, model.dt)
plt.plot(time, model.history['u'])
plt.xlabel('Time (s)')
plt.ylabel('Membrane Potential (u)')
plt.title('0D Aliev-Panfilov Simulation')
plt.grid()
plt.show()

