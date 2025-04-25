# Running Stats Dashboard

This project is a personal dashboard that tracks and visualizes running statistics. It displays various stats such as total distance, best 10K, best half marathon time, and also includes a distance vs. time graph.

## Project Structure

- **data**: Contains the `runs.csv` file, where your running data (e.g., distance, time, date) is stored.
- **scripts**: Includes Python scripts for processing the data and generating visualizations:
  - `update_stats.py`: Processes the `runs.csv` file and calculates statistics such as total distance, average pace, best 10K time, and best half marathon time.
  - `run_dashboard.sh`: A shell script to automate running the `update_stats.py` script.
- **output**: Stores the generated distance-over-time graph (`distance_graph.png`).

## How It Works

### 1. Data Processing
The script `update_stats.py` processes the running data from the `runs.csv` file. It calculates:
- Total distance covered
- Average pace
- Best 10K and best half marathon times

The processed data is saved and can be used for further analysis or reporting.

### 2. Data Visualization
Using `matplotlib`, the script generates a graph of distance over time and saves it as `distance_graph.png` in the `output` folder. This visualization helps track your running progress over time.

### 3. Running the Project
To run the project:
1. Make sure you have Python installed, along with the necessary libraries:
   ```
   pip install matplotlib
   ```
2. Run the script `update_stats.py` to process the data and generate the graph:
   ```
   python scripts/update_stats.py
   ```
3. The generated graph will be saved in the `output` folder as `distance_graph.png`.

## Credits

Special thanks to ChatGPT, which guided me through the process of writing the graph generation code and helped with structuring the project.

---

### Changes:
- Removed the Flask app section since you're not using it.
- Focused on the graph generation part, explaining how the data is processed and visualized.
- Acknowledged ChatGPT's help with the graph code.

Feel free to modify or expand on this! Let me know if you'd like any more changes.
