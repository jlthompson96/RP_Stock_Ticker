import time
import unicornhat as uh
from datetime import datetime
import requests
import logging
from PIL import Image, ImageDraw, ImageFont

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Unicorn HAT setup
uh.brightness(0.5)
uh.clear()

# Load font
FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 6)

# Polygon.io API setup
API_KEY = "POLYGON.IO API KEY"
STOCKS = ["AAPL", "TSLA", "NVDA", "MSFT", "RKLB", "PLTR", "CRWD", "CRSP", "MRVI"]  # List of stocks

# Function to fetch stock open price
def get_open_price(stock):
    api_url = f"https://api.polygon.io/v1/open-close/{stock}/{datetime.now().strftime('%Y-%m-%d')}?adjusted=true&apiKey={API_KEY}"
    try:
        response = requests.get(api_url)
        data = response.json()
        logging.info(f"Open price API Response for {stock}: {data}")  # Log full response
        return data.get("open")
    except Exception as e:
        logging.error(f"Error fetching open price for {stock}: {e}")
        return None

# Function to fetch last trade price
def get_last_trade_price(stock):
    api_url = f"https://api.polygon.io/v2/last/trade/{stock}?apiKey={API_KEY}"
    try:
        response = requests.get(api_url)
        data = response.json()
        logging.info(f"Last trade API Response for {stock}: {data}")  # Log full response
        return data.get("results", {}).get("p")
    except Exception as e:
        logging.error(f"Error fetching last trade price for {stock}: {e}")
        return None

# Function to scroll text across Unicorn HAT
def scroll_text(text, color):
    width, height = uh.get_shape()
    text_width = FONT.getbbox(text)[2]
    img = Image.new("RGB", (text_width + width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, font=FONT, fill=color)
    
    for x_offset in range(text_width + width):
        for x in range(width):
            for y in range(height):
                if 0 <= x + x_offset < img.width:
                    pixel = img.getpixel((x + x_offset, y))
                    uh.set_pixel(x, y, *pixel)
        uh.show()
        time.sleep(0.15)  # Further slowing down scrolling speed

# Function to display stock info
def display_stock_info():
    for stock in STOCKS:
        open_price = get_open_price(stock)
        last_price = get_last_trade_price(stock)
        
        if open_price is None or last_price is None:
            continue

        percent_change = ((last_price - open_price) / open_price) * 100
        
        # Determine color
        if last_price > open_price:
            color = (0, 255, 0)  # Green
        else:
            color = (255, 0, 0)  # Red
        
        text = f"{stock} ${last_price:.2f} ({percent_change:.2f}%)"
        logging.info(f"Scrolling: {text}")
        scroll_text(text, color)
        time.sleep(1)
    
# Main loop
while True:
    display_stock_info()
    time.sleep(10)  # Short pause before cycling again
