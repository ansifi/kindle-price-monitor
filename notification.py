from plyer import notification
import plotly.graph_objects as go
import webbrowser
import tempfile
import os

def generate_price_chart(prices, timestamps):
    """
    Generate an interactive price chart using Plotly and save it as an HTML file.
    """
    # Create the chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timestamps, y=prices, mode='lines+markers', name='Price'))
    fig.update_layout(
        title="Price Trend",
        xaxis_title="Time",
        yaxis_title="Price ($)",
        template="plotly_white"
    )

    # Save the chart to a temporary HTML file
    temp_dir = tempfile.gettempdir()
    chart_path = os.path.join(temp_dir, 'price_chart.html')
    fig.write_html(chart_path)

    return chart_path

def display_notification(current_price, prices, timestamps):
    # prices = [100, 95, 90, 85, 80]
    # timestamps = ["2023-10-01 10:00", "2023-10-01 11:00", "2023-10-01 12:00", "2023-10-01 13:00", "2023-10-01 14:00"]
   
     # Generate the price chart
    chart_path = generate_price_chart(prices, timestamps)

    # Open the chart in the default web browser
    webbrowser.open(f"file://{chart_path}")

    notification.notify(
        title="Price Drop Alert",
        message=f"Price has dropped to ${current_price}",
        timeout=3  # Notification will appear for 3 seconds
    )