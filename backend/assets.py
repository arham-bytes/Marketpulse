# Assets Catalog containing top 100 cryptos and popular stocks

CRYPTO_ASSETS = [
    {"id": "bitcoin", "symbol": "BTC", "name": "Bitcoin", "color": "#f7931a", "icon": "₿"},
    {"id": "ethereum", "symbol": "ETH", "name": "Ethereum", "color": "#627eea", "icon": "Ξ"},
    {"id": "tether", "symbol": "USDT", "name": "Tether", "color": "#26a17b", "icon": "₮"},
    {"id": "binancecoin", "symbol": "BNB", "name": "BNB", "color": "#f3ba2f", "icon": "B"},
    {"id": "solana", "symbol": "SOL", "name": "Solana", "color": "#9945ff", "icon": "◎"},
    {"id": "ripple", "symbol": "XRP", "name": "XRP", "color": "#00aeff", "icon": "✕"},
    {"id": "usd-coin", "symbol": "USDC", "name": "USDC", "color": "#2775ca", "icon": "S"},
    {"id": "cardano", "symbol": "ADA", "name": "Cardano", "color": "#0033ad", "icon": "₳"},
    {"id": "dogecoin", "symbol": "DOGE", "name": "Dogecoin", "color": "#c2a633", "icon": "Ð"},
    {"id": "avalanche-2", "symbol": "AVAX", "name": "Avalanche", "color": "#e84142", "icon": "A"},
    {"id": "shiba-inu", "symbol": "SHIB", "name": "Shiba Inu", "color": "#ff8a00", "icon": "S"},
    {"id": "polkadot", "symbol": "DOT", "name": "Polkadot", "color": "#e6007a", "icon": "●"},
    {"id": "tron", "symbol": "TRX", "name": "TRON", "color": "#ec0623", "icon": "T"},
    {"id": "chainlink", "symbol": "LINK", "name": "Chainlink", "color": "#2a5ada", "icon": "C"},
    {"id": "polygon", "symbol": "MATIC", "name": "Polygon", "color": "#8247e5", "icon": "P"},
    {"id": "litecoin", "symbol": "LTC", "name": "Litecoin", "color": "#bfbbbb", "icon": "Ł"},
    {"id": "near", "symbol": "NEAR", "name": "NEAR Protocol", "color": "#000000", "icon": "N"},
    {"id": "uniswap", "symbol": "UNI", "name": "Uniswap", "color": "#ff007a", "icon": "U"},
    {"id": "pepe", "symbol": "PEPE", "name": "Pepe", "color": "#00ff00", "icon": "P"},
    {"id": "render-token", "symbol": "RENDER", "name": "Render", "color": "#e62e2d", "icon": "R"},
    {"id": "stellar", "symbol": "XLM", "name": "Stellar", "color": "#000000", "icon": "S"},
    {"id": "aptos", "symbol": "APT", "name": "Aptos", "color": "#1fc7d4", "icon": "A"},
    {"id": "sui", "symbol": "SUI", "name": "Sui", "color": "#6fbcf0", "icon": "S"},
    {"id": "hedera-hashgraph", "symbol": "HBAR", "name": "Hedera", "color": "#000000", "icon": "H"},
    {"id": "kaspa", "symbol": "KAS", "name": "Kaspa", "color": "#70c3ba", "icon": "K"},
    {"id": "monero", "symbol": "XMR", "name": "Monero", "color": "#ff6600", "icon": "M"},
    {"id": "cosmos", "symbol": "ATOM", "name": "Cosmos", "color": "#2e3148", "icon": "A"},
    {"id": "okb", "symbol": "OKB", "name": "OKB", "color": "#3075ee", "icon": "O"},
    {"id": "ethereum-classic", "symbol": "ETC", "name": "Ethereum Classic", "color": "#328332", "icon": "E"},
    {"id": "fantom", "symbol": "FTM", "name": "Fantom", "color": "#1969ff", "icon": "F"},
    {"id": "filecoin", "symbol": "FIL", "name": "Filecoin", "color": "#00cbd8", "icon": "F"},
    {"id": "internet-computer", "symbol": "ICP", "name": "Internet Computer", "color": "#29abe2", "icon": "I"},
    {"id": "stacks", "symbol": "STX", "name": "Stacks", "color": "#5546ff", "icon": "S"},
    {"id": "lido-dao", "symbol": "LDO", "name": "Lido DAO", "color": "#00a3ff", "icon": "L"},
    {"id": "arbitrum", "symbol": "ARB", "name": "Arbitrum", "color": "#28a0f0", "icon": "A"},
    {"id": "optimism", "symbol": "OP", "name": "Optimism", "color": "#ff0420", "icon": "O"},
    {"id": "vechain", "symbol": "VET", "name": "VeChain", "color": "#15bdff", "icon": "V"},
    {"id": "maker", "symbol": "MKR", "name": "Maker", "color": "#1aab9b", "icon": "M"},
    {"id": "injective-protocol", "symbol": "INJ", "name": "Injective", "color": "#00a3ff", "icon": "I"},
    {"id": "theta-token", "symbol": "THETA", "name": "Theta Network", "color": "#2ab8c5", "icon": "T"},
    {"id": "immutable-x", "symbol": "IMX", "name": "Immutable", "color": "#0d0d0d", "icon": "I"},
    {"id": "thorchain", "symbol": "RUNE", "name": "THORChain", "color": "#00e6c4", "icon": "R"},
    {"id": "graph", "symbol": "GRT", "name": "The Graph", "color": "#2f254f", "icon": "G"},
    {"id": "feth", "symbol": "FET", "name": "Artificial Superintelligence Alliance", "color": "#0a192f", "icon": "F"},
    {"id": "arweave", "symbol": "AR", "name": "Arweave", "color": "#000000", "icon": "A"},
    {"id": "felsius", "symbol": "CEL", "name": "Celsius", "color": "#44007f", "icon": "C"},
    {"id": "jupiter-exchange-solana", "symbol": "JUP", "name": "Jupiter", "color": "#1ec6a5", "icon": "J"},
    {"id": "floki", "symbol": "FLOKI", "name": "Floki", "color": "#f2a007", "icon": "F"},
    {"id": "bonk", "symbol": "BONK", "name": "Bonk", "color": "#f2a007", "icon": "B"},
    {"id": "algorand", "symbol": "ALGO", "name": "Algorand", "color": "#000000", "icon": "A"},
    {"id": "gala", "symbol": "GALA", "name": "Gala", "color": "#0d1b2a", "icon": "G"},
    {"id": "eos", "symbol": "EOS", "name": "EOS", "color": "#000000", "icon": "E"},
    {"id": "flow", "symbol": "FLOW", "name": "Flow", "color": "#00ef8b", "icon": "F"},
    {"id": "quant-network", "symbol": "QNT", "name": "Quant", "color": "#000000", "icon": "Q"},
    {"id": "fida", "symbol": "FIDA", "name": "Bonfida", "color": "#1ec6a5", "icon": "F"},
    {"id": "chiliz", "symbol": "CHZ", "name": "Chiliz", "color": "#cd0124", "icon": "C"},
    {"id": "mina-protocol", "symbol": "MINA", "name": "Mina", "color": "#f6851b", "icon": "M"},
    {"id": "beam", "symbol": "BEAM", "name": "Beam", "color": "#00e6c4", "icon": "B"},
    {"id": "axie-infinity", "symbol": "AXS", "name": "Axie Infinity", "color": "#0055ff", "icon": "A"},
    {"id": "synthetix-network-token", "symbol": "SNX", "name": "Synthetix", "color": "#00d1ff", "icon": "S"},
    {"id": "decentraland", "symbol": "MANA", "name": "Decentraland", "color": "#ff2d55", "icon": "M"},
    {"id": "the-sandbox", "symbol": "SAND", "name": "The Sandbox", "color": "#0084ff", "icon": "S"},
    {"id": "dydx", "symbol": "DYDX", "name": "dYdX", "color": "#6966ff", "icon": "D"},
    {"id": "dexe", "symbol": "DEXE", "name": "DeXe", "color": "#00e6c4", "icon": "D"},
    {"id": "kava", "symbol": "KAVA", "name": "Kava", "color": "#ff5c5c", "icon": "K"},
    {"id": "pancakeswap-token", "symbol": "CAKE", "name": "PancakeSwap", "color": "#d1884f", "icon": "C"},
    {"id": "woonetwork", "symbol": "WOO", "name": "WOO Network", "color": "#3366ff", "icon": "W"},
    {"id": "zcash", "symbol": "ZEC", "name": "Zcash", "color": "#ecb22e", "icon": "Z"},
    {"id": "dash", "symbol": "DASH", "name": "Dash", "color": "#008de4", "icon": "D"},
    {"id": "iota", "symbol": "IOTA", "name": "IOTA", "color": "#000000", "icon": "I"},
    {"id": "waves", "symbol": "WAVES", "name": "Waves", "color": "#0055ff", "icon": "W"},
    {"id": "neo", "symbol": "NEO", "name": "NEO", "color": "#58bf00", "icon": "N"},
    {"id": "nem", "symbol": "XEM", "name": "NEM", "color": "#41bfb3", "icon": "N"},
    {"id": "qtum", "symbol": "QTUM", "name": "Qtum", "color": "#2c9ae9", "icon": "Q"},
    {"id": "yearn-finance", "symbol": "YFI", "name": "yearn.finance", "color": "#006ae3", "icon": "Y"},
    {"id": "loopring", "symbol": "LRC", "name": "Loopring", "color": "#1c60ff", "icon": "L"},
    {"id": "enjincoin", "symbol": "ENJ", "name": "Enjin Coin", "color": "#6236ff", "icon": "E"},
    {"id": "0x", "symbol": "ZRX", "name": "0x", "color": "#302e2e", "icon": "Z"},
    {"id": "bancor", "symbol": "BNT", "name": "Bancor", "color": "#0000d6", "icon": "B"},
    {"id": "ankr", "symbol": "ANKR", "name": "Ankr", "color": "#2075ee", "icon": "A"},
    {"id": "ravencoin", "symbol": "RVN", "name": "Ravencoin", "color": "#f05a28", "icon": "R"},
    {"id": "basic-attention-token", "symbol": "BAT", "name": "Basic Attention Token", "color": "#ff5000", "icon": "B"},
    {"id": "omg", "symbol": "OMG", "name": "OMG Network", "color": "#1a1a1a", "icon": "O"},
    {"id": "icon", "symbol": "ICX", "name": "ICON", "color": "#00a8cc", "icon": "I"},
    {"id": "siacoin", "symbol": "SC", "name": "Siacoin", "color": "#00cba0", "icon": "S"},
    {"id": "audius", "symbol": "AUDIO", "name": "Audius", "color": "#cc00ff", "icon": "A"},
    {"id": "compound-governance-token", "symbol": "COMP", "name": "Compound", "color": "#00d395", "icon": "C"},
    {"id": "sushi", "symbol": "SUSHI", "name": "Sushi", "color": "#e05b9b", "icon": "S"},
    {"id": "harmony", "symbol": "ONE", "name": "Harmony", "color": "#00bfff", "icon": "O"},
    {"id": "wax", "symbol": "WAXP", "name": "WAX", "color": "#f58634", "icon": "W"},
    {"id": "playdapp", "symbol": "PDA", "name": "PlayDapp", "color": "#1c82e6", "icon": "P"},
    {"id": "polymath", "symbol": "POLY", "name": "Polymath", "color": "#4c5cf4", "icon": "P"},
    {"id": "wazirx", "symbol": "WRX", "name": "WazirX", "color": "#0052cc", "icon": "W"},
    {"id": "syscoin", "symbol": "SYS", "name": "Syscoin", "color": "#008de4", "icon": "S"},
    {"id": "dent", "symbol": "DENT", "name": "Dent", "color": "#f0324b", "icon": "D"},
    {"id": "storm", "symbol": "STMX", "name": "StormX", "color": "#0062ff", "icon": "S"},
    {"id": "dogelon-mars", "symbol": "ELON", "name": "Dogelon Mars", "color": "#ff7a00", "icon": "E"},
    {"id": "steem", "symbol": "STEEM", "name": "Steem", "color": "#3b5998", "icon": "S"},
    {"id": "reserve-rights-token", "symbol": "RSR", "name": "Reserve Rights", "color": "#000000", "icon": "R"},
    {"id": "civic", "symbol": "CVC", "name": "Civic", "color": "#3ab03e", "icon": "C"}
]

