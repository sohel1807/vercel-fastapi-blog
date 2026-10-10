---
title: Deploying this blog on Vercel
date: 2026-10-10
summary: Push the repo, import the project, and let Vercel run the Python app.
---

This project is a FastAPI app in `index.py`. Vercel detects that and runs it.

1. Push the repo to GitHub, GitLab, or Bitbucket.
2. In Vercel, import the repository.
3. Leave the defaults. `requirements.txt` and `vercel.json` are already in the root.
4. Deploy.

Locally you can run:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn index:app --reload
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).
