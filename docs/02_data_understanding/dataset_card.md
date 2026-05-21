# Dataset Card

## Dataset Name

Kaggle Digit Recognizer

## Task

Handwritten digit classification.

## Input Format

Each image is represented as a row of pixel intensity values.

Typical structure:

- `label`: target digit from 0 to 9
- `pixel0` to `pixel783`: flattened 28×28 grayscale image pixels

## Image Shape

Original image shape:

```text
28 × 28
```

Flattened vector size:

```text
784 pixels
```

Model-ready CNN shape:

```text
28 × 28 × 1
```

## Target Classes

| Class | Meaning |
|---|---|
| 0 | digit zero |
| 1 | digit one |
| 2 | digit two |
| 3 | digit three |
| 4 | digit four |
| 5 | digit five |
| 6 | digit six |
| 7 | digit seven |
| 8 | digit eight |
| 9 | digit nine |

## Key Data Checks

Before modeling, check:

- dataset shape
- missing values
- duplicate rows
- label distribution
- pixel value range
- sample image visualizations
- class balance

## Known Limitations

- The images are low-resolution.
- The task is cleaner than many real-world vision problems.
- Digits are centered and already preprocessed.
- The dataset does not include extreme handwriting diversity.
- Strong performance on this dataset does not automatically mean strong real-world OCR performance.

## How This Dataset Helps

This dataset is useful for learning:

- image tensor preparation
- CNN fundamentals
- augmentation
- classification evaluation
- error analysis
- inference design
