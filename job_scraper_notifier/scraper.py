from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


import logging

# Configure logging
logging.basicConfig(filename="scraper.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    logging.info("Starting job scraping...")
    # Your existing scraping code here
    def scrape_jobs_selenium(query, location, num_pages=1):
        job_list = []

        # Set up Chrome WebDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        for page in range(num_pages):
            url = f"https://www.indeed.com/jobs?q={query}&l={location}&start={page*10}"
            driver.get(url)
            time.sleep(3)  # Wait for page to load
            
            job_cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")

            for job_card in job_cards:
                try:
                    title = job_card.find_element(By.TAG_NAME, "h2").text.strip()
                except:
                    title = "No Title"
                
                try:
                    company = job_card.find_element(By.CLASS_NAME, "jobTitle.css-1psdjh5.eu4oa1w0").text.strip()
                except:
                    company = "No Company"

                try:
                    location = job_card.find_element(By.CLASS_NAME, "company_location.css-i375s1.e37uo190").text.strip()
                except:
                    location = "No Location"
                
                job_list.append({"Title": title, "Company": company, "Location": location})

        driver.quit()
        df = pd.DataFrame(job_list)
        df.to_csv("job_listing.csv",index=False)
        print("Job data saved to job_listings.csv")
        return job_list

    # Run the scraper
    if __name__ == "__main__":
        jobs = scrape_jobs_selenium("python developer", "remote", num_pages=2)
        for job in jobs[:5]:  # Display first 5 jobs
            print(job)
    logging.info("Scraping completed successfully!")
except Exception as e:
    logging.error(f"Scraping failed: {e}")
