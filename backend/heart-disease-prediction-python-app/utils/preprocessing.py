# app/utils/preprocessing.py

import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


class HeartDataPreprocessor:

    def __init__(self, target_column="target"):

        self.target_column = target_column

        self.numeric_columns = []
        self.categorical_columns = []

        self.preprocessor = None

    def drop_id_columns(self, df):

        id_cols = [

            col

            for col in df.columns

            if (
                col.lower() == "id"
                or col.lower().endswith("_id")
            )
        ]

        if id_cols:

            print(
                f"Dropping ID Columns: {id_cols}"
            )

            df.drop(
                columns=id_cols,
                inplace=True
            )

        return df

    # =====================================================
    # Load Dataset
    # =====================================================

    def load_data(self, file_path):

        df = pd.read_csv(file_path)

        # Remove IDs
        df = self.drop_id_columns(df)

        df.columns = [
            col.strip().lower()
            for col in df.columns
        ]

        self.detect_column_types(df)

        return df

    # =====================================================
    # Detect Column Types Automatically
    # =====================================================

    def detect_column_types(self, df):

        feature_df = df.drop(
            columns=[self.target_column],
            errors="ignore"
        )

        self.numeric_columns = feature_df.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()

        self.categorical_columns = feature_df.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        

        return {
            "numeric_columns": self.numeric_columns,
            "categorical_columns": self.categorical_columns
        }

    # =====================================================
    # Data Cleaning
    # =====================================================

    def clean_data(self, df):

        df = df.copy()

        df.columns = [
            col.strip().lower()
            for col in df.columns
        ]

        df.drop_duplicates(inplace=True)

        return df

    # =====================================================
    # Missing Values
    # =====================================================

    def handle_missing_values(self, df):

        df = df.copy()

        for col in self.numeric_columns:

            if col in df.columns:

                df[col] = df[col].fillna(
                    df[col].median()
                )

        for col in self.categorical_columns:

            if col in df.columns:

                mode_value = (
                    df[col].mode()[0]
                    if not df[col].mode().empty
                    else "Unknown"
                )

                df[col] = df[col].fillna(
                    mode_value
                )

        return df

    # =====================================================
    # Outlier Treatment
    # =====================================================

    def handle_outliers(self, df):

        df = df.copy()

        for col in self.numeric_columns:

            if col not in df.columns:
                continue

            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            df[col] = np.clip(
                df[col],
                lower,
                upper
            )

        return df

    # =====================================================
    # Build Pipeline
    # =====================================================

    def build_pipeline(self):

        numeric_pipeline = Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(
                        strategy="median"
                    )
                ),
                (
                    "scaler",
                    StandardScaler()
                )
            ]
        )

        categorical_pipeline = Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(
                        strategy="most_frequent"
                    )
                ),
                (
                    "encoder",
                    OneHotEncoder(
                        handle_unknown="ignore"
                    )
                )
            ]
        )

        self.preprocessor = ColumnTransformer(
            transformers=[
                (
                    "numeric",
                    numeric_pipeline,
                    self.numeric_columns
                ),
                (
                    "categorical",
                    categorical_pipeline,
                    self.categorical_columns
                )
            ],
            remainder="drop"
        )

        return self.preprocessor

    # =====================================================
    # Fit Transform
    # =====================================================

    def fit_transform(self, X):

        if self.preprocessor is None:

            self.build_pipeline()

        return self.preprocessor.fit_transform(X)

    # =====================================================
    # Transform
    # =====================================================

    def transform(self, X):

        return self.preprocessor.transform(X)

    # =====================================================
    # Split X and y
    # =====================================================

    def split_features_target(self, df):

        X = df.drop(
            columns=[self.target_column]
        )

        y = df[self.target_column]

        return X, y

    # =====================================================
    # Feature Columns
    # =====================================================

    def feature_columns(self):

        return (
            self.numeric_columns +
            self.categorical_columns
        )

    # =====================================================
    # Dataset Summary
    # =====================================================

    def dataset_summary(self, df):

        return {

            "rows":
                len(df),

            "columns":
                len(df.columns),

            "numeric_columns":
                self.numeric_columns,

            "categorical_columns":
                self.categorical_columns,

            "missing_values":
                df.isnull().sum().sum(),

            "duplicates":
                df.duplicated().sum()
        }