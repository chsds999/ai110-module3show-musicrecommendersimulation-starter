# 🎵 Music Recommender Simulation

## Project Summary

I built a Python command-line recommender that ranks a catalog of 18 songs based on a listener’s preferred genre, mood, and energy. It displays the top five tracks for each example profile and explains how each track earned its score.

## How The System Works

Music recommenders can look for patterns in listening behavior, such as likes, skips, and playlist saves. This simulator uses content-based filtering. It compares the listener’s preferences with the attributes of each song in `data/songs.csv`.

- **Song data** uses `genre`, `mood`, and `energy` for scoring. The title and artist identify the track in the results.
- **User profiles** specify a preferred `genre`, a preferred `mood`, and a target `energy` from 0 to 1. The first example profile asks for happy pop with an energy of 0.80.

### Scoring and Ranking

The baseline gives 2 points for an exact genre match, 1 point for an exact mood match, and up to 1 point for energy similarity. Energy similarity is calculated as `1 - abs(song_energy - target_energy)`. A smaller energy gap earns more points.

For the happy-pop profile, Sunrise City earns 2 points for pop, 1 point for happy, and 0.98 for its energy of 0.82. That gives it 3.98 out of 4.00. The program scores every song, sorts the scores from highest to lowest, and displays the five highest-ranked songs with their reasons.

## Getting Started

### Setup

Run these commands from the project root on macOS or Linux.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m src.main
```

On Windows PowerShell, create the environment with `py -m venv .venv` and activate it with `.\.venv\Scripts\Activate.ps1`. Then use the same install and run commands.

### Running Tests

```bash
python -m pytest -q
```

Both starter tests passed during the baseline verification run.

## Sample Recommendation Output

```text
Loaded songs: 18

High-Energy Pop — Top 5 recommendations

1. Sunrise City by Neon Echo - Score: 3.98
   Because: Genre match (+2.00), Mood match (+1.00), Energy similarity (+0.98)
2. Gym Hero by Max Pulse - Score: 2.87
   Because: Genre match (+2.00), Energy similarity (+0.87)
3. Rooftop Lights by Indigo Parade - Score: 1.96
   Because: Mood match (+1.00), Energy similarity (+0.96)
4. City in Motion by Metro Signal - Score: 0.97
   Because: Energy similarity (+0.97)
5. Night Drive Loop by Neon Echo - Score: 0.95
   Because: Energy similarity (+0.95)
```

## Experiments You Tried

### Comparing Listener Profiles

I ran the baseline with High-Energy Pop, Chill Lofi, and Intense Rock. Each profile’s top song matched both its genre and mood. Gym Hero placed second for both Pop and Rock. Its pop genre helped it in the first list, while its intense mood helped it in the second. The Chill Lofi and Intense Rock lists shared no tracks.

```text
Chill Lofi — Top 5 recommendations

1. Midnight Coding by LoRoom - Score: 3.98
   Because: Genre match (+2.00), Mood match (+1.00), Energy similarity (+0.98)
2. Library Rain by Paper Lanterns - Score: 3.95
   Because: Genre match (+2.00), Mood match (+1.00), Energy similarity (+0.95)
3. Focus Flow by LoRoom - Score: 3.00
   Because: Genre match (+2.00), Energy similarity (+1.00)
4. Spacewalk Thoughts by Orbit Bloom - Score: 1.88
   Because: Mood match (+1.00), Energy similarity (+0.88)
5. Last Train Home by Blue Avenue - Score: 0.98
   Because: Energy similarity (+0.98)
```

```text
Intense Rock — Top 5 recommendations

1. Storm Runner by Voltline - Score: 3.99
   Because: Genre match (+2.00), Mood match (+1.00), Energy similarity (+0.99)
2. Gym Hero by Max Pulse - Score: 1.97
   Because: Mood match (+1.00), Energy similarity (+0.97)
3. Run Through the Rain by Static Avenue - Score: 0.96
   Because: Energy similarity (+0.96)
4. Into the Strobe by Prism Circuit - Score: 0.94
   Because: Energy similarity (+0.94)
5. City in Motion by Metro Signal - Score: 0.93
   Because: Energy similarity (+0.93)
```

### Changing the Scoring Weights

I halved the genre bonus from 2 points to 1 and doubled the maximum energy bonus from 1 point to 2. Mood stayed at 1 point.

| High-Energy Pop song | Baseline rank and score | Experimental rank and score |
|---|---|---|
| Sunrise City | #1 · 3.98 | #1 · 3.96 |
| Gym Hero | #2 · 2.87 | #3 · 2.74 |
| Rooftop Lights | #3 · 1.96 | #2 · 2.92 |

Rooftop Lights moved ahead of Gym Hero because it matched the happy mood and was closer to the target energy. Chill Lofi and Intense Rock kept the same order.

## Limitations and Risks

- The catalog has 18 songs, including eight fictional tracks added to broaden genre and mood coverage. Genres with few tracks have fewer chances to appear.
- Exact genre matching treats pop and indie pop as separate labels. With the baseline weights, an exact genre match can outweigh a better fit on mood and energy.
- The ranking uses three song attributes. Listener ratings would help evaluate whether people enjoy the recommendations.

See the [Model Card](model_card.md) for the full evaluation and limitations.

## Reflection

I learned how much a recommender’s weights affect what a listener sees. Rooftop Lights moved ahead of Gym Hero even though the songs and the profile stayed the same. I also found it interesting that Gym Hero could rank second for two different profiles. The score breakdown showed which preferences mattered in each case.

AI helped me brainstorm new songs and work through the scoring math. I checked the calculations against the terminal output. The experiment showed me how an exact genre bonus can make related music harder to discover. Next, I’d collect listener ratings to see where the rankings fit people’s taste and where they miss.
