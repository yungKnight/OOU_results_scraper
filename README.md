# OOU_results_scraper
A dynamic web scraper written in Python and based off Playwright and Scrapy that aims to extract student results from the university page at ease depending on user input, meant to be able to run in parallel mode in times of multiple input to save time, and saves the extracted results for each student dynamically on your computer 


## Project Dependencies Version

- Python >= 3.12.1
- Scrapy >= 2.1.0
- Playwright >= 1.43.0

## Installation

To set up this project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yungKnight/OOU_results_scraper.git
   ```

2. **Check into directory:**
   ```sh
   cd OOU_results_scraper
   ```

3. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

4. **Activate virtual environment: (On windows)**
   ```sh
   source venv\Scripts\activate
   ```

5. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Navigate to your project directory**
   ```sh
   cd path/to/OOU_results_scraper
    ```

2. **Execute the scraper:**
   ```sh
   pytest oou_scraper.py
    ```

3. When you run the script, it will prompt you to enter the matric number and password.


## Additional Information
- **Parallel Execution:** The scraper is designed to run in parallel mode for handling multiple inputs simultaneously. Ensure your system meets the necessary requirements for parallel processing.
- **Dynamic Saving:** The results for each student are saved dynamically on your computer in the specified directory.
