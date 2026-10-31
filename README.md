# Machine Learning Classification Assignment

## Breast Cancer Wisconsin Classification

This project implements and compares five machine learning classification algorithms on the Breast Cancer Wisconsin dataset.

The target variable is binary:

- 0 = Malignant
- 1 = Benign

## Dataset

Dataset: Breast Cancer Wisconsin Diagnostic Dataset

Dataset characteristics used in this project:

- Total records: 569
- Input features: 30
- Target classes: 2
- Malignant records: 212
- Benign records: 357
- Missing values: 0
- Duplicate records: 0

The dataset was accessed using the Scikit-Learn dataset interface inside the BITS Virtual Lab environment.

## Machine Learning Workflow

The project follows the following workflow:

1. Load dataset
2. Inspect data quality
3. Separate features and target
4. Create stratified train-test split
5. Standardize features where required
6. Train classification models
7. Evaluate models
8. Save trained models and preprocessing artifacts
9. Test saved models
10. Deploy model evaluation using Streamlit

An 80:20 train-test split was used with random_state=42 and stratification on the target variable.

## Models Implemented

The following classifiers were trained:

1. Logistic Regression
2. Decision Tree
3. K-Nearest Neighbors (KNN)
4. Gaussian Naive Bayes
5. Support Vector Machine (SVM)

StandardScaler was used for Logistic Regression, KNN and SVM.

## Evaluation Metrics

Models were evaluated using:

- Accuracy
- Area Under ROC Curve (AUC)
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient (MCC)
- Confusion Matrix
- Classification Report

## Model Performance

| Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9825 | 0.9954 | 0.9861 | 0.9861 | 0.9861 | 0.9623 |
| Decision Tree | 0.9123 | 0.9157 | 0.9559 | 0.9028 | 0.9286 | 0.8174 |
| KNN | 0.9561 | 0.9788 | 0.9589 | 0.9722 | 0.9655 | 0.9054 |
| Naive Bayes | 0.9386 | 0.9878 | 0.9452 | 0.9583 | 0.9517 | 0.8676 |
| SVM | 0.9825 | 0.9950 | 0.9861 | 0.9861 | 0.9861 | 0.9623 |

## Observations

### Logistic Regression

Logistic Regression achieved an accuracy of 0.9825 and AUC of 0.9954. It produced 41 correct malignant predictions and 71 correct benign predictions, with one error in each direction.

### Decision Tree

Decision Tree achieved an accuracy of 0.9123. It had the lowest overall test accuracy among the five classifiers in this experiment.

### K-Nearest Neighbors

KNN achieved an accuracy of 0.9561 and AUC of 0.9788. Standardized features were used because KNN is based on distances between observations.

### Naive Bayes

Gaussian Naive Bayes achieved an accuracy of 0.9386 and AUC of 0.9878.

### Support Vector Machine

SVM achieved an accuracy of 0.9825 and AUC of 0.9950. Its classification predictions matched Logistic Regression on this test set.

## Overall Result

Logistic Regression and SVM achieved the highest test accuracy of 0.9825.

Logistic Regression recorded a slightly higher AUC (0.9954) than SVM (0.9950) on this test split.

Therefore, Logistic Regression showed the strongest overall result in this specific experiment while SVM produced nearly identical classification performance.

These results are specific to the train-test split and model configurations used in this assignment.

## Streamlit Applicatio# Machine Learning Classification Assignment

## Breast Cancer Wisconsin Classification

This project implements and compares five machine learning classification algorithms on the Breast Cancer Wisconsin dataset.

The target variable is binary:

- 0 = Malignant
- 1 = Benign

## Dataset

Dataset: Breast Cancer Wisconsin Diagnostic Dataset

Dataset characteristics used in this project:

- Total records: 569
- Input features: 30
- Target classes: 2
- Malignant records: 212
- Benign records: 357
- Missing values: 0
- Duplicate records: 0

The dataset was accessed using the Scikit-Learn dataset interface inside the BITS Virtual Lab environment.

## Machine Learning Workflow

The project follows the following workflow:

1. Load dataset
2. Inspect data quality
3. Separate features and target
4. Create stratified train-test split
5. Standardize features where required
6. Train classification models
7. Evaluate models
8. Save trained models and preprocessing artifacts
9. Test saved models
10. Deploy model evaluation using Streamlit

An 80:20 train-test split was used with random_state=42 and stratification on the target variable.

## Models Implemented

