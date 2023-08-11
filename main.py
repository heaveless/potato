from fastapi.middleware.cors import CORSMiddleware
from src.commons.config import CORS_ORIGIN
from src.app import App

from src.modules.blog.blog_module import BlogModule

app = App(
    title="Potato",
    description="Profile Manager",
    modules=[
        BlogModule
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGIN.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)