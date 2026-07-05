from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from database import get_connection
from auth_utils import hash_password, verify_password, create_access_token

router = APIRouter()

class UserSignUp(BaseModel):
    username: str
    email: str
    password: str

class UserLogIn(BaseModel):
    email: str
    password: str

@router.post("/signup")
def signup(user: UserSignUp):
    username = user.username.strip()
    email = user.email.strip().lower()
    password = user.password

    if not username or not email or not password:
        raise HTTPException(status_code=400, detail="All fields are required")

    pwd_hash = hash_password(password)

    try:
        conn = get_connection()
        cur = conn.cursor()

        # Check email
        cur.execute("SELECT id FROM users WHERE email = %s", (email,))
        if cur.fetchone():
            cur.close()
            conn.close()
            raise HTTPException(status_code=400, detail="Email is already registered")

        # Check username
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        if cur.fetchone():
            cur.close()
            conn.close()
            raise HTTPException(status_code=400, detail="Username is already taken")

        # Insert user
        cur.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, pwd_hash)
        )
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "User registered successfully"}
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Signup error: {e}")
        raise HTTPException(status_code=500, detail="Error occurred during user registration")

@router.post("/login")
def login(user: UserLogIn):
    email = user.email.strip().lower()
    password = user.password

    try:
        conn = get_connection()
        cur = conn.cursor()

        # Fetch user details
        cur.execute("SELECT id, username, password_hash, email FROM users WHERE email = %s", (email,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            raise HTTPException(status_code=400, detail="Invalid email or password")

        user_id, username, stored_hash, user_email = row

        if not verify_password(stored_hash, password):
            raise HTTPException(status_code=400, detail="Invalid email or password")

        # Generate access token
        access_token = create_access_token(
            data={"sub": str(user_id), "email": user_email, "username": username}
        )

        return {
            "message": "Login successful",
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user_id,
                "username": username,
                "email": user_email
            }
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Login error: {e}")
        raise HTTPException(status_code=500, detail="Error occurred during login")
