# 💰 FinAgentX

**FinAgentX** is an AI-powered autonomous financial planning advisor built using a multi-agent system. It provides real-time, personalized financial advice and investment portfolio management.

---

# 🚀 Features

- ✅ Real-time stock & crypto market data (via [Finnhub.io](https://finnhub.io/))
- 🧠 Modular multi-agent architecture
- 📊 Financial planning and risk assessment (WIP)
- 🔄 Dummy vs Live Data Mode
- 🤖 Future: LLMs, RAG, and Reinforcement Learning agents

---

## 🧠 Architecture (WIP)

```mermaid
graph TD
    User -->|Input| PlannerAgent
    PlannerAgent --> RiskAssessorAgent
    PlannerAgent --> MarketDataAgent
    MarketDataAgent -->|Market Info| PlannerAgent
    RiskAssessorAgent -->|Risk Score| PlannerAgent
    PlannerAgent -->|Final Advice| User
```

# Folder Structure : 
```
FinAgentX/
├── agents/
│   ├── market_agent.py
│   └── ...
├── core/
│   └── base.py (BaseAgent)
├── main.py
├── .env
├── README.md
└── requirements.txt
```

# Setup instructions : 
## 1. Clone the repo
git clone https://github.com/BaibhabKarmakar/FinAgentX.git
cd FinAgentX

## 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

## 3. Install dependencies
pip install -r requirements.txt

## 4. Add your Finnhub API key to a .env file
echo "FINNHUB_API_KEY=your_key_here" > .env

## 5. Run
python main.py



