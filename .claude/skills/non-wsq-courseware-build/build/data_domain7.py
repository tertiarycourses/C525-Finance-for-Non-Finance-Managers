DOMAIN7 = [
    dict(num=4, topic=7,
        title="Trend analysis and industry benchmarking",
        objective="LO3 — trend performance over three years and benchmark against a sector median.",
        desc="You compare two fictional business-services companies against a fictional sector benchmark, trend their "
             "revenue over FY2023-FY2025, compute the FY2025 ratio set, and decide which company warrants a deeper "
             "review. Amounts are SGD thousands.",
        build="A comparison table and a concise management note that keeps your calculation distinct from the supplied benchmark.",
        services="Microsoft Excel, mock-data.xlsx",
        steps=[
            ("Compute each company's FY2023-FY2025 revenue trend and its FY2025 revenue growth.", ""),
            ("Calculate FY2025 gross margin, operating margin, current ratio and debt-to-equity from the company data.", ""),
            ("Compare each FY2025 ratio against the sector median, and explain at least one limitation of comparing firms against a single median.", ""),
            ("Choose which company needs a deeper review, and support the recommendation with three figures.", ""),
        ],
        test="Your comparison table distinguishes the ratios you calculated from the benchmark you were given, and your recommendation cites three figures.",
    ),
]
