from core.base import BaseAgent
from agents.market_agent import MarketDataAgent

class PlannerAgent(BaseAgent):
    def __init__(self , name , user_input):
        super().__init__(name)
        self.user_input = user_input
        self.market_agent = MarketDataAgent("MarketAgent")
    
    def run(self):
        print(f"\n📌 User Goal : {self.user_input['goal']}")
        print(f"🎯 Target amount : ₹{self.user_input['target_amount']}\n")

        symbols = ["AAPL" , "GOOGL" , "TSLA" , "BINANCE:BTCUSDT" , "NFLX"]
        print(" Fetching Market Data...")

        for symbol in symbols:
            data = self.market_agent.run(symbol)
            print(f"{symbol}:")
            print(data)
            print()

        # Placeholder Logic : 
        print("Planning logic coming soon!")