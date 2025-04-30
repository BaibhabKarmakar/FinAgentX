from core.base import BaseAgent
from agents.market_agent import MarketDataAgent
from storage.plan_saver import save_plan

class PlannerAgent(BaseAgent):
    def __init__(self, goal, user_input, rate_range=(10, 15)):
        super().__init__(goal)
        self.user_input = user_input
        self.market_agent = MarketDataAgent("MarketAgent")
        self.rate_range = rate_range

    def run(self):
        print(f"\n📌 User Goal: {self.user_input['goal']}")
        print(f"🎯 Target Amount: ${self.user_input['target_amount']}\n")

        symbols = ["AAPL", "GOOGL", "TSLA", "BINANCE:BTCUSDT", "NFLX"]
        print("Fetching Market Data...\n")

        current_data = {}
        for symbol in symbols:
            data = self.market_agent.run(symbol)
            current_data[symbol] = data
            print(f"📊 {symbol} Market Summary:")
            print(f"   - Current Price     : ${data['current_price']}")
            print(f"   - High Today        : ${data['high']}")
            print(f"   - Low Today         : ${data['low']}")
            print(f"   - Open Price        : ${data['open']}")
            print(f"   - Previous Close    : ${data['previous_close']}\n")

        self.plan(
            target_amount=self.user_input["target_amount"],
            current_data=current_data,
            investment_years=self.user_input.get("duration_years", 10)
        )

    def plan(self, target_amount, current_data: dict, investment_years: int = 10):
        print("\nGenerating your investment plan...\n")

        min_rate, max_rate = self.rate_range
        avg_rate = (min_rate + max_rate) / 2
        rates = [min_rate, avg_rate, max_rate]
        n = investment_years * 12
        sip_results = {}

        for rate in rates:
            r = rate / 12 / 100
            try:
                sip = target_amount / (((1 + r) ** n - 1) / r * (1 + r))
                sip_results[str(rate)] = round(sip, 2)
            except ZeroDivisionError:
                sip_results[str(rate)] = None

        print(f"To reach ${target_amount} in {investment_years} years:")
        for rate, sip in sip_results.items():
            if sip:
                print(f"📈 At {rate}% annual return: ${sip:,.2f} per month.")
            else:
                print(f"❌ Could not calculate SIP at {rate}% annual return.")

        print("\nRecommended Stocks for SIP Allocation:")
        for symbol, data in current_data.items():
            print(f" - {symbol}: Current Price = ${data['current_price']}")

        save_plan(
            user_goal=self.user_input["goal"],
            target_amount=target_amount,
            monthly_investment=sip_results,
            duration_years=investment_years,
            recommended_assets=[
                {
                    "symbol": sym,
                    "price": data["current_price"]
                }
                for sym, data in current_data.items()
            ]
        )