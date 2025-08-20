from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import csv
import os
import threading
import time
import sys

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#these are methods that basically shoot data to the frontend
def load_csv(filename: str, key_column: str = "name"):
    """Loads a CSV into a dict keyed by a specific column."""
    data = {}
    csv_path = os.path.join(os.path.dirname(__file__), filename)
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row[key_column].lower()] = row
    return data

@app.get("/raceinfo") #for race data
async def race_info(race: str = Query(..., description="Race name (from CSV 'name' column)")):
    race_data = track_data.get(race.lower())
    if not race_data:
        raise HTTPException(status_code=404, detail=f"No data found for race '{race}'")
    return JSONResponse(content=race_data)

@app.get("/driverinfo") #for driver data (not used rn)
async def driver_info(driver: str = Query(..., description="Driver name (from CSV 'name' column)")):
    driver_row = driver_data.get(driver.lower())
    if not driver_row:
        raise HTTPException(status_code=404, detail=f"No data found for driver '{driver}'")
    return JSONResponse(content=driver_row)

@app.get("/tabledata") #for table data
async def table_data_endpoint():
    return list(table_data.values())

#loading different CSV files so they can be read by dictreader
track_data = load_csv("trackinfo.csv", key_column="name")
driver_data = load_csv("drivers.csv", key_column="name")
table_data = load_csv("table.csv", key_column="pos")  
raw_data = load_csv("data.csv", key_column="race_id")

@app.get("/races/upcoming") #for raw race data for frontend
def get_upcoming_races():
    return list(raw_data.values())

    

# commented out because i dont need driver data rn
    return {
        "race_id": race_id,
        "predictions": [
            {"driver": "Max Verstappen", "expected_finish": 1, "podium_prob": 0.9},
            {"driver": "Lando Norris", "expected_finish": 2, "podium_prob": 0.7},
            {"driver": "Lewis Hamilton", "expected_finish": 3, "podium_prob": 0.6}
        ]
    }