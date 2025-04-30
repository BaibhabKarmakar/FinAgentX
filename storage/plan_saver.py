import os
import json
from datetime import datetime

def save_plan(user_goal, target_amount, monthly_investment, duration_years, recommended_assets):
    # Ensure monthly_investment is a dictionary with return rates as keys
    if isinstance(monthly_investment, (int, float)):
        monthly_investment = {
            "10%": monthly_investment,
            "12.5%": monthly_investment,
            "15%": monthly_investment
        }

    data = {
        "goal": user_goal,
        "target_amount": target_amount,
        "monthly_investment": monthly_investment,
        "duration_years": duration_years,
        "recommended_assets": recommended_assets,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    os.makedirs("storage", exist_ok=True)
    file_path = "storage/user_plans.json"

    # Load existing plans if available
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            plans = json.load(f)
    else:
        plans = []
    
    plans.append(data)

    with open(file_path, "w") as f:
        json.dump(plans, f, indent=4)

    print("Plan saved successfully!\n")

def load_saved_plans():
    file_path = "storage/user_plans.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return []