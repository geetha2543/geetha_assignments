import os
from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, text 
app = FastAPI()


SCHEMA = ["name", "age"]

def get_db():
    DATABASE = os.path.join(".", "people.db")
    db = create_engine("sqlite:///" + DATABASE)
    return db 
    
class NotFound(Exception):
    pass
    
def get_all():
    eng = get_db()
    with eng.connect() as conn:
        res = conn.execute(text("select name, age from people")).fetchall()
    return [dict(zip(SCHEMA,row)) for row in res]    

def get_age(name):
    eng = get_db()
    with eng.connect() as conn:
        #list of tuples/rows - fetchall 
        #tuple/one row - fetchone
        res = conn.execute(text("select age from people where name = :name"),
                dict(name=name)).fetchone()
        if res:
            return res[0]
        else:
            raise NotFound("NotFound")
  
@app.get("/all")      
async def hello_all():
    return get_all()


@app.post("/helloj")
@app.get("/helloj/{name}/{format}")
async def helloj_fastapi(request: Request,name:str="abc",format:str="json"):
    fformat, fname = format, name 
    if request.method == 'GET':
        fname = request.query_params.get("name", name)
        fformat = request.query_params.get("format", format)
    else:
        if request.headers.get('Content-Type','').startswith("application/json"):
            body = await request.json()
            fname = body.get("name", name)  
            fformat = request.query_params.get("format", format)
    age = None
    try:
        age = get_age(fname)
        obj = dict(name=fname, age=age)
    except NotFound:
        obj = dict(name=fname, details="Not found")
    resp = JSONResponse(obj)  
    if age is not None:
        resp.status_code = 200
    else:
        resp.status_code = 500
    return resp 
  
 
