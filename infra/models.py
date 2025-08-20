from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Track(Base):
    __tablename__ = "tracks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    downforce_type = Column(String, nullable=False)  # high/medium/low
    straight_length_m = Column(Integer)
    similarity_group = Column(String)  # e.g., low-df, high-df

    races = relationship("Race", back_populates="track")

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    drivers = relationship("Driver", back_populates="team")
    ratings = relationship("TeamRating", back_populates="team")

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    team = relationship("Team", back_populates="drivers")
    results = relationship("Result", back_populates="driver")

class Race(Base):
    __tablename__ = "races"
    id = Column(Integer, primary_key=True)
    season = Column(Integer, nullable=False)
    round = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False)

    track = relationship("Track", back_populates="races")
    results = relationship("Result", back_populates="race")

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True)
    race_id = Column(Integer, ForeignKey("races.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    position = Column(Integer)
    points = Column(Float)
    avg_lap_time_ms = Column(Integer)

    race = relationship("Race", back_populates="results")
    driver = relationship("Driver", back_populates="results")

class TeamRating(Base):
    __tablename__ = "team_ratings"
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    season = Column(Integer, nullable=False)
    downforce_rating = Column(Float)
    tire_wear_rating = Column(Float)
    aero_rating = Column(Float)
    straight_speed_rating = Column(Float)

    team = relationship("Team", back_populates="ratings")
