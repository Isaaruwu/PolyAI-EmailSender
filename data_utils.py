import pandas as pd

def transform_data(csv_file: str, columns_to_remove: list[int] = None) -> pd.DataFrame:
    df = pd.read_csv(csv_file)
    df = df.drop(df.columns[columns_to_remove], axis=1) if columns_to_remove else df

    return df.dropna()
