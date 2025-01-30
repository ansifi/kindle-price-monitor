from plyer import notification

def display_notification(price):
    notification.notify(
        title="Price Drop Alert",
        message=f"Price has dropped to ${price}",
        timeout=3  # Notification will appear for 3 seconds
    )