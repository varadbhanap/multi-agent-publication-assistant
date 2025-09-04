# multi-agent-publication-assistant
# Multi-Agent Publication Assistant

This project is a submission for the **Agentic AI Developer Certification Program by Ready Tensor (Module 2)**. It implements a multi-agent system using **CrewAI** to help users improve the public presentation of their AI/ML projects by analyzing a GitHub repository and providing actionable feedback.

## 🚀 Project Overview

The system takes a GitHub repository URL as input and orchestrates a team of three specialized AI agents to produce a comprehensive report with suggestions for improving the project's `README.md`, metadata, and overall structure. This demonstrates core concepts from Module 2, including multi-agent collaboration, tool integration, and agent orchestration.

### How It Meets Certification Requirements
-   **Multi-Agent System (3 agents)**:
    1.  **Repo Analyst**: Fetches data from the repository.
    2.  **Content Strategist**: Improves marketing aspects like title, summary, and tags.
    3.  **Structure Critic**: Checks for technical documentation best practices.
-   **Agent Orchestration**:
    -   Uses **CrewAI** to manage a sequential workflow where the analysis from the first agent is passed as context to the subsequent agents.
-   **Tool Integration (3 tools)**:
    1.  **Custom ReadFileTool**: Reads the content of a specific file (e.g., `README.md`) from a GitHub repo.
    2.  **Custom DirectoryListTool**: Lists the file structure of a GitHub repo to understand its organization.
    3.  **Built-in SerperDevTool**: A web search tool used by the Content Strategist to research relevant keywords and competing projects.

## 🛠️ Technology Stack

-   **Orchestration Framework**: [CrewAI](https://www.crewai.com/)
-   **LLM**: [Groq](https://groq.com/) using the `llama3-70b-8192` model (for speed and performance)
-   **Tools**: LangChain/CrewAI Tools, Custom Python tools using `requests`
-   **Primary Libraries**: `crewai`, `langchain-groq`, `python-dotenv`

## ⚙️ Setup and Installation

### 1. Prerequisites
-   Python 3.9+
-   A **Groq API Key**: Get one for free at [Groq Console](https://console.groq.com/keys)
-   A **Serper API Key**: Get a free key at [Serper.dev](https://serper.dev/) (for the search tool)

### 2. Clone the Repository
```bash
git clone <your-repo-url>
cd multi-agent-publication-assistant
```

### 3. Install Dependencies
Create and activate a virtual environment, then install the required packages.
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a file named `.env` in the root directory of the project and add your API keys:
```
GROQ_API_KEY="your_groq_api_key_here"
SERPER_API_KEY="your_serper_api_key_here"
```

## ▶️ How to Run

Run the main script from the root directory:
```bash
python src/main.py
```
The application will prompt you to enter a GitHub repository URL.

### Example Usage
```
## Welcome to the AI Publication Assistant Crew! ##
-------------------------------------------------
Please enter the GitHub repository URL to analyze: [https://github.com/joaomdmoura/crewAI](https://github.com/joaomdmoura/crewAI)
```

The agents will then begin their work, and you will see their progress printed to the console. The final, consolidated report will be displayed at the end.
