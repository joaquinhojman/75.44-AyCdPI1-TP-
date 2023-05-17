import uvicorn
import login as login
import register as register
import home as home
import my_home as my_home
import aplication as aplication
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.include_router(login.router)
app.include_router(register.router)
app.include_router(home.router)
app.include_router(my_home.router)
app.include_router(aplication.router)

app.mount('/static', StaticFiles(directory='./src/static'), name='static')

templates = Jinja2Templates(directory="./src/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, log_level="info")
