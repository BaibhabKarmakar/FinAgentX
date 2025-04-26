from core.base import BaseAgent
from agents.market_agent import MarketDataAgent
from storage.plan_saver import save_plan

class PlannerAgent(BaseAgent):
    def __init__(self , name , user_input):
        super().__init__(name)
        self.user_input = user_input
        self.market_agent = MarketDataAgent("MarketAgent")
    
    def run(self):
        print(f"\n📌 User Goal : {self.user_input['goal']}")
        print(f"🎯 Target amount : ${self.user_input['target_amount']}\n")

        symbols = ["AAPL" , "GOOGL" , "TSLA" , "BINANCE:BTCUSDT" , "NFLX"]
        print(" Fetching Market Data...")

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

        # Placeholder Logic : 
        self.plan(
            self.user_input['target_amount'] , 
            current_data,
            investment_years = self.user_input.get("duration_years" , 10)
        )

    def plan(self , target_amount , current_data: dict , investment_years: int = 10):
        print("\n Generating your investment plan ...\n")

        avg_return_rate = 0.12
        monthly_rate = avg_return_rate / 12

        # Use SIP formula: FV = P * [((1 + r)^n - 1) / r] * (1 + r)
        n = investment_years * 12
        r = monthly_rate
        try:
            sip_per_month = target_amount / (((1 + r) ** n - 1) / r * (1 + r))
            print(f"To reach ${target_amount:,.2f} in {investment_years} years,")
            print(f"Investment approximately ${sip_per_month:,.2f} per month.")
        except ZeroDivisionError:
            print("Could not calculate SIP . Try a longer investment duration.")
        
        print("\n Recommended Stocks for SIP Allocation:")

        for symbol, data in current_data.items():
            print(f" - {symbol}: Current Price = ${data['current_price']}")

        save_plan(
            user_goal = self.user_input["goal"],
            target_amount = target_amount,
            monthly_investment = sip_per_month,
            duration_years = investment_years,
            recommended_assets = [
                {
                    "symbol": sym,
                    "price": data["current_price"]
                }
                for sym , data in current_data.items()
            ]

        )