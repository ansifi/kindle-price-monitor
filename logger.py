import pandas as pd
from datetime import datetime
from config import LOG_FILE

def log_price_change(price, notification_sent):
    log_data = {
        'timestamp': [datetime.now()],
        'price': [price],
        'notification_sent': [notification_sent]
    }
    df = pd.DataFrame(log_data)
    df.to_csv(LOG_FILE, mode='a', header=False, index=False)
    print("Price change logged successfully!")
