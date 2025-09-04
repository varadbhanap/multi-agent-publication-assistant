from crewai import Agent
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool

from src.tools.github_tools import ReadFileTool, DirectoryListTool

# Initialize the LLM
llm = ChatGroq(model="llama3-70b-8192", temperature=0.2)

# Initialize the tools
search_tool = SerperDevTool()
read_file_tool = ReadFileTool()
list_directory_tool = DirectoryListTool()

class PublicationAgents:
    def repo_analyzer_agent(self) -> Agent:
        return Agent(
            role="GitHub Repository Analyst",
            goal="Analyze the structure and content of a GitHub repository, focusing on the README file and overall file organization.",
            backstory=(
                "As an expert in software project management and documentation, you have a keen eye for what makes a repository understandable and accessible. "
                "You are tasked with the initial inspection of a project to gather all necessary data for your team."
            ),
            tools=[read_file_tool, list_directory_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def content_strategist_agent(self) -> Agent:
        return Agent(
            role="Content and Metadata Strategist",
            goal="Improve the project's discoverability and appeal by refining its title, summary, and suggesting relevant tags based on its content.",
            backstory=(
                "With a background in marketing and technical writing, you specialize in making complex projects shine. "
                "You know how to craft compelling narratives and use keywords to attract the right audience. Your goal is to make the project stand out."
            ),
            tools=[search_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def structure_critic_agent(self) -> Agent:
        return Agent(
            role="Documentation Structure Critic",
            goal="Review the README for completeness and clarity, ensuring it follows best practices for technical documentation.",
            backstory=(
                "You are a meticulous technical editor with a passion for well-structured documentation. You believe that a great README is the cornerstone of a successful open-source project. "
                "You check for essential sections like Installation, Usage, and License, and suggest improvements to the overall layout."
            ),
            tools=[read_file_tool, list_directory_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )
