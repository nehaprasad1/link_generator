from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional

app = FastAPI()

# Mount static files (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates folder
templates = Jinja2Templates(directory="templates")

# Platform URL mapping
PLATFORM_URLS = {
    "github": "https://github.com/",
    "leetcode": "https://leetcode.com/u/",
    "linkedin": "https://www.linkedin.com/in/",
    "instagram": "https://www.instagram.com/",
    "youtube": "https://www.youtube.com/@"
}

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request, username: Optional[str] = None, platform: Optional[str] = None):
    generated_link = None
    
    # Construct the link if both inputs exist
    if username and platform:
        base_url = PLATFORM_URLS.get(platform.lower())
        if base_url:
            # We strip whitespace just in case of typos
            generated_link = f"{base_url}{username.strip()}"

    # Modern Keyword Argument syntax to avoid "unhashable dict" error
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "username": username,
            "platform": platform,
            "generated_link": generated_link
        }
    )