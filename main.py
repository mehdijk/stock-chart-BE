from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/stock-price")
async def get_stock_data(symbol: str = "META", period: str = "1d", interval: str = "1m"):
    data = yf.download(symbol, interval=interval, period=period)
    data = data.reset_index()
    
    # Format Datetime column
    data["Datetime"] = data["Datetime"].dt.strftime('%Y-%m-%d %H:%M:%S%z')

    return data[["Datetime", "Close"]].values.tolist()

