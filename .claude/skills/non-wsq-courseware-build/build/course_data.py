"""SINGLE SOURCE OF TRUTH — C525 Finance for Non-Finance Managers (non-WSQ).

Topics follow the WSQ/IBF parent TGS-2022602569 "Financial Analysis for
Non-Finance Managers" 1:1 — same count, same titles, same order.
"""

TITLE        = "Finance for Non-Finance Managers"
SHORT_TITLE  = "Finance for Non-Finance Managers (C525)"
COURSE_CODE  = "C525"
VERSION      = "v10"
VERSION_DATE = "21 September 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr Alfred Ang"
DAYS         = 2
MODE         = "Instructor-led, hands-on Excel activities"

DARK_THEME = False

COMPANY = "Northstar Supplies Pte Ltd"

LAB_SLUGS = {
    1: "statement-analysis",
    2: "cash-flow",
    3: "forecast",
    4: "trends-benchmarks",
    5: "investment-decision",
}

LEARNING_OUTCOMES = [
    "LO1: Outline the process of financial statement analysis, including the balance sheet, "
    "income statement and cash flow statement, and the ratios derived from them.",
    "LO2: Assess an organisation's financial health from financial analysis, including "
    "profitability, liquidity, leverage, efficiency and cash flow.",
    "LO3: Evaluate an organisation's historical financial performance and benchmark it "
    "against industry, including for the financial services sector.",
    "LO4: Define indicators for investment suitability and apply capital budgeting methods "
    "to evaluate potential investment returns.",
]
LO_TITLES = ["Read the statements", "Diagnose financial health",
             "Benchmark performance", "Evaluate investments"]

