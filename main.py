from fastapi import FastAPI
from fastapi.responses import JSONResponse
from router import blog_get, blog_post, user
from db import models, database



app = FastAPI(
    title="FastAPI Tutorial",
    description="FastAPI tutorial for API development",
    version="0.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/api/v1/openapi.json",
    # favicon of fastapi logo
    favicon="https://cdn.oaistatic.com/_next/static/media/apple-touch-icon.82af6fe1.png",

)

# import router from the router module
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)



@app.get(
        "/",
        tags=["Home"],
        summary="Home page",
        description="Home page of the API",
        response_description="Home page",
        status_code=200,
        ) 
def index():
    # return json response with message
    return JSONResponse(content={
        "message": "Welcome to Precogs MVP API","status":200,"data":{
        "endpoints":{
            "GET /blog/all":"Get all blogs with pagination",
            "GET /blog/{id}/comments/{comment_id}":"Get a specific blog comment",
            "GET /blog/type/{type}":"Get blog by type",
            "GET /blog/{id}":"Get blog by id",
            "POST /blog/new":"Create new blog"
            }
    }}
    )

# create all tables in the database

models.Base.metadata.create_all(bind=database.engine)