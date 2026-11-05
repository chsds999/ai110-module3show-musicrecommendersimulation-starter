from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert their numeric fields."""
    songs = []

    with open(csv_path, encoding="utf-8", newline="") as file:
        for song in csv.DictReader(file):
            song["id"] = int(song["id"])
            song["tempo_bpm"] = int(song["tempo_bpm"])

            for field in ("energy", "valence", "danceability", "acousticness"):
                song[field] = float(song[field])

            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a song's relevance score and the reasons it earned points."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("Genre match (+2.00)")

    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("Mood match (+1.00)")

    energy_gap = abs(song["energy"] - user_prefs["energy"])
    energy_points = 1.0 - energy_gap
    score += energy_points
    reasons.append(f"Energy similarity (+{energy_points:.2f})")

    return score, reasons

def recommend_songs(
    user_prefs: Dict, songs: List[Dict], k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs with their scores and explanations."""
    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        recommendations.append((song, score, explanation))

    recommendations.sort(key=lambda recommendation: recommendation[1], reverse=True)
    return recommendations[:k]