TOPICS = [
    dict(num=1, code="01",
         title="The different financial ratios",
         subtitle="Balance sheet · income statement · cash flow statement · liquidity, leverage and efficiency ratios",
         concepts=[
            "Financial statements are summary-level reports covering financial results, financial position and cash flows.",
            "The balance sheet states net worth: Assets = Liabilities + Equity, split into current and long-term.",
            "The income statement shows performance: Profits = Revenues - Expenses, down from revenue to net income.",
            "The cash flow statement tracks money moving through operating, investing and financing activities.",
            "Liquidity ratios test short-term survival: current, acid test (quick), cash and operating cash flow ratios.",
            "Leverage ratios test solvency: debt ratio, debt-to-equity, interest coverage and debt service coverage.",
            "Efficiency ratios test how hard assets work: asset, inventory, receivables and payables turnover.",
         ]),
    dict(num=2, code="02",
         title="Profitability Analysis",
         subtitle="Gross, operating and net margin · return on assets · return on equity",
         concepts=[
            "Profitability ratios reflect the ability of the business to generate earnings; higher is generally more favourable.",
            "Gross margin = Gross profit / Net sales — what survives the direct cost of sales.",
            "Operating margin = Operating income / Net sales — what survives running the business.",
            "Net profit margin = Net income / Net sales — what survives interest and tax.",
            "Return on assets = Net income / Total assets — how well the asset base earns.",
            "Return on equity = Net income / Total equity — the return the owners actually receive.",
         ]),
    dict(num=3, code="03",
         title="Cash Flow Analysis",
         subtitle="Why profit is not cash · improving cash flow management · reading a monthly cash flow statement",
         concepts=[
            "A company can report a profit and still run out of cash — timing, not profitability, causes most failures.",
            "Operating cash flow = Operating income + Depreciation - Taxes +/- Change in working capital.",
            "Investing cash flows capture gains and losses from buying and selling assets.",
            "Financing cash flows capture movement between the company, its shareholders and its creditors.",
            "Cash flow management improves by collecting receivables sooner, paying payables on terms and controlling inventory.",
         ]),
    dict(num=4, code="04",
         title="Projected financial and cash-flow statements",
         subtitle="Proforma statements · forecasting the income statement, balance sheet and cash flow",
         concepts=[
            "Proforma (projected) statements support planning and let you compare actual against predicted performance.",
            "Projections are prepared for the income statement and balance sheet; projected cash flow is derived from both.",
            "Forecasting the income statement starts from expected sales and applies cost and expense assumptions.",
            "Forecasting cash flow means estimating monthly sales, predicting when payments are received, then estimating costs.",
            "Keep assumptions as visible, editable inputs so the forecast can be re-run when the assumptions change.",
         ]),
    dict(num=5, code="05",
         title="The process of financial statements analysis",
         subtitle="Ratio analysis · horizontal (trend) analysis · vertical (common-size) analysis",
         concepts=[
            "Financial statement analysis evaluates the financial situation and supports administrative and economic decisions.",
            "There are three methods: ratio analysis, horizontal (trend) analysis and vertical (common-size) analysis.",
            "Ratio analysis uses the ratios of a business to evaluate its financial position at a point in time.",
            "Horizontal analysis measures the percentage change of the same line item across two or more periods.",
            "Vertical analysis states every item as a percentage of a base — gross sales for the income statement, total assets for the balance sheet.",
         ]),
    dict(num=6, code="06",
         title="Use financial analysis to determine the health of an organisation",
         subtitle="Reading the balance sheet, income statement and cash flow statement for signals of health",
         concepts=[
            "From the balance sheet: debt relative to equity, short-term liquidity, and how long collection and payment take.",
            "From the income statement: revenue growth, gross profit margin, net profit after all expenses, and interest cover.",
            "From the cash flow statement: the liquidity situation, sources of cash, free cash flow, and whether cash rose or fell.",
            "From ratios: gross and net profit margin, coverage ratio, current and quick ratio for obligations.",
            "From ratios: debt-to-equity, inventory turnover, total asset turnover, ROE and ROA for efficiency and return.",
         ]),
    dict(num=7, code="07",
         title="Evaluate organisation's historical financial performance",
         subtitle="Trend analysis of the balance sheet and income statement · trend analysis of ratios",
         concepts=[
            "Historical evaluation runs in steps: generate the ratios, then trend the balance sheet, then trend the income statement.",
            "Trending the balance sheet shows how the asset, liability and equity mix has shifted over time.",
            "Trending the income statement shows whether growth in revenue is converting into growth in profit.",
            "Trending the ratios themselves is often more revealing than any single period's value.",
            "A direction of travel matters more than one year's number — read several periods before judging.",
         ]),
    dict(num=8, code="08",
         title="Investment suitability based on financial analysis",
         subtitle="Revenues · profits · operational efficiency · capital efficiency and solvency · DuPont",
         concepts=[
            "Revenues: assess quantity, quality and timing, revenue growth ignoring one-time items, concentration and revenue per employee.",
            "Profits: read gross, operating and net profit margin together rather than any one alone.",
            "Operational efficiency: receivables turnover and inventory turnover show how well working capital is managed.",
            "Market data: price to earnings, price to book and price-earnings-growth ratios place the company against its price.",
            "The DuPont index decomposes ROE into Net profit margin x Asset turnover x Equity multiplier.",
         ]),
    dict(num=9, code="09",
         title="Analysis for the financial services industry",
         subtitle="Banking ratios · insurance ratios · why the standard ratio set does not transfer",
         concepts=[
            "Banking profitability: net interest margin = (Interest income - Interest expense) / Total assets.",
            "Banking efficiency: efficiency ratio = Non-interest expense / Revenue; operating leverage compares the two growth rates.",
            "Banking strength: liquidity coverage ratio, leverage ratio (Tier 1 / Total assets) and the CET1 ratio.",
            "Insurance: persistency ratio, solvency ratio and combined ratio describe the book and its margin.",
            "Insurance: incurred claims ratio, commission expense ratio and claim settlement ratio describe claims performance.",
         ]),
    dict(num=10, code="10",
         title="Benchmarking of financial performance against industry",
         subtitle="Sector averages · choosing comparators · the limits of benchmarking",
         concepts=[
            "A ratio only means something against a comparator — the same company last year, or its sector this year.",
            "Sectoral averages move over time, so benchmark against the same period, not a remembered figure.",
            "Choose comparators of similar size, business model and geography, or the comparison misleads.",
            "State the limitation alongside the comparison: accounting policy, scale and business mix all distort it.",
         ]),
    dict(num=11, code="11",
         title="Use Capital Budgeting to evaluate potential investment returns",
         subtitle="Time value of money · payback · discounted payback · NPV · profitability index · IRR",
         concepts=[
            "Capital budgeting plans long-term investments and focuses on cash flows rather than accounting profits.",
            "Time value of money: PV = FV / (1+i)^n and FV = PV x (1+i)^n — money in hand beats the same sum later.",
            "Payback period measures how long the initial outlay takes to be recovered, ignoring the time value of money.",
            "Discounted payback discounts each future inflow to present value before measuring recovery.",
            "Net present value sums the discounted cash flows net of the outlay; accept a positive NPV.",
            "Profitability index = PV of inflows / PV of outflows; accept a project with PI greater than 1.",
            "Internal rate of return is the discount rate at which NPV equals zero; accept when IRR beats the threshold rate.",
         ]),
]

DAY_THEMES = {
    1: "Financial statements, ratios, profitability, cash flow and projections",
    2: "Analysis process, financial health, historical performance, benchmarking and capital budgeting",
}

