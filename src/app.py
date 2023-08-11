from typing import List, Callable
from fastapi import FastAPI, APIRouter


class App(FastAPI):
    def __init__(self, title: str, description: str, modules: List):
        super().__init__(
            title=title, 
            description=description
        )
        
        self.modules = modules
        self._register_controllers()

    def _register_controllers(self):
        for module in self.modules:
            module_instance = module()
            for controller in module_instance.controllers:
                router: APIRouter = controller.get_router()
                self.include_router(router)