# Problem Statement

## Background

Handwritten digit recognition is a classic computer vision classification problem. Each input image contains a single handwritten digit from 0 to 9. The task is to correctly classify the digit based on pixel intensity values.

Although the dataset is simple, the project is useful because it allows the full computer vision workflow to be practiced in a controlled environment.

## Machine Learning Problem

This is a supervised multi-class image classification problem.

- Input: grayscale image of handwritten digit
- Output: digit class from 0 to 9
- Number of classes: 10
- Model type: convolutional neural network
- Evaluation type: classification metrics

## Engineering Problem

The engineering problem is broader than classification accuracy.

The full system should be able to:

1. Load raw tabular pixel data.
2. Convert pixel rows into image tensors.
3. Normalize images consistently.
4. Train a CNN model.
5. Evaluate model behavior.
6. Identify error patterns.
7. Save the trained model.
8. Prepare the model for inference.
9. Define a clean API contract.

## Portfolio Framing

Weak framing:

> MNIST digit recognition with CNN.

Strong framing:

> Vision Classification Pipeline from Raw Pixels to Deployment-Ready Inference API.

The second framing shows that the project is about engineering process, not just model accuracy.
