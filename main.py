from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files like CSS or JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates folder
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    platforms = ["GitHub", "LeetCode", "LinkedIn"]  # platform list

    return templates.TemplateResponse("index.html", {
        "request": request,
        "platforms": platforms
    })
