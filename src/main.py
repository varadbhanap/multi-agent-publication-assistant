import os
from dotenv import load_dotenv
from crewai import Crew, Process

# Load environment variables
load_dotenv()

from src.agents import PublicationAgents
from src.tasks import PublicationTasks

# Set up API keys
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# --- Main Execution ---
if __name__ == "__main__":
    print("## Welcome to the AI Publication Assistant Crew! ##")
    print("-------------------------------------------------")
    repo_url = input("Please enter the GitHub repository URL to analyze: ")

    # Initialize agents and tasks
    agents = PublicationAgents()
    tasks = PublicationTasks()

    repo_analyzer = agents.repo_analyzer_agent()
    content_strategist = agents.content_strategist_agent()
    structure_critic = agents.structure_critic_agent()

    # Define tasks
    analysis = tasks.analysis_task(repo_analyzer, repo_url)
    strategy = tasks.strategy_task(content_strategist, [analysis])
    structure = tasks.structure_task(structure_critic, [analysis])

    # Assemble the crew
    crew = Crew(
        agents=[repo_analyzer, content_strategist, structure_critic],
        tasks=[analysis, strategy, structure],
        process=Process.sequential,
        verbose=2,
    )

    # Kick off the work
    result = crew.kickoff()

    print("\n\n################################################")
    print("## Here is the Final Report ##")
    print("################################################")
    print(result)
