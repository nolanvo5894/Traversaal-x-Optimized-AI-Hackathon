from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Verify the environment variable is loaded
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable not set. Please check your .env file.")

from .agent import AgentPro
from typing import Any
from agentpro.tools import CodeEngine, YouTubeSearchTool, SlideGenerationTool # add more tools when available

code_tool = CodeEngine()
youtube_tool = YouTubeSearchTool()
slide_tool = SlideGenerationTool()
__all__ = ['AgentPro', 'code_tool', 'youtube_tool', 'slide_tool'] # add more tools when available
