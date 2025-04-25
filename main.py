import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.market_agent import MarketDataAgent
from agents.planner_agent import PlannerAgent

def test_market_agent():
    symbols = ["AAPL" , "GOOGL" , "TSLA" , "BINANCE:BTCUSDT" , "NFLX"]
    agent = MarketDataAgent()

    for sym in symbols:
        data = agent.run(sym)
        print(f"{sym}:")
        print(data)
        print("\n")

def test_planner_agent():
    user_input = {
        "goal": "financial freedom",
        "target_amount": 5000000
    }
    agent = PlannerAgent(name = "PlannerAgent" , user_input = user_input)
    agent.run()

if __name__ == "__main__":
    test_market_agent()
    test_planner_agent()