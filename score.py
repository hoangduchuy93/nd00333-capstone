from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core.dataset import Dataset

def clean_data(data):
    df = data.to_pandas_dataframe().dropna()
    # Fill NaN
    df["Age"].fillna(df["Age"].median(skipna=True), inplace=True)
    df['Embarked'].fillna(df["Embarked"].value_counts().idxmax(), inplace=True)
    df.drop("Cabin", axis=1, inplace=True)

    # Create categorial variable for traveling along
    df["TravelAnone"] = np.where((df["SibSp"]+df["Parch"])<0, 0, 1)
    df.drop("SibSp", axis=1, inplace=True)
    df.drop("Parch", axis=1, inplace=True)

    # Create categorical variables and drop some variables
    df = pd.get_dummies(df, columns=["Pclass", "Embarked", "Sex"], drop_first=True)
    df.drop("PassengerId", axis=1, inplace=True)
    df.drop("Name", axis=1, inplace=True)
    df.drop("Ticket", axis=1, inplace=True)

    Selected_features = [col for col in df.columns.values if col not in ["Survived"]]
    x_df = df[Selected_features]
    y_df = df["Survived"]
    return x_df, y_df

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    # TODO: Create TabularDataset using TabularDatasetFactory
    # Data is located at:
    # "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv"
    data_url = "https://raw.githubusercontent.com/hoangduchuy93/nd00333-capstone/refs/heads/main/train_survival.csv"
    ds = TabularDatasetFactory.from_delimited_files(data_url)
    
    x, y = clean_data(ds)

    # TODO: Split data into train and test sets.

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)

    #save model
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/model.joblib')
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()