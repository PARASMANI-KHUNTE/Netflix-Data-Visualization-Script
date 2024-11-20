🎥 Netflix Data Visualization Script
A Python-based script for analyzing and visualizing Netflix data from a CSV file. This project helps uncover insights like the distribution of movies vs. TV shows and trends in release years using interactive plots.

✨ Features
📊 Data Cleaning: Automatically handles inconsistent or invalid date entries.
📈 Data Visualization:
Count of Movies vs. TV Shows: See which type dominates the Netflix catalog.
Release Year Trends: Discover how Netflix's content library has evolved over time.
🛠️ Prerequisites
Ensure you have the following installed before proceeding:

Python: Version 3.13 or higher.
Required Libraries:
pandas
matplotlib
seaborn
📥 Installation Guide
1️⃣ Clone or Download the Repository
bash
Copy code
git clone https://github.com/PARASMANI-KHUNTE/Netflix-Data-Visualization-Script.git
cd Netflix-Data-Visualization-Scrip
2️⃣ Install Python
Download and install Python 3.13+ from the official website.
Ensure Python is added to your system's PATH during installation.
3️⃣ Install Required Libraries
Run the following command to install the necessary Python libraries:

bash
Copy code
pip install pandas matplotlib seaborn
4️⃣ Add the Dataset
Place the netflix_titles.csv file in the same directory as the script. You can download it from sources like Kaggle or use your custom Netflix data.

🚀 How to Run the Script
Step 1: Open Terminal or Command Prompt
Navigate to the directory where the script is located:

bash
Copy code
cd path/to/your/directory
Step 2: Run the Script
Execute the script using Python:

bash
Copy code
python AssignmentOne.py
🖼️ Visualizations You’ll See
Count of Movies and TV Shows
A bar chart illustrating the distribution of movies and TV shows in the dataset.

Distribution of Release Years
A histogram showing how the content library has grown over the years.

🛠️ Troubleshooting
❌ Error: ModuleNotFoundError
If you encounter:

vbnet
Copy code
ModuleNotFoundError: No module named 'pandas'
Ensure the required libraries are installed:

bash
Copy code
pip install pandas matplotlib seaborn
❌ Error: Invalid date_added
The script automatically cleans invalid dates by replacing them with NaT (Not a Time).

🙌 Contribute
Have ideas for improvement or found a bug? Contributions are welcome!

Fork the repository
Create a new branch for your feature/bugfix
Submit a pull request
📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

👩‍💻 Author
Parasmani Khunte
🌐 [GitHub Profile](https://github.com/PARASMANI-KHUNTE) | 💼 [LinkedIn Profile](https://www.linkedin.com/in/parasmani-khunte-330488228/)
