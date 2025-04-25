import csv
import matplotlib.pyplot as plt

from datetime import datetime

def load_runs(file):
    with open("data/runs.csv", "r") as f:

        reader = csv.DictReader(f)
        return [row for row in reader]

def calculate_stats(runs):
    total_distance = 0
    total_time = 0
    best_10k = float("inf")
    best_21k = float("inf")

    for run in runs:
        dist = float(run["distance_km"])
        time = float(run["time_min"])
        total_distance += dist
        total_time += time

        if 9.5 <= dist <= 10.5 and time < best_10k:
            best_10k = time
        if 20.5 <= dist <= 21.5 and time < best_21k:
            best_21k = time

    avg_pace = total_time / total_distance
    return total_distance, avg_pace, best_10k, best_21k


def write_markdown(stats):
    # Open the file with UTF-8 encoding
    with open("output/dashboard.md", "w", encoding="utf-8") as f:
        f.write("# 🏃 Running Stats Dashboard\n")
        f.write(f"**Total Distance:** {stats[0]:.2f} km\n\n")
        f.write(f"**Average Pace:** {stats[1]:.2f} min/km\n\n")
        f.write(f"**Best 10K Time:** {stats[2]} min\n\n")
        f.write(f"**Best Half Marathon:** {stats[3]} min\n\n")
        f.write("🚀 Keep pushing!\n")

def plot_distance_over_time(runs):
    dates = [row["date"] for row in runs]
    distances = [float(row["distance_km"]) for row in runs]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, distances, marker='o')
    plt.title("Distance Over Time")
    plt.xlabel("Date")
    plt.ylabel("Distance (km)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/distance_graph.png")
   

if __name__ == "__main__":
    runs = load_runs("data/runs.csv")
    stats = calculate_stats(runs)
    plot_distance_over_time(runs)

    write_markdown(stats)
