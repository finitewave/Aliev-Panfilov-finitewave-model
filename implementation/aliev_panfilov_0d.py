"""
This module provides a simple interface to run the Aliev-Panfilov model in a 0D setting,
i.e., without spatial dimensions. It includes classes for defining stimulation protocols
and for managing the simulation of the Aliev-Panfilov equations over time.

"""

from aliev_panfilov import ops


class Stimulation:
    """
    Stimulus description for a 0D simulation.

    Parameters
    ----------
    t_start : float
        Start time (ms) of the first stimulus window.
    duration : float
        Duration (ms) of a single pulse.
    amplitude : float
        Pulse amplitude in the same units as du/dt contribution (typically "units/ms").

    Method
    ------
    stim(t: float) -> float
        Returns the instantaneous stimulus value at time t.

    """

    def __init__(self, t_start: float, duration: float, amplitude: float):
        self.t_start = t_start
        self.duration = duration
        self.amplitude = amplitude

    def stim(self, t: float) -> float:
        return self.amplitude if self.t_start <= t < self.t_start + self.duration else 0.0


class AlievPanfilov0D:
    """
    Aliev-Panfilov 0D model wrapper.
    """
    def __init__(self, dt: float, stimulations: list[Stimulation]):
        self.dt = dt
        self.stimulations = stimulations
        self.variables = ops.get_variables()
        self.parameters = ops.get_parameters()
        self.history = {s: [] for s in self.variables}

    def step(self, i: int):
        """
        Perform a single time step update.

        Parameters
        ----------
        i : int
            Current time step index.
        """
        self.variables["v"] += self.dt*ops.calc_dv(self.variables["v"],
                                                   self.variables["u"], 
                                                   self.parameters["a"], 
                                                   self.parameters["k"], 
                                                   self.parameters["eps"], 
                                                   self.parameters["mu1"], 
                                                   self.parameters["mu2"])
        self.variables["u"] += self.dt*(ops.calc_rhs(self.variables["u"],
                                                     self.variables["v"], 
                                                     self.parameters["a"], 
                                                     self.parameters["k"])
                                        + sum(stim.stim(t=self.dt*i) for stim in self.stimulations))

    def run(self, t_max: float):
        """
        Run the simulation up to time t_max.
        
        Parameters
        ----------
        t_max : float
            Maximum simulation time.
        """
        n_steps = int(t_max/self.dt)
        for i in range(n_steps):
            self.step(i)
            for s in self.variables:
                self.history[s].append(self.variables[s])