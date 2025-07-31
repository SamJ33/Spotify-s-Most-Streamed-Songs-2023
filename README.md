# 🎧 Analyzing Spotify’s Most-Streamed Songs of 2023

This Power BI dashboard project dives deep into the data behind Spotify’s most-streamed songs of 2023. From uncovering artist dominance to exploring listening patterns across days of the week, this analysis provides insights into global music consumption trends.

## 📊 Project Overview

The purpose of this project was to explore and visualize Spotify's streaming data for 2023. It allowed me to develop and sharpen my data transformation and visualization skills using:

- **Power BI** for building interactive dashboards
- **Power Query** for data cleaning and transformation
- **DAX (Data Analysis Expressions)** for creating custom measures and KPIs
- **Bravo for Power BI** to optimize and manage DAX calculations

---

## 🔍 Key Insights

1. **🎵 Artist Dominance**  
   A small group of artists such as **Taylor Swift**, **The Weeknd**, and **Bad Bunny** consistently led streaming charts throughout the year.

2. **📈 Longevity of Viral Hits**  
   Songs like *Blinding Lights* and *Heat Waves*—released years prior—continued to accumulate millions of streams, highlighting the extended lifecycle of viral tracks.

3. **🗓️ Streaming Peaks on Weekends**  
   Listening activity spiked on **Fridays and Saturdays**, likely influenced by new music releases and increased leisure time.

---

## 📁 Dataset

The dataset contains detailed metadata for each track. Columns include:

| Column Name             | Description |
|-------------------------|-------------|
| `track_name`            | Song title |
| `artist_name`           | Main performing artist |
| `artist_count`          | Number of contributing artists |
| `released_year/month/day` | Release date details |
| `in_spotify_playlists`  | Count of Spotify playlists including the track |
| `in_spotify_charts`     | Number of times the track appeared on Spotify charts |
| `streams`               | Total Spotify streams in 2023 |
| `in_apple_playlists`, `in_apple_charts` | Similar chart presence data from Apple Music |
| `in_deezer_playlists`, `in_deezer_charts` | Same for Deezer |
| `in_shazam_charts`      | Chart appearances on Shazam |
| `bpm`, `key`, `mode`    | Musical composition details |
| `danceability`, `valence`, `energy` | Audio features indicating feel and mood |
| `acousticness`, `instrumentalness`, `liveness`, `speechiness` | More nuanced audio characteristics |
| `spotify_track_url`     | Direct Spotify link to the track |
| `album_cover_url`       | Album art image URL | 

> 📌 Note: Data was cleaned and enriched in Power Query before analysis.

---

## 🧠 Skills Learned & Tools Used

| Skill / Tool      | Description |
|-------------------|-------------|
| Power BI          | Designed interactive visual dashboards |
| Power Query       | Cleaned and transformed raw datasets |
| DAX               | Created custom metrics (e.g., daily averages, total streams by artist) |
| Bravo for Power BI| Optimized DAX code and reviewed model performance |
| Data Storytelling | Developed a narrative around user behavior and artist performance |

---

## 📸 Dashboard Highlights

The Power BI dashboard includes:

- 📈 **Top Artists & Songs** ranked by total streams  
- 🧭 **Time-Based Trends**: daily/weekly listening behaviors  
- 🌍 **Geographic Insights** (if region-level data is included)  
- 🔁 **Song Longevity Tracking** across months  
- 📅 **Release Day Impact** on streaming success  
