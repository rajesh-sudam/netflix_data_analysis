Netflix Content Trends Analysis

Project Overview
This project explores the Netflix Titles dataset using Python, Pandas, Matplotlib, and Seaborn to uncover trends in Netflix's content library.

The objective is to understand:

How Netflix content has grown over time
Movie vs TV Show distribution
Country-wise content contributions
Content ratings distribution
Genre popularity
Director and actor trends
Content release and addition patterns
Dataset
Dataset: Netflix Titles Dataset

Features include:

Show ID
Title
Type (Movie / TV Show)
Director
Cast
Country
Release Year
Date Added
Rating
Duration
Genre
Description
Project Structure
Netflix/
│
├── data/
│   └── netflix_titles.csv
│
├── src/
│   └── analysis.ipynb
│
├── visuals/
│   ├── content_growth.png
│   ├── rating_distribution.png
│   ├── top_countries.png
│   └── ...
│
├── tests/
│   └── test_data.py
│
├── .github/
│   └── workflows/
│       └── python.yml
│
├── requirements.txt
├── .gitignore
└── README.md
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Pytest
Git
GitHub Actions
Exploratory Data Analysis
Data Cleaning
Missing value analysis
Date formatting
Feature extraction
Data quality validation
Visualizations
Netflix Content Added Per Year
Movies vs TV Shows Trends
Top Countries by Content Count
Content Rating Distribution
Most Frequent Actors
Most Frequent Directors
Genre Distribution
Monthly Content Additions
Key Insights
Netflix experienced significant growth after 2015.
Movies dominate the platform compared to TV Shows.
The United States contributes the largest amount of content.
Drama-related genres appear most frequently.
Most content targets mature audiences.
Content additions peaked during Netflix's rapid expansion years.
Running the Project
Clone Repository
git clone https://github.com/rajesh-sudam/netflix_data_analysis.git
cd netflix_data_analysis
Install Dependencies
pip install -r requirements.txt
Run Analysis
jupyter notebook
or

python src/analyze.py
Tests
Run project tests:

pytest
GitHub Actions
This project includes a GitHub Actions workflow that:

Sets up Python
Installs dependencies
Executes automated tests
Verifies project integrity on every push
Workflow file:

.github/workflows/python.yml
Future Improvements
Interactive Streamlit Dashboard
Genre Trend Analysis
Actor Collaboration Network
Recommendation System
Deployment to Streamlit Cloud
