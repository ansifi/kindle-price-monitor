# Kindle Price Monitoring

This project monitors the price of the Kindle Fire on Amazon and sends an automated notification when the price drops by a specified threshold.

## Setup

1. Clone the repository and navigate to the project folder.
2. Set up a Python virtual environment (using Miniconda or another tool).
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Configure your settings in `config.py` (AMAZON_URL, etc.).
5. Run the script:
   ```
   python main.py
   ```

## Features
- Web scraping for price extraction
- Automated notifications via popup
- Logs price changes and notifications
- Configurable price drop threshold

## Requirements
- Python 3.9
"# kindle-price-monitor" 
