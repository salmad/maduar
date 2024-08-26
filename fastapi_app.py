from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
import uvicorn
from typing import Optional, List
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI(
    title="InstantCoder: Skip the BS, Launch Python App Now",
    description="Welcome to the ultimate shortcut for Python developers who want results, not headaches"
                "With InstantCoder, all you do is write your Python code, push it, and let us handle the rest. It’s the fastest, easiest way to turn your ideas into reality",
    version="0.0.0",
)
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



@app.get("/landing_page", response_class=HTMLResponse)
def landing_page(request: Request):
    return  templates.TemplateResponse(request=request,name='maduar_landing_template.html',context={})


@app.get("/blogpost", response_class=HTMLResponse)
def landing_page(request: Request):
    
    return  "Write something here"

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)