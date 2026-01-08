import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert TotalCharges to numeric and drop missing values
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)

    # Drop identifier
    if 'customerID' in df.columns:
        df.drop(columns=['customerID'], inplace=True)

    # Encode categorical variables
    categorical_cols = df.select_dtypes(include='object').columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df