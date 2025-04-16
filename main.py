from datetime import date, timedelta
from data_fetcher import fetch_stock_data
from visualization import plot_line, plot_candlestick, plot_bar

def main():
    # Configuration
    TICKER = "AAPL"
    DAYS_BACK = 720
    
    # Fetch data
    data = fetch_stock_data(TICKER, DAYS_BACK)
    
    if data is None or data.empty:
        print("No data available.")
        return
    
    print(data.head())
    
    # Visualizations
    plot_line(data, "Close_AAPL", "Time Series Analysis (Line Plot)")
    plot_candlestick(
        data, 
        ["Open_AAPL", "High_AAPL", "Low_AAPL", "Close_AAPL"], 
        "Time Series Analysis (Candlestick Chart)"
    )
    plot_bar(data, "Close_AAPL", "Time Series Analysis (Bar Plot)")
    
    # Custom date range plot
    custom_start = (date.today() - timedelta(days=180)).strftime("%Y-%m-%d")
    custom_end = date.today().strftime("%Y-%m-%d")
    plot_line(
        data, 
        "Close_AAPL", 
        "Custom Date Range Line Plot", 
        date_range=[custom_start, custom_end]
    )
    
    # Interactive candlestick
    plot_candlestick(
        data,
        ["Open_AAPL", "High_AAPL", "Low_AAPL", "Close_AAPL"],
        "Interactive Candlestick with Slider & Buttons",
        interactive=True
    )

if __name__ == "__main__":
    main()