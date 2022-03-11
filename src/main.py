import uvicorn
import strawberry
from fastapi import FastAPI

from strawberry.fastapi import GraphQLRouter
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from src.config import TORTOISE_ORM

async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
register_tortoise(
    app, 
    config=TORTOISE_ORM,
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/status")
async def status():
    return {"success": True}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("wedding-backend.main:app", host="0.0.0.0", port=8000, reload=True)