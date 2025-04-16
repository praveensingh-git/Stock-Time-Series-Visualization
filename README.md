# 📈 Stock Time Series Visualization

This project is a modular Python-based system that fetches stock price data from Yahoo Finance and generates interactive visualizations using Plotly. It focuses on Apple Inc. (AAPL) over the past 2 years.

---
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100">

## 🔍 Features

- 📊 Fetch historical stock data via `yfinance`
- ✅ Auto-corrects column format from `yfinance` MultiIndex output
- 📈 Generates:
  - Line plot of stock closing prices
  - OHLC Candlestick chart (with and without slider)
  - Bar chart of closing prices
  - Line plot for a custom 6-month date range
- 🧩 Modular design using:
  - `data_fetcher.py` for data retrieval
  - `visualization.py` for reusable chart functions
  - `main.py` as the execution script
---
## 📂 Project Structure
```
project/
├── data_fetcher.py    # Data acquisition module
├── visualization.py   # Advanced plotting functions
└── main.py           # Main execution script
```


## 🛠️ Setup Instructions

### ✅ Step 1: Clone this repository or copy files
```
   git clone https://github.com/praveensingh-git/Stock-Time-Series-Visualization.git
   cd Stock-Time-Series-Visualization
```

### ✅ Step 2: Install required packages

Make sure ![Python](https://img.shields.io/badge/python-3.8%2B-red) is installed, then run:

```
pip install yfinance pandas plotly scipy
```
### ✅ Step 3: Run the program
From the terminal or IDE:
```
python main.py
```

# 📊 Stock Data Visualization Code
---
1. Line Plot: Time Series Analysis (Line Plot)
 ```
plot_line(data, "Close_AAPL", "Time Series Analysis (Line Plot)")
Expected Output: Displays the time series of the stock's closing price.
```

2. Candlestick Chart: Time Series Analysis (Candlestick Chart)
```
plot_candlestick(
    data, 
    ["Open_AAPL", "High_AAPL", "Low_AAPL", "Close_AAPL"], 
    "Time Series Analysis (Candlestick Chart)"
)
```


## 3. Bar Plot: Time Series Analysis (Bar Plot)

```
plot_bar(data, "Close_AAPL", "Time Series Analysis (Bar Plot)")
Expected Output: Displays a bar chart of AAPL’s closing price over the selected date range.
```

## 4. Custom Date Range Line Plot: Custom Date Range Line Plot
```
custom_start = (date.today() - timedelta(days=180)).strftime("%Y-%m-%d")
custom_end = date.today().strftime("%Y-%m-%d")
plot_line(
    data, 
    "Close_AAPL", 
    "Custom Date Range Line Plot", 
    date_range=[custom_start, custom_end]
)
```


## 5. Interactive Candlestick Chart: Interactive Candlestick with Slider & Buttons

```
plot_candlestick(
    data,
    ["Open_AAPL", "High_AAPL", "Low_AAPL", "Close_AAPL"],
    "Interactive Candlestick with Slider & Buttons",
    interactive=True
)
```

# Author 

















