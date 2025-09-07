This project is a multi-agent research system designed to break down complex oil & gas (or any) research questions, search credible sources, cross-check information, add citations, and produce a concise professional report.
How to set up and run your system

    Clone or download the project to your local machine.

    Install dependencies (example):

    pip install python-dotenv tavily


    (Add other dependencies from your agents module as required.)

    Set up environment variables in a .env file:

    OPENAI_API_KEY=your_openai_api_key     # optional
    GEMINI_API_KEY=your_gemini_api_key     # required
    TAVILY_API_KEY=your_tavily_api_key     # required


    Instantiate the Tavily client in your script before use:

    from tavily import TavilyClient
    tavily_client = TavilyClient(api_key=tavily_api_key)


    Run the pipeline:

    python run_research.py


    The final structured report will print to the console (≤ 500 words).

Example research questions

    You can replace the query with any domain-specific topic. For example:

    How digital twins can be used for real-time condition monitoring of oil and gas pipelines?

    What are the economic and environmental trade-offs of offshore drilling in the North Sea?

    How can AI-driven predictive maintenance improve safety in liquefied natural gas facilities?

    What role do carbon capture technologies play in future energy transitions?

What each agent does

    Planner → Breaks down the user’s research query into smaller, structured sub-questions.

    Researcher → Uses Tavily search to gather findings, summarizes them, and records sources.

    Verifier → Cross-checks research results, highlights conflicts, and ensures credibility.

    Citation → Adds proper in-text citations to strengthen the research narrative.

    Synthesizer → Combines verified findings into a polished report with sections:
    Introduction, Economic Impact, Environmental Challenges, Future Outlook, Citations.

    Orchestrator → Controls the pipeline, ensuring each agent runs in sequence and returns the final report.

How the team coordinates

    Orchestrator receives the main query.

    Sends it to Planner → produces a numbered plan of sub-questions.

    Researcher executes the plan, querying Tavily for each part.

    Findings are reviewed by the Verifier → conflicting or weak evidence is flagged.

    Citation formats references into the draft.

    Synthesizer merges everything into a concise, professional report.

    Orchestrator returns the final summary to the user.
Link for Video:
https://drive.google.com/file/d/1jmLueo8qBu7i8xjqavxcdCS1fWQ9R0Y4/view?usp=drive_link