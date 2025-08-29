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

def load_csv_list(filename: str):
    """Loads a CSV into a list of dicts."""
    csv_path = os.path.join(os.path.dirname(__file__), filename)
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def load_race_predictions(race_id: int):
    """Load race-specific predictions from CSV file."""
    csv_path = os.path.join(os.path.dirname(__file__), "race_predictions.csv")
    predictions = []
    
    try:
        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['race_id']) == race_id:
                    predictions.append({
                        "driver": row['driver'],
                        "team": row['team'],
                        "rating": float(row['rating']),
                        "performance": float(row['performance']),
                        "podium_prob": row['podium_prob'],
                        "pts_prob": row['pts_prob'],
                        "points": row['points'],
                        "expected_finish": int(row['expected_finish'])
                    })
    except FileNotFoundError:
        # Fallback to mock data if CSV doesn't exist
        return generate_fallback_predictions(race_id)
    
    # Sort by expected finish position
    predictions.sort(key=lambda x: x['expected_finish'])
    return predictions

def load_qualifying_predictions(race_id: int):
    """Load race-specific qualifying predictions from CSV file."""
    csv_path = os.path.join(os.path.dirname(__file__), "qualifying_predictions.csv")
    predictions = []
    
    try:
        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['race_id']) == race_id:
                    predictions.append({
                        "driver": row['driver'],
                        "team": row['team'],
                        "q1_time": row['q1_time'],
                        "q2_time": row['q2_time'],
                        "q3_time": row['q3_time'],
                        "pole_prob": row['pole_prob'],
                        "q3_prob": row['q3_prob']
                    })
    except FileNotFoundError:
        # Fallback to mock data if CSV doesn't exist
        return generate_fallback_qualifying_predictions(race_id)
    
    # Sort by position
    predictions.sort(key=lambda x: int(row['pos']))
    return predictions

def generate_fallback_predictions(race_id: int):
    """Generate fallback predictions if CSV file is not available."""
    # This is fallback data - replace with actual ML model predictions
    base_predictions = [
        {"driver": "Max Verstappen", "team": "Red Bull", "rating": 98.5, "performance": 99.0, "podium_prob": "92%", "pts_prob": "95%", "points": "+25", "expected_finish": 1},
        {"driver": "Lando Norris", "team": "McLaren", "rating": 97.8, "performance": 98.2, "podium_prob": "88%", "pts_prob": "92%", "points": "+18", "expected_finish": 2},
        {"driver": "Charles Leclerc", "team": "Ferrari", "rating": 96.5, "performance": 97.1, "podium_prob": "85%", "pts_prob": "89%", "points": "+15", "expected_finish": 3},
        {"driver": "Oscar Piastri", "team": "McLaren", "rating": 96.2, "performance": 96.8, "podium_prob": "82%", "pts_prob": "86%", "points": "+12", "expected_finish": 4},
        {"driver": "Lewis Hamilton", "team": "Ferrari", "rating": 95.8, "performance": 96.3, "podium_prob": "78%", "pts_prob": "83%", "points": "+10", "expected_finish": 5},
        {"driver": "George Russell", "team": "Mercedes", "rating": 94.5, "performance": 95.1, "podium_prob": "75%", "pts_prob": "80%", "points": "+8", "expected_finish": 6},
        {"driver": "Carlos Sainz", "team": "Ferrari", "rating": 94.2, "performance": 94.7, "podium_prob": "72%", "pts_prob": "77%", "points": "+6", "expected_finish": 7},
        {"driver": "Fernando Alonso", "team": "Aston Martin", "rating": 93.8, "performance": 94.2, "podium_prob": "68%", "pts_prob": "74%", "points": "+4", "expected_finish": 8},
        {"driver": "Lance Stroll", "team": "Aston Martin", "rating": 92.5, "performance": 93.1, "podium_prob": "65%", "pts_prob": "71%", "points": "+2", "expected_finish": 9},
        {"driver": "Valtteri Bottas", "team": "Kick Sauber", "rating": 91.8, "performance": 92.4, "podium_prob": "62%", "pts_prob": "68%", "points": "+1", "expected_finish": 10}
    ]
    
    # Adjust predictions based on race_id (different tracks favor different teams)
    # This is where you'd implement track-specific logic
    if race_id == 1:  # Australian GP - high downforce track
        # McLaren and Ferrari typically strong on high downforce tracks
        pass
    elif race_id == 2:  # Chinese GP - mixed characteristics
        pass
    elif race_id == 3:  # Japanese GP - high speed corners
        pass 
    
    return base_predictions

