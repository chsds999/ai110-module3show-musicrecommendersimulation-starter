# 🎧 Model Card — Music Recommender Simulation

**Author:** Sai Cherukuru  
**Contact:** chsds999@gmail.com

## 1. Model Name

VibeFinder 1.0

## 2. Intended Use

VibeFinder is a classroom simulator that recommends five songs based on a listener’s preferred genre, mood, and energy. It assumes the listener can describe what they want with one genre, one mood, and one energy level from 0 to 1. A real streaming service would need a larger catalog and feedback from listeners to evaluate its recommendations.

## 3. How the Model Works

I replaced the starter placeholders for loading, scoring, and ranking with a working command-line recommender. It reads the catalog and compares each song with the listener’s preferences.

An exact genre match earns two points, and an exact mood match earns one. A song can earn up to one more point based on how close its energy is to the listener’s target. The program sorts the songs by total score and shows the top five with an explanation of how each earned its points.

## 4. Data

The catalog has 18 songs. I kept the 10 starter tracks and added eight fictional tracks to expand the range of genres and moods. The catalog includes genres such as pop, lofi, rock, folk, and EDM, and moods such as happy, chill, intense, and sad.

The file also stores tempo, valence, danceability, and acousticness. The recommender scores songs using genre, mood, and energy. The catalog has no listener ratings or information about lyrics or language.

## 5. Strengths

The recommender works well when the catalog contains songs that match the requested genre, mood, and energy. For example, Midnight Coding and Library Rain both matched chill lofi. Midnight Coding ranked first because its energy was closer to the target of 0.40. The point breakdown made it easy to see why one song ranked above the other.

## 6. Limitations and Bias

The baseline gives an exact genre match twice as many points as a mood match. Gym Hero ranked above Rooftop Lights for happy pop, even though Rooftop Lights matched the happy mood and was closer to the target energy. The system treats pop and indie pop as separate labels. With only 18 songs and uneven genre coverage, that preference for exact matches can narrow what listeners discover.

## 7. Evaluation

I ran the CLI with three profiles and checked the top five songs and their explanations. Both starter tests passed. I judged whether the rankings fit the profiles I entered. Measuring how much listeners actually liked the results would require listener feedback.

- **High-Energy Pop and Chill Lofi.** Sunrise City led the pop list, while Midnight Coding led the lofi list. Both matched their profile’s genre and mood, but each was close to a different energy target.
- **High-Energy Pop and Intense Rock.** Gym Hero ranked second in both. Its pop genre helped in the first list, while its intense mood and high energy helped in the second.
- **Chill Lofi and Intense Rock.** Their top five songs did not overlap. The lofi list favored mellow songs, while the rock list included high-energy punk and EDM tracks.

I also halved the genre bonus from two points to one and doubled the maximum energy score from one point to two. The mood bonus stayed at one point. Rooftop Lights moved from third to second for High-Energy Pop, passing Gym Hero. The Chill Lofi and Intense Rock lists kept the same order. For a happy-pop playlist, the new order better reflects the requested mood and energy when an exact pop match matters less.

## 8. Future Work

- Let listeners select multiple genres or give partial credit to
  related genres such as pop and indie pop.
- Add a discovery pick that matches the requested mood and energy
  from a different genre.
- Collect listener ratings and compare them with the rankings to
  see which scoring weights fit people’s preferences.

## 9. Personal Reflection

I was surprised that Gym Hero ranked second for two different profiles. The explanations showed that one song can fit different listeners for different reasons. I also saw how changing the weights could move a song up the list even when the catalog and the profile stayed the same.

AI helped me brainstorm songs and work through the scoring math. I
checked the calculations against the terminal output. The project made me pay more attention to what music apps might be prioritizing when they recommend a song, especially when the result fits one part of my taste better than another.