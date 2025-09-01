"""
ops.py — mathematical core of the Aliev–Panfilov model.

This module provides functions to compute the Aliev–Panfilov model equations,
as well as functions to retrieve default parameters and initial
values for the state variables.

The Aliev–Panfilov model is a simplified representation of cardiac electrical
activity, capturing essential features of excitation and recovery in cardiac tissue.

References:
- Aliev, R. R., & Panfilov, A. V. (1996). A simple two-variable model of cardiac
  excitation. Chaos, Solitons & Fractals, 7(3), 293-301.

DOI: https://doi.org/10.1016/0960-0779(95)00089-5

"""

__all__ = (
    "get_variables",
    "get_parameters",
    "calc_rhs",
    "calc_dv",
)


def get_variables() -> dict[str, float]:
    """
    Returns default initial values for state variables.
    """
    return {"u": 0.0, "v": 0.0}


def get_parameters() -> dict[str, float]:
    """
    Returns default parameter values for the model.
    """
    return {"a": 0.1, "k": 8.0, "eps": 0.01, "mu1": 0.2, "mu2": 0.3}


def calc_rhs(u, v, a, k) -> float:
    """
    Computes the right-hand side of the Aliev–Panfilov model for the transmembrane potential u.
    This function implements the ordinary differential equation governing the
    evolution of the transmembrane potential `u`, which represents the electrical
    activity of cardiac cells. The equation includes a nonlinear source term
    that models the excitation and recovery dynamics of the cardiac tissue.
    
    Parameters
    ----------
    u : float
        Current value of the transmembrane potential.
    v : float
        Current value of the recovery variable.
    a : float
        Excitability threshold.
    k : float
        Strength of the nonlinear source term.
    Returns
    -------
    float
        The computed right-hand side of the differential equation for `u`.
    """
    return -k*u*(u - a)*(u - 1) - u*v


def calc_dv(v, u, a, k, eps, mu1, mu2):
    """
    Computes the update of the recovery variable v for the Aliev–Panfilov model.

    This function implements the ordinary differential equation governing the
    evolution of the recovery variable `v`, which models the refractoriness of
    the cardiac tissue. The rate of recovery depends on both `v` and `u`, with a
    nonlinear interaction term involving a cubic expression in `u`.

    Parameters
    ----------
    v : float
        Current value of the recovery variable.
    u : float
        Current value of the transmembrane potential.
    dt : float
        Time step for integration.
    a : float
        Excitability threshold.
    k : float
        Strength of the nonlinear source term.
    eps : float
        Baseline recovery rate.
    mu1 : float
        Recovery scaling parameter.
    mu2 : float
        Offset parameter for recovery rate.

    Returns
    -------
    float
        Updated value of the recovery variable `v`.
    """
    
    dv = (- (eps + (mu1 * v) / (mu2 + u)) * (v + k * u * (u - a - 1.)))
    return dv