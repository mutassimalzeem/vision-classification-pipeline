# Project Scope

## In Scope

- Data loading
- Data inspection
- Pixel normalization
- Image reshaping
- Baseline dense model
- CNN model
- Augmentation strategy
- Regularization strategy
- Confusion matrix
- Misclassification analysis
- Model saving
- Inference pipeline design
- FastAPI prediction endpoint design
- Portfolio case study

## Out of Scope

- Object detection
- Image segmentation
- Transfer learning
- Vision transformers
- OCR pipelines
- Cloud deployment automation
- Mobile app deployment

## Assumptions

- The dataset images are grayscale.
- Each sample contains one centered handwritten digit.
- Input images are 28×28 pixels.
- The model is trained for educational and portfolio purposes.
- The deployment plan is lightweight and API-focused.

## Constraints

- Dataset is relatively small and clean.
- Images are low-resolution.
- The dataset does not represent all real-world handwriting conditions.
- High accuracy is expected, so evaluation should focus on model behavior, not just score.
