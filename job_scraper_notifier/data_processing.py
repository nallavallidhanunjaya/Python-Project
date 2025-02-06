import pandas as pd
import numpy as np

def load_and_clean_data(csv_file):
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    # Remove duplicate job listings
    df.drop_duplicates(inplace=True)

    # Fill missing values with "Not Available"
    df.fillna("Not Available", inplace=True)

    return df

def filter_jobs(df, keyword):
    # Convert titles to lowercase for case-insensitive filtering
    return df[df['Title'].str.contains(keyword, case=False, na=False)]

def save_filtered_jobs(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Filtered jobs saved to {output_file}")

if __name__ == "__main__":
    # Load and clean job data
    df = load_and_clean_data("job_listing.csv")

    # Example: Filter jobs for "Remote" roles
    remote_jobs = filter_jobs(df, "Remote")

    # Save filtered jobs
    save_filtered_jobs(remote_jobs, "remote_jobs.csv")

    # Print a preview
    print("Top 5 Remote Jobs:\n", remote_jobs.head())
