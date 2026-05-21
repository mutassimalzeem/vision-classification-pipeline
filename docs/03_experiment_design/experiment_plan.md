# Experiment Plan

## Objective

Run controlled experiments to move from a simple baseline to a stronger CNN model.

## Experiment 1 — Dense Baseline

### Purpose

Establish a simple performance baseline.

### Model Idea

Flattened pixel input followed by dense layers.

### Expected Learning

This experiment shows how a non-convolutional neural network performs when spatial structure is not explicitly used.

### Metrics to Record

- training accuracy
- validation accuracy
- training loss
- validation loss
- confusion matrix

---

## Experiment 2 — CNN Baseline

### Purpose

Use convolutional layers to capture spatial patterns in images.

### Model Idea

Convolution + pooling + dense classifier.

### Expected Learning

This experiment should outperform the dense baseline because CNNs preserve spatial image structure.

### Metrics to Record

- training accuracy
- validation accuracy
- training loss
- validation loss
- confusion matrix
- misclassified examples

---

## Experiment 3 — CNN with Regularization

### Purpose

Reduce overfitting and improve generalization.

### Possible Techniques

- dropout
- batch normalization
- early stopping
- learning rate scheduling

### Metrics to Record

- validation accuracy improvement
- gap between training and validation accuracy
- stability of validation loss

---

## Experiment 4 — CNN with Augmentation

### Purpose

Improve robustness to small handwriting variations.

### Possible Augmentations

- small rotation
- small translation
- small zoom

### Metrics to Record

- validation accuracy
- confusion matrix changes
- misclassification pattern changes

## Experiment Comparison Table

| Experiment | Model Type | Augmentation | Regularization | Validation Accuracy | Key Finding |
|---|---|---|---|---|---|
| EXP-001 | Dense baseline | No | No | TBD | TBD |
| EXP-002 | CNN baseline | No | Optional | TBD | TBD |
| EXP-003 | CNN regularized | No | Yes | TBD | TBD |
| EXP-004 | CNN augmented | Yes | Yes | TBD | TBD |
