import pandas as pd

def preprocess_input(input_data: dict, expected_columns: list) -> pd.DataFrame:
    """
    Converts dictionary input into a DataFrame for model prediction,
    using the expected column order from the model.
    """
 
    for col in expected_columns:
        if col not in input_data:
            input_data[col] = 0

    df = pd.DataFrame([input_data])[expected_columns]
    return df