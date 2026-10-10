---
title: Hello from a tiny FastAPI blog
date: 2026-10-01
summary: A short note on why this site exists and how the posts are stored.
---

This site is a small FastAPI app. Each post is a Markdown file in `posts/` with a little YAML header for title, date, and summary.

That is the whole content model. No database, no CMS, no build step for the writing itself — just files.

When you add a new `.md` file and redeploy, it shows up on the home page.
