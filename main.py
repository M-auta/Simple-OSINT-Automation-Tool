"""
OSINT Investigation Automation Tool
------------------------------------
This script aggregates, processes, and generates structured reports
from open-source data based on user-provided keywords.

Author: Your Name
"""

import requests
import logging
import datetime
import json
from typing import List, Dict


# -------------------------------
# CONFIGURATION
# -------------------------------

logging.basicConfig(
    filename="investigation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

REPORT_FILE = "investigation_report.txt"


# -------------------------------
# DATA INGESTION
# -------------------------------

def fetch_public_api_data(keyword: str) -> List[Dict]:
    """
    Fetch mock public data from a placeholder API.
    Replace with real OSINT APIs where permitted.
    """
    logging.info(f"Fetching data for keyword: {keyword}")

    # Example public placeholder API
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return []


# -------------------------------
# DATA FILTERING / CLEANING
# -------------------------------

def filter_data_by_keyword(data: List[Dict], keyword: str) -> List[Dict]:
    """
    Filter dataset based on keyword match.
    """
    logging.info("Filtering data")

    keyword = keyword.lower()
    filtered = [
        item for item in data
        if keyword in item.get("title", "").lower()
        or keyword in item.get("body", "").lower()
    ]

    logging.info(f"Found {len(filtered)} relevant records")
    return filtered


# -------------------------------
# REPORT GENERATION
# -------------------------------

def generate_report(keyword: str, results: List[Dict]) -> None:
    """
    Generate structured text report.
    """
    logging.info("Generating report")

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("OSINT Investigation Report\n")
        f.write("=" * 40 + "\n")
        f.write(f"Keyword: {keyword}\n")
        f.write(f"Generated on: {datetime.datetime.now()}\n")
        f.write(f"Total Matches: {len(results)}\n\n")

        for idx, item in enumerate(results, start=1):
            f.write(f"Result #{idx}\n")
            f.write(f"Title: {item.get('title')}\n")
            f.write(f"Content: {item.get('body')}\n")
            f.write("-" * 40 + "\n")

    logging.info("Report successfully created")


# -------------------------------
# MAIN WORKFLOW
# -------------------------------

def run_investigation(keyword: str):
    logging.info("Starting investigation workflow")

    raw_data = fetch_public_api_data(keyword)
    filtered_results = filter_data_by_keyword(raw_data, keyword)
    generate_report(keyword, filtered_results)

    logging.info("Investigation completed successfully")


# -------------------------------
# ENTRY POINT
# -------------------------------

if __name__ == "__main__":
    print("=== OSINT Investigation Tool ===")
    user_keyword = input("Enter keyword to investigate: ").strip()

    if not user_keyword:
        print("Keyword cannot be empty.")
    else:
        run_investigation(user_keyword)
        print("Investigation complete. Check investigation_report.txt")
