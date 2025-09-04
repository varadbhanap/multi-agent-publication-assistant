from crewai import Task

class PublicationTasks:
    def analysis_task(self, agent, repo_url) -> Task:
        return Task(
            description=f"""
                Analyze the GitHub repository at the following URL: {repo_url}.
                Your primary goal is to understand the project's purpose and structure.
                
                Steps:
                1. Use the ListDirectory tool to see the repository's file structure.
                2. Use the ReadFile tool to read the content of the README.md file.
                
                Compile a summary of your findings, including the repository structure and the full content of the README.md file. This will be the context for the other agents.
            """,
            expected_output="A detailed report containing the repository's file structure and the complete content of the README.md file.",
            agent=agent,
        )

    def strategy_task(self, agent, context) -> Task:
        return Task(
            description="""
                Based on the provided analysis of the repository, develop suggestions to improve the project's public presentation.
                
                Focus on these areas:
                1. **Project Title:** Propose 2-3 alternative titles that are more descriptive or engaging.
                2. **Project Summary:** Write a new, concise one-paragraph summary explaining what the project does and for whom.
                3. **Tags/Keywords:** Suggest 5-7 relevant tags or keywords that would improve discoverability on platforms like GitHub and Ready Tensor. Use the search tool if you need to research similar projects or technologies.
            """,
            expected_output="A list of actionable suggestions including new titles, a revised summary, and a list of relevant tags/keywords.",
            agent=agent,
            context=context,
        )

    def structure_task(self, agent, context) -> Task:
        return Task(
            description="""
                Review the provided README content and repository structure for clarity, completeness, and adherence to best practices.
                
                Your review should check for the following essential sections:
                - Installation instructions
                - Usage examples
                - License information
                - Contribution guidelines (if applicable)
                
                Provide a list of missing sections and suggest specific improvements to the README's structure and formatting to make it more professional and user-friendly. For example, recommend using markdown for code blocks or adding a table of contents.
            """,
            expected_output="A constructive critique of the README, identifying missing sections and providing concrete suggestions for structural and formatting improvements.",
            agent=agent,
            context=context,
        )
