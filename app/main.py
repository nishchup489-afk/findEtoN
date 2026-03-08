from fastapi import FastAPI , Request , Response , Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from pathlib import Path
from decimal import Decimal , getcontext


BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

app = FastAPI()

def get_e(n):
    getcontext().prec = n+2

    e = Decimal(2)
    term = Decimal(1)

    for i in range(2, n+5):
        term /= i # faster than 1/factorial(n)
        e += term

        if term < Decimal(10)**-(n + 2):
            break

    return str(e)[:n+2]

@app.get("/" , response_class=HTMLResponse )
def home(request:Request):
    return(templates.TemplateResponse(
        "index.html" , 
        {"request" : request}
    ))

@app.post("/calc" , response_class=HTMLResponse )
def calc_e(request: Request , user_input :int = Form()):

    result = get_e(user_input)

    return(templates.TemplateResponse(
        "index.html" , 
        {
            "request" : request,
            "result" : result
        }
    ))