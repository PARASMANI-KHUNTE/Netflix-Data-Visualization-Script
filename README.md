# Netflix-Data-Visualization-Script
This Python script reads a CSV file containing Netflix titles, cleans the data, and provides insightful visualizations using libraries like Pandas, Matplotlib, and Seaborn.

Features
Data Cleaning: Handles inconsistent or invalid dates in the dataset.
Visualizations:
Count of Movies vs. TV Shows.
Distribution of release years.
Prerequisites
Before running this script, ensure you have the following installed:

Python 3.13 or above
Required Python packages:
pandas
matplotlib
seaborn
Installation Guide
1. Clone or Download the Repository
bash
Copy code
git clone https://github.com/PARASMANI-KHUNTE/Netflix-Data-Visualization-Script.git
cd Netflix-Data-Visualization-Script
2. Install Python
Download and install Python 3.13 or higher from the official Python website. Ensure Python is added to your system's PATH.

3. Install Required Packages
Run the following command to install the necessary Python libraries:

bash
Copy code
pip install pandas matplotlib seaborn
4. Prepare the Dataset
Ensure you have the netflix_titles.csv file in the same directory as the script.

How to Run the Script
Step 1: Open Terminal or Command Prompt
Navigate to the directory containing the script:

bash
Copy code
cd path/to/your/directory
Step 2: Run the Script
Run the script using Python:

bash
Copy code
python AssignmentOne.py
Expected Output
Visualizations:
Count of Movies and TV Shows:

A bar plot showing the number of movies vs. TV shows in the dataset.
Distribution of Release Years:

A histogram visualizing the frequency of titles released over the years.
Troubleshooting
Error: ModuleNotFoundError
If you encounter an error like:

vbnet
Copy code
ModuleNotFoundError: No module named 'pandas'
Ensure all required libraries are installed. Re-run:

bash
Copy code
pip install pandas matplotlib seaborn
Error: Invalid date_added
The script automatically cleans inconsistent dates. Invalid dates are converted to NaT (Not a Time).

Contribution
Feel free to contribute by submitting pull requests or reporting issues.

License
This project is licensed under the MIT License.

Author
Your Name
GitHub: YourGitHubProfile
LinkedIn: YourLinkedInProfile

This README.md provides clear instructions for setup, running, and troubleshooting, ensuring ease of use for all users.







