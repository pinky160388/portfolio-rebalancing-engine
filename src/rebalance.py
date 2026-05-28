class Security:

    def __init__(self, name, target_pct, current_pct, unit_price):
        self.name = name
        self.target_pct = target_pct
        self.current_pct = current_pct
        self.unit_price = unit_price


TOTAL_ASSET = 100000


def rebalance_portfolio(portfolio):

    results = {}

    for security in portfolio:

        variance = security.target_pct - security.current_pct

        rebalance_amount = (variance / 100) * TOTAL_ASSET

        shares = round(abs(rebalance_amount / security.unit_price))

        if variance > 0:
            action = "BUY"
        elif variance < 0:
            action = "SELL"
        else:
            action = "HOLD"

        results[security.name] = {
            "action": action,
            "shares": shares
        }

    return results
