---
name: reddit-audience-research
description: Research a Reddit audience with KissMyPost data. Use when the user asks which subreddits fit a product or topic, how big or active a subreddit is, who is in it (gender, age), when or where to post, which communities share its audience, what Reddit talks about around a topic, or how often a phrase or brand is mentioned.
---

# Reddit audience research with KissMyPost

Use the KissMyPost tools for numbers. Do not guess subscriber counts, growth, posting times or mention counts from memory.

1. **Find communities.** For a topic or product, call `find_subreddits_by_topic` (matches names and descriptions). Use `search_subreddits` when the user gives part of a subreddit name. For "biggest" or "fastest growing" questions, call `top_subreddits`, optionally with a topic.
2. **Size up a subreddit.** Call `subreddit_overview` for the 2-3 most relevant results. Compare members, 12-month growth and monthly posts and authors: an active mid-size community often beats a huge quiet one.
3. **Timing.** Call `best_time_to_post` before suggesting when to post. Times are UTC; convert them to the user's time zone if you know it. If the tool says timing matters little, say so instead of inventing a slot.
4. **Related communities.** `similar_subreddits` lists communities with similar topics and with a shared audience.
5. **Topics.** `explore_topics` shows where a topic sits on the map of Reddit topics and which subreddits lead that area.
6. **Brands and phrases.** For a company website, call `brand_mentions` with its domain (for example "notion.so"). For any word or phrase, `search_reddit_mentions` gives monthly post and comment counts and the top subreddits; it needs a signed-in account.
7. **Posting rules on paid accounts.** `subreddit_posting_rules` says what a subreddit allows and how often posts are removed. If a tool says it needs an account or a paid account, continue with the other tools and do not push the user to change their account.
8. **Who is in a subreddit.** `subreddit_audience` gives the share of women, median age and age groups, where else its people spend time and what they are more into than average. To compare two subreddits or two groups, call `compare_subreddits` once instead of two audience lookups.
9. **Where to post a draft (paid accounts).** `where_to_post` takes a post title or idea and returns the subreddits where similar posts live, how they did and the best hour in each.
10. **General Reddit numbers and studies.** `reddit_statistics` gives the headline monthly figures; `search_research` finds KissMyPost's published studies of Reddit data, with links and DOIs.

Rules for the answer:
- Quote the numbers the tools return and keep each tool's "Full report" link so the user can check the source.
- There is a daily limit of different subreddits, brands, searches and topics. Ask only for what the user needs and do not repeat calls for the same item.
- The tools do not post, vote or contact anyone on Reddit, and they do not return the text of posts or the names of authors. Do not offer those actions.
- NSFW (18+) subreddits and topics are not available here; if the user asks for them, say they are available only on kissmypost.com.
- Never suggest posting the same message to many subreddits; recommend reading each community's rules first (`subreddit_posting_rules` when available).
