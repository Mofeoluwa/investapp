# etf_recommender.py

def recommend_etfs(risk, horizon, goal):
    """
    Returns a list of ETF recommendations (up to three) based on the risk tolerance,
    investment horizon, and investment goal (growth/income).
    """
    # Sample ETF database. In a real application, these could be fetched from the net.
    etf_data = [
        {
            "name": "Vanguard Total Bond Market ETF",
            "ticker": "BND",
            "risk": "low",
            "goal": "income",
            "description": "Broad exposure to U.S. investment-grade bonds, suited for lower-risk portfolios."
        },
        {
            "name": "iShares Core U.S. Aggregate Bond ETF",
            "ticker": "AGG",
            "risk": "low",
            "goal": "income",
            "description": "Tracks the investment-grade U.S. bond market, ideal for conservative investors."
        },
        {
            "name": "Vanguard S&P 500 ETF",
            "ticker": "VOO",
            "risk": "medium",
            "goal": "growth",
            "description": "Tracks the S&P 500 index and offers exposure to large-cap U.S. stocks."
        },
        {
            "name": "iShares Core S&P 500 ETF",
            "ticker": "IVV",
            "risk": "medium",
            "goal": "growth",
            "description": "Another option to track the S&P 500, providing diversified large-cap exposure."
        },
        {
            "name": "Invesco QQQ ETF",
            "ticker": "QQQ",
            "risk": "high",
            "goal": "growth",
            "description": "Tracks the Nasdaq-100 index, heavy on tech and innovation—suited for aggressive growth."
        },
        {
            "name": "ARK Innovation ETF",
            "ticker": "ARKK",
            "risk": "high",
            "goal": "growth",
            "description": "Focuses on companies involved in disruptive innovation and emerging technologies."
        },
        {
            "name": "Vanguard Dividend Appreciation ETF",
            "ticker": "VIG",
            "risk": "medium",
            "goal": "income",
            "description": "Invests in companies with a record of increasing dividends, balancing growth and income."
        },
        {
            "name": "Schwab U.S. Dividend Equity ETF",
            "ticker": "SCHD",
            "risk": "medium",
            "goal": "income",
            "description": "Focuses on quality dividend-paying companies for investors interested in income."
        }
    ]

    # Filter ETFs based on risk and investment goal
    filtered = [etf for etf in etf_data if etf["risk"] == risk and etf["goal"] == goal]

    # If no ETF matches both criteria, relax the goal filter and try only risk.
    if not filtered:
        filtered = [etf for etf in etf_data if etf["risk"] == risk]

    # Optionally, add a simple horizon adjustment:
    # For very short investment horizons, warn if risk is not low.
    if horizon < 3 and risk != "low":
        # Instead of printing, we'll add a warning in the results.
        warning = "[Warning] With an investment horizon of less than 3 years, it is generally advisable to consider lower risk investments."
        filtered.insert(0, {"name": "Attention", "ticker": "", "risk": risk, "goal": goal, "description": warning})

    # Limit the recommendations to the top 3 options (or fewer if not enough ETFs match)
    return filtered[:3]
