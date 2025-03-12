# Book Scraper using BeautifulSoup
## Project Description
This Python script scrapes book data from Books to Scrape using BeautifulSoup and requests. It extracts book details such as:
✅ Title
✅ Price
✅ Availability (In Stock/Out of Stock)
✅ Book Link

The scraped data is then saved into a CSV file (books.csv) using Pandas for easy analysis.
## How It Works
🔹 The script iterates through multiple pages of books on the website.
🔹 It extracts book details using HTML parsing with BeautifulSoup.
🔹 If the page does not exist (404 error), the script stops.
🔹 The data is saved into a CSV file for further use.

## Installation & Setup
### Requirements:
Make sure you have the following installed:

Python 3.x
Required Python libraries (requests, BeautifulSoup4, pandas)
### Installation Steps:
 **1. Clone this repository:**
    git clone https://github.com/ZubeKahloon/Scraping_With_BeautifulSoup.git

**2. Navigate to the project directory:**
   cd Scraping_With_BeautifulSoup

**3. Install required dependencies:**
   pip install -r requirements.txt

**4. Run the script:**
   python filename.py
   After execution, a books.csv file will be created containing the scraped book data.

## Technologies Used
🔹 Python 🐍
🔹 BeautifulSoup (Web Scraping)
🔹 Requests (Fetching Web Pages)
🔹 Pandas (Data Processing & CSV Handling)

## Contributing
Want to improve this project? Feel free to fork the repository and submit a pull request. 🚀

## Author & Contact
Developed by **Zube**
