DOMAIN1 = [
    dict(num=1, topic=1,
        title="Financial statement analysis and ratios",
        objective="LO1 · LO2 — read a set of statements and derive the core ratio set.",
        desc="Northstar Supplies Pte Ltd, a fictional Singapore distributor, asks for a short credit review. "
             "You work from its income statement and balance sheet, derive the profit lines and the core ratios, "
             "reconcile the balance sheet, and write a short credit note. All values are illustrative SGD thousands.",
        build="A completed workbook of profit lines and ratios, plus a 100-word credit note citing specific figures.",
        services="Microsoft Excel, mock-data.xlsx",
        steps=[
            ("Calculate gross profit, operating profit and net profit for each year from the Income Statement.", ""),
            ("Classify current assets and current liabilities, then calculate current ratio, quick ratio, debt-to-equity, gross margin and net margin.", ""),
            ("Check that Assets = Liabilities + Equity. If the statements do not reconcile, identify and quantify the gap rather than forcing a balance.", ""),
            ("Write a 100-word credit note describing two improvements or risks, each supported by a specific figure.", ""),
        ],
        test="Your three profit lines tie back to the income statement, the five ratios use the stated definitions, "
             "and the balance-sheet check either reconciles or the gap is quantified.",
    ),
]
