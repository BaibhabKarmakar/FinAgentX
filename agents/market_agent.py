import requests
import os
from dotenv import load_dotenv
from core.utils import BaseAgent

load_dotenv()

class MarketDataAgent(BaseAgent):
    def __init__(self):
        super().__init__("MarketDataAgent")
        self.api_key = os.getenv("FINHUB_API_KEY")
        self.base_url = "https://finnhub.io/api/v1"

    def run(self , symbol="AAPL"):
        endpoint = f"{self.base_url}/quote"
        params = {
            "symbol": symbol,
            "token": self.api_key
        }
        try:
            response = requests.get(endpoint , params=params)
            data = response.json()
            if "c" in data:
                return {
                    "symbol": symbol,
                    "current_price": data["c"],
                    "high": data["h"],
                    "low": data["l"],
                    "open": data["o"],
                    "previous_close": data["pc"]
                }
            else:
                return {"error": "Invalid symbol or API limit reached!"}
        except Exception as e:
            return {"error": str(e)}