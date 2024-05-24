# OOU_results_scraper
A dynamic web scraper written in Python and based off Playwright and Scrapy that aims to extract student results from the university page at ease depending on user input, meant to be able to run in parallel mode in times of multiple input to save time, and saves the extracted results for each student dynamically on your computer 


## Project Dependencies Version

- Python >= 3.12.1
- Scrapy >= 2.1.0
- Playwright >= 1.43.0

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository_url>

2. **Navigate to your project directory**
   ```sh
   cd path/to/OOU_results_scraper
   
3. **Install required dependencies by running this command on your terminal using ```pip```:**

   ```
   pip install pytest pytest-asyncio asyncio playwright scrapy
   ```
   
   +++ This installs ```pytest```, the ```pytest-asyncio``` plugin, ```asyncio```, ```playwright``` and ```scrapy``` +++

4. **Install browser for ```playwright``` (chromium browser for this project):**

   ```
   playwright install chromium
   ```
## Usage
1. **Navigate to your project directory**
   ```sh
   cd path/to/OOU_results_scraper

2. **Execute the scraper:**
   ```sh
   python oou_scraper.py

## Additional Information
- **Parallel Execution:** The scraper is designed to run in parallel mode for handling multiple inputs simultaneously. Ensure your system meets the necessary requirements for parallel processing.
- **Dynamic Saving:** The results for each student are saved dynamically on your computer in the specified directory.
