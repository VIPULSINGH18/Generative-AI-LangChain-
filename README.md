# Generative-AI-LangChain-

<div align="center">

# 🧪 Research & Weather Assistant Agent
### An Autonomous AI Agent powered by LangGraph & Google Gemini

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-green?style=for-the-badge)
![LangGraph](https://img.shields.io/badge/LangGraph-🕸️-blue?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

### 📸 Project Dashboard & Capabilities

| **Agent Interface** | **Weather Query** | **Reasoning Logic** |
| :---: | :---: | :---: |
| <img src="https://github.com/user-attachments/assets/cf71f135-1011-4081-81ac-7daaf876e4b0" width="100%"> | <img src="https://github.com/user-attachments/assets/c0c1329d-220d-4c76-9164-17d6c28f635e" width="100%"> | <img src="https://github.com/user-attachments/assets/d9507c7c-cb6b-415c-a864-42a76827645c" width="100%"> |
| **Search Tool** | **Confidence Score** | **Terminal Output** |
| <img src="https://github.com/user-attachments/assets/002e1b15-63d3-4c2a-9771-b9430e98cfb3" width="100%"> | <img src="https://github.com/user-attachments/assets/19f8ae9e-eed4-4084-a656-94c325318fcd" width="100%"> | <img src="https://github.com/user-attachments/assets/7af16f39-3fbf-4cd2-a5a5-155e9401a54e" width="100%"> |

<br />

**A production-style AI agent that thinks, decides, acts, and stops safely.**
*Not just a text generator — an engineered system.*

[View Demo](#) · [Report Bug](issues) · [Request Feature](issues)

</div>

---

## 🚀 Project Overview

This project is an **end-to-end autonomous AI agent system**. Unlike standard chatbots that simply predict the next word, this agent uses the **ReAct (Reason + Act)** paradigm to solve complex queries.

It autonomously determines *if* it needs to search the web, check the weather, or answer directly. It features a robust **confidence scoring system** to let users know how reliable the answer is.

### 🌟 Key Capabilities

| Feature | Description |
| :--- | :--- |
| **🌍 Real-Time Weather** | Fetches live weather data for any global location via **Weatherstack API**. |
| **📰 Live Research** | Performs web searches for current events using **DuckDuckGo**. |
| **🧠 Autonomous Reasoning** | Uses **LangGraph** to loop through `Thought` → `Action` → `Observation`. |
| **📊 Confidence Scoring** | Self-evaluates its answers and displays a **Confidence Badge** (High/Low) in the UI. |
| **🛑 Safety Loops** | Implements **recursion limits** to prevent infinite agent loops and handle tool failures gracefully. |

---

## 🧠 Architecture & Engineering

This project demonstrates **AI Engineering** concepts over simple prompt engineering. It uses a cyclic graph to manage state and decision-making. 

```mermaid
graph TD
    User(User Query) --> Agent[🤖 ReAct Agent]
    Agent -->|Decides Tool Needed| Router{Router}
    
    Router -->|Need News?| Search[🔎 DuckDuckGo Tool]
    Router -->|Need Weather?| Weather[☁️ Weather API]
    
    Search --> Agent
    Weather --> Agent
    
    Agent -->|Reasoning Loop| Agent
    Agent -->|Confident Answer| Final[✅ Final Answer + Confidence Score]
    Final --> UI[🖥️ Streamlit Frontend]
The ReAct Loop Process
Thought: The agent analyzes the user request (e.g., "Weather in Delhi?").

Decision: It chooses the correct tool (Weather API).

Action: It executes the Python function.

Observation: It reads the real data (JSON).

Repeat: It loops back to synthesize the final answer.

🧰 Tech Stack
Brain: Google Gemini (Flash Model) - Chosen for high speed, large context, and reliability.

Orchestration: LangChain & LangGraph - For building stateful, cyclic agent workflows.

Tools: DuckDuckGo Search & Weatherstack API.

Frontend: Streamlit - Custom CSS styling for a futuristic, dark-themed UI.

Language: Python 3.12+

📂 Project Structure
Bash

Research-Weather-Agent/
│
├── assets/              # 📸 Stores images for README
│   └── dashboard_preview.png
├── agent_frontend.py    # 🎨 Main Streamlit App + UI Logic
├── .env                 # 🔐 API Keys (Keep secret!)
├── requirements.txt     # 📦 Python Dependencies
└── README.md            # 📄 Documentation
⚡ Getting Started
1. Clone the Repository
Bash

git clone [https://github.com/yourusername/Research-Weather-Agent.git](https://github.com/yourusername/Research-Weather-Agent.git)
cd Research-Weather-Agent
2. Set Up Virtual Environment
Bash

python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Configure Environment Keys
Create a .env file in the root directory:

Ini, TOML

GOOGLE_API_KEY=your_gemini_api_key
WEATHER_API_KEY=your_weatherstack_key
5. Run the Agent 🚀
Bash

streamlit run agent_frontend.py
🎯 Why This Project Matters (Recruiter POV)
This project moves beyond "calling an API" to building a reliable system. Key engineering decisions included:

Control Flow: Using LangGraph instead of simple chains to allow cyclic reasoning (Loops).

Reliability: Implementing recursion_limit to ensure the agent doesn't get stuck in infinite thought loops.

User Trust: The Confidence Score mechanism ensures the user knows when the AI is hallucinating versus when it cites sources.

Error Handling: If a tool (like Weather API) fails, the agent catches the error and informs the user instead of crashing.

🚧 Future Roadmap
[ ] RAG Integration: Connect to local PDFs for document-based Q&A.

[ ] Multi-Agent System: Separate 'Research Agent' and 'Writer Agent'.

[ ] Source Citations: Hyperlink specific URLs used in the final answer.

<div align="center">

👤 Author
Vipul Kumar Singh AI / ML Engineer | Agentic AI Enthusiast

Focused on building reliable, controllable, production-ready AI systems.

Connect on LinkedIn • View GitHub Profile

</div>
