# Portfolio Rebalancing Engine

## Overview

This project implements a simple portfolio rebalancing engine.

The application calculates the number of shares to BUY, SELL, or HOLD in order to rebalance a portfolio based on:

* Target allocation percentage
* Current allocation percentage
* Security unit price
* Total portfolio value

The total portfolio value used in this solution is:

```python
TOTAL_ASSET = 100000
```

---

## Problem Statement

Account ABC holds the following securities:

* IBM
* MSFT
* ORCL
* AAPL
* HD

Each security has:

* Target percentage allocation
* Current percentage allocation
* Unit price

The goal is to determine how many shares should be bought or sold to achieve the target allocation and reduce portfolio variance to zero.

---

## Rebalancing Logic

The following logic is used:

### Step 1 — Calculate variance

```python
variance_percent = target_percent - current_percent
```

### Step 2 — Convert variance into portfolio exposure

```python
variance_amount = (variance_percent / 100) * TOTAL_ASSET
```

### Step 3 — Convert exposure into shares

```python
shares = variance_amount / unit_price
```

### Action Rules

* Positive shares → BUY
* Negative shares → SELL
* Zero shares → HOLD

---

## Assumptions

* Total portfolio value remains constant
* Prices are static during calculation
* Fractional shares are allowed
* Monetary values are based on the provided total asset value
* Rounding is limited to 2 decimal places

---

## Project Structure

```text
portfolio-rebalancing-engine/
│
├── src/
│   └── rebalance.py
│
├── tests/
│   └── test_rebalance.py
│
├── requirements.txt
└── README.md
```

---

## Automated Test Cases

The following automated tests are included:

1. Verify BUY action for underweight securities
2. Verify SELL action for overweight securities
3. Verify HOLD action when target equals current allocation
4. Validate correct share calculations
5. Validate portfolio rebalance behavior

---

## Manual Test Scenarios

### Test Case 1 — Buy Scenario

* Security current allocation is below target
* Expected result: BUY action generated

### Test Case 2 — Sell Scenario

* Security current allocation is above target
* Expected result: SELL action generated

### Test Case 3 — Hold Scenario

* Security current allocation equals target
* Expected result: HOLD action generated

### Test Case 4 — Zero Price Validation

* Security price equals zero
* Expected result: division safety handling

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run application

```bash
python src/rebalance.py
```

### Run tests

```bash
pytest
```

---

## Technologies Used

* Python 3
* Pytest
* Dataclasses

---

## Author

Technical assessment implementation for portfolio rebalancing and testing scenario.

