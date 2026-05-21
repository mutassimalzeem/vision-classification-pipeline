# Inference Pipeline Design

## Objective

Define how the trained model will make predictions on new input.

## Inference Flow

```text
Input image or pixel array
        ↓
Validate input
        ↓
Preprocess input
        ↓
Load trained model
        ↓
Run prediction
        ↓
Convert probabilities to class label
        ↓
Return prediction and confidence
```

## Input Requirements

Expected input:

- grayscale image
- 28×28 pixels
- one digit per image
- pixel values normalized or convertible to normalized format

## Preprocessing During Inference

The inference preprocessing must match training preprocessing.

Required steps:

1. convert image to grayscale if needed
2. resize to 28×28 if needed
3. normalize pixel values
4. reshape to model input shape
5. add batch dimension

## Output

The prediction output should include:

- predicted digit
- confidence score
- probability distribution across all 10 classes

## Important Rule

Training preprocessing and inference preprocessing must be consistent.

If they differ, the model may perform poorly even if training accuracy was high.

## Failure Cases

The system should handle:

- missing file
- unsupported file type
- wrong image size
- invalid pixel values
- corrupted input
- blank image
