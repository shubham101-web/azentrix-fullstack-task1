import pandas as pd

def transform_data(df):

    # Make copy to avoid modifying original data
    df = df.copy()

    # --------------------------------------------------
    # STEP 1: REMOVE NESTED COLUMN (countryInfo)
    # --------------------------------------------------
    if "countryInfo" in df.columns:
        df.drop(columns=["countryInfo"], inplace=True)

    # --------------------------------------------------
    # STEP 2: HANDLE NULL VALUES
    # --------------------------------------------------
    df.fillna("", inplace=True)

    # --------------------------------------------------
    # STEP 3: CLEAN COLUMN NAMES
    # --------------------------------------------------
    df.columns = [
        c.lower().replace(" ", "_")
        for c in df.columns
    ]

    # --------------------------------------------------
    # STEP 4: CONVERT NUMERIC COLUMNS SAFELY
    # --------------------------------------------------
    numeric_cols = ["cases", "recovered", "deaths", "active"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # --------------------------------------------------
    # STEP 5: SAFE DIVISION FUNCTION
    # --------------------------------------------------
    def safe_div(a, b):
        return (a / b.replace(0, 1)) * 100

    # --------------------------------------------------
    # STEP 6: DERIVED COLUMNS
    # --------------------------------------------------
    df["recovery_rate"] = safe_div(df["recovered"], df["cases"])
    df["death_rate"] = safe_div(df["deaths"], df["cases"])
    df["active_rate"] = safe_div(df["active"], df["cases"])

    # --------------------------------------------------
    # STEP 7: REMOVE DUPLICATES
    # --------------------------------------------------
    df.drop_duplicates(inplace=True)

    return df