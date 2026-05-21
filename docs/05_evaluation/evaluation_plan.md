# Evaluation Plan

## Objective

Evaluate the model beyond a single accuracy number.

## Primary Metric

Accuracy is useful because this is a balanced multi-class classification task.

However, accuracy alone is not enough.

## Additional Evaluation Tools

| Tool | Purpose |
|---|---|
| Confusion matrix | shows which digits are confused |
| Classification report | gives precision, recall, and F1-score |
| Misclassified image grid | reveals visual failure patterns |
| Training curves | shows overfitting or underfitting |
| Per-class analysis | identifies weak classes |

## Questions to Answer

1. Which digits are classified most accurately?
2. Which digits are most commonly confused?
3. Does the model confuse visually similar digits?
4. Does augmentation reduce errors?
5. Is the model overfitting?
6. Is the model confident when wrong?

## Required Visualizations

- training accuracy vs validation accuracy
- training loss vs validation loss
- confusion matrix heatmap
- misclassified sample grid
- optional confidence distribution

## Final Evaluation Summary Format

Use this structure:

```text
The final CNN achieved X validation accuracy. The confusion matrix showed that the model most often confused A with B and C with D. Visual inspection of misclassified samples suggests that ambiguous handwriting, thin strokes, and tilted digits caused many of the errors.
```
