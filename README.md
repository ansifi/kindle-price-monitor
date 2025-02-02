# Kindle Price Monitor

This project monitors the price of the Kindle Fire on Amazon and sends an automated notification when the price drops by a specified threshold.

[![Watch the video](https://img.youtube.com/vi/IeScBgtNUzo/maxresdefault.jpg)](https://youtu.be/IeScBgtNUzo)

## Features
- **Web Scraping**: Extracts the Kindle price from Amazon.
- **Automated Notifications**: Displays a pop-up when the price drops.
- **Logging**: Logs price changes and notification events.
- **Configurable Threshold**: Users can set a price drop threshold.

## Prerequisites
- **Python 3.9 or later**
- **Miniconda (Optional, recommended for environment management)**
- **Google Chrome** (For Selenium-based scraping, if needed)

## Installation & Setup

### 1. Clone the Repository
```sh
 git clone https://github.com/yourusername/kindle-price-monitor.git
 cd kindle-price-monitor
```

### 2. Set Up a Virtual Environment
Using Miniconda:
```sh
 conda create --name kindle-price-monitor python=3.9
 conda activate kindle-price-monitor
```
Using venv:
```sh
 python -m venv venv
 source venv/bin/activate  # On macOS/Linux
 venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
 pip install -r requirements.txt
```

### 4. Configure `config.py`
Edit the `config.py` file and set up:
- `AMAZON_URL`: The Amazon product page URL.
- `USER_AGENT`: Your browser's user-agent string.
- `PRICE_DROP_THRESHOLD`: Set the price drop limit.
- `CHECK_FREQUENCY`: Frequency of price checks (in seconds).

### 5. Run the Script
```sh
 python main.py
```

## File Structure
```
kindle-price-monitor/
│-- __pycache__/             # Compiled Python files (ignore in Git)
│-- config.py                # Configuration settings
│-- logger.py                # Logs price changes
│-- main.py                  # Main script to run the monitor
│-- notification.py           # Handles popup notifications
│-- price_log.csv            # CSV file logging price history
│-- README.md                # Project documentation
│-- requirements.txt         # Required Python packages
│-- scraper.py               # Web scraping logic
```

## Dependencies
These are installed via `requirements.txt`:
- `beautifulsoup4` (For web scraping)
- `requests` (For making HTTP requests)
- `pandas` (For data handling)
- `plyer` (For notifications)
- `logging` (For logging events)
- `csv` (For handling price logs)



