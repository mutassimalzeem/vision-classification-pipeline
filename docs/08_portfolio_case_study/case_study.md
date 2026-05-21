# Case Study: Vision Classification Pipeline from Raw Pixels to Deployment-Ready Inference API

## 1. Project Overview

This project builds an end-to-end computer vision classification pipeline using the Kaggle Digit Recognizer dataset. The task is to classify handwritten digits from grayscale images represented as flattened pixel values.

Instead of treating this as a simple MNIST-style notebook, the project focuses on the full machine learning lifecycle:

- data understanding
- preprocessing
- baseline modeling
- CNN modeling
- augmentation
- evaluation
- error analysis
- inference design
- API readiness

## 2. Problem Framing

The task is a supervised multi-class image classification problem. Each input image contains a handwritten digit from 0 to 9.

The broader engineering challenge is to transform raw pixel data into a reliable inference pipeline.

## 3. Dataset Understanding

Each image is represented as 784 pixel values, corresponding to a 28×28 grayscale image.

The training data contains labels. The test data contains only pixel values.

Key preprocessing steps include:

- separating labels from pixels
- normalizing pixel values
- reshaping flat vectors into images
- preparing image tensors for CNN input

## 4. Modeling Approach

The project follows a staged modeling strategy.

### Dense Baseline

A simple dense neural network is used first to establish a baseline.

### CNN Baseline

A convolutional neural network is then used to capture local image patterns such as edges, curves, and strokes.

### Augmented CNN

Small transformations such as rotation, shift, and zoom are used to improve robustness.

## 5. Evaluation Strategy

The final model is evaluated using:

- validation accuracy
- training and validation loss curves
- confusion matrix
- classification report
- misclassified image analysis

The goal is not only to measure performance, but also to understand failure patterns.

## 6. Error Analysis

Misclassified samples are reviewed visually to identify common causes of error.

Possible error causes include:

- ambiguous handwriting
- similar digit shapes
- tilted digits
- thin or incomplete strokes
- overconfident wrong predictions

## 7. Inference Design

The trained model is prepared for inference by defining a consistent preprocessing pipeline.

The planned API accepts an image or pixel array and returns:

- predicted digit
- confidence score
- class probabilities

## 8. Deployment Readiness

The project includes an API contract and deployment plan using FastAPI.

The deployment-ready design includes:

- model loading
- input validation
- prediction endpoint
- structured response
- error handling
- confidence reporting

## 9. Key Learnings

This project helped build understanding of:

- how image data is represented numerically
- why CNNs are useful for vision tasks
- how augmentation improves robustness
- why evaluation should go beyond accuracy
- how model inference differs from model training
- how to document ML projects professionally

## 10. Limitations

This dataset is clean and controlled. Real-world handwriting recognition would require more robust preprocessing, larger datasets, more diverse handwriting examples, and stronger deployment testing.

## 11. Future Improvements

Possible future improvements:

- add a simple frontend drawing canvas
- deploy the API online
- add model versioning
- compare TensorFlow and PyTorch implementations
- test on custom handwritten images
- add confidence thresholding
- convert model to TensorFlow Lite
