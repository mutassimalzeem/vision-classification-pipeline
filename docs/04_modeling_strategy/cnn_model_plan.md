# CNN Model Plan

## Objective

Build a convolutional neural network for handwritten digit classification.

## Why CNN?

CNNs are designed for image data. They learn local patterns such as:

- edges
- curves
- corners
- strokes
- digit-specific shapes

## Input Shape

```text
28 × 28 × 1
```

## Core CNN Components

| Component | Purpose |
|---|---|
| Conv2D | learns local visual patterns |
| ReLU | adds non-linearity |
| MaxPooling2D | reduces spatial size |
| Dropout | reduces overfitting |
| Dense | final classification layers |
| Softmax | outputs class probabilities |

## Model Design Principles

Start simple.

A good first CNN does not need to be very deep. The goal is to build a clean, understandable baseline.

## What to Track

- architecture summary
- training curves
- validation accuracy
- confusion matrix
- misclassified examples
- comparison with dense baseline

## Expected Improvement

The CNN should outperform the dense baseline because it uses spatial structure.
