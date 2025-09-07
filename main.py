import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,function_tool
from tavily import TavilyClient
_: bool = load_dotenv(find_dotenv())
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
tavily_api_key: str = os.getenv("TAVILY_API_KEY", "")
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
@function_tool()
def o_g_researcher(query: str) -> str:
    response = tavily_client.search(query)
    return response
planner: Agent = Agent(
    name="Planner",
    instructions=(
        "You are a planning agent. Break down the oil and gas research question "
        "into smaller parts and then make a plan in numbered list to do the deep research."
    ),
    model=llm_model,
)

researcher: Agent = Agent(
    name="Researcher",
    instructions=(
        "You are a research agent. Use Tavily search to gather findings on each sub-question. "
        "Summarize results clearly and cite sources."
    ),
    model=llm_model,
    tools=[o_g_researcher]
)

verifier: Agent = Agent(
    name="Verifier",
    instructions=(
        "You are a verifying agent. Cross-check findings from the researcher with other sources, highlight "
        "conflicts, and ensure credibility of sources."
    ),
    model=llm_model,
)
citation: Agent = Agent(
    name="In-Text Citation",
    instructions=(
        "You are a in-text citation agent, give citations for the information sources"
    ),
    model=llm_model,
)
synthesizer: Agent = Agent(
    name="Synthesizer",
    instructions=(
        "You are a synthesizer. Combine verified findings into a structured professional report "
        "with clear sections: Introduction, Economic Impact, Environmental Challenges, "
        "Future Outlook, and Citations."
    ),
    model=llm_model,
)

orchestrator = Agent(
    name="Orchestrator",
    instructions=(
        "You are the orchestrator. Execute the following pipeline step by step: "
        "1. Use Planner to break down query. "
        "2. Pass plan to Researcher. "
        "3. Pass research to Verifier. "
        "4. Pass verified results to Citation. "
        "5. Pass citation-enhanced content to Synthesizer. "
        "Finally, return the Synthesizer's final report summary under 500 words."
    ),
    model=llm_model,
)

deep_research_team_lead = orchestrator

query = "How digital twins can be used for the real time condition monitoring of oil and gas pipelines?"
res = Runner.run_sync(deep_research_team_lead, query)

print("\n=== Deep Research Report on Oil & Gas ===\n")
print(res)