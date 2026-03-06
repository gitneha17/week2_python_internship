**#🐍 Week 2 – Data Cleaning Script (Python)
**
👩‍💻 Intern Name: Neha Beldar
🏢 Organization: Skybrisk
📅 Internship Month: 1

## 📌 Project Overview

This project focuses on performing **basic data cleaning operations using Python and the Pandas library**. Data cleaning is an essential step in the data analysis process because raw datasets often contain missing values, duplicate records, or irrelevant data.

The goal of this project is to create a Python script that cleans a dataset and prepares it for further analysis.

## 🎯 Objectives

* Load a dataset using Python
* Identify and remove duplicate records
* Handle missing values
* Filter relevant data
* Save the cleaned dataset for further use

## 🛠 Technologies Used

* **Python**
* **Pandas Library**
* **CSV Dataset**

## 📂 Project Structure

Week2_DataCleaning/
│
├── data_cleaning.py
├── student_scores.csv
└── cleaned_student_scores.csv

## ⚙️ Data Cleaning Steps

The Python script performs the following operations:

1. **Load Dataset**

   * The dataset is loaded using `pandas.read_csv()`.

2. **Remove Duplicate Records**

   * Duplicate rows are removed using `drop_duplicates()` to ensure data consistency.

3. **Handle Missing Values**

   * Missing values in the dataset are handled using `fillna()`.

4. **Filter Data**

   * The dataset is filtered to extract students who scored above a specific threshold.

5. **Save Cleaned Dataset**

   * The cleaned dataset is exported to a new CSV file using `to_csv()`.


## ▶️ How to Run the Script

1. Install required library
pip install pandas

2. Run the Python script
python data_cleaning.py

3. The cleaned dataset will be generated as:
cleaned_student_scores.csv


## 📊 Sample Dataset

| Name  | Subject | Score | City   |
| ----- | ------- | ----- | ------ |
| Amit  | Math    | 85    | Nashik |
| Neha  | Math    | 90    | Nashik |
| Rahul | Science | NaN   | Mumbai |
| Pooja | Math    | 78    | Pune   |


## 📈 Output

After running the script:

* Duplicate records are removed
* Missing values are handled
* Filtered results are generated
* A **cleaned CSV file** is created

## 📚 Concepts Learned

* Data preprocessing
* Handling missing values
* Removing duplicates
* Filtering datasets
* Exporting cleaned data
* Working with Pandas DataFrames

## 🚀 Author

**Neha Beldar**

Data Analytics & Cloud Computing Enthusiast
