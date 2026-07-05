# MarketPulse 📈

MarketPulse is a professional-grade personal portfolio tracker, asset pricing, live charting, and financial news dashboard. Designed with premium dark-mode aesthetics, fluid micro-interactions, and a secure backend architecture, MarketPulse lets users track their portfolio holdings, analyze real-time market data, and compare asset performance dynamically.

---

## Key Features 🚀

### 1. **Personal Portfolio Holdings Tracker**
*   Add and track custom holdings of cryptocurrencies and stocks with acquisition quantities and average buy prices.
*   Enforces secure backend session validation to ensure holdings remain private and protected.
*   Shows live holdings value updates dynamically adjusting to real-time market price movements.

### 2. **Interactive Live Charting**
*   Integrated **Chart.js** displaying real historical asset pricing data.
*   Adjustable timeframes (`1H`, `1D`, `3D`, `1W`, `1M`) for comprehensive technical summaries.
*   Quick asset selector dropdown defaulting to **Bitcoin (BTC)**, with searchable listings supporting all top cryptos and stocks.

### 3. **Live Prices & Market Explorer**
*   Queries **Yahoo Finance (`yfinance`)** as the primary live price provider for ultra-low latency, highly accurate real-time market rates.
*   Implements **CoinGecko API** as a robust secondary fallback provider.
*   Searchable listings covering the **top 100 cryptocurrencies** and **top global stocks** (Apple, Nvidia, Microsoft, Tesla, etc.) with custom branding colors and live sparkline graphs.

### 4. **Secure Authentication System**
*   Token-based sessions powered by **JWT (JSON Web Tokens)**.
*   State-of-the-art password hashing using **bcrypt** (cost factor 12) for secure credential storage.
*   Protected endpoints behind custom FastAPI dependency injection guards.

### 5. **Financial News Feed**
*   Aggregates live market news articles relating to selected assets to keep users up-to-date.

### 6. **Premium UI/UX & Navigation Toggles**
*   Dynamic navigation dropdowns for **Notifications** and **User Profiles** that auto-close on clicking outside.
*   Dynamic avatar circles reflecting the logged-in user's initials.
*   Fully responsive sidebar navigation designed for modern desktop displays.

---

## Tech Stack 🛠️

*   **Frontend**: HTML5 (Semantic Structure), Vanilla CSS3 (Custom design tokens, glassmorphism, responsive grids), and Vanilla Javascript (ES6+, asynchronous fetch API).
*   **Backend**: Python 3, FastAPI (High-performance web framework), Uvicorn (ASGI server).
*   **Database**: PostgreSQL connection pooling (relational data model for user registry and portfolio assets).
*   **APIs & Libraries**: yfinance (Yahoo Finance), CoinGecko API, PyJWT, bcrypt.

---

## Directory Structure 📂

```text
Marketpulse/
├── backend/
│   ├── routes/
│   │   ├── auth.py          # Session signup and logins
│   │   ├── portfolio.py     # Holdings manager protected routes
│   │   ├── prices.py        # Yahoo Finance / CoinGecko APIs
│   │   └── news.py          # Financial news endpoint
│   ├── auth_utils.py        # Password hashing & JWT dependencies
│   ├── assets.py            # Global list of 100+ cryptos and stocks
│   ├── database.py          # PostgreSQL database connector pool
│   ├── main.py              # FastAPI initialization & CORS configurations
│   └── requirements.txt     # Python dependencies list
└── frontend/
    ├── marketpulse_landing.html  # User signup / login gateway
    ├── dashboard.html            # Main tracking dashboard & live chart
    ├── portfolio.html            # Complete user holdings analysis
    ├── markets.html              # Market overview search tables
    ├── news.html                 # Latest financial news articles
    ├── settings.html             # Profile configurations panel
    └── style.css                 # Shared styling library & dropdown layouts
```

---

## Getting Started & Local Setup 💻

### 1. Database Configuration
1. Ensure **PostgreSQL** is running locally on port `5432`.
2. Create a database named `marketpulse`.
3. Set up the schema tables for `users`, `portfolio_items`, and `price_cache` as per database configurations.

### 2. Start the Backend Server
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Activate your virtual environment and install dependencies:
   ```bash
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Launch the FastAPI server:
   ```bash
   python -m uvicorn main:app --reload
   ```
   *The backend will run on `http://127.0.0.1:8000`.*

### 3. Start the Frontend Server
You can launch the static files in the `frontend` folder using any local static server. For example:
*   Using **VS Code Live Server Extension** (Port `5500`).
*   Using Python's built-in server (Port `3000`):
    ```bash
    python -m http.server 3000
    ```
*Open `marketpulse_landing.html` in your browser to begin.*
