from src.rebalance import Security, rebalance_portfolio


def test_ibm_should_buy():
    portfolio = [
        Security("IBM", 20, 10, 150)
    ]

    result = rebalance_portfolio(portfolio)

    assert result["IBM"]["action"] == "BUY"


def test_orcl_should_sell():
    portfolio = [
        Security("ORCL", 20, 30, 220)
    ]

    result = rebalance_portfolio(portfolio)

    assert result["ORCL"]["action"] == "SELL"


def test_msft_should_hold():
    portfolio = [
        Security("MSFT", 20, 20, 90)
    ]

    result = rebalance_portfolio(portfolio)

    assert result["MSFT"]["action"] == "HOLD"


def test_aapl_should_hold():
    portfolio = [
        Security("AAPL", 20, 20, 450)
    ]

    result = rebalance_portfolio(portfolio)

    assert result["AAPL"]["action"] == "HOLD"
