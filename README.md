# 💰 FinAgentX

**FinAgentX** is an AI-powered autonomous financial planning advisor built using a multi-agent system. It provides real-time, personalized financial advice and investment portfolio management.

---

## 🚀 Features
- Market data analysis
- Financial planning
- Risk assessment
- Modular multi-agent architecture
- Future support for LLMs, RAG, and reinforcement learning

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
