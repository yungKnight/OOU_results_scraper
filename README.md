# OOU_results_scraper
A dynamic web scraper written in Python and based off Playwright and Scrapy that aims to extract student results from the university page at ease depending on user input and meant to be able to run in parallel in times of multiple input to save time 


# PROJECT DEPENDENCIES VERSION
* Python >= 3.12.1
* Scrapy >= 2.1.0
* Playwright >= 1.43.0


# INSTALLATION
1. Clone the repository

2. Navigate to your project directory
   
3. Install required dependencies by running this command on your terminal using ```pip```:

   ```
   pip install pytest pytest-asyncio asyncio playwright scrapy
   ```
   
   +++ This installs ```pytest```, the ```pytest-asyncio``` plugin, ```asyncio```, ```playwright``` and ```scrapy``` +++

5. Install browser for ```playwright``` (chromium browser for this project):

   ```
   playwright install chromium
   ```
