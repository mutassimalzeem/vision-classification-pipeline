# Baseline Model Plan

## Objective

Build a simple neural network baseline before using CNNs.

## Why Start with a Baseline?

A baseline helps answer:

- Is the preprocessing correct?
- Is the model learning anything?
- How much improvement does CNN provide?
- Is the training setup working?

## Input

Flattened image vector:

```text
784 pixel values
```

## Model Concept

A dense neural network treats each pixel as an independent feature.

It does not explicitly understand local image structure, but it can still learn useful patterns.

## Expected Result

The dense baseline should perform reasonably well, but the CNN should perform better.

## What to Document

- architecture summary
- number of parameters
- training and validation accuracy
- training and validation loss
- confusion matrix
- limitations

## Limitation

The dense model ignores spatial relationships between neighboring pixels.

For image data, this is a major limitation because local patterns such as strokes and edges matter.
