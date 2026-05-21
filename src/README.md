# Source Code Plan

This folder will contain production-style Python modules after implementation.

No implementation code is included in this documentation-first version.

## Planned Structure

```text
src/
├── data/
│   └── preprocessing.py
├── models/
│   └── cnn_model.py
├── inference/
│   └── predict.py
└── utils/
    └── visualization.py
```

## Purpose

The notebooks will be used for experimentation.

The `src/` folder will later contain reusable production-style logic.

## Planned Responsibilities

| Module | Responsibility |
|---|---|
| `preprocessing.py` | normalize, reshape, validate image data |
| `cnn_model.py` | define CNN architecture |
| `predict.py` | load model and run inference |
| `visualization.py` | plot samples, curves, confusion matrix |
