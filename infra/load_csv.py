from pathlib import Path
import pandas as pd
from sqlalchemy import text
from .db import engine, Base

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_csv_to_table(csv_name: str, table_name: str):
    path = DATA_DIR / csv_name
    df = pd.read_csv(path)
    df.to_sql(table_name, engine, if_exists="append", index=False)

def main():
    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    # Optional: clear existing rows for a clean reload
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM results"))
        conn.execute(text("DELETE FROM team_ratings"))
        conn.execute(text("DELETE FROM races"))
        conn.execute(text("DELETE FROM drivers"))
        conn.execute(text("DELETE FROM teams"))
        conn.execute(text("DELETE FROM tracks"))

    # Load in dependency order
    load_csv_to_table("tracks.csv", "tracks")
    load_csv_to_table("teams.csv", "teams")
    load_csv_to_table("drivers.csv", "drivers")
    load_csv_to_table("race_calendar.csv", "races")
    load_csv_to_table("team_ratings.csv", "team_ratings")
    load_csv_to_table("driver_results.csv", "results")

    print("✅ Loaded CSV data into the database at", engine.url)

if __name__ == "__main__":
    main()
