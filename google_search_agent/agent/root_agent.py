from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

# Define and expose root_agent — ADK looks specifically for this variable
root_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.5-flash",  # use a valid supported model ID
    description="Agent to answer questions using Google Search.",
    instruction="You are an expert researcher. You always stick to the facts.",
    tools=[google_search],
)
