# Survey Data Visualization Project

This project visualizes the results of a synthetic survey dataset using Python. It uses various static plots to uncover patterns in user satisfaction, demographics, and engagement.

## Features

* Generates a dummy survey dataset of 500 responses.
* Saves dataset as a CSV file (`survey_data.csv`).
* Creates the following visualizations:

  * Bar chart of survey responses by age group
  * Pie chart of gender distribution
  * Bar chart of average satisfaction by platform used
  * Heatmap showing recommendation rate by age group
* Saves all plots as PNG files.

## Dataset Fields

* **Age Group**: \['Under 18', '18-25', '26-35', '36-50', '50+']
* **Gender**: \['Male', 'Female', 'Other']
* **Satisfaction**: Integer rating from 1 (low) to 5 (high)
* **Platform Used**: \['Mobile App', 'Website', 'Email']
* **Usage Frequency**: \['Daily', 'Weekly', 'Monthly', 'Rarely']
* **Would Recommend**: \['Yes', 'No']

## Dependencies

* Python 3.x
* pandas
* numpy
* matplotlib
* seaborn

Install dependencies using:

```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run

Execute the script using:

```bash
python survey_visualization.py
```

This will:

* Generate a synthetic survey dataset and save it to `survey_data.csv`
* Generate and save all visualizations as PNG images

## Output Files

* `survey_data.csv` — the raw dataset
* `age_group_bar.png`
* `gender_pie.png`
* `satisfaction_by_platform.png`
* `recommendation_heatmap.png`

## License

MIT License
