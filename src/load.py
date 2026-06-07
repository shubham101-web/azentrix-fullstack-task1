import sqlite3
import os

def load_data(df):

    # Create database folder if not exists
    if not os.path.exists("database"):
        os.makedirs("database")

    # Connect to SQLite database
    conn = sqlite3.connect("database/covid.db")

    # Write DataFrame to SQL table
    df.to_sql(
        "covid_stats",
        conn,
        if_exists="replace",
        index=False
    )

    # Save and close connection
    conn.commit()
    conn.close()

    print("Database created successfully!")