import time
from scraper import get_amazon_price
from notification import display_notification
from logger import log_price_change
from config import PRICE_DROP_THRESHOLD, CHECK_FREQUENCY

def main():
    previous_price = None
    prices = []  # Stores historical prices
    timestamps = []  # Stores corresponding timestamps

    while True:
        current_price = get_amazon_price()

        if current_price is None:
            print("Failed to fetch price. Retrying...")
        else:
            print(f"Current price: ${current_price}")

            # Track price and timestamp
            prices.append(current_price)
            timestamps.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # Check for price drop
            if previous_price is not None:
                price_drop = previous_price - current_price
                if price_drop >= PRICE_DROP_THRESHOLD:
                    print(f"Price drop detected: ${price_drop}")
                    display_notification(current_price, prices, timestamps)
                    log_price_change(current_price, True)  # Log with notification
                else:
                    log_price_change(current_price, False)  # Log without notification

            previous_price = current_price

        # Wait before next check
        time.sleep(CHECK_FREQUENCY)

if __name__ == '__main__':
    main()