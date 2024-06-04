from fastapi import FastAPI

app = FastAPI()

import ast


@app.get("/direct/{input}")
def direct_response(input: str):

    tainted = input

    # ruleid: tainted-code-stdlib-fastapi
    eval(tainted)
    # ruleid: tainted-code-stdlib-fastapi
    exec(tainted)

    # ok: tainted-code-stdlib-fastapi
    ast.literal_eval(tainted)

    # ok: tainted-code-stdlib-fastapi
    eval("clean")
    # ok: tainted-code-stdlib-fastapi
    exec("clean")

    # ok: tainted-code-stdlib-fastapi
    ast.literal_eval("clean")
