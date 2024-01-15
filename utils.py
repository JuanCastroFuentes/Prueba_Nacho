import pandas as pd 
def import_excel_file_as_pd_df(file_path_to_import: str) -> pd.DataFrame:
    """This is a simple function to import Excel files into a pandas DataFrame."""
    df = pd.read_excel(file_path_to_import, engine='openpyxl', skiprows=[1, 2],header=0)
    return df