import os
import requests
from langchain.tools import BaseTool
from typing import Type, Any
from pydantic.v1 import BaseModel, Field

def parse_github_url(url: str) -> tuple[str, str]:
    """Parses a GitHub URL to extract owner and repo."""
    parts = url.strip('/').split('/')
    owner = parts[-2]
    repo = parts[-1]
    return owner, repo

class ReadFileToolInput(BaseModel):
    """Input for ReadFileTool."""
    repo_url: str = Field(description="The URL of the GitHub repository.")
    file_path: str = Field(description="The path to the file to be read from the repository.")

class ReadFileTool(BaseTool):
    name = "ReadFile"
    description = "Reads the content of a specific file from a GitHub repository. Useful for getting the content of READMEs or other text files."
    args_schema: Type[BaseModel] = ReadFileToolInput

    def _run(self, repo_url: str, file_path: str) -> str:
        try:
            owner, repo = parse_github_url(repo_url)
            # Use raw content URL for direct file access
            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{file_path}"
            response = requests.get(raw_url)
            response.raise_for_status()
            return response.text
        except Exception as e:
            return f"Error reading file: {e}"

class DirectoryListToolInput(BaseModel):
    """Input for DirectoryListTool."""
    repo_url: str = Field(description="The URL of the GitHub repository.")

class DirectoryListTool(BaseTool):
    name = "ListDirectory"
    description = "Lists the contents of the root directory of a GitHub repository to understand its structure."
    args_schema: Type[BaseModel] = DirectoryListToolInput

    def _run(self, repo_url: str) -> str:
        try:
            owner, repo = parse_github_url(repo_url)
            api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
            response = requests.get(api_url)
            response.raise_for_status()
            contents = response.json()
            # Format the output for better readability
            file_list = [f"- {item['name']} ({item['type']})" for item in contents]
            return "\n".join(file_list)
        except Exception as e:
            return f"Error listing directory: {e}"
