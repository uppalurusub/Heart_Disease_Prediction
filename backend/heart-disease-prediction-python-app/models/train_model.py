# train_model.py

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

from utils.preprocessing import (
    HeartDataPreprocessor
)

# =====================================================
# Training Class
# =====================================================

class HeartDiseaseModelTrainer:

    def __init__(self):

        self.preprocessor = HeartDataPreprocessor()

        self.model = RandomForestClassifier(
            n_estimators=300,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )

        os.makedirs(
            "models",
            exist_ok=True
        )

    # =====================================================
    # Load Dataset
    # =====================================================

    def load_dataset(self):

        df = self.preprocessor.load_data(
            "data/heart_disease.csv"
        )

        print(f"Dataset Shape: {df.shape}")

        return df

    # =====================================================
    # Data Preparation
    # =====================================================

    def prepare_data(self, df):

        # Clean Data
        df = self.preprocessor.clean_data(df)

        # Missing Values
        df = self.preprocessor.handle_missing_values(df)

        # Outliers
        df = self.preprocessor.handle_outliers(df)

        # Split X and y
        X, y = self.preprocessor.split_features_target(df)

        return X, y

    # =====================================================
    # Train Model
    # =====================================================

    def train(self):

        df = self.load_dataset()

        X, y = self.prepare_data(df)

        

        # Train Test Split BEFORE fitting scaler
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )

        # Fit Preprocessor on Train Only
        X_train_processed = (
            self.preprocessor.fit_transform(X_train)
        )

        X_test_processed = (
            self.preprocessor.transform(X_test)
        )

        # Train Model
        self.model.fit(
            X_train_processed,
            y_train
        )

        # Predictions
        predictions = self.model.predict(
            X_test_processed
        )

        probabilities = (
            self.model.predict_proba(
                X_test_processed
            )
        )

        # Evaluation
        self.evaluate(
            y_test,
            predictions,
            probabilities
        )

        # Save Artifacts
        self.save_artifacts()

    # =====================================================
    # Evaluation
    # =====================================================

    def evaluate(
        self,
        y_test,
        predictions,
        probabilities
    ):

        print("\nModel Performance")
        print("-" * 50)

        print(
            "Accuracy:",
            round(
                accuracy_score(
                    y_test,
                    predictions
                ),
                4
            )
        )

        print(
            "Precision:",
            round(
                precision_score(
                    y_test,
                    predictions,
                    average="weighted"
                ),
                4
            )
        )

        print(
            "Recall:",
            round(
                recall_score(
                    y_test,
                    predictions,
                    average="weighted"
                ),
                4
            )
        )

        print(
            "F1 Score:",
            round(
                f1_score(
                    y_test,
                    predictions,
                    average="weighted"
                ),
                4
            )
        )

        print(
            "ROC AUC:",
            round(
                roc_auc_score(
                    y_test,
                    probabilities,
                    multi_class="ovr",
                    average="weighted"
                ),
                4
            )
        )

        print("\nConfusion Matrix")

        print(
            confusion_matrix(
                y_test,
                predictions
            )
        )

    # =====================================================
    # Save Model Artifacts
    # =====================================================

    def save_artifacts(self):

        # Save Model
        joblib.dump(
            self.model,
            "models/heart_model.pkl"
        )

        print(
            "\nSaved: models/heart_model.pkl"
        )

        # Save Preprocessor
        joblib.dump(
            self.preprocessor.preprocessor,
            "models/preprocessor.pkl"
        )

        print(
            "Saved: models/preprocessor.pkl"
        )

        feature_names = (
            self.preprocessor.preprocessor
            .get_feature_names_out()
        )

        # Feature Importance
        feature_importance = pd.DataFrame({

            "feature":
                feature_names,

            "importance":
                self.model.feature_importances_
        })

        feature_importance = (
            feature_importance
            .sort_values(
                by="importance",
                ascending=False
            )
        )

        # Save Feature Importance
        joblib.dump(
            feature_importance.to_dict(
                orient="records"
            ),
            "models/feature_importance.pkl"
        )

        print(
            "Saved: models/feature_importance.pkl"
        )

        print("\nTop Features")

        print(
            feature_importance.head(10)
        )

# =====================================================
# Main
# =====================================================

if __name__ == "__main__":

    trainer = HeartDiseaseModelTrainer()

    trainer.train()