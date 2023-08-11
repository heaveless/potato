from fastapi.routing import APIRouter
from .helpers import class_based_view as ClassBasedView

def Controller(tag: str = None):
    prefix = tag

    if prefix:
        prefix = "/" + prefix

    def wrapper(cls) -> ClassBasedView:
        router = APIRouter(tags=[tag] if tag else None)

        for name, method in cls.__dict__.items():
            if callable(method) and hasattr(method, "method"):
                if not method.__path__:
                    raise Exception("Missing path")
                else:
                    if prefix:
                        method.__path__ = prefix + method.__path__
                    if not method.__path__.startswith("/"):
                        method.__path__ = "/" + method.__path__
                    if method.method == "GET":
                        router.add_api_route(
                            method.__path__,
                            method,
                            methods=["GET"],
                            **method.__kwargs__
                        )
                    elif method.method == "POST":
                        router.add_api_route(
                            method.__path__,
                            method,
                            methods=["POST"],
                            **method.__kwargs__
                        )
                    elif method.method == "PUT":
                        router.add_api_route(
                            method.__path__,
                            method,
                            methods=["PUT"],
                            **method.__kwargs__
                        )
                    elif method.method == "DELETE":
                        router.add_api_route(
                            method.__path__,
                            method,
                            methods=["DELETE"],
                            **method.__kwargs__
                        )
                    elif method.method == "PATCH":
                        router.add_api_route(
                            method.__path__,
                            method,
                            methods=["PATCH"],
                            **method.__kwargs__
                        )
                    else:
                        raise Exception("Invalid method")

        def get_router() -> APIRouter:
            return router

        cls.get_router = get_router

        return ClassBasedView(router=router, cls=cls)

    return wrapper


def Get(path: str, **kwargs):
    def decorator(func):
        func.method = "GET"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator


def Post(path: str, **kwargs):
    def decorator(func):
        func.method = "POST"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator


def Delete(path: str, **kwargs):
    def decorator(func):
        func.method = "DELETE"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator


def Put(path: str, **kwargs):
    def decorator(func):
        func.method = "PUT"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator


def Patch(path: str, **kwargs):
    def decorator(func):
        func.method = "PATCH"
        func.__path__ = path
        func.__kwargs__ = kwargs
        return func

    return decorator