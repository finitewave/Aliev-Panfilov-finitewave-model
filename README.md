## Aliev-Panfilov Finitewave model template

The Aliev-Panfilov model is a mathematical representation of cardiac tissue dynamics, capturing the essential features of wave propagation in excitable media. This model is particularly useful for studying the behavior of cardiac arrhythmias and other phenomena related to heart rhythms.

This model implementation can be used separately from the Finitewave, allowing for standalone simulations and testing of the Aliev-Panfilov dynamics without the need for the entire framework.

### Reference
Aliev, R. R., & Panfilov, A. V. (1996). A simple two-variable model of cardiac
  excitation. Chaos, Solitons & Fractals, 7(3), 293-301.

DOI: https://doi.org/10.1016/0960-0779(95)00089-5

### How to use
```bash
python -m examples.aliev_panfilov_example
```

This will initiate a simulation using the Aliev-Panfilov model and display the results.

### How to test
```bash
python -m pytest -q
```

### Repository structure
```text
.
├── aliev_panfilov/                  # Aliev-Panfilov model equations package (ops.py)
│   ├── __init__.py
│   └── ops.py                       
├── implementation/                  # 0D model implementation
│   ├── __init__.py
│   └── aliev_panfilov_0d.py
├── example/
│   └── aliev_panfilov_example.py    # minimal script to run a short trace
├── tests/
│   └── aliev_panfilov_test.py       # Aliev-Panfilov model test
├── .gitignore
├── LICENSE                          # MIT
├── pyproject.toml                   
└── README.md                        # this file
```

### Variables
Model state variables:
- `u` - Transmembrane potential.
- `v` - Recovery variable.

### Parameters
Parameters and their defualt values:
- `a    = 0.1` - Excitability threshold.
- `k    = 8.0` - Strength of the nonlinear source term.
- `eps  = 0.01`- Baseline recovery rate.
- `mu_1 = 0.2` - Recovery scaling parameter.
- `mu_2 = 0.3` - Offset parameter for recovery rate.

