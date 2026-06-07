import os
import logging
from extract import extract_data
from transform import transform_data
from load import load_data

# --------------------------------------------------
# STEP 0: CREATE LOGS FOLDER (IF NOT EXISTS)
# --------------------------------------------------
# Ye ensure karta hai ki "logs" folder available ho
# warna logging file create nahi ho payegi
if not os.path.exists("logs"):
    os.makedirs("logs")

# --------------------------------------------------
# STEP 1: CONFIGURE LOGGING SYSTEM
# --------------------------------------------------
# Ye setup pipeline.log file me logs save karega
logging.basicConfig(
    filename="logs/pipeline.log",   # log file path
    filemode="a",                   # append mode (old logs keep rahenge)
    level=logging.INFO,             # INFO level logs capture karega
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# STEP 2: MAIN PIPELINE FUNCTION
# --------------------------------------------------
def run_pipeline():

    try:
        # Pipeline start log
        logging.info("Pipeline Started")

        # --------------------------------------------------
        # STEP 3: DATA EXTRACTION
        # --------------------------------------------------
        print("🚀 Extracting data...")
        df = extract_data()

        # Log number of rows extracted
        logging.info(f"Extracted Rows = {len(df)}")

        # --------------------------------------------------
        # STEP 4: DATA TRANSFORMATION
        # --------------------------------------------------
        print("🔄 Transforming data...")
        df = transform_data(df)

        # Transformation complete log
        logging.info("Data Transformation Completed")

        # --------------------------------------------------
        # STEP 5: LOAD DATA INTO DATABASE
        # --------------------------------------------------
        print("💾 Loading data into database...")
        load_data(df)

        # Database load success log
        logging.info("Data Loaded into SQLite Database")

        # Final success log
        logging.info(f"SUCCESS | Total Rows Processed = {len(df)}")

        print("✅ Pipeline completed successfully!")

    except Exception as e:

        # Error log (important for debugging)
        logging.error(f"FAILED | Error Occurred: {e}")

        print("❌ Error occurred:", e)

# --------------------------------------------------
# STEP 6: RUN PIPELINE
# --------------------------------------------------
run_pipeline()