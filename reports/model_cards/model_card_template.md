# Model Card Template

## Model Name

Example:

```text
CNN Digit Classifier v1
```

## Model Version

```text
v1.0
```

## Intended Use

Classify 28×28 grayscale handwritten digit images into one of ten classes: 0 through 9.

## Not Intended For

This model is not intended for:

- full OCR systems
- real-world document processing without further validation
- high-stakes decision-making
- recognizing letters or symbols
- recognizing digits from complex backgrounds

## Training Dataset

Kaggle Digit Recognizer training data.

## Input

Expected input shape:

```text
28 × 28 × 1
```

Expected input type:

```text
normalized grayscale image
```

## Output

Predicted digit class and confidence score.

## Evaluation Metrics

| Metric | Value |
|---|---|
| Validation accuracy | TBD |
| Precision | TBD |
| Recall | TBD |
| F1-score | TBD |

## Strengths

- Performs well on clean 28×28 digit images.
- Lightweight and fast for inference.
- Suitable for learning CV classification pipeline design.

## Limitations

- Trained on clean digit images.
- May fail on noisy or complex backgrounds.
- May confuse visually similar digits.
- Requires preprocessing consistency.
- Not tested on broad real-world handwriting data.

## Ethical and Practical Considerations

This is an educational model. It should not be used in high-stakes systems without additional validation, monitoring, and robustness testing.

## Recommended Improvements

- Test on custom handwritten images.
- Add confidence thresholding.
- Add out-of-distribution detection.
- Add API monitoring.
- Compare with stronger architectures.
