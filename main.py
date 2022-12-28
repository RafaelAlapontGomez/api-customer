from fastapi import FastAPI

from app.v1.router.customer_router import router as customer_router

app = FastAPI()

app.include_router(customer_router)