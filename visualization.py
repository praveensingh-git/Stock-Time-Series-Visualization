import plotly.express as px
import plotly.graph_objects as go

def plot_line(data, column, title, date_range=None):
    """Create a line plot"""
    fig = px.line(data, x=data.index, y=column, title=title)
    if date_range:
        fig.update_xaxes(range=date_range)
    fig.show()

def plot_candlestick(data, ohlc_columns, title, interactive=False):
    """Create a candlestick chart"""
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data[ohlc_columns[0]],
        high=data[ohlc_columns[1]],
        low=data[ohlc_columns[2]],
        close=data[ohlc_columns[3]]
    )])
    
    fig.update_layout(title=title)
    
    if interactive:
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
    else:
        fig.update_xaxes(rangeslider_visible=False)
    
    fig.show()

def plot_bar(data, column, title):
    """Create a bar plot"""
    px.bar(data, x=data.index, y=column, title=title).show()