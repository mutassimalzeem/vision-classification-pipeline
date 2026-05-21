# Project Roadmap

## Phase 1 — Problem Understanding

### Goal

Understand the task, dataset, and project framing.

### Tasks

- Read the Kaggle competition page.
- Understand the input and output format.
- Define the business-style framing.
- Write project success criteria.

### Deliverables

- `PROJECT_CHARTER.md`
- `docs/01_problem_framing/problem_statement.md`
- `docs/01_problem_framing/success_criteria.md`

---

## Phase 2 — Data Understanding

### Goal

Understand how raw pixel values represent images.

### Tasks

- Inspect training data shape.
- Identify label distribution.
- Reshape flat 784-pixel rows into 28×28 images.
- Visualize sample digits.
- Check pixel value range.
- Normalize pixel values.

### Deliverables

- `docs/02_data_understanding/dataset_card.md`
- `docs/02_data_understanding/data_dictionary.md`
- `docs/02_data_understanding/preprocessing_plan.md`

---

## Phase 3 — Dense Baseline

### Goal

Build a simple neural network baseline before CNN.

### Tasks

- Create train-validation split.
- Normalize data.
- Train a simple dense model.
- Record baseline accuracy and loss.
- Save experiment notes.

### Deliverables

- Baseline experiment log
- Training curve
- Validation result

---

## Phase 4 — CNN Baseline

### Goal

Build a convolutional neural network suitable for image data.

### Tasks

- Reshape input to `(28, 28, 1)`.
- Build CNN using convolution, pooling, and dense layers.
- Train model.
- Compare with dense baseline.

### Deliverables

- CNN experiment log
- Model architecture summary
- Baseline vs CNN comparison

---

## Phase 5 — Augmentation and Regularization

### Goal

Improve generalization and reduce overfitting.

### Tasks

- Apply small rotations.
- Apply small shifts or zoom.
- Add dropout if needed.
- Use early stopping.
- Compare results with previous CNN.

### Deliverables

- Augmentation experiment log
- Regularization notes
- Updated performance comparison

---

## Phase 6 — Evaluation and Error Analysis

### Goal

Understand where the model performs well and where it fails.

### Tasks

- Generate confusion matrix.
- Create classification report.
- Visualize misclassified images.
- Identify commonly confused digit pairs.
- Explain possible reasons for errors.

### Deliverables

- `docs/05_evaluation/evaluation_plan.md`
- `docs/05_evaluation/confusion_matrix_analysis.md`
- `docs/05_evaluation/error_analysis_guide.md`

---

## Phase 7 — Inference Pipeline

### Goal

Design how the trained model will be used for prediction.

### Tasks

- Save trained model.
- Load model for inference.
- Define preprocessing for one image.
- Return predicted digit and confidence.
- Handle invalid input.

### Deliverables

- `docs/06_inference_api/inference_pipeline_design.md`
- `docs/06_inference_api/input_validation_plan.md`

---

## Phase 8 — API Design

### Goal

Design a deployment-ready prediction API.

### Tasks

- Define `/predict` endpoint.
- Define request format.
- Define response format.
- Define error messages.
- Document API contract.

### Deliverables

- `docs/06_inference_api/api_contract.md`

---

## Phase 9 — Portfolio Packaging

### Goal

Present the project as a professional ML engineering case study.

### Tasks

- Write final case study.
- Add architecture diagram.
- Add experiment table.
- Add screenshots.
- Write LinkedIn post.
- Polish README.

### Deliverables

- `docs/08_portfolio_case_study/case_study.md`
- `docs/08_portfolio_case_study/portfolio_summary.md`
- `docs/08_portfolio_case_study/linkedin_post.md`
