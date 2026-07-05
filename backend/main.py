from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.prices import router as prices_router
from routes.portfolio import router as portfolio_router
from routes.news import router as news_router
from routes.auth import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prices_router, prefix="/api/prices")
app.include_router(portfolio_router, prefix="/api/portfolio")
app.include_router(news_router, prefix="/api/news")
app.include_router(auth_router, prefix="/api/auth")

@app.get("/")
def read_root():
    return {"message": "MarketPulse API is running!"}