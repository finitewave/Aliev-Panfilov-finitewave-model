import numpy as np
import matplotlib.pyplot as plt

from implementation.aliev_panfilov_0d import AlievPanfilov0D, Stimulation


stimulations = [Stimulation(t_start=5.0, duration=0.1, amplitude=9)]
t_max = 50.0

model = AlievPanfilov0D(dt=0.01, stimulations=stimulations)
model.run(t_max=t_max)

# fig = plt.figure(figsize=(10, 5))
plt.plot(model.times, model.history['u'], lw=2)
plt.xlabel('Time (s)')
plt.ylabel('Membrane Potential (u)')
plt.title('0D Aliev-Panfilov Simulation')
plt.grid()
plt.show()

# fig.savefig("aliev_panfilov_ap.png", dpi=300)
