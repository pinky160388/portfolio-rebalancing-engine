from dataclasses import dataclass
from typing import List


@dataclass
class Security:
    symbol: str
    target_percent: float
    current_percent: float
    unit_price: float


TOTAL_ASSET = 100000


def calculate_shares_to_trade(security: Security) -> int:
    """
    Calculates number of shares to buy/sell.

    Negative variance => BUY
    Positive variance => SELL
    """

    variance_percent = security.target_percent - security.current_percent

    variance_amount = (variance_percent / 100) * TOTAL_ASSET

    shares = variance_amount / security.unit_price

    return round(shares)


def rebalance_portfolio(securities: List[Security]) -> dict:
    result = {}

    for security in securities:
        shares = calculate_shares_to_trade(security)

        if shares < 0:
            action = "BUY"
        elif shares > 0:
            action = "SELL"
        else:
            action = "HOLD"

        result[security.symbol] = {
            "action": action,
            "shares": abs(shares)
        }

    return result


if __name__ == "__main__":

    portfolio = [
        Security("IBM", 20, 10, 150),
        Security("MSFT", 20, 20, 90),
        Security("ORCL", 20, 30, 220),
        Security("AAPL", 20, 20, 450),
        Security("HD", 20, 20, 70),
    ]

    output = rebalance_portfolio(portfolio)

    for symbol, data in output.items():
        print(f"{symbol}: {data['action']} {data['shares']} shares")
