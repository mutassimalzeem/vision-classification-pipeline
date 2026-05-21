# Data Dictionary

## Training Data

| Column | Type | Description |
|---|---|---|
| label | integer | Target digit class from 0 to 9 |
| pixel0 to pixel783 | integer | Grayscale pixel values of the flattened 28×28 image |

## Test Data

| Column | Type | Description |
|---|---|---|
| pixel0 to pixel783 | integer | Grayscale pixel values of the flattened 28×28 image |

## Pixel Value Meaning

Each pixel value represents grayscale intensity.

| Value Range | Meaning |
|---|---|
| 0 | black/background |
| 1–254 | varying brightness |
| 255 | white/maximum intensity |

## Model Input Transformation

Raw row:

```text
[784 pixel values]
```

Image form:

```text
28 × 28
```

CNN input form:

```text
28 × 28 × 1
```

## Target Encoding

The target labels are already integer-encoded.

Example:

```text
7 means handwritten digit seven
```

For TensorFlow/Keras, this can be used with sparse categorical crossentropy.
