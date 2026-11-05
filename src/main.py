"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.80},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.40},
        "Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.90},
    }

    for name, user_prefs in profiles.items():
        print(f"\n{name} — Top 5 recommendations\n")
        recommendations = recommend_songs(user_prefs, songs, k=5)

        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"   Because: {explanation}")


if __name__ == "__main__":
    main()