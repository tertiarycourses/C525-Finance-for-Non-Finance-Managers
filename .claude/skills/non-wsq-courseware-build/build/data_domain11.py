DOMAIN11 = [
    dict(num=5, topic=11,
        title="Capital budgeting and investment suitability",
        objective="LO4 — apply payback, discounted payback, NPV, PI and IRR to a real choice.",
        desc="A fictional operations team must choose one of two mutually exclusive projects. You build the discounted "
             "cash-flow model, compute every capital budgeting measure, and make a recommendation you can defend when "
             "the measures disagree. Cash flows are end-of-year SGD thousands, with Year 0 as the initial outlay.",
        build="A completed investment model and a short recommendation stating the discount rate and all cash-flow timing assumptions.",
        services="Microsoft Excel, mock-data.xlsx",
        steps=[
            ("Calculate cumulative undiscounted and discounted cash flows for each project, and state simple and discounted payback including the fraction of the recovery year.", ""),
            ("Calculate NPV with Year 0 outside the NPV function (or by discounting each cash flow by its own period), then calculate the profitability index.", ""),
            ("Compare the projects against the stated decision inputs. If NPV and payback rank them differently, say which measure you weight more and why.", ""),
            ("Test a 12% discount rate and describe whether your recommendation changes.", ""),
        ],
        test="Your NPV does not double-discount Year 0, and you can state what happens to the ranking at 12%.",
    ),
]
