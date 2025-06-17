from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from stack import Stack

app = FastAPI()

class BracketString(BaseModel):
    text: str

@app.post("/brackets/check/")
async def check_brackets(data: BracketString) -> Dict[str, bool]:
    s = data.text
    stack = []
    map = {'(': ')', '[': ']', '{': '}'}
    ob = set(map.keys())
    cb = set(map.values())
    for c in s:
        if c in ob:
            stack.append(c)
        elif c in cb:
            if not stack:
                return {"norm:": False}
            to_pop = stack.pop()
            if map[to_pop] != c:
                return {"norm:": False}
    return {"norm:": not stack}