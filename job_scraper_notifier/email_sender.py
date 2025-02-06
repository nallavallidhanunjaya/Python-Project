import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging
logging.basicConfig(filename="email.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    logging.info("Starting email sending process...")
    # Your existing email sending code here
    # Email Credentials (Replace with your own)
    EMAIL_SENDER = "dhanunjaya.pics@gmail.com"
    EMAIL_PASSWORD = "eamh lwhg tccb pqov"
    EMAIL_RECEIVER = "pardhunelakuditi99@gmail.com, "

    def load_job_data(csv_file):
        """Load job listings from CSV."""
        return pd.read_csv(csv_file)

    def format_job_listings(df):
        """Format job listings as an HTML table for email."""
        if df.empty:
            return "<p>No new job listings available.</p>"

        html = df.to_html(index=False, escape=False)
        return f"<h2>Latest Job Listings</h2>{html}"

    def send_email(subject, body):
        """Send an email with job listings."""
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(" Failed to send email:", e)

        if __name__ == "__main__":
            # Load job data
            df = load_job_data("remote_jobs.csv")

            # Format email body
            email_body = format_job_listings(df)

            # Send email
            send_email("Latest Remote Job Listings", email_body)
            logging.info("Email sent successfully!")
except Exception as e:
    logging.error(f"Email sending failed: {e}")