STOCK_ASSETS = [
    {"symbol": "AAPL", "name": "Apple Inc.", "color": "#a2aaad", "icon": ""},
    {"symbol": "MSFT", "name": "Microsoft Corporation", "color": "#f25022", "icon": "M"},
    {"symbol": "GOOGL", "name": "Alphabet Inc.", "color": "#4285f4", "icon": "G"},
    {"symbol": "AMZN", "name": "Amazon.com, Inc.", "color": "#ff9900", "icon": "A"},
    {"symbol": "TSLA", "name": "Tesla, Inc.", "color": "#e82127", "icon": "T"},
    {"symbol": "NVDA", "name": "NVIDIA Corporation", "color": "#76b900", "icon": "N"},
    {"symbol": "META", "name": "Meta Platforms, Inc.", "color": "#0668e1", "icon": "M"},
    {"symbol": "NFLX", "name": "Netflix, Inc.", "color": "#e50914", "icon": "N"},
    {"symbol": "AMD", "name": "Advanced Micro Devices", "color": "#ed1c24", "icon": "A"},
    {"symbol": "INTC", "name": "Intel Corporation", "color": "#0071c5", "icon": "I"},
    {"symbol": "BABA", "name": "Alibaba Group Holding", "color": "#ff6a00", "icon": "A"},
    {"symbol": "JPM", "name": "JPMorgan Chase & Co.", "color": "#1g82c3", "icon": "J"},
    {"symbol": "BAC", "name": "Bank of America Corp.", "color": "#012169", "icon": "B"},
    {"symbol": "WMT", "name": "Walmart Inc.", "color": "#007dc6", "icon": "W"},
    {"symbol": "COST", "name": "Costco Wholesale Corp.", "color": "#005ea6", "icon": "C"},
    {"symbol": "DIS", "name": "The Walt Disney Company", "color": "#11385b", "icon": "D"},
    {"symbol": "NKE", "name": "NIKE, Inc.", "color": "#000000", "icon": "N"},
    {"symbol": "V", "name": "Visa Inc.", "color": "#1a1f71", "icon": "V"},
    {"symbol": "MA", "name": "Mastercard Inc.", "color": "#eb001b", "icon": "M"},
    {"symbol": "PYPL", "name": "PayPal Holdings, Inc.", "color": "#003087", "icon": "P"},
    {"symbol": "ADBE", "name": "Adobe Inc.", "color": "#ff0000", "icon": "A"},
    {"symbol": "CRM", "name": "Salesforce, Inc.", "color": "#00a1e0", "icon": "S"},
    {"symbol": "ORCL", "name": "Oracle Corporation", "color": "#f80000", "icon": "O"},
    {"symbol": "CSCO", "name": "Cisco Systems, Inc.", "color": "#00b4e5", "icon": "C"},
    {"symbol": "HD", "name": "The Home Depot, Inc.", "color": "#f96302", "icon": "H"},
    {"symbol": "McDonalds", "name": "McDonald's Corporation", "color": "#ffc72c", "icon": "M"},
    {"symbol": "PEP", "name": "PepsiCo, Inc.", "color": "#004b93", "icon": "P"},
    {"symbol": "KO", "name": "The Coca-Cola Company", "color": "#fe001a", "icon": "K"},
    {"symbol": "XOM", "name": "Exxon Mobil Corporation", "color": "#003d7a", "icon": "X"},
    {"symbol": "CVX", "name": "Chevron Corporation", "color": "#0056a1", "icon": "C"},
    {"symbol": "LLY", "name": "Eli Lilly and Company", "color": "#005ea6", "icon": "L"},
    {"symbol": "PFE", "name": "Pfizer Inc.", "color": "#003087", "icon": "P"},
    {"symbol": "MRNA", "name": "Moderna, Inc.", "color": "#18bc9c", "icon": "M"},
    {"symbol": "QCOM", "name": "QUALCOMM Incorporated", "color": "#002d62", "icon": "Q"},
    {"symbol": "TXN", "name": "Texas Instruments Inc.", "color": "#ff0000", "icon": "T"},
    {"symbol": "SBUX", "name": "Starbucks Corporation", "color": "#00704a", "icon": "S"},
    {"symbol": "UPS", "name": "United Parcel Service", "color": "#351c15", "icon": "U"},
    {"symbol": "GE", "name": "General Electric Company", "color": "#005ca9", "icon": "G"},
    {"symbol": "IBM", "name": "International Business Machines", "color": "#006699", "icon": "I"},
    {"symbol": "T", "name": "AT&T Inc.", "color": "#00a8e0", "icon": "T"},
    {"symbol": "VZ", "name": "Verizon Communications", "color": "#cd040b", "icon": "V"},
    {"symbol": "CAT", "name": "Caterpillar Inc.", "color": "#ffcd00", "icon": "C"},
    {"symbol": "BA", "name": "The Boeing Company", "color": "#0033a0", "icon": "B"},
    {"symbol": "DE", "name": "Deere & Company", "color": "#367c2b", "icon": "D"},
    {"symbol": "HON", "name": "Honeywell International Inc.", "color": "#e31837", "icon": "H"},
    {"symbol": "MMM", "name": "3M Company", "color": "#ff0000", "icon": "3"},
    {"symbol": "GS", "name": "The Goldman Sachs Group", "color": "#0060a9", "icon": "G"},
    {"symbol": "MS", "name": "Morgan Stanley", "color": "#003366", "icon": "M"},
    {"symbol": "SCHW", "name": "The Charles Schwab Corp.", "color": "#00a4e4", "icon": "S"},
    {"symbol": "AXP", "name": "American Express Company", "color": "#002677", "icon": "A"}
]

