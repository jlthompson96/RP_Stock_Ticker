# 📈 Stock Ticker Display

This Python script runs on a **Raspberry Pi** with a **Unicorn HAT** LED matrix to display real-time stock price updates. It fetches stock data from **Polygon.io** and scrolls the stock ticker, last trade price, and percentage change from the opening price.

## 🛠 Hardware Requirements
- **Raspberry Pi 3/4/5** (Tested on Raspberry Pi 5)
- **Pimoroni Unicorn HAT** (Original, not HD)
- **Power Supply** (Ensure adequate power for the LED matrix)
- **MicroSD Card** (With Raspberry Pi OS installed)
- **Internet Connection** (For API requests)

## 📦 Software & Packages Needed
Ensure your Raspberry Pi is set up with the necessary dependencies:

### 📌 **System Setup**
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-pil python3-requests
pip3 install unicornhat
pip3 install rpi_ws281x

## ✨ Features

### 📡 **Stock Data Retrieval**
- Fetches **opening prices** of multiple stocks at the start of the day.
- Retrieves **last trade price** for real-time updates.

### 🎨 **Dynamic Display on Unicorn HAT**
- Scrolls **stock symbol**, **last price**, and **% change**.
- **Color-coded price changes**:
  - 🟢 **Green** if the price is up.
  - 🔴 **Red** if the price is down.

### 🛠 **Performance & Logging**
- **Slowed down scrolling speed** for better readability.
- **Log statements** track API responses and display updates in the console.

### 🔄 **Auto-Refresh**
- Loops through stocks continuously with a **10-second refresh interval**.

---

## ⚙️ **How It Works**
1. The script fetches the **opening price** for each stock from **Polygon.io**.
2. It then retrieves the **last trade price**.
3. Calculates the **percentage change** from the opening price.
4. Displays the stock **symbol, price, and % change** on the **Unicorn HAT LED matrix**.
5. **Colors and scrolling** help indicate trends.
6. The display **updates every 10 seconds**.

---

## 🔧 **Possible Enhancements**
- ✨ **Blinking effect** for large price swings.
- 🔄 **Ability to switch between different data sources**.
- 💾 **Data caching** for reduced API calls.
- 🖥 **Web dashboard** to configure displayed stocks.
