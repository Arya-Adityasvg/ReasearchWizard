# ReasearchWizard
A simple AI agent that helps out in researching various topics and saves that info in a .txt file.
# 📘 AI Research Assistant Agent

This project is an **AI-powered Research Assistant** built with **LangChain**, **OpenRouter (DeepSeek R1)**, and **custom tools**. The agent can:
- Search the web 🌐
- Query Wikipedia 📚
- Save structured research results to a `.txt` file 💾

It ensures research summaries are **detailed, minimum 100 words**, and formatted with bullet points or sections.

------------------------------------------------------------
## 🚀 Features
- **openai/gpt-oss-120b LLM** (via OpenRouter API).
- **Custom Tools**:
  - `search_tool` → DuckDuckGo web search.
  - `wiki_tool` → Wikipedia lookup.
  - `save_tool` → Saves structured results into a `.txt` file.
- **Structured Output** enforced using **Pydantic models**.
- **Validation** → Summary must be at least 100 words.
- **Agent-based workflow** → Uses LangChain’s `create_tool_calling_agent` and `AgentExecutor`.

------------------------------------------------------------
## 📂 Project Structure

project/
│── main.py           # Entry point for the agent
│── tools.py          # Contains custom tools (search, wiki, save_to_txt)
│── .env              # Environment variables (API keys & endpoints)
│── requirements.txt  # Python dependencies
│── README.txt        # Project documentation
│── research_output.txt (generated)  # Saved research results

------------------------------------------------------------
## ⚙️ Setup

### 1. Clone the repo
git clone <your-repo-link>
cd project

### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

### 3. Install dependencies
pip install -r requirements.txt

------------------------------------------------------------
## 🔑 Environment Variables

Create a `.env` file in the project root:

OPENAI_API_KEY=your_openrouter_api_key_here
OPENAI_API_BASE=https://openrouter.ai/api/v1

------------------------------------------------------------
## ▶️ Usage

Run the agent:
python main.py

You’ll be prompted for a research query, e.g.:

🔍 What can I help you research? South American football

The agent will:
1. Search the web and Wikipedia.
2. Generate a structured research summary (≥100 words).
3. Save results into `research_output.txt` (with timestamps).

------------------------------------------------------------
## 📝 Output Example

**research_output.txt** (sample structure):

--- Research Output ---
Timestamp: 2025-09-04 18:30:22

Topic: South American football
Summary:
- South American football has a deep cultural significance...
- Famous clubs include Boca Juniors, River Plate, Flamengo...
- Historical influence of Copa Libertadores...

Sources:
- Wikipedia
- DuckDuckGo

Tools Used:
- search_tool
- wiki_tool
- save_tool

------------------------------------------------------------
## 📌 Notes
- Uses **LangChain** latest versions.
- Compatible with **Python 3.11.x**.
- Summaries are enforced to be **≥100 words**.
- Falls back to saving raw output if parsing fails.

------------------------------------------------------------
## 🛠️ Requirements
- Python 3.11+
- langchain
- langchain_openai
- langchain_community
- python-dotenv
- pydantic v2+

Install via:
pip install -r requirements.txt

