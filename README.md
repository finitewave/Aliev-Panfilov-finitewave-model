## Aliev-Panfilov Finitewave model template

The Aliev-Panfilov model is a mathematical representation of cardiac tissue dynamics, capturing the essential features of wave propagation in excitable media. This model is particularly useful for studying the behavior of cardiac arrhythmias and other phenomena related to heart rhythms.

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
python -m test
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
│   └── aliev_panfilov_test.py       # smoke test
├── .gitignore
├── LICENSE                          # MIT
├── pyproject.toml                   # placeholders to replace
└── README.md                        # this file
```

### Variables
Model state variables:
- `u` — Transmembrane potential.
- `v` - Recovery variable.

### Parameters
Parameters and their defualt values:
- `a`    - Excitability threshold.                # Default: 0.1
- `k`    - Strength of the nonlinear source term. # Default: 8.0
- `eps`  - Baseline recovery rate.                # Default: 0.01
- `mu_1` - Recovery scaling parameter.            # Default: 0.2
- `mu_2` - Offset parameter for recovery rate.    # Default: 0.3

