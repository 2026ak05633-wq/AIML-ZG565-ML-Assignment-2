import streamlit as st
import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Breast Cancer Classification",
    page_icon="🔬",
    layout="wide"
)

st.title("Breast Cancer Wisconsin Classification")
st.write(
    "Compare five machine learning classifiers using uploaded test data."
)

st.info(
    "Target encoding: 0 = Malignant, 1 = Benign"
)

# --------------------------------------------------
# Model configuration
# --------------------------------------------------

model_files = {
    "Logistic Regression": "logistic_regression.pkl",
    "Decision Tree": "decision_tree.pkl",
    "K-Nearest Neighbors": "knn.pkl",
    "Naive Bayes": "naive_bayes.pkl",
    "Support Vector Machine": "svm.pkl"
}

scaled_models = {
    "Logistic Regression",
    "K-Nearest Neighbors",
    "Support Vector Machine"
}

# --------------------------------------------------
# Load preprocessing artifact
# --------------------------------------------------

scaler = joblib.load("scaler.pkl")

# --------------------------------------------------
# User controls
# --------------------------------------------------

st.sidebar.header("Model Evaluation")

selected_model = st.sidebar.selectbox(
    "Select classifier",
    list(model_files.keys())
)

uploaded_file = st.sidebar.file_uploader(
    "Upload test CSV",
    type=["csv"]
)

# --------------------------------------------------
# Evaluation
# --------------------------------------------------

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Dataset")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])
    st.dataframe(df.head())

    if "target" not in df.columns:

        st.error(
            "The uploaded CSV must contain a 'target' column."
        )

    else:

        X = df.drop("target", axis=1)
        y = df["target"]

        model = joblib.load(
            model_files[selected_model]
        )

        if selected_model in scaled_models:
            X_model = scaler.transform(X)
        else:
            X_model = X

        predictions = model.predict(X_model)

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(X_model)[:, 1]
        else:
            probabilities = None

        accuracy = accuracy_score(y, predictions)
        precision = precision_score(y, predictions)
        recall = recall_score(y, predictions)
        f1 = f1_score(y, predictions)
        mcc = matthews_corrcoef(y, predictions)

        if probabilities is not None:
            auc = roc_auc_score(y, probabilities)
        else:
            auc = None

        # --------------------------------------------------
        # Metrics
        # --------------------------------------------------

        st.subheader("Evaluation Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Accuracy",
            f"{accuracy:.4f}"
        )

        col2.metric(
            "Precision",
            f"{precision:.4f}"
        )

        col3.metric(
            "Recall",
            f"{recall:.4f}"
        )

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "F1 Score",
            f"{f1:.4f}"
        )

        col5.metric(
            "MCC",
            f"{mcc:.4f}"
        )

        if auc is not None:
            col6.metric(
                "AUC",
                f"{auc:.4f}"
            )

        # --------------------------------------------------
        # Confusion matrix
        # --------------------------------------------------

        st.subheader("Confusion Matrix")

        cm = confusion_matrix(y, predictions)

        cm_df = pd.DataFrame(
            cm,
            index=[
                "Actual Malignant",
                "Actual Benign"
            ],
            columns=[
                "Predicted Malignant",
                "Predicted Benign"
            ]
        )

        st.dataframe(cm_df)

        # --------------------------------------------------
        # Classification report
        # --------------------------------------------------

        st.subheader("Classification Report")

        report = classification_report(
            y,
            predictions,
            target_names=[
                "Malignant",
                "Benign"
            ],
            output_dict=True
        )

        report_df = pd.DataFrame(
            report
        ).transpose()

        st.dataframe(report_df.round(4))

else:

    st.warning(
        "Upload test_data.csv from the sidebar to evaluate a model."
    )