def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","9:45",15,"admin","Welcome, trainer and learner introductions, course outline and ground rules"),
        ("9:45","11:30",105,"topic","Topic 1 - "+TOPICS[0]["title"]),
        ("11:30","12:35",65,"lab","Hands-on: "+lab_titles([1])),
        ("12:35","13:05",30,"lunch","Lunch break"),
        ("13:05","14:05",60,"topic","Topic 2 - "+TOPICS[1]["title"]),
        ("14:05","14:40",35,"topic","Topic 3 - "+TOPICS[2]["title"]),
        ("14:40","15:35",55,"lab","Hands-on: "+lab_titles([2])),
        ("15:35","16:20",45,"topic","Topic 4 - "+TOPICS[3]["title"]),
        ("16:20","17:30",70,"lab","Hands-on: "+lab_titles([3])),
     ]),
     2: (DAY_THEMES[2], [
        ("9:30","9:45",15,"admin","Day 1 recap and Q&A"),
        ("9:45","11:00",75,"topic","Topic 5 - "+TOPICS[4]["title"]),
        ("11:00","11:45",45,"topic","Topic 6 - "+TOPICS[5]["title"]),
        ("11:45","12:30",45,"topic","Topic 7 - "+TOPICS[6]["title"]),
        ("12:30","13:00",30,"lunch","Lunch break"),
        ("13:00","13:35",35,"topic","Topic 8 - "+TOPICS[7]["title"]),
        ("13:35","14:05",30,"topic","Topic 9 - "+TOPICS[8]["title"]),
        ("14:05","14:30",25,"topic","Topic 10 - "+TOPICS[9]["title"]),
        ("14:30","15:35",65,"lab","Hands-on: "+lab_titles([4])),
        ("15:35","16:20",45,"topic","Topic 11 - "+TOPICS[10]["title"]),
        ("16:20","17:15",55,"lab","Hands-on: "+lab_titles([5])),
        ("17:15","17:30",15,"recap","Course recap, Q&A and close"),
     ]),
    }

COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="Key Concepts",
    concepts=[
        ("The three statements", "Balance sheet, income statement and cash flow statement answer three different questions about the same business."),
        ("Ratios, not raw numbers", "A figure means little alone; a ratio against a comparator is what carries the signal."),
        ("Profit is not cash", "Profitable companies fail when cash arrives later than it leaves."),
        ("Direction over level", "Several periods of trend say more about health than any single year."),
        ("Cash flows, discounted", "Investment decisions rest on the timing of cash, not on accounting profit."),
        ("Always name the limit", "State what a comparison cannot tell you, alongside what it can."),
    ],
    framework_title="From Statement to Decision",
    framework=[
        ("Read", "Locate the line items on the three statements."),
        ("Compute", "Derive the liquidity, leverage, efficiency and profitability ratios."),
        ("Compare", "Trend against prior periods and benchmark against the sector."),
        ("Decide", "Judge financial health and investment suitability, and say why."),
    ],
    statement=dict(headline="Numbers only speak when something is beside them.",
                   body="Every judgement in this course is a comparison — to last year, to the sector, or to the cost of capital.",
                   kicker="KEY IDEA"),
    pillars_title="What You'll Be Able To Do",
    pillars=[
        ("Read any set of statements", ["Locate assets, liabilities and equity", "Trace revenue down to net income", "Follow cash through three activities"]),
        ("Diagnose financial health", ["Compute the ratio set", "Read liquidity and solvency", "Spot the cash-timing problems"]),
        ("Judge an investment", ["Discount future cash flows", "Apply payback, NPV, PI and IRR", "Recommend with a stated basis"]),
    ],
    arc_title="How Every Activity Progresses",
    arc=[
        "The trainer demonstrates the calculation on a worked example.",
        "You rebuild it in Excel on fictional company data.",
        "You verify your own figures against the stated check.",
        "You explain your decision to the class and hear the alternatives.",
    ],
)

LG_SETUP = dict(
    needs=["A laptop with Microsoft Excel (or a compatible spreadsheet application).",
           "The activity workbooks from the course repository or the LMS."],
    verify_text="Open any activity workbook and confirm you can see both the source tabs and the blank 'Your Analysis' tab.",
    verify_code="",
    conventions=["All company names and figures are fictional and are for classroom practice only.",
                 "Values are stated in SGD thousands unless the workbook says otherwise."],
)
LAB_NOTE = "All data in these activities is synthetic. It is for learning, not investment advice."

LG_GLOSSARY = [
    ("Current ratio", "Current assets divided by current liabilities; a test of short-term liquidity."),
    ("Acid test (quick) ratio", "Current assets less inventories, divided by current liabilities."),
    ("EBITDA", "Earnings before interest, tax, depreciation and amortisation."),
    ("Working capital", "Current assets less current liabilities."),
    ("Gross margin", "Gross profit divided by net sales."),
    ("Operating margin", "Operating income divided by net sales."),
    ("Net profit margin", "Net income divided by net sales."),
    ("Return on equity (ROE)", "Net income divided by total equity."),
    ("Return on assets (ROA)", "Net income divided by total assets."),
    ("Debt-to-equity", "Total liabilities divided by shareholders' equity."),
    ("Horizontal analysis", "Percentage change of the same line item across two or more periods."),
    ("Vertical analysis", "Every line stated as a percentage of a base figure."),
    ("Proforma statement", "A projected financial statement built from stated assumptions."),
    ("Time value of money", "The principle that a sum today is worth more than the same sum later."),
    ("Net present value (NPV)", "The sum of discounted cash flows net of the initial outlay."),
    ("Profitability index (PI)", "Present value of inflows divided by present value of outflows."),
    ("Internal rate of return (IRR)", "The discount rate at which net present value equals zero."),
    ("DuPont index", "ROE decomposed into net profit margin, asset turnover and equity multiplier."),
]

VERSION_HISTORY = [
    ("v10", VERSION_DATE,
     "Deck rebuilt in the current non-WSQ house style (all-white, native shapes, no SmartArt). "
     "Content follows the parent course's 11 topics.", TRAINER),
]
