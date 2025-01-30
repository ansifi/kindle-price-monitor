import time
from scraper import get_amazon_price
from notification import display_notification
from logger import log_price_change
from config import PRICE_DROP_THRESHOLD, CHECK_FREQUENCY

def main():
    previous_price = None

    while True:
        current_price = get_amazon_price()

        if current_price is None:
            print("Failed to fetch price. Retrying...")
        else:
            print(f"Current price: ${current_price}")

            if previous_price is not None:
                price_drop = previous_price - current_price
                if price_drop >= PRICE_DROP_THRESHOLD:
                    print(f"Price drop detected: ${price_drop}")
                    display_notification(current_price)
                    log_price_change(current_price, True)
                else:
                    log_price_change(current_price, False)

            previous_price = current_price

        # Wait before checking again
        time.sleep(CHECK_FREQUENCY)

if __name__ == '__main__':
    main()