def generate_fallback_qualifying_predictions(race_id: int):
    """Generate fallback qualifying predictions if CSV file is not available."""
    # Fallback qualifying data
    return [
        {"driver": "Max Verstappen", "team": "Red Bull", "q1_time": "1:24.156", "q2_time": "1:23.847", "q3_time": "1:23.456", "pole_prob": "85%", "q3_prob": "95%"},
        {"driver": "Lando Norris", "team": "McLaren", "q1_time": "1:24.234", "q2_time": "1:23.912", "q3_time": "1:23.567", "pole_prob": "12%", "q3_prob": "92%"},
        {"driver": "Charles Leclerc", "team": "Ferrari", "q1_time": "1:24.345", "q2_time": "1:24.023", "q3_time": "1:23.678", "pole_prob": "3%", "q3_prob": "88%"},
        {"driver": "Oscar Piastri", "team": "McLaren", "q1_time": "1:24.456", "q2_time": "1:24.134", "q3_time": "1:23.789", "pole_prob": "0%", "q3_prob": "85%"},
        {"driver": "Lewis Hamilton", "team": "Ferrari", "q1_time": "1:24.567", "q2_time": "1:24.245", "q3_time": "1:23.890", "pole_prob": "0%", "q3_prob": "82%"},
        {"driver": "George Russell", "team": "Mercedes", "q1_time": "1:24.678", "q2_time": "1:24.356", "q3_time": "1:23.901", "pole_prob": "0%", "q3_prob": "78%"},
        {"driver": "Carlos Sainz", "team": "Ferrari", "q1_time": "1:24.789", "q2_time": "1:24.467", "q3_time": "1:23.912", "pole_prob": "0%", "q3_prob": "75%"},
        {"driver": "Fernando Alonso", "team": "Aston Martin", "q1_time": "1:24.890", "q2_time": "1:24.578", "q3_time": "1:23.923", "pole_prob": "0%", "q3_prob": "72%"},
        {"driver": "Lance Stroll", "team": "Aston Martin", "q1_time": "1:25.001", "q2_time": "1:24.689", "q3_time": "1:23.934", "pole_prob": "0%", "q3_prob": "68%"},
        {"driver": "Valtteri Bottas", "team": "Kick Sauber", "q1_time": "1:25.112", "q2_time": "1:24.800", "q3_time": "1:23.945", "pole_prob": "0%", "q3_prob": "65%"}
    ]

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

@app.get("/races/upcoming") #for raw race data for frontend
def get_upcoming_races():
    return list(raw_data.values())

@app.get("/predictions/{race_id}") #for race-specific predictions
async def get_race_predictions(race_id: int):
    """Get predictions for a specific race from CSV file"""
    predictions = load_race_predictions(race_id)
    return JSONResponse(content={
        "race_id": race_id,
        "predictions": predictions
    })

@app.get("/qualifying/{race_id}") #for race-specific qualifying predictions
async def get_qualifying_predictions(race_id: int):
    """Get qualifying predictions for a specific race from CSV file"""
    predictions = load_qualifying_predictions(race_id)
    return JSONResponse(content={
        "race_id": race_id,
        "predictions": predictions
    })

@app.get("/teams") #for team data
async def get_teams():
    return load_csv_list("teams.csv")

@app.get("/drivers") #for driver data
async def get_drivers():
    return load_csv_list("drivers.csv")

@app.get("/team-ratings") #for team ratings
async def get_team_ratings():
    return load_csv_list("team_ratings.csv")

#loading different CSV files so they can be read by dictreader
track_data = load_csv("trackinfo.csv", key_column="name")
driver_data = load_csv("drivers.csv", key_column="name")
table_data = load_csv("table.csv", key_column="pos")  
raw_data = load_csv("data.csv", key_column="race_id") 