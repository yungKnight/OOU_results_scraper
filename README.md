# OOU Results Scraper

A robust web scraper built with Python, leveraging Playwright and Scrapy to efficiently extract student results from the university portal. Designed for seamless batch processing with parallel execution capabilities to handle multiple student records simultaneously while dynamically saving extracted results to your local machine.

## Features

- **Parallel Processing**: Handle multiple student credentials concurrently to save time
- **Dynamic Result Storage**: Automatically saves results for each student in organized JSON format
- **Error Handling**: Gracefully handles cases where results are unavailable or network issues occur
- **User-Friendly**: Interactive prompts for easy credential input

## Project Dependencies

- Python >= 3.12.1
- Scrapy >= 2.1.0
- Playwright >= 1.43.0
- pytest >= 6.0.0

## Installation

Follow these steps to set up the project:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yungKnight/OOU_results_scraper.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd OOU_results_scraper
   ```

3. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   
   **On Windows:**
   ```sh
   venv\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```sh
   source venv/bin/activate
   ```

5. **Install required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

6. **Install Playwright browser dependencies:**
   ```sh
   playwright install
   ```

## Usage

1. **Navigate to your project directory:**
   ```sh
   cd path/to/OOU_results_scraper
   ```

2. **Run the scraper:**
   ```sh
   pytest -s oou_scraper.py
   ```

3. **Follow the interactive prompts:**
   - Enter the number of student credentials you want to process
   - Input each student's matric number and password when prompted
   - The scraper will process all credentials in parallel and save results automatically

## Output

- Results are saved in the `results/` directory
- Each student's results are stored as a separate JSON file named `result_{StudentName}.json`
- Files contain structured data with Session, Semester, Course, and Grade information

## Error Handling

The scraper includes comprehensive error handling for common scenarios:
- **Unavailable Results**: Displays "Results not available for student at the moment" when results aren't accessible
- **Network Issues**: Continues processing other students even if one fails
- **Invalid Credentials**: Handles authentication errors gracefully

## System Requirements

- **Memory**: Sufficient RAM for parallel browser instances (recommended: 4GB+)
- **Network**: Stable internet connection for accessing the university portal
- **Storage**: Adequate disk space for saving result files

## Troubleshooting

- Ensure all dependencies are properly installed
- Verify that Playwright browsers are installed using `playwright install`
- Check your internet connection if the scraper fails to load pages
- Make sure the university portal is accessible and operational