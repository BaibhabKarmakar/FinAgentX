from agents.market_agent import MarketDataAgent

def test_market_agent():
    symbols = ["AAPL" , "GOOGL" , "TSLA" , "BINANCE:BTCUSDT" , "NFLX"]
    agent = MarketDataAgent()

    for sym in symbols:
        data = agent.run(sym)
        print(f"{sym}:")
        print(data)
        print("\n")

if __name__ == "__main__":
    test_market_agent()