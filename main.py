from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from service.odoo import odoo
import json
art = """
                          _
                         / )
                        / /    _
              _        / /    / )
             ( `.     / /-.  / /
              `\ \   / // /`/ /
                ; `-`  (_/ / /
                |       (_/ /
                \          /
                 )       /`
        laços   /      /`
"""
app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def root():
    return art


@app.get("/user/{pk}")
async def users(pk: int):
    user = odoo.env["res.users"]
    user_data = user.read([pk], ["name"])
    return user_data