The following classifiers were trained:

1. Logistic Regression
2. Decision Tree
3. K-Nearest Neighbors (KNN)
4. Gaussian Naive Bayes
5. Support Vector Machine (SVM)

StandardScaler was used for Logistic Regression, KNN and SVM.

## Evaluation Metrics

Models were evaluated using:

- Accuracy
- Area Under ROC Curve (AUC)
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient (MCC)
- Confusion Matrix
- Classification Report

## Model Performance

| Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9825 | 0.9954 | 0.9861 | 0.9861 | 0.9861 | 0.9623 |
| Decision Tree | 0.9123 | 0.9157 | 0.9559 | 0.9028 | 0.9286 | 0.8174 |
| KNN | 0.9561 | 0.9788 | 0.9589 | 0.9722 | 0.9655 | 0.9054 |
| Naive Bayes | 0.9386 | 0.9878 | 0.9452 | 0.9583 | 0.9517 | 0.8676 |
| SVM | 0.9825 | 0.9950 | 0.9861 | 0.9861 | 0.9861 | 0.9623 |

## Observations

### Logistic Regression

Logistic Regression achieved an accuracy of 0.9825 and AUC of 0.9954. It produced 41 correct malignant predictions and 71 correct benign predictions, with one error in each direction.

### Decision Tree

Decision Tree achieved an accuracy of 0.9123. It had the lowest overall test accuracy among the five classifiers in this experiment.

### K-Nearest Neighbors

KNN achieved an accuracy of 0.9561 and AUC of 0.9788. Standardized features were used because KNN is based on distances between observations.

### Naive Bayes

Gaussian Naive Bayes achieved an accuracy of 0.9386 and AUC of 0.9878.

### Support Vector Machine

SVM achieved an accuracy of 0.9825 and AUC of 0.9950. Its classification predictions matched Logistic Regression on this test set.

## Overall Result

Logistic Regression and SVM achieved the highest test accuracy of 0.9825.

Logistic Regression recorded a slightly higher AUC (0.9954) than SVM (0.9950) on this test split.

Therefore, Logistic Regression showed the strongest overall result in this specific experiment while SVM produced nearly identical classification performance.

These results are specific to the train-test split and model configurations used in this assignment.

## Streamlit Application# Machine Learning Classification Assignment

## Breast Cancer Wisconsin Classification

This project implements and compares five machine learning classification algorithms on the Breast Cancer Wisconsin dataset.

The target variable is binary:

- 0 = Malignant
- 1 = Benign

## Dataset

Dataset: Breast Cancer Wisconsin Diagnostic Dataset

Dataset characteristics used in this project:

- Total records: 569
- Input features: 30
- Target classes: 2
- Malignant records: 212
- Benign records: 357
- Missing values: 0
- Duplicate records: 0

The dataset was accessed using the Scikit-Learn dataset interface inside the BITS Virtual Lab environment.

## Machine Learning Workflow

The project follows the following workflow:

1. Load dataset
2. Inspect data quality
3. Separate features and target
4. Create stratified train-test split
5. Standardize features where required
6. Train classification models
7. Evaluate models
8. Save trained models and preprocessing artifacts
9. Test saved models
10. Deploy model evaluation using Streamlit

An 80:20 train-test split was used with random_state=42 and stratification on the target variable.

## Models Implemented

The following classifiers were trained:

1. Logistic Regression
2. Decision Tree
3. K-Nearest Neighbors (KNN)
4. Gaussian Naive Bayes
5. Support Vector Machine (SVM)

StandardScaler was used for Logistic Regression, KNN and SVM.

## Evaluation Metrics

Models were evaluated using:

- Accuracy
- Area Under ROC Curve (AUC)
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient (MCC)
- Confusion Matrix
- Classification Report

## Model Performance

| Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9825 | 0.9954 | 0.9861 | 0.9861 | 0.9861 | 0.9623 |
| Decision Tree | 0.9123 | 0.9157 | 0.9559 | 0.9028 | 0.9286 | 0.8174 |
| KNN | 0.9561 | 0.9788 | 0.9589 | 0.9722 | 0.9655 | 0.9054 |
| Naive Bayes | 0.9386 | 0.9878 | 0.9452 | 0.9583 | 0.9517 | 0.8676 |
| SVM | 0.9825 | 0.9950 | 0.9861 | 0.9861 | 0.9861 | 0.9623 |

## Observations

### Logistic Regression

