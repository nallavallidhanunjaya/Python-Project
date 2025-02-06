#!/bin/bash

# Variables
BUCKET_NAME="python-project-practice-020601"
PROJECT_DIR="/home/opc/dhanunjaya/job_scraper_notifier"
ZIP_FILE="job_scraper_notifier.zip"

# Step 1: Download latest project files from S3
echo "Downloading latest code from S3..."
aws s3 cp s3://$BUCKET_NAME/$ZIP_FILE /home/opc/dhanunjaya

# Step 2: Extract the files
echo "Extracting project files..."
rm -rf $PROJECT_DIR  # Remove old project folder
mkdir -p $PROJECT_DIR
unzip -o /home/opc/job_scraper_notifier/$ZIP_FILE -d $PROJECT_DIR

# Step 3: Install dependencies
#echo "Installing dependencies..."
#pip3 install -r $PROJECT_DIR/requirements.txt

# Step 4: Run scraper and email scripts
echo "Running job scraper..."
python3 $PROJECT_DIR/scraper.py

echo "Sending job listings email..."
python3 $PROJECT_DIR/send_email.py

echo "Job completed successfully!"
