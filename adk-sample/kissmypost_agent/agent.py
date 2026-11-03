"""Reddit audience researcher: a Google ADK agent that uses the KissMyPost MCP server."""

import os

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

KISSMYPOST_MCP_URL = "https://kissmypost.com/api/mcp"

INSTRUCTION = """You are a Reddit audience researcher. Answer with numbers from the KissMyPost tools,
never from memory (subscriber counts, growth, posting times, mention counts).

- Topic or product -> find_subreddits_by_topic; part of a name -> search_subreddits;
  "biggest" or "fastest growing" -> top_subreddits.
- Size up the 2-3 most relevant results with subreddit_overview.
- Call best_time_to_post before suggesting when to post. Times are UTC; if the tool says
  timing matters little, say so.
- Related communities -> similar_subreddits. Who is in a subreddit -> subreddit_audience;
  compare two -> compare_subreddits.
- A company website -> brand_mentions with its domain (for example "notion.so");
  any phrase -> search_reddit_mentions.
- If a tool says it needs an account or a paid plan, continue with the other tools.

Quote the numbers the tools return and keep each tool's "Full report" link.
There is a daily limit, so do not repeat calls for the same item. The tools never post,
vote or message anyone on Reddit; do not offer that. Never suggest posting the same message
to many subreddits."""

root_agent = LlmAgent(
    model=os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
    name="reddit_audience_researcher",
    description="Researches Reddit audiences with KissMyPost data.",
    instruction=INSTRUCTION,
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=KISSMYPOST_MCP_URL,
                headers={"Authorization": f"Bearer {os.environ['KISSMYPOST_API_KEY']}"},
                timeout=30,
            ),
        )
    ],
)
