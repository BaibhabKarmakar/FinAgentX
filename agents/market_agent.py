from core.utils import BaseAgent

class MarketDataAgent(BaseAgent):
    def run(self , input_data):
        # placeholder: Simulate market data retrieval
        print(f"{self.name}: Fetching market Data...")
        return {"amrket_data": "sample data"}