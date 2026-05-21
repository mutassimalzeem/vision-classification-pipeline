# Preprocessing Plan

## Objective

Convert raw pixel columns into model-ready image tensors.

## Step 1 — Separate Features and Labels

Training data contains labels and pixel columns.

- `y`: label column
- `X`: pixel columns

Test data contains only pixel columns.

## Step 2 — Normalize Pixel Values

Raw pixel values usually range from 0 to 255.

Normalize to:

```text
0 to 1
```

Reason:

- helps neural networks train faster
- improves numerical stability
- keeps input scale consistent

## Step 3 — Reshape Features

Raw input shape:

```text
number_of_samples × 784
```

CNN input shape:

```text
number_of_samples × 28 × 28 × 1
```

The final dimension represents one grayscale channel.

## Step 4 — Train-Validation Split

Create a validation set before training.

Recommended split:

```text
80% train
20% validation
```

or

```text
90% train
10% validation
```

## Step 5 — Visual Inspection

Before training, visualize sample digits.

Check:

- whether labels match images
- whether reshaping is correct
- whether images are readable
- whether pixel inversion is needed

## Step 6 — Augmentation Preparation

Augmentation should be small because digits should remain readable.

Possible augmentations:

- slight rotation
- slight zoom
- slight horizontal/vertical shift

Avoid:

- strong rotation
- horizontal flip
- vertical flip
- heavy distortion

Flipping can change digit meaning or create unrealistic examples.
