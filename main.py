import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.market_agent import MarketDataAgent
from agents.planner_agent import PlannerAgent
from storage.plan_saver import load_saved_plans

def get_user_input():
    print("Welcome to FinAgentX Investment Planner!\n")
    goal = input("Enter your financial goal (e.g., Financial Freedom , Buy a Car) : ")
    try:
        target_amount = float(input("Enter your target amount(USD) : "))
        duration_years = int(input("Enter the number of years to achieve this goal:"))
    except ValueError:
        print("Invalid Input , Please Enter numeric values for amount and years.")
        return get_user_input()
    return goal, target_amount , duration_years
def test_market_agent():
    symbols = ["AAPL" , "GOOGL" , "TSLA" , "BINANCE:BTCUSDT" , "NFLX"]
    agent = MarketDataAgent()

    for sym in symbols:
        data = agent.run(sym)
        print(f"{sym}:")
        print(data)
        print("\n")

def test_planner_agent():
    goal , target_amount , duration_years = get_user_input()
    user_input = {
        "goal": goal,
        "target_amount": target_amount,
        "duration_years" : duration_years
    }
    agent = PlannerAgent(name = "PlannerAgent" , user_input = user_input)
    agent.run()

if __name__ == "__main__":
    test_market_agent()
    test_planner_agent()

print("\n All saved Investment plans:")
plans = load_saved_plans()
for i, plan in enumerate(plans , 1):
    print(f"\nPlan {i} - {plan['timestamp']}")
    print(f" 🎯 Goal          : {plan['goal']}")
    print(f" 💰 Target Amount : ${plan['target_amount']}")
    print(f" 📆 Duration      : {plan['duration_years']} years")
    print(f" 📊 Monthly SIP   : ${plan['monthly_investment']:.2f}")
    print(f" 📌 Assets:")

    for assets in plan["recommended_assets"]:
        print(f"   - {assets['symbol']} @ ${assets['price']}")