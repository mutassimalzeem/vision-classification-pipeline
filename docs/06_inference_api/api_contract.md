# API Contract

## Endpoint

```text
POST /predict
```

## Purpose

Accept an image or pixel array and return the predicted digit.

## Request Type Option 1 — Image Upload

```text
Content-Type: multipart/form-data
```

Field:

```text
file: image file
```

Supported formats:

- PNG
- JPG
- JPEG

## Request Type Option 2 — Pixel Array

```json
{
  "pixels": [0, 0, 12, 255, "..."]
}
```

Expected length:

```text
784
```

## Successful Response

```json
{
  "prediction": 7,
  "confidence": 0.9821,
  "probabilities": {
    "0": 0.001,
    "1": 0.003,
    "2": 0.004,
    "3": 0.002,
    "4": 0.001,
    "5": 0.0008,
    "6": 0.001,
    "7": 0.9821,
    "8": 0.003,
    "9": 0.002
  }
}
```

## Error Response Examples

### Invalid File Type

```json
{
  "error": "Unsupported file type. Please upload PNG, JPG, or JPEG."
}
```

### Invalid Pixel Array

```json
{
  "error": "Pixel array must contain exactly 784 values."
}
```

### Low Confidence Prediction

```json
{
  "prediction": 4,
  "confidence": 0.421,
  "warning": "Low confidence prediction. Input may be ambiguous or out-of-distribution."
}
```

## API Design Notes

The API should not only return the class label. It should also return confidence and probabilities so downstream users can understand prediction uncertainty.

## Future API Improvements

- batch prediction endpoint
- confidence thresholding
- image quality validation
- request logging
- model versioning
