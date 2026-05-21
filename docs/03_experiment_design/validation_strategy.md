# Validation Strategy

## Goal

Estimate how well the model generalizes to unseen digit images.

## Recommended Approach

Use a train-validation split from the labeled training data.

Recommended options:

```text
80% training / 20% validation
```

or

```text
90% training / 10% validation
```

## Why Validation Is Needed

Training accuracy alone does not show generalization.

A model may perform well on training data but fail on unseen samples. Validation performance helps detect overfitting.

## What to Monitor

- training loss
- validation loss
- training accuracy
- validation accuracy
- train-validation gap

## Overfitting Signs

Possible signs of overfitting:

- training accuracy keeps increasing
- validation accuracy stops improving
- training loss decreases
- validation loss increases
- large train-validation accuracy gap

## Underfitting Signs

Possible signs of underfitting:

- low training accuracy
- low validation accuracy
- both losses remain high
- model architecture may be too simple

## Final Test Predictions

The Kaggle test set should only be used for final prediction submission, not validation.