Logistic Regression achieved an accuracy of 0.9825 and AUC of 0.9954. It produced 41 correct malignant predictions and 71 correct benign predictions, with one error in each direction.

### Decision Tree

Decision Tree achieved an accuracy of 0.9123. It had the lowest overall test accuracy among the five classifiers in this experiment.

### K-Nearest Neighbors

KNN achieved an accuracy of 0.9561 and AUC of 0.9788. Standardized features were used because KNN is based on distances between observations.

### Naive Bayes

Gaussian Naive Bayes achieved an accuracy of 0.9386 and AUC of 0.9878.

### Support Vector Machine

SVM achieved an accuracy of 0.9825 and AUC of 0.9950. Its classification predictions matched Logistic Regression on this test set.

## Overall Result

Logistic Regression and SVM achieved the highest test accuracy of 0.9825.

Logistic Regression recorded a slightly higher AUC (0.9954) than SVM (0.9950) on this test split.

Therefore, Logistic Regression showed the strongest overall result in this specific experiment while SVM produced nearly identical classification performance.

These results are specific to the train-test split and model configurations used in this assignment.

## Streamlit Application# Machine Learning Classification Assignment

## Breast Cancer Wisconsin Classification

This project implements and compares five machine learning classification algorithms on the Breast Cancer Wisconsin dataset.

The target variable is binary:

- 0 = Malignant
- 1 = Benign

## Dataset

Dataset: Breast Cancer Wisconsin Diagnostic Dataset

Dataset characteristics used in this project:

- Total records: 569
- Input features: 30
- Target classes: 2
- Malignant records: 212
- Benign records: 357
- Missing values: 0
- Duplicate records: 0

The dataset was accessed using the Scikit-Learn dataset interface inside the BITS Virtual Lab environment.

## Machine Learning Workflow

The project follows the following workflow:

1. Load dataset
2. Inspect data quality
3. Separate features and target
4. Create stratified train-test split
5. Standardize features where required
6. Train classification models
7. Evaluate models
8. Save trained models and preprocessing artifacts
9. Test saved models
10. Deploy model evaluation using Streamlit

An 80:20 train-test split was used with random_state=42 and stratification on the target variable.

## Models Implemented

The following classifiers were trained:

1. Logistic Regression
2. Decision Tree
3. K-Nearest Neighbors (KNN)
4. Gaussian Naive Bayes
5. Support Vector Machine (SVM)

StandardScaler was used for Logistic Regression, KNN and SVM.

## Evaluation Metrics

Models were evaluated using:

- Accuracy
- Area Under ROC Curve (AUC)
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient (MCC)
- Confusion Matrix
- Classification Report

## Model Performance

| Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9825 | 0.9954 | 0.9861 | 0.9861 | 0.9861 | 0.9623 |
| Decision Tree | 0.9123 | 0.9157 | 0.9559 | 0.9028 | 0.9286 | 0.8174 |
| KNN | 0.9561 | 0.9788 | 0.9589 | 0.9722 | 0.9655 | 0.9054 |
| Naive Bayes | 0.9386 | 0.9878 | 0.9452 | 0.9583 | 0.9517 | 0.8676 |
| SVM | 0.9825 | 0.9950 | 0.9861 | 0.9861 | 0.9861 | 0.9623 |

## Observations

### Logistic Regression

Logistic Regression achieved an accuracy of 0.9825 and AUC of 0.9954. It produced 41 correct malignant predictions and 71 correct benign predictions, with one error in each direction.

### Decision Tree

Decision Tree achieved an accuracy of 0.9123. It had the lowest overall test accuracy among the five classifiers in this experiment.

### K-Nearest Neighbors

KNN achieved an accuracy of 0.9561 and AUC of 0.9788. Standardized features were used because KNN is based on distances between observations.

### Naive Bayes

Gaussian Naive Bayes achieved an accuracy of 0.9386 and AUC of 0.9878.

### Support Vector Machine

SVM achieved an accuracy of 0.9825 and AUC of 0.9950. Its classification predictions matched Logistic Regression on this test set.

## Overall Result

Logistic Regression and SVM achieved the highest test accuracy of 0.9825.

Logistic Regression recorded a slightly higher AUC (0.9954) than SVM (0.9950) on this test split.

Therefore, Logistic Regression showed the strongest overall result in this specific experiment while SVM produced nearly identical classification performance.

These results are specific to the train-test split and model configurations used in this assignment.

## Streamlit Application
