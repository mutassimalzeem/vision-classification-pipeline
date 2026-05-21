# Input Validation Plan

## Why Input Validation Matters

A trained model can produce confident but meaningless predictions if the input is invalid.

Input validation protects the inference system from:

- corrupted files
- wrong image formats
- wrong input shapes
- blank images
- unexpected pixel ranges
- out-of-distribution data

## Validation Checks

| Check | Expected Behavior |
|---|---|
| File exists | reject missing input |
| File type | allow PNG, JPG, JPEG |
| Image mode | convert to grayscale |
| Image size | resize or reject based on design |
| Pixel range | ensure valid pixel values |
| Shape | ensure 28×28×1 before prediction |
| Blank image | return warning or reject |
| Confidence | warn if prediction confidence is low |

## Recommended Error Style

Return clear messages.

Bad:

```json
{
  "error": "Invalid input"
}
```

Better:

```json
{
  "error": "Expected 784 pixel values, but received 750."
}
```

## Portfolio Note

Input validation is a strong portfolio signal because it shows production thinking.
