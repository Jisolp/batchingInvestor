# Batching Investors

## Description
The script analyzes investor descriptions from an Excel sheet, checks how well they match specific industry-related keywords, assigns priority levels based on keyword relevance, and organizes the data into batches for further analysis or outreach.

## Process:
1. Load Data: Reads an Excel file containing company descriptions.
2. Keyword Matching: Checks if the description contains predefined keywords.
3. Priority Assignment: Categorizes companies into four priority levels based on keyword match percentage.
4. Batching: Groups companies into batches of 50 within each priority category.
5. Export Results: Saves the processed data into a new Excel file with separate sheets for each priority and batch.

## Prerequisites
- Python
- `pandas` library
- A CSV file containing (`Email`, `Name`, `Company`,`Company location and Description`)

## Installation
1. Clone this repository to your local machine.
2. Install the required Python libraries:
3. Prepare your `investor.csv` file
5. RUN python batch.py
