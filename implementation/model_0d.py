"""
implementation/model_0d.py — 0D (single-cell) wrapper for running a model outside the framework.

Purpose
-------
- Provide a small, readable class where the author can plug in an integrator and stimulus.
- Use pure Python only (no numba/jax/torch here).
- Time derivatives (RHS) come from `model_template.ops` (or your final package with ops.py).
"""

from model_template import ops


class Stimulation:
    """
    Stimulus description for a 0D simulation.

    Parameters
    ----------
    t_start : float
        Start time (ms) of the first stimulus window.
    t_end : float
        End time (ms) of the last stimulus window. Outside this, stimulus is 0.
    duration : float
        Duration (ms) of a single pulse.
    amplitude : float
        Pulse amplitude in the same units as du/dt contribution (typically "units/ms").

    Method
    ------
    stim(t_ms: float) -> float
        Returns the instantaneous stimulus value at time t_ms.

    """

    def __init__(self, t_start: float, t_end: float, duration: float, amplitude: float):
        self.t_start = t_start
        self.t_end = t_end
        self.duration = duration
        self.amplitude = amplitude

    def stim(self):
        raise NotImplementedError("Stimulation.stim: implement your stimulus time-course.")


class Model0D:
    """
    Model OD implementation.
    """
    def __init__(self, dt: float, stimulations: list[Stimulation]):
        self.dt = dt
        self.stimulations = stimulations
        self.variables = None
        self.parameters = None

    def step(self):
        raise NotImplementedError("Model0D.step: implement your integration scheme (e.g., explicit Euler).")

    def run(self, t_max: float):
        raise NotImplementedError("Model0D.run: implement a loop around step().")