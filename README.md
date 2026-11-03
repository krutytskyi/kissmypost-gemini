# KissMyPost: Reddit Audience Research for Antigravity and Gemini CLI

KissMyPost is a Reddit analytics and audience research tool, and this plugin brings it into Google Antigravity (App and the `agy` CLI) and Gemini CLI. Use it as a subreddit finder for a product or topic, to size up a community (members, growth, activity), to see who is in a subreddit, to plan Reddit marketing with the best time to post and each subreddit's posting rules, to find communities that share the same people, and to track Reddit brand mentions month by month. The agent answers with real numbers instead of guesses, and every answer links to the full report on kissmypost.com.

## Install

### Antigravity

```bash
agy plugin install https://github.com/krutytskyi/kissmypost-gemini
```

Then open `/plugin` (CLI) or **Customizations → Plugins** (App), turn **KissMyPost: Reddit Audience Research** on and paste your API key when asked.

Prefer to add the server by hand? Run:

```bash
agy mcp add --header "Authorization: Bearer YOUR_KEY" kissmypost https://kissmypost.com/api/mcp
```

or put this in `~/.gemini/config/mcp_config.json`:

```json
{
  "mcpServers": {
    "kissmypost": {
      "serverUrl": "https://kissmypost.com/api/mcp",
      "headers": { "Authorization": "Bearer YOUR_KEY" }
    }
  }
}
```

### Gemini CLI

```bash
gemini extensions install https://github.com/krutytskyi/kissmypost-gemini
```

Gemini CLI asks for the API key during install and keeps it in your system keychain.

## Use with ADK (Google Agent Development Kit)

Building your own agent with Gemini? [`adk-sample/`](adk-sample) is a ready "Reddit audience researcher" agent that plugs KissMyPost in as an ADK `McpToolset` over Streamable HTTP:

```bash
cd adk-sample && pip install -r requirements.txt
cp kissmypost_agent/.env.example kissmypost_agent/.env   # add GOOGLE_API_KEY and KISSMYPOST_API_KEY
adk web
```

See [adk-sample/README.md](adk-sample/README.md) for the code and example questions.

## API key

The server needs a free KissMyPost account. Create a key (it starts with `kmp_`) at [kissmypost.com/mcp](https://kissmypost.com/mcp?utm_source=github&utm_medium=directory). Paid accounts unlock a few more tools; the plugin is the same.

## What is inside

- **MCP server** `kissmypost` at `https://kissmypost.com/api/mcp` (remote, Streamable HTTP, read-only tools). Nothing runs on your machine.
- **Skill** `reddit-audience-research` (Antigravity loads it as a skill, Gemini CLI as its context file): which KissMyPost tool to call for each kind of question and how to present the numbers.

Try:

- When is the best time to post in r/SaaS?
- Which subreddits talk about espresso, and which is the biggest?
- How often does Reddit mention notion.so?
- Who is in r/fitness: share of women, median age, where else they hang out?
- Which subreddits have the same people as r/running?

## What it sends and where

The plugin talks to one destination only: `https://kissmypost.com/api/mcp`. When the agent calls a tool, it sends the tool name and its arguments, such as a subreddit name, a topic, a brand domain or a search phrase, plus your API key. The plugin has no hooks, scripts or local commands, and it does not read your files, chat history or environment. The tools never post, vote or message anyone on Reddit.

## Privacy and support

- Privacy policy: https://kissmypost.com/privacy (see "ChatGPT and other AI assistants (MCP)" for what the server logs and for how long).
- Terms: https://kissmypost.com/terms
- Support: hi@kissmypost.com or https://kissmypost.com/contact
