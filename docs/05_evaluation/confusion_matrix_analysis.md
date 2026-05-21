# Confusion Matrix Analysis Guide

## What Is a Confusion Matrix?

A confusion matrix shows how often each true class was predicted as each possible class.

Rows usually represent true labels.

Columns usually represent predicted labels.

## Why It Matters

Accuracy tells how often the model is correct overall.

The confusion matrix tells where the model is wrong.

## What to Look For

### 1. Strong Diagonal

A strong diagonal means most predictions are correct.

### 2. Off-Diagonal Errors

Off-diagonal cells show mistakes.

Example:

```text
True digit: 4
Predicted digit: 9
```

This means the model confused 4 with 9.

### 3. Common Digit Confusions

Possible confusing pairs:

- 4 and 9
- 3 and 5
- 7 and 1
- 8 and 9
- 0 and 6

## Analysis Template

Use this after generating the matrix:

```text
The confusion matrix shows that the model performs strongly on digits __, __, and __.

The most common confusion occurs between digit __ and digit __.

This may be because both digits share similar visual structures, especially when handwritten with __.

Compared to the previous experiment, the augmented CNN reduced confusion between __ and __, but errors remained for __.
```

## Portfolio Tip

Do not only show the confusion matrix image.

Explain what it means.

That explanation is what makes the project look professional.
