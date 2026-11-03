# KissMyPost agent for Google ADK

A minimal [Agent Development Kit (ADK)](https://adk.dev) agent, "Reddit audience researcher", that uses the KissMyPost MCP server as its tools. Ask it which subreddits fit a product, how big and active a community is, who is in it, when to post, or how often Reddit mentions a brand, and it answers with real numbers from KissMyPost and links to the full reports.

The agent connects to `https://kissmypost.com/api/mcp` with ADK's `McpToolset` over Streamable HTTP and sends your key as `Authorization: Bearer <KISSMYPOST_API_KEY>`. The tools are read-only: they never post, vote or message anyone on Reddit. The model is Gemini through the Gemini API.

## Keys

- **KissMyPost key (free):** sign in at https://kissmypost.com/mcp and create a key. It starts with `kmp_`. Paid accounts unlock a few more tools; the agent is the same.
- **Gemini API key:** https://aistudio.google.com/apikey

## Run

```bash
cd adk-sample
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp kissmypost_agent/.env.example kissmypost_agent/.env   # then put your two keys in it
```

Chat in the terminal:

```bash
adk run kissmypost_agent
```

or open the ADK dev UI at http://localhost:8000 and pick `kissmypost_agent`:

```bash
adk web
```

To use another Gemini model, set `GEMINI_MODEL` in `.env`.

## Try

- When is the best time to post in r/SaaS?
- Which subreddits talk about espresso, and which is the biggest?
- How often does Reddit mention notion.so?

## Files

- `kissmypost_agent/agent.py`: the agent (`root_agent`) and the `McpToolset` connection.
- `kissmypost_agent/.env.example`: the environment variables the agent reads.
- `requirements.txt`: pinned versions (`google-adk[mcp]` 2.13.0, `mcp` 2.3.0).

## Use the tools in your own agent

```python
import os
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

kissmypost = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://kissmypost.com/api/mcp",
        headers={"Authorization": f"Bearer {os.environ['KISSMYPOST_API_KEY']}"},
        timeout=30,
    ),
    # tool_filter=["find_subreddits_by_topic", "subreddit_overview", "best_time_to_post"],
)
```

Add `kissmypost` to any agent's `tools`. There is a daily limit of different subreddits, brands and searches per account, so let the agent ask only for what it needs.

Privacy policy: https://kissmypost.com/privacy. Support: hi@kissmypost.com.
