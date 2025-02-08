#!/bin/bash

# Variables
BUCKET_NAME="python-project-practice-020601"
ZIP_FILE="job_scraper_notifier.zip"
PROJECT_DIR="/home/opc/dhanunjaya/job_scraper_notifier"
DOWNLOAD_PATH="/home/opc/dhanunjaya/$ZIP_FILE"

# Step 1: Download latest project files from S3
echo "Downloading latest code from S3..."
aws s3 cp s3://$BUCKET_NAME/$ZIP_FILE $DOWNLOAD_PATH

# Step 2: Extract the files
echo "Extracting project files..."
rm -rf $PROJECT_DIR  # Remove old project folder
mkdir -p $PROJECT_DIR
unzip -o $DOWNLOAD_PATH -d $PROJECT_DIR

# Step 3: Install dependencies
#echo "Installing dependencies..."
#pip3 install -r $PROJECT_DIR/requirements.txt

# Step 4: Run scraper and email scripts
echo "Running job scraper..."
python3 $PROJECT_DIR/scraper.py

echo "Sending job listings email..."
python3 $PROJECT_DIR/send_email.py

echo "✅ Job completed successfully!"
