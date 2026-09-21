DOMAIN3 = [
    dict(num=2, topic=3,
        title="Cash flow reconstruction and liquidity",
        objective="LO2 — rebuild cash movement and explain why profit is not cash.",
        desc="Harbour Services Pte Ltd reports a profit while its cash is tightening. You reconstruct the movement of "
             "cash using the indirect method, reconcile closing cash, and recommend how to protect liquidity. "
             "Values are illustrative SGD thousands.",
        build="A cash-flow workbook whose three activity subtotals reconcile to closing cash, plus a brief liquidity recommendation.",
        services="Microsoft Excel, mock-data.xlsx",
        steps=[
            ("Create the operating, investing and financing cash-flow sections from the inputs; show cash outflows as negative values.", ""),
            ("Calculate net cash from operations, net change in cash and closing cash. Reconcile closing cash to opening cash plus the three activity subtotals.", ""),
            ("Calculate the operating cash-flow ratio using current liabilities, and explain why accounting profit differs from operating cash flow.", ""),
            ("Recommend two actions to protect liquidity, without confusing borrowing with operating cash generation.", ""),
        ],
        test="Opening cash plus the three activity subtotals equals your closing cash figure exactly.",
    ),
]
