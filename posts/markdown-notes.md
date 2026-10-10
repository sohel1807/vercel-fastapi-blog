---
title: Writing in Markdown
date: 2026-10-05
summary: Headings, lists, code, and links — what this blog renderer supports.
---

Posts are ordinary Markdown. Useful bits:

## Headings

Use `##` and `###` inside a post. The page title comes from the front matter, so start content at heading two.

## Lists

- Keep lists short
- Prefer one idea per line
- Link out when a sentence needs a source

## Code

Inline like `fastapi` and blocks like this:

```python
from fastapi import FastAPI

app = FastAPI()
```

## Links

A [FastAPI](https://fastapi.tiangolo.com/) app can still be a quiet place to write.
