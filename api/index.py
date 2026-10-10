from datetime import date, datetime
from pathlib import Path

import frontmatter
import markdown
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"

app = FastAPI(title="A small blog")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


def parse_date(value) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value))


def load_posts() -> list[dict]:
    posts = []
    if not POSTS_DIR.exists():
        return posts

    for path in POSTS_DIR.glob("*.md"):
        doc = frontmatter.load(path)
        posts.append(
            {
                "slug": path.stem,
                "title": doc.get("title") or path.stem.replace("-", " ").title(),
                "date": parse_date(doc.get("date") or date.today()),
                "summary": doc.get("summary") or "",
                "body": markdown.markdown(
                    doc.content,
                    extensions=["fenced_code", "tables", "smarty"],
                ),
            }
        )

    posts.sort(key=lambda item: item["date"], reverse=True)
    return posts


def get_post(slug: str) -> dict | None:
    for post in load_posts():
        if post["slug"] == slug:
            return post
    return None


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"posts": load_posts(), "page_title": "Notes"},
    )


@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
        request,
        "about.html",
        {"page_title": "About"},
    )


@app.get("/posts/{slug}", response_class=HTMLResponse)
def post_page(request: Request, slug: str):
    post = get_post(slug)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return templates.TemplateResponse(
        request,
        "post.html",
        {"post": post, "page_title": post["title"]},
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse(
            request,
            "404.html",
            {"page_title": "Not found"},
            status_code=404,
        )
    return HTMLResponse(str(exc.detail), status_code=exc.status_code)
