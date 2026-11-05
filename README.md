# Hospital Patient Data Analyzer (PS No. 17)

## 1. Project Overview
Hospital Patient Data Analyzer is a Python-based project that cleans and analyzes hospital patient records from a CSV file to derive insights such as department-wise workload, average length of stay, and age group distributions.

## 2. Objectives
- Analyze hospital patient records efficiently using Pandas.
- Calculate department-wise and gender-wise patient counts.
- Compute individual and average length of stay for patients.
- Categorize patient age into standard brackets (0-40, 41-60, 61+).
- Clean invalid, missing, and duplicate records.
- Visualize patient distributions using Matplotlib charts.

## 3. Technologies Used
- **Language:** Python 3
- **Libraries:** Pandas, Matplotlib
- **Data Source:** CSV File (`patients.csv`)

## 4. Key Features
1. **Data Cleaning:** Automatically detects and removes duplicate `Patient_ID` records and imputes missing `Age` values using the median.
2. **Department-wise Analysis:** Counts patient admissions per department.
3. **Length of Stay Analysis:** Calculates the duration of hospital stay from admit and discharge dates.
4. **Age Distribution & Visualization:** Groups patients by age brackets and plots a Matplotlib bar chart.
5. **Gender-wise Breakdown:** Groups patient admissions by gender.

## 5. Requirements & Installation
Install the required dependencies using pip:
```bash
python -m pip install pandas matplotlib 

## 6. How to Run
1. Open the project folder in VS Code or Terminal.
2. Ensure patients.csv is present in the root folder alongside one.py.
3. Run the following command:
python one.py
4. Choose options 1 to 6 from the interactive CLI menu.

## 7. Input File Format (patients.csv)
The CSV file must contain the following schema:
Patient_ID,Age,Gender,Department,Admit_Date,Discharge_Date

## 8. Expected Outputs
- Department Count: Formatted breakdown (e.g., Cardiology: 2 | Ortho: 1) and total count.
- Length of Stay: Stay in days per patient and calculated average stay.
- Age Groups & Visualization: Inline summary counts and a pop-up bar chart window.
- Data Cleaning Report: Number of duplicates removed and median imputed.
## Project Mentor

**Mentored by:** [Mr. Satyaprakash Sethy](https://github.com/SATYAPRAKASHSETHY)

**GitHub:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)

**Role:** Python Mentor / Technical Guide 
