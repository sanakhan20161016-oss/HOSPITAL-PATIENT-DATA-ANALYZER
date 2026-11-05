import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
def load_data():
    try:
        df = pd.read_csv("patients.csv")
        print("\nPatient data loaded successfully!")
        return df
    except FileNotFoundError:
        print("Error: patients.csv file not found!")
        return None


# Clean patient data
def clean_data(df):
    duplicate_count = df.duplicated(subset="Patient_ID").sum()
    df = df.drop_duplicates(subset="Patient_ID", keep="first").copy()

    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df.loc[df["Age"] < 0, "Age"] = None

    missing_age = df["Age"].isna().sum()

    if missing_age > 0:
        median_age = df["Age"].median()
        if pd.isna(median_age):
            median_age = 0
        else:
            median_age = int(round(median_age))
        df["Age"] = df["Age"].fillna(median_age)
    else:
        median_val = df["Age"].median()
        median_age = int(round(median_val)) if not pd.isna(median_val) else 0

    df["Gender"] = df["Gender"].fillna("Unknown")
    df["Department"] = df["Department"].fillna("Unknown")

    df["Admit_Date"] = pd.to_datetime(df["Admit_Date"], errors="coerce")
    df["Discharge_Date"] = pd.to_datetime(df["Discharge_Date"], errors="coerce")

    df["Length_of_Stay"] = (df["Discharge_Date"] - df["Admit_Date"]).dt.days

    return df, duplicate_count, missing_age, median_age


# Department-wise patient count (Test Case 1 match)
def department_analysis(df):
    counts = df["Department"].value_counts()
    formatted_counts = " | ".join([f"{dept}: {count}" for dept, count in counts.items()])
    print(formatted_counts)
    print("Total patients:", len(df))


# Length of stay analysis (Test Case 2 match)
def stay_analysis(df):
    valid_stays = df["Length_of_Stay"].dropna()

    if valid_stays.empty:
        print("\nNo valid stay dates found.")
        return

    for _, row in df.iterrows():
        if pd.notna(row["Length_of_Stay"]):
            print(f"{row['Patient_ID']}: {int(row['Length_of_Stay'])} days")

    avg_stay = valid_stays.mean()
    print(f"Average stay: {avg_stay:.2f} days")


# Age group analysis and bar chart (Test Case 4 match)
def age_analysis(df):
    valid_stays = df["Length_of_Stay"].dropna()
    if not valid_stays.empty:
        print(f"Average stay: {valid_stays.mean():.2f} days")

    bins = [-1, 40, 60, float("inf")]
    labels = ["0-40", "41-60", "61+"]
    df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

    age_counts = df["Age_Group"].value_counts().reindex(labels, fill_value=0)
    formatted_groups = " | ".join([f"{group}: {count}" for group, count in age_counts.items()])
    print(f"Age groups: {formatted_groups}")

    # Bar chart display
    plt.figure(figsize=(6, 4))
    age_counts.plot(kind="bar", color="steelblue", edgecolor="black")
    plt.title("Hospital Patients by Age Group")
    plt.xlabel("Age Groups")
    plt.ylabel("Number of Patients")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# Data cleaning report (Test Case 3 match)
def cleaning_report(duplicates, missing, median):
    print("Duplicates removed:", duplicates)
    if missing > 0:
        print("Missing Age filled with median:", median)
    else:
        print("No missing Age values found.")


# Gender-wise analysis
def gender_analysis(df):
    print("\nGender-wise Patient Count:")
    counts = df["Gender"].value_counts()
    print(" | ".join([f"{g}: {c}" for g, c in counts.items()]))


# Main program
def main():
    df = load_data()

    if df is None:
        return

    required_columns = [
        "Patient_ID", "Age", "Gender",
        "Department", "Admit_Date", "Discharge_Date"
    ]

    if not all(column in df.columns for column in required_columns):
        print("Error: CSV file has missing columns!")
        return

    df, duplicates, missing, median = clean_data(df)

    print("\n===== HOSPITAL PATIENT DATA ANALYZER =====")

    while True:
        print("\n1. Department-wise Patient Count")
        print("2. Length of Stay Analysis")
        print("3. Age Groups and Bar Chart")
        print("4. Data Cleaning Report")
        print("5. Gender-wise Analysis")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            department_analysis(df)
        elif choice == "2":
            stay_analysis(df)
        elif choice == "3":
            age_analysis(df)
        elif choice == "4":
            cleaning_report(duplicates, missing, median)
        elif choice == "5":
            gender_analysis(df)
        elif choice == "6":
            print("\nThank you for using Hospital Patient Data Analyzer!")
            break
        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()