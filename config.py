# config.py

# Amazon Product URL (Kindle Fire example, you can change it to the correct URL)
AMAZON_URL = 'https://www.amazon.in/Certified-Refurbished-Kindle-Oasis-10th/dp/B07L94CPN4/ref=sr_1_1?crid=J2GJEKIDGYY6&dib=eyJ2IjoiMSJ9.HcGjqs-ffsjCVcnAR_VHjVjl_QaAxLvmheNHJa1EoHAa7jPnEZChlyGQxChfI3gusdUEdaqqA2mC8xlxabHxIhvxc4mGThOZcyIFMZOxSxkl8nifVR4G9JEM25UcEQ53zsYjN1U_EJUTXkHNyfp6ysKFdhgVGgcOWBeudhTvBACb_75F4n1BupZEbVc2GMZKuz9zxaQcBDu70sMzYh8kCZKodpo0O0k3aJOURCH0s98.huWO8F0IValMI-y5H0WNND70lFoWixL7zt3mBvm0nJM&dib_tag=se&keywords=kindle&qid=1738241997&sprefix=kindle%2Caps%2C314&sr=8-1'  # URL for the Kindle Fire product page

# Price drop threshold (Set this value for the price drop trigger in dollars)
PRICE_DROP_THRESHOLD = 0  # Trigger notification if price drops by $5 or more

# Price check frequency (Set this value in hours to check the price)
CHECK_FREQUENCY = 5  # Check the price every 5 seconds

# User Agent to simulate a browser request (Usually fine as is, can be modified if needed)
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Log file path (This file will store all the price checks and notifications)
LOG_FILE = 'price_log.csv'  # Default file path for logging, you can change it if desired