# Quick maps for O(1) checks
CRYPTO_MAP_BY_SYM = {c["symbol"].lower(): c for c in CRYPTO_ASSETS}
CRYPTO_MAP_BY_ID = {c["id"].lower(): c for c in CRYPTO_ASSETS}
STOCK_MAP_BY_SYM = {s["symbol"].lower(): s for s in STOCK_ASSETS}

def get_asset_type(symbol: str) -> str:
    """Check if a symbol/ID is crypto or stock."""
    sym_lower = symbol.lower().strip()
    if sym_lower in CRYPTO_MAP_BY_SYM or sym_lower in CRYPTO_MAP_BY_ID:
        return "crypto"
    if sym_lower in STOCK_MAP_BY_SYM:
        return "stock"
    
    # Defaults/Guessing:
    # If the symbol has 4 letters or less and is alphabetical, and doesn't map to crypto, we treat it as stock.
    # Otherwise, it might be stock by default. Let's make stocks the fallback.
    return "stock"

def get_coingecko_id(symbol: str) -> str:
    """Get CoinGecko ID for a crypto symbol or return the input itself if it's already an ID."""
    sym_lower = symbol.lower().strip()
    if sym_lower in CRYPTO_MAP_BY_ID:
        return sym_lower
    if sym_lower in CRYPTO_MAP_BY_SYM:
        return CRYPTO_MAP_BY_SYM[sym_lower]["id"]
    return None

def search_assets(query: str):
    """Filter top cryptos and stocks matching query."""
    q = query.lower().strip()
    results = []
    
    # Search Cryptos
    for c in CRYPTO_ASSETS:
        if q in c["id"].lower() or q in c["symbol"].lower() or q in c["name"].lower():
            results.append({**c, "type": "crypto"})
            
    # Search Stocks
    for s in STOCK_ASSETS:
        if q in s["symbol"].lower() or q in s["name"].lower():
            results.append({**s, "type": "stock"})
            
    return results[:20]  # Limit to 20 search results
