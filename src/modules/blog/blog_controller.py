from fastapi import Depends
from src.decorators.http import Controller, Get
from .blog_service import BlogService

@Controller("blog")
class BlogController:
    service: BlogService = Depends(BlogService)

    @Get("/")
    def get_many(self):
        return self.service.get_many()