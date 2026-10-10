# Small FastAPI blog

A tiny website: Markdown posts, Jinja templates, FastAPI, ready for Vercel.

## Local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn api.index:app --reload
```

Open http://127.0.0.1:8000

## Write a post

Add a file in `posts/`, for example `posts/a-new-note.md`:

```md
---
title: A new note
date: 2026-10-11
summary: One line for the home page.
---

Your Markdown here.
```

## Deploy on Vercel

1. Push this folder to GitHub.
2. Import the repo in [Vercel](https://vercel.com/new).
3. Deploy. Framework preset can stay as Other.

`vercel.json` sends every request to the FastAPI app in `api/index.py`.
