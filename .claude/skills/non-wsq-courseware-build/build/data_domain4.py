DOMAIN4 = [
    dict(num=3, topic=4,
        title="Projected income statement and cash flow",
        objective="LO2 — build a proforma forecast from visible, editable assumptions.",
        desc="Meridian Components Pte Ltd needs a simple FY2026 forecast. You build a projected income statement and "
             "cash flow from a stated set of assumptions, then re-run the model on a downside scenario. All values are "
             "fictional SGD thousands.",
        build="A workbook holding a base and a downside forecast, with every assumption visible and editable.",
        services="Microsoft Excel, mock-data.xlsx",
        steps=[
            ("Build a projected FY2026 income statement from the base year and the Assumptions sheet, separating cash operating expenses from depreciation.", ""),
            ("Calculate projected profit before tax, tax and profit after tax, using cell references to the assumption inputs.", ""),
            ("Build an indirect operating cash-flow forecast, then closing cash after capital expenditure and debt repayment.", ""),
            ("Run a downside scenario at 2% revenue growth and 65% COGS as a share of revenue, and state the effect on profit and closing cash.", ""),
        ],
        test="Changing an assumption cell updates the whole forecast, and the downside scenario produces a different closing cash figure.",
    ),
]
