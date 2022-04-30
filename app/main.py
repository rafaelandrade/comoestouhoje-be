import time
import sentry_sdk

from fastapi import FastAPI
from starlette.requests import Request
from starlette_context import plugins, context
from starlette_context.middleware import RawContextMiddleware
from starlette.responses import JSONResponse

app = FastAPI(
    title="BE-comoestouhoje",
    description="backend of comoestouhoje service",
    version="1.0.0",
    docs_url="/comoestouhoje/docs",
    redoc_url="/comoestouhoje/redoc"
)


async def catch_exception_middleware(request: Request, call_next):
    start_request_time = time.time()

    try:
        response = await call_next(request)
        process_request_time = round((time.time() - start_request_time) * 1000, 2)
        print(f"process_request_time: {process_request_time} - status {response.status}")
        return response
    except Exception as _:
        return JSONResponse({
            "error": True,
            "message": "Internal Server Error",
        }, status_code=500)

app.middleware('http')(catch_exception_middleware)
app.add_middleware(RawContextMiddleware, plugins=(plugins.RequestIdPlugin(), plugins.CorrelationIdPlugin()))


@app.get("/")
async def root():
    return {"error": False, "message": "Hello World!"}
