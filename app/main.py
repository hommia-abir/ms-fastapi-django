import pathlib #or u could import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
BASE_DIR= pathlib.Path(__file__).parent
app=FastAPI()  #to get to this variable : app.main.app
templates=Jinja2Templates(directory=str(BASE_DIR / "templates"))
#rest api is an incredibally common way for two apps to communicate
#with fast api , every endpoint by default will return a JSON file
@app.get("/",response_class=HTMLResponse) #http get
def home_view(request:Request):
    return templates.TemplateResponse("home.html",{"request":request,"abc":123})#it is mandatory to poass
#it at least a dictionary with the request itself coming in , you could also include any arguments(variables) u want to pass
#and these arguments can be accessed in the page that u're rendering
@app.post("/") #http post
def home_detail_view():
    return {"hello":"world"}
