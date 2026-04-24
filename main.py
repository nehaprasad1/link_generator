from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
import os
import uvicorn

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
# NEW: This block is critical for cloud deployment
if __name__ == "__main__":
    # Render and other clouds assign a random port via the 'PORT' environment variable.
    # This line fetches that port. If it's missing (like on your local PC), it defaults to 8000.
    port = int(os.environ.get("PORT", 8000))
    
    # We pass the dynamic 'port' variable to uvicorn so the container stays alive on the cloud.
    uvicorn.run(app, host="0.0.0.0", port=port)