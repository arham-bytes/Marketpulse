from fastapi import APIRouter, Depends, HTTPException
from database import get_connection
from auth_utils import get_current_user

router = APIRouter()

@router.get("/")
def get_portfolio(current_user: dict = Depends(get_current_user)):
    user_id = current_user["id"]
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, symbol, quantity, buy_price, bought_at FROM portfolio WHERE user_id = %s", (user_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    portfolio = []
    for row in rows:
        portfolio.append({
            "id": row[0],
            "symbol": row[1],
            "quantity": float(row[2]),
            "buy_price": float(row[3]),
            "bought_at": str(row[4])
        })
    return portfolio

@router.post("/add")
def add_to_portfolio(symbol: str, quantity: float, buy_price: float, current_user: dict = Depends(get_current_user)):
    user_id = current_user["id"]
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO portfolio (symbol, quantity, buy_price, user_id) VALUES (%s, %s, %s, %s)",
        (symbol.lower().strip(), quantity, buy_price, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": f"{symbol} added to portfolio!"}

@router.delete("/remove/{id}")
def remove_from_portfolio(id: int, current_user: dict = Depends(get_current_user)):
    user_id = current_user["id"]
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM portfolio WHERE id = %s AND user_id = %s", (id, user_id))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Removed from portfolio!"}