# Macroeconomics B Course Material Index

Generated from the files currently in `course_material/`.

Scope: this index covers every course material file in the folder except this
index file itself. It includes lecture slides, exercise PDFs, notebooks, data
files, and helper scripts.

## Quick Sequence

| Stage | Core topic | Main files |
| --- | --- | --- |
| Course setup | Course organization, assessment, lecture plan | `lecture_00_intro.pdf` |
| Week 1 exercise setup | Python/FRED setup, business-cycle statistics, HP filtering | `week01.pdf`, `week01_task_bcstats (1).ipynb`, `week01_solution_bcstats.ipynb`, `week01_fred_consumption.xlsx`, `Ex_class_1_hold_2.pdf` |
| Lecture 1 / Ch. 15 | Investment, asset prices, present value, stock pricing, Tobin's q | `lecture_01_ch15 (1).pdf`, `L1_investment_asset_prices.ipynb`, `week02_investment_assetprices.pdf`, `week02_investment_assetprices_solutions.pdf` |
| Lecture 2 / Ch. 15 continuation | Business investment, housing investment, capital dynamics, housing q | `L2_business_housing_investment.ipynb`, `denmark_housing_q_data.py`, `week02_investment_assetprices.pdf` |
| Lecture 3 / Ch. 16 | Consumption, PIH, two-period optimization, Ricardian equivalence, borrowing constraints | `lecture_03_ch16 (1).pdf`, `L3_consumption (1).ipynb`, `week03_consumption_handin_task.pdf` |
| Lecture 4 / Ch. 17 | IS-LM, Taylor rule, aggregate demand, monetary transmission | `lecture_04_ch17 (1).pdf`, `L4_monetary_policy_aggregate_demand.ipynb` |
| Lecture 5 / Ch. 18 | Phillips curve, AS curve, inflation expectations, supply shocks | `lecture_05_ch18.pdf`, `L5_phillips_curve.ipynb`, `lecture_05_notebook_utils.py` |
| Lecture 6 / Ch. 19 | Dynamic AS-AD, energy shocks, persistence, policy response | `lecture_06_ch19.pdf`, `L6_as_ad_supply_shocks.ipynb`, `lecture_06_notebook_utils.py` |

## PDF Slides And Exercise Sheets

### `lecture_00_intro.pdf`

- Type: lecture slide PDF.
- Length: 8 pages.
- Author: Brigitte Hochmuth.
- Role: course orientation and practical overview.
- Main contents:
  - Contact details, office hours, and Absalon as the material/announcement hub.
  - Course scope: short-run macroeconomic fluctuations around long-run trend,
    investment and asset prices, consumption, monetary policy, aggregate demand,
    inflation, Phillips curves, aggregate supply, stabilization policy, open
    economy material, numerical examples, simulations, and Python work.
  - Organization: 7 weeks in Block 4, 3x2 lecture hours, 2x2 exercise hours.
  - Textbook: *Introducing Advanced Macroeconomics: Growth and Business Cycles*,
    3rd edition.
  - Assignments and exam: two mandatory pass/fail hand-ins are required for exam
    qualification; final assessment is a 48-hour individual take-home exam in
    block week 8.
  - Lecture plan from 20 Apr through 8 Jun.
- Use this first to understand the course structure, administrative rules, and
  where each topic sits in the lecture calendar.

### `Ex_class_1_hold_2.pdf`

- Type: exercise-class slide PDF.
- Length: 23 pages.
- Author: Pedro Duarte Gomes.
- Role: introduces the exercise-class format and gives a Chapter 13/business-cycle
  bridge into the first data exercise.
- Main contents:
  - Jigsaw exercise format:
    - expert phase in assigned problem groups,
    - exchange phase where students teach each other,
    - wrap-up with joint problem solving.
  - Expectations: active preparation, peer explanation, questions, and flexible
    pacing depending on attendance and preparation.
  - Business-cycle definition from Burns and Mitchell.
  - HP-filter objective and its interpretation:
    - separates a series into trend and cyclical component,
    - penalizes variation in trend growth,
    - motivates using cyclical components for business-cycle statistics.
  - Output gap as cyclical component.
  - Identification of troughs and peaks.
  - Business-cycle statistics:
    - volatility,
    - correlation/comovement,
    - persistence/autocorrelation.
  - Stylized facts emphasized in the slides:
    - GDP fluctuations are sizable,
    - consumption, investment, imports, and other macro aggregates differ in
      volatility and cyclicality,
    - GDP and many macro series are persistent.
- Related files: `week01.pdf`, `week01_task_bcstats (1).ipynb`,
  `week01_solution_bcstats.ipynb`.

### `week01.pdf`

- Type: exercise sheet PDF.
- Length: 3 pages.
- Title: Exercise Sheet 1: Setup and Business-Cycle Statistics.
- Author: Brigitte Hochmuth.
- Role: first practical Python/FRED exercise.
- Main workflow:
  - Open the task notebook in VS Code.
  - Verify that Python cells and imports run.
  - Download at least two quarterly U.S. macro series from FRED; real GDP is
    required and consumption or investment are suggested comparison series.
  - Use `fredapi` as the main data source, with Excel fallback files if the API
    setup fails.
  - Put the series in one DataFrame, clean missing values, make one raw line
    plot, and optionally save downloaded data.
- Statistical tasks:
  - Summary table with mean, standard deviation, minimum, and maximum.
  - Log one quarterly series and apply the HP filter with `lambda = 1600`.
  - Store trend and cycle.
  - Plot either the log series and trend or the cyclical component.
  - Compute volatility of the cyclical component.
  - Compute correlation between GDP's cycle and another series' cycle.
  - Repeat business-cycle statistics on the sample ending in 2019Q4 and compare
    with the full sample.
- Short-answer prompts:
  - Which series is more volatile?
  - Is the correlation positive or negative?
  - How do raw series and HP-filtered cycles differ?
  - Why remove trend before computing business-cycle statistics?
  - Does ending the sample in 2019 change the consumption-vs-GDP conclusion?
  - Why might the COVID lockdown period affect consumption and business-cycle
    statistics?
- Related notebooks: `week01_task_bcstats (1).ipynb`,
  `week01_solution_bcstats.ipynb`.

### `lecture_01_ch15 (1).pdf`

- Type: lecture slide PDF.
- Length: 49 pages.
- Title: Investment and Asset Prices - Macroeconomics B, Lecture 1 on Chapter 15.
- Author: Brigitte Hochmuth.
- Role: first substantive theory lecture, linking asset pricing to investment.
- Learning goals:
  - Read empirical figures on investment and asset prices.
  - Explain present value and discounting.
  - Derive the one-period stock-pricing equation.
  - Explain how the real interest rate, risk premia, and expected profits affect
    asset prices.
  - Define Tobin's q and explain its investment relevance.
- Main topics:
  - Investment in the short-run demand identity `Y = C + I + G`.
  - Business fixed investment, housing investment, and inventory investment.
  - Asset prices as forward-looking indicators.
  - Denmark output gap and house price growth.
  - Property prices, stock prices, valuation, and business-cycle timing.
  - Bond pricing from no-arbitrage.
  - Present value of one or many future payments.
  - Equity pricing:
    - required equity return includes real interest rate plus risk premium,
    - one-period stock-pricing equation,
    - forward iteration,
    - no-bubbles condition,
    - fundamental share price.
  - Special cases:
    - constant expected dividends,
    - constant dividend growth and the Gordon formula.
  - Comparative statics from the Gordon formula:
    - higher dividends raise value,
    - higher real interest rates lower value,
    - higher risk premia lower value,
    - higher expected growth raises value when it remains below the discount
      rate.
  - Why stock prices are volatile and can lead the business cycle.
  - Tobin's average q:
    - `q = value of installed capital / replacement cost`,
    - `q > 1` makes investment attractive,
    - `q < 1` makes investment unattractive.
  - Adjustment costs as the reason investment does not jump infinitely when
    `q > 1`.
  - Optimal investment rule: `q_t = 1 + c'(I_t)`.
  - Linking q to expected profits, interest rates, and animal spirits/business
    confidence.
  - Empirical limitations of the q-investment relationship.
- Key formulas/models:
  - Bond price: `P_B = 1 / (1 + r)`.
  - One-period equity price: `V_t = (D_t^e + V_{t+1}^e) / (1 + r + epsilon)`.
  - Gordon formula: `V_t = D_t^e / (r + epsilon - g)`.
  - Tobin's q: `q = V / K` under normalized replacement cost.
  - Investment condition with adjustment costs: `q_t = 1 + c'(I_t)`.
- Related files:
  - `L1_investment_asset_prices.ipynb` implements the data and numerical
    pieces.
  - `week02_investment_assetprices.pdf` turns the lecture into exercises.
  - `week02_investment_assetprices_solutions.pdf` gives worked solutions.

### `week02_investment_assetprices.pdf`

- Type: exercise sheet PDF.
- Length: 4 pages.
- Title: Exercise Sheet 2: Investment and Asset Prices.
- Author: Brigitte Hochmuth.
- Role: group-based exercise sheet for Lecture 1 and Lecture 2 material.
- Class plan:
  - Groups 1-4 solve Problems 1-4.
  - Each group prepares a short solution and interpretation.
  - Problem 5 is a joint class problem.
  - Optional extension is harder and intended for early finishers or extra
    discussion.
- Problem 1: Asset prices and valuation.
  - Derive one-period bond price.
  - Compute present value of three future payments at `r = 0.04` and `r = 0.07`.
  - Derive one-period share-pricing equation with risk premium `epsilon`.
  - Apply Gordon formula to dividend growth.
  - Invert Gordon formula to infer required dividend growth from observed
    dividend yield.
- Problem 2: Tobin's q and business investment with depreciation.
  - Capital accumulation: `K_{t+1} = (1 - delta)K_t + I_t`.
  - Quadratic adjustment cost around replacement investment.
  - Firm first-order condition: `q_t = 1 + a(I_t - delta K_t)`.
  - Gross investment expression: replacement investment plus q-driven net
    investment.
  - Steady state: `I* = delta K*`, `q* = 1`.
  - Numerical two-period capital-stock update.
- Problem 3: Average q, marginal q, and investment subsidies.
  - Firm value `V(K) = A K^alpha`.
  - Average q and marginal q relation: `q_m = alpha q_avg`.
  - Subsidy changes purchase price from `1` to `1 - s`.
  - Local q-theory investment condition.
  - Interpretation of decreasing returns and policy wedges.
- Problem 4: Housing, taxation, and construction.
  - User cost of housing: `v = r(1 - tau) + delta + s`.
  - Housing demand and supply with predetermined housing stock.
  - Short-run house price, housing q, and construction response.
  - Long-run steady state with `p_H* = P`.
  - Tax increase from `s = 0.005` to `s = 0.015`.
- Problem 5: Discount-rate and user-cost shock.
  - Compares business investment and housing investment after monetary easing.
  - Business side uses Gordon valuation and the investment rule from Problem 2.
  - Housing side uses the baseline user-cost model from Problem 4.
  - Students compare level and percentage changes.
- Optional extension:
  - Property-tax increase during a recession.
  - Decomposes immediate house-price fall into tax/user-cost and income-shock
    components.
  - Asks for policy-timing evaluation and missing real-world channels.
- Related solution: `week02_investment_assetprices_solutions.pdf`.

### `week02_investment_assetprices_solutions.pdf`

- Type: worked-solution PDF.
- Length: 7 pages.
- Title: Exercise Sheet 2: Investment and Asset Prices - Solutions.
- Author: Brigitte Hochmuth.
- Role: complete solution key for `week02_investment_assetprices.pdf`.
- Notable worked results:
  - Problem 1:
    - Bond price derived from `(1 + r)P_B = 1`.
    - Present value is about `119.17` at `r = 0.04` and `111.95` at `r = 0.07`.
    - Furthest future payment is most affected by the interest-rate increase.
    - Gordon baseline value is `120`; with `r = 0.05`, value falls to about
      `85.71`.
    - Implied dividend growth from a 1.5 percent yield, `r = 0.03`, and
      `epsilon = 0.04` is `5.5 percent`, above a 2.5 percent long-run real GDP
      benchmark.
  - Problem 2:
    - Investment rule: `I_t = delta K_t + (q_t - 1) / a`.
    - Numerical example gives `I_0 = 5.4`, `K_1 = 100.4`, `I_1 = 5.22`,
      `K_2 = 100.60`.
  - Problem 3:
    - At `K = 100`, `q_avg` is about `1.592` and `q_m` is about `1.274`.
    - Investment rises from about `2.74` to `3.74` when subsidy `s = 0.10`.
  - Problem 4:
    - Baseline user cost `v = 0.05`.
    - Baseline long-run housing stock `H* = 200`, price `p_H* = 2`, and
      investment `I_H* = 5`.
    - After higher property tax, `v' = 0.06`, `H*' = 166.67`,
      `I_H*' = 4.17`.
    - Immediate short-run price falls to about `1.67`, housing q to `0.833`,
      and housing investment to about `3.33`.
  - Problem 5:
    - Business investment rises from `5.0` to `5.5`, a 10 percent increase.
    - Housing investment rises from `5.0` to `7.5`, a 50 percent increase.
    - In the calibration, housing investment responds more strongly.
  - Optional extension:
    - Joint tax and recession shock lowers first-period house price to about
      `1.583`, housing q to `0.792`, investment to `2.917`, and next stock to
      `197.917`.
    - Decomposition attributes about 80 percent of the immediate price fall to
      the tax/user-cost change and 20 percent to the income shock.
- Use this to check both algebra and economic interpretation for the exercise
  sheet.

### `lecture_03_ch16 (1).pdf`

- Type: lecture slide PDF.
- Length: 46 pages.
- Title: Consumption - Macroeconomics B, Lecture 3, Chapter 16.
- Author: Brigitte Hochmuth.
- Role: consumption theory lecture.
- Starting point:
  - Connects back to Lecture 1 investment and asset prices.
  - Moves from investment to consumption as the other major component of
    private aggregate demand.
  - Main question: does consumption depend mainly on current income or lifetime
    resources?
- Roadmap:
  - Keynesian benchmark and empirical puzzle.
  - Intertemporal optimization, intertemporal budget constraint, and
    Keynes-Ramsey rule.
  - Consumption function and permanent income hypothesis.
  - Ricardian equivalence.
  - Credit constraints and precautionary saving.
  - Data evidence and MPC heterogeneity.
  - Notebook exercise.
- Main topics:
  - Fixed-rate vs adjustable-rate mortgages and why mortgage type changes
    household exposure to monetary policy.
  - 2022-23 Danish interest-rate tightening as motivation for cash-flow
    heterogeneity.
  - Three channels:
    - intertemporal substitution,
    - wealth effects,
    - cash-flow and borrowing-constraint effects.
  - Keynesian consumption function:
    - `C_t = C_bar + b Y_t^d`,
    - MPC `b`,
    - decreasing APC.
  - Cross-section vs time-series puzzle in the APC.
  - Two-period household setup:
    - initial wealth,
    - labor income,
    - disposable income,
    - borrowing/lending at real interest rate.
  - Intertemporal budget constraint and human wealth.
  - Lifetime utility and optimal consumption choice.
  - Keynes-Ramsey rule and economic interpretation of patience vs interest
    rate.
  - CRRA closed-form current-consumption rule:
    - current consumption depends on total wealth, not only current income.
  - Danish evidence on consumption and wealth.
  - Life-cycle profiles.
  - Permanent income hypothesis and annuity rule.
  - Temporary vs permanent income shocks.
  - Ricardian equivalence:
    - government intertemporal budget constraint,
    - taxes vs debt,
    - failure conditions.
  - Borrowing constraints and precautionary saving.
  - Generalized consumption function with lifetime resources and frictions.
- Key formulas/models:
  - Keynesian consumption: `C_t = C_bar + b Y_t^d`.
  - Human wealth: discounted future labor/disposable income.
  - Two-period consumption: `C_1 = theta (V_1 + H_1)`.
  - PIH annuity logic: temporary shocks have small annual effects over long
    horizons, permanent shocks have larger effects.
- Related files:
  - `L3_consumption (1).ipynb` implements the two-period model, FRED data, PIH
    responses, and constraints.
  - `week03_consumption_handin_task.pdf` turns the lecture into the first
    mandatory hand-in.

### `lecture_04_ch17 (1).pdf`

- Type: lecture slide PDF.
- Length: 51 pages.
- Title: Monetary Policy and Aggregate Demand - Macroeconomics B, Lecture 4,
  Chapter 17.
- Author: Brigitte Hochmuth.
- Role: builds the demand side of the short-run macro model.
- Starting point:
  - Investment and consumption both react to real interest rates.
  - The lecture combines these blocks into aggregate demand and monetary
    transmission.
- Roadmap:
  - Why demand matters in the short run.
  - Goods-market equilibrium and the IS curve.
  - Money market and the IS-LM benchmark.
  - Monetary policy and the Taylor rule.
  - From IS-LM to AD.
  - Unconventional monetary policy.
- Main topics:
  - Very low policy rates followed by rapid tightening by the ECB and Fed.
  - Three links in short-run aggregate demand:
    - goods market block,
    - policy block,
    - transmission block from policy rate to relevant real rate.
  - Keynes, classics, and the Great Depression.
  - Goods-market equilibrium:
    - `Y = C + I + G`,
    - private demand,
    - autonomous demand,
    - tax effects,
    - multiplier.
  - Exact linear IS curve and output-gap version.
  - Real interest rate as a negative driver of demand through investment and
    other private-spending channels.
  - LM curve and money-market equilibrium.
  - Full IS-LM model and diagrammatic shifts.
  - Why modern central banks target an interest rate rather than a money stock.
  - Taylor rule:
    - policy rate responds to inflation and output/demand conditions,
    - parameters such as `h` and `beta` control policy sensitivity and AD slope.
  - Replacing LM with a horizontal policy line.
  - Policy-rate transmission to private borrowing rates and real rates.
  - Policy labs:
    - government spending increase,
    - pessimistic firms,
    - ECB rate cut.
  - AD curve derivation in `(Y, pi)` space.
  - Distinguishing movements along AD from shifts of AD.
  - Unconventional monetary policy tools.
- Key formulas/models:
  - Goods-market multiplier from linear demand.
  - IS curve in levels and gaps.
  - Money demand/supply equilibrium.
  - Taylor-type policy rule.
  - AD curve from IS plus policy rule.
- Related file: `L4_monetary_policy_aggregate_demand.ipynb`.

### `lecture_05_ch18.pdf`

- Type: lecture slide PDF.
- Length: 48 pages.
- Title: The Phillips Curve and the AS Curve - Macroeconomics B, Lecture 5,
  Chapter 18.
- Author: Brigitte Hochmuth.
- Role: adds the supply side to the short-run model.
- Main topics:
  - Recap of Lecture 4:
    - nominal policy rate to real rate,
    - policy rule plus IS to AD.
  - Motivation from recent inflation in Denmark and the United States.
  - Price stickiness and nominal adjustment:
    - menu costs,
    - sticky wages,
    - staggered contracts,
    - efficiency-wage style mechanisms.
  - Micro rigidities as the foundation for the Phillips curve.
  - Output gap and unemployment as linked cyclical indicators.
  - Original Phillips curve evidence from the UK.
  - 1960s apparent Phillips-curve stability and 1970s stagflation breakdown.
  - Expectations and the natural rate of unemployment.
  - Long-run vertical Phillips curve.
  - Multiple short-run Phillips curves.
  - Accelerationist/backward-looking intuition.
  - Okun-style link from unemployment to output.
  - AS curve derivation in `(y, pi)` space.
  - Demand shocks vs supply shocks in AS-AD language.
  - Supply-shock term in the AS equation.
  - Policy trade-off after an adverse supply shock.
  - Static, adaptive, and anchored expectations.
  - Why unanchored expectations are costly.
  - Group exercise using the Lecture 5 notebook.
  - Modern empirical themes:
    - flatter Phillips curve,
    - Denmark since 2000,
    - 2021-2025 inflation episode,
    - U.S. disinflation in 2022-2024.
- Key formulas/models:
  - Reduced-form Phillips curve.
  - Expectations-augmented Phillips curve.
  - Natural-rate condition.
  - AS equation with output gap and supply shock:
    - `pi_t = pi_t^e + gamma (y_t - y_bar) + s_t`.
- Related files:
  - `L5_phillips_curve.ipynb`.
  - `lecture_05_notebook_utils.py`.

### `lecture_06_ch19.pdf`

- Type: lecture slide PDF.
- Length: 45 pages.
- Title: AS-AD Dynamics And Energy Price Shocks - Macroeconomics B, Lecture 6,
  Chapter 19.
- Author: Brigitte Hochmuth.
- Role: combines AS and AD into a dynamic model and applies it to energy shocks.
- Main topics:
  - Lecture 4 supplied AD; Lecture 5 supplied AS.
  - 2022 European energy shock as motivating case.
  - Denmark headline and core HICP.
  - Why energy prices are a supply shock:
    - energy is an input into production and transport,
    - higher energy costs shift AS upward.
  - Business cycles as output fluctuations around trend.
  - International comovement of macro fluctuations.
  - Impulse vs propagation:
    - impulse is initial disturbance,
    - propagation is the model's dynamic adjustment.
  - Model components:
    - demand block,
    - Taylor-type policy response,
    - transmission to AD,
    - supply block with expectations and shocks.
  - Taylor-type policy and AD slope.
  - AS-AD system in gaps.
  - Graphical equilibrium.
  - Adjustment toward long-run equilibrium.
  - Persistence coefficient and speed of adjustment.
  - Temporary demand shock vs temporary supply shock.
  - Impulse responses.
  - Identifying shocks from output and inflation movements.
  - 2022 energy shock through the model.
  - Policy tightening and three policy stances in the notebook.
  - Current-event stress test: Strait of Hormuz and oil-supply risk.
  - Exam-answer communication:
    - classify the shock as demand-side `z_t` or supply-side `s_t`,
    - state inflation/output effects,
    - discuss policy trade-off and persistence.
- Key formulas/models:
  - AS curve with supply shock: `pi_t = pi_t^e + gamma(y_t - y_bar) + s_t`.
  - AD block from policy rule and transmission.
  - Dynamic gap system using demand shock `z_t` and supply shock `s_t`.
  - Persistence coefficient `beta = 1 / (1 + a gamma)` in the companion
    notebook.
- Related files:
  - `L6_as_ad_supply_shocks.ipynb`.
  - `lecture_06_notebook_utils.py`.

### `week03_consumption_handin_task.pdf`

- Type: mandatory hand-in PDF.
- Length: 4 pages.
- Title: Week 3 Mandatory Hand-in: Consumption.
- Author: Brigitte Hochmuth.
- Role: pass/fail exam-qualification assignment based mainly on consumption,
  with a short link to aggregate demand.
- Submission rules:
  - Mandatory pass/fail hand-in.
  - Must pass to qualify for the exam.
  - Group work allowed in groups of at most 4 students.
  - Submit completed notebook renamed `week03_consumption_GROUPNAME.ipynb`.
- Referenced but not present in the current folder:
  - `week03_consumption_student_start.ipynb`.
  - `week03_fred_consumption.csv`.
- Passing requirements:
  - Clean-kernel run without errors.
  - Requested figures and tables with clear labels.
  - Short Markdown interpretations after main outputs.
  - Correct use of intertemporal budget constraint, Keynes-Ramsey logic, PIH
    annuity factor, and borrowing-constraint mechanism.
  - Group-specific household profile in Part 3.
  - Concise final economic narrative referring to the group's own numbers.
- Part 1: Current income and Keynesian benchmark.
  - Uses `C = C_bar + bY^d`, with `C_bar = 200` and `b = 0.75`.
  - Plot consumption against disposable income.
  - Compute MPC and APC at selected disposable-income values.
  - Explain the APC cross-section vs long-run aggregate issue.
- Part 2: Two-period consumption and real interest rate.
  - Implements human wealth, `theta`, and two-period allocation.
  - Baseline: `V_1 = 20`, `Y_1^d = 250`, `Y_2^d = 320`, `r = 0.03`,
    `phi = 0.03`, `sigma = 0.8`.
  - Computes `C_1`, `C_2`, total wealth, saving/borrowing.
  - Raises real rate from 3 percent to 7 percent and decomposes `C_1` change
    into substitution/wealth components.
  - Plots `C_1` over interest rates for multiple intertemporal elasticities.
  - Numerically verifies closed-form `C_1` by grid-searching lifetime utility.
- Part 3: Cash-flow exposure and borrowing constraints.
  - Computes mortgage annuity payments for `D = 2,000,000 DKK`, `M = 25`, and
    a rate increase from 1 percent to 5 percent.
  - Calculates present value of a 3-year cash-flow loss.
  - Compares PIH household with 30-year horizon against constrained household
    with MPC 0.9.
  - Requires a group-specific household profile and break-even constrained MPC.
- Part 4: Temporary vs permanent income shocks.
  - Uses annuity factor `A(N, r)` and `theta_N`.
  - Plots `theta_N` for horizons `N = 1,...,60`.
  - Compares consumption response to temporary and permanent DKK 5,000 income
    increases for `N = 5, 30, 60`.
  - Computes aggregate response when 35 percent of households are constrained
    with MPC 0.9.
- Part 5: Real data.
  - Uses provided CSV or FRED series `DPIC96`, `PCEC96`, and `PSAVERT`.
  - Plots indexed real disposable personal income and real consumption.
  - Plots APC and saving rate.
  - Estimates `Delta log C_t = alpha + beta Delta log Y_t^d + error_t`.
  - Repeats estimate excluding 2020Q1-2021Q4.
  - Creates scatter plot with fitted regression line.
- Part 6: Economic take-away.
  - 250-400 words.
  - Must cite one own number from the two-period model, one from mortgage
    cash-flow experiment, one estimated `beta`, and one limitation.
- Related file: `L3_consumption (1).ipynb` is the closest available lecture
  notebook in this folder.

## Jupyter Notebooks

### `week01_task_bcstats (1).ipynb`

- Type: starter notebook.
- Size: 18 cells, with 9 Markdown cells and 9 code cells.
- Role: student-facing task notebook for Week 1 business-cycle statistics.
- Main sections:
  - Connect to FRED.
  - Download data from FRED.
  - Optional fallback files.
  - Summary statistics.
  - HP filter.
  - Plot trend and cycle.
  - Business-cycle statistics.
  - Short questions.
- Core data series:
  - `GDPC1`: real GDP.
  - `PCEC96`: real consumption.
  - `GPDIC1`: real private domestic investment.
- Main packages:
  - `numpy`.
  - `pandas`.
  - `matplotlib.pyplot`.
  - `fredapi.Fred`.
  - `statsmodels.tsa.filters.hp_filter.hpfilter`.
- Workflow expectations:
  - Students paste their own FRED API key.
  - Download GDP, consumption, and investment.
  - Convert monthly `PCEC96` to quarterly before merging.
  - Keep common observations only.
  - Apply HP filter with `lamb = 1600`.
  - Compute and interpret volatility, correlation, and pre-COVID differences.
- Relation to PDF: implements `week01.pdf`.

### `week01_solution_bcstats.ipynb`

- Type: solution notebook.
- Size: 20 cells, with 10 Markdown cells and 10 code cells.
- Role: completed version of Week 1 business-cycle statistics task.
- Main sections:
  - Connect to FRED.
  - Download data from FRED.
  - Optional fallback files.
  - Summary statistics.
  - Raw-series plot.
  - HP filter.
  - Plot trend and cycle.
  - Business-cycle statistics.
  - Short questions.
- Core data series:
  - `GDPC1`: real GDP.
  - `PCEC96`: real consumption.
  - `GPDIC1`: real private domestic investment.
- Main packages:
  - `numpy`.
  - `pandas`.
  - `matplotlib.pyplot`.
  - `fredapi.Fred`.
  - `statsmodels.tsa.filters.hp_filter.hpfilter`.
- Main operations:
  - Reads from FRED or Excel fallbacks.
  - Resamples monthly consumption to quarterly.
  - Creates raw macro-series plot.
  - Logs the series and HP-filters them.
  - Computes cyclical volatility and GDP-cycle correlations.
  - Repeats statistics for sample ending in 2019Q4.
- Interpretation included in notebook:
  - Consumption is typically less volatile than GDP in the pre-2020 sample.
  - Investment remains clearly the most volatile series.
- Relation to PDF: solution companion to `week01.pdf`.

### `L1_investment_asset_prices.ipynb`

- Type: lecture notebook.
- Size: 31 cells, with 18 Markdown cells and 13 code cells.
- Role: computational companion to `lecture_01_ch15 (1).pdf`.
- Main sections:
  - Lecture 1 Notebook: Data Replication and Numerical Implementation.
  - Notebook Part 1: Replicate the Denmark Figure.
  - Descriptive Statistics.
  - Notebook Part 2: Numerical Implementation.
  - Present value of future payments.
  - Bond pricing.
  - Gordon growth model.
  - Forward iteration and convergence.
  - Notebook Part 3: Tobin's q and the optimal level of investment.
  - Numerical exercise: compute optimal investment.
  - Figure: optimal level of investment.
  - How optimal investment responds to `q` and `a`.
- Main packages:
  - `pathlib.Path`.
  - `io`.
  - `matplotlib.pyplot`.
  - `numpy`.
  - `pandas`.
  - `requests`.
  - `statsmodels.tsa.filters.hp_filter.hpfilter`.
- Data sources:
  - FRED API, requiring an API key.
  - Denmark real GDP series `CLVMNACSCAB1GQDK`.
  - Denmark house price series `QDKR368BIS`.
- Main outputs:
  - Denmark output/house-price figure from 2000 onward.
  - Mean, standard deviation, and correlation for the Denmark series.
  - Present-value calculations for alternative rates and horizons.
  - Bond-price calculations.
  - Gordon-model value sensitivities to dividends, real rates, risk premia, and
    growth.
  - Forward-iteration convergence exercise.
  - Tobin's q and investment response plots.
- Key model links:
  - Present value and discounting.
  - One-period bond pricing.
  - Gordon growth valuation.
  - q-theory with adjustment costs.

### `L2_business_housing_investment.ipynb`

- Type: lecture notebook.
- Size: 18 cells, with 11 Markdown cells and 7 code cells.
- Role: Lecture 2 computational continuation of Chapter 15, focused on business
  and housing investment.
- Main sections:
  - Investment function: `q_t = 1 + c'(I_t)`.
  - Capital accumulation dynamics.
  - Shock tracing.
  - Housing Tobin's q.
  - Denmark housing q from FRED.
  - Average vs marginal q.
  - Summary.
- Main packages:
  - `numpy`.
  - `matplotlib.pyplot`.
  - `denmark_housing_q_data.SERIES_IDS`.
  - `denmark_housing_q_data.load_or_fetch_denmark_housing_q`.
- Local function:
  - `investment(q, a)`.
- Data sources via helper script:
  - `QDKN628BIS`: Denmark residential property price index.
  - `OPCNRE01DKQ661N`: residential construction cost index.
  - `DNKPERMITQISMEI`: building permits for dwellings as housing-activity proxy.
- Main outputs:
  - Investment as a function of q and adjustment-cost parameter `a`.
  - Capital-stock path from investment shocks.
  - Shock-tracing exercises.
  - Housing q and housing investment dynamics.
  - Denmark housing q plot from rebased price and cost indices.
  - Average vs marginal q under decreasing returns.
- Important note from notebook:
  - The older FRED work-started series `WSCNDW01DKQ489N` stops in 2018, so the
    notebook uses building permits to avoid that cutoff.
- Depends on: `denmark_housing_q_data.py`.

### `L3_consumption (1).ipynb`

- Type: lecture notebook.
- Size: 45 cells, with 25 Markdown cells and 20 code cells.
- Role: computational companion to `lecture_03_ch16 (1).pdf`.
- Main sections:
  - Keynesian benchmark and APC.
  - Real data: consumption and income.
  - FRED data setup.
  - Two-period model and closed-form solution.
  - Temporary versus permanent income.
  - Borrowing constraints and precautionary saving.
  - Summary.
- Main packages:
  - `io`.
  - `numpy`.
  - `matplotlib.pyplot`.
  - `pandas`.
  - `requests`.
- Local function:
  - `fetch_fred(series_id, api_key, frequency=None)`.
- Data sources:
  - FRED API with fallback text data.
  - `PCEC96`: real personal consumption expenditures.
  - `DSPIC96`: real disposable personal income.
  - Suggested extension uses `PSAVERT`: personal saving rate.
- Main outputs:
  - Keynesian consumption function plots and APC calculations.
  - FRED-based consumption/income data work.
  - Two-period consumption allocation.
  - Closed-form CRRA solution and numerical grid-search verification.
  - Temporary vs permanent income-response table.
  - Borrowing-constraint illustrations.
  - Precautionary-saving illustration.
- Key model links:
  - `C = C_bar + bY^d`.
  - Intertemporal budget constraint.
  - Human wealth.
  - Keynes-Ramsey rule.
  - `C_1 = theta(V_1 + H_1)`.
  - PIH annuity factor.
  - Borrowing constraints and precautionary saving.

### `L4_monetary_policy_aggregate_demand.ipynb`

- Type: lecture notebook.
- Size: 41 cells, with 25 Markdown cells and 16 code cells.
- Role: computational companion to `lecture_04_ch17 (1).pdf`.
- Main sections:
  - Notebook map and calibration.
  - Exact linear IS benchmark and multiplier.
  - Full IS-LM model.
  - Taylor rule and horizontal policy line.
  - From IS-LM to the AD curve.
  - Bridge figure tracing AD from IS and policy line.
  - Data lab: policy rates and central bank balance sheets.
  - FRED data access.
  - Summary.
- Main packages:
  - `numpy`.
  - `pandas`.
  - `matplotlib.pyplot`.
  - `requests`.
- Local functions:
  - `reduced_form_is_parameters(p)`.
  - `is_curve_r_gap(y_gap, p)`.
  - `is_curve_level(Y, p, shock=0.0)`.
  - `lm_curve(Y, p, shock=0.0)`.
  - `is_lm_equilibrium(p, is_shock=0.0, lm_shock=0.0)`.
  - `real_rate_from_taylor(pi, p)`.
  - `policy_line(Y, r_policy)`.
  - `policy_equilibrium(p, r_policy, is_shock=0.0)`.
  - `bridge_points(pi, p)`.
  - `ad_objects(p)`.
  - `ad_inflation(y_gap, p)`.
  - `download_fred_csv(series_id)`.
- Data sources:
  - FRED `EFFR`: Fed effective funds rate.
  - FRED `ECBDFR`: ECB deposit facility rate.
  - FRED `WALCL`: Federal Reserve total assets.
  - FRED `ECBASSETSW`: Eurosystem total assets.
- Main outputs:
  - IS multiplier calculations.
  - IS curve plots and shock scenarios.
  - IS-LM equilibrium under IS and LM shocks.
  - Taylor-rule real-rate response.
  - Policy-line equilibrium.
  - AD curve and shift experiments.
  - Policy-rate and balance-sheet data plots.
- Key model links:
  - Exact linear goods-market model.
  - IS-LM benchmark.
  - Modern central-bank interest-rate targeting.
  - Taylor-type policy rule.
  - AD curve derivation.

### `L5_phillips_curve.ipynb`

- Type: lecture notebook.
- Size: 21 cells, with 16 Markdown cells and 5 code cells.
- Role: computational companion to `lecture_05_ch18.pdf`.
- Main sections:
  - Notebook map and calibration.
  - Recent inflation: Denmark and the United States.
  - Phillips curve for Denmark before and after 2020.
  - AS curve simulation: anchored vs static expectations.
  - Sensitivity to slope parameter `gamma`.
  - Summary.
- Main packages:
  - `numpy`.
  - `pandas`.
  - `matplotlib.pyplot`.
  - `lecture_05_notebook_utils.fetch_eurostat`.
  - `lecture_05_notebook_utils.simulate_as`.
- Data sources:
  - Eurostat `prc_hicp_manr` for Denmark HICP inflation.
  - Eurostat `ei_cphi_m` for U.S. comparable inflation.
  - Eurostat `une_rt_m` for Denmark unemployment.
- Main outputs:
  - Year-on-year HICP inflation comparison for Denmark and the United States.
  - Danish Phillips-curve scatter before and after 2020.
  - Static vs anchored expectation simulations.
  - Sensitivity of AS dynamics to `gamma`.
- Key model links:
  - Phillips curve.
  - Expected inflation.
  - Natural unemployment/output relationship.
  - AS curve.
  - Supply shocks.
- Depends on: `lecture_05_notebook_utils.py`.

### `L6_as_ad_supply_shocks.ipynb`

- Type: lecture notebook.
- Size: 19 cells, with 12 Markdown cells and 7 code cells.
- Role: computational companion to `lecture_06_ch19.pdf`.
- Main sections:
  - AS-AD with static expectations.
  - Persistence and policy response.
  - Demand versus supply shocks.
  - Group exercise: energy supply shock.
  - Summary.
  - Energy prices and euro-area inflation.
- Main packages:
  - `numpy`.
  - `pandas`.
  - `matplotlib.pyplot`.
  - `lecture_06_notebook_utils` functions.
- Data sources:
  - FRED `PNGASEUUSDM`: natural gas price.
  - FRED `ENRGY0EZ19M086NEST`: euro-area energy HICP.
  - FRED `CP0000EZ19M086NEST`: euro-area all-items HICP.
  - Built-in fallback series if FRED access fails.
- Main outputs:
  - Static-expectations AS-AD simulations.
  - Persistence simulations under different policy parameter values.
  - Demand-shock vs supply-shock paths.
  - Group exercise table for energy supply shock.
  - Energy inflation, headline inflation, and natural-gas price plot with 2022
    highlighted.
- Key model links:
  - Demand shock `z_t`.
  - Supply shock `s_t`.
  - Policy strength parameter `a`.
  - AS slope parameter `gamma`.
  - Persistence coefficient `beta = 1 / (1 + a gamma)`.
- Depends on: `lecture_06_notebook_utils.py`.

## Data And Utility Files

### `week01_fred_consumption.xlsx`

- Type: Excel workbook.
- Sheets: one sheet, `Sheet1`.
- Dimensions: `A1:B230`.
- Header row: cells `A1` and `B1` are blank.
- Data rows: 229 apparent monthly observations.
- Date coverage:
  - first observation: 2007-01-01,
  - last observation: 2026-01-01.
- Values:
  - first value: `11181.0`,
  - last value: `16700.2`,
  - minimum value in file: `11068.0`,
  - maximum value in file: `16700.2`.
- Likely role:
  - fallback consumption data for Week 1 notebook work.
  - The notebooks expect this file to be read as the fallback for FRED
    `PCEC96` and then renamed to `Consumption`.
- Practical note:
  - Because the workbook has blank headers, code may need explicit column names
    after reading.
  - Dates are stored as Excel serial dates.

### `denmark_housing_q_data.py`

- Type: Python helper script.
- Role: data-fetching and preprocessing helper for
  `L2_business_housing_investment.ipynb`.
- Main constants:
  - `FRED_API_URL = "https://api.stlouisfed.org/fred/series/observations"`.
  - `SERIES_IDS`:
    - `price_index`: `QDKN628BIS`.
    - `cost_index`: `OPCNRE01DKQ661N`.
    - `permits_index`: `DNKPERMITQISMEI`.
  - `CACHE_FILENAME = "denmark_housing_q_fred_cache.csv"`.
- Main functions:
  - `_to_quarter_index(date_values)`: converts dates to quarterly PeriodIndex.
  - `fetch_fred_series(series_id, api_key=FRED_API_KEY, session=None)`:
    fetches one FRED series and returns a sorted quarterly pandas Series.
  - `_build_dataset(raw_df)`:
    - sorts and drops missing data,
    - uses 2015 as base year,
    - rebases house price and construction cost indices to 2015 = 100,
    - constructs `housing_q = price_rebased / cost_rebased`,
    - rebases permits to 2015 = 100,
    - creates `permits_4q_ma`.
  - `_cache_to_frame(cache_path)` and `_frame_to_cache(df, cache_path)`:
    local cache helpers.
  - `load_or_fetch_denmark_housing_q(api_key=FRED_API_KEY, cache_path=None)`:
    tries live FRED first, writes cache on success, and falls back to local
    cache if live fetch fails.
- Output columns from `_build_dataset`:
  - original `price_index`, `cost_index`, `permits_index`,
  - `price_rebased`,
  - `cost_rebased`,
  - `housing_q`,
  - `permits_rebased`,
  - `permits_4q_ma`.
- Practical note:
  - The script contains an embedded FRED API key.
  - If sharing publicly, treat the key as something to remove or replace.

### `lecture_05_notebook_utils.py`

- Type: Python helper script.
- Role: shared functions for `L5_phillips_curve.ipynb`.
- Main constant:
  - `EUROSTAT_BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"`.
- Main functions:
  - `fetch_eurostat(dataset, retries=4, sleep=4, **filters)`:
    - downloads a Eurostat series as monthly pandas Series,
    - passes filters to the Eurostat API,
    - retries failed requests,
    - extracts time dimension and observations from Eurostat JSON.
  - `simulate_as(par, regime)`:
    - simulates inflation under a one-off supply shock,
    - supports `regime = "static"` and `regime = "anchored"`,
    - initializes expected inflation at target,
    - updates expected inflation differently across regimes.
- Model connection:
  - Supports the Lecture 5 contrast between static expectations and anchored
    expectations after an AS/supply shock.

### `lecture_06_notebook_utils.py`

- Type: Python helper script.
- Role: shared functions for `L6_as_ad_supply_shocks.ipynb`.
- Main constant:
  - `FRED_BASE_URL = "https://api.stlouisfed.org/fred/series/observations"`.
- Main functions:
  - `fetch_fred_series(series_id, fred_api_key, start="2018-01-01", frequency=None, fallback=None)`:
    - downloads one FRED series,
    - supports optional frequency conversion parameter,
    - falls back to a provided local Series if download fails.
  - `annual_percentage_change(series)`:
    - computes year-on-year monthly percentage change as
      `100 * (series / series.shift(12) - 1)`.
  - `simulate_as_ad(T, a, gamma, s_path=None, z_path=None, pi0=0.0)`:
    - builds supply-shock path `s` and demand-shock path `z`,
    - sets `beta = 1 / (1 + a gamma)`,
    - simulates inflation gap and output gap,
    - returns a DataFrame with period, output gap, inflation gap, supply shock,
      and demand shock.
  - `policy_table(a_values, gamma, s1, T)`:
    - evaluates different policy strength values `a`,
    - reports impact output gap, impact inflation gap, and period-4 inflation
      gap.
  - `fallback_monthly_series(values, start, name)`:
    - creates fallback monthly pandas Series for notebook plotting.
- Model connection:
  - Encodes the dynamic AS-AD shock propagation logic used in Lecture 6.

## Cross-File Dependency Map

- `week01.pdf`
  - implemented by `week01_task_bcstats (1).ipynb`;
  - solved by `week01_solution_bcstats.ipynb`;
  - may use `week01_fred_consumption.xlsx` as fallback data.
- `lecture_01_ch15 (1).pdf`
  - implemented by `L1_investment_asset_prices.ipynb`;
  - practiced in `week02_investment_assetprices.pdf`;
  - checked in `week02_investment_assetprices_solutions.pdf`.
- `L2_business_housing_investment.ipynb`
  - imports `denmark_housing_q_data.py`;
  - extends the Chapter 15 investment and housing material from Exercise Sheet
    2.
- `lecture_03_ch16 (1).pdf`
  - implemented by `L3_consumption (1).ipynb`;
  - assessed through `week03_consumption_handin_task.pdf`.
- `lecture_04_ch17 (1).pdf`
  - implemented by `L4_monetary_policy_aggregate_demand.ipynb`.
- `lecture_05_ch18.pdf`
  - implemented by `L5_phillips_curve.ipynb`;
  - notebook imports `lecture_05_notebook_utils.py`.
- `lecture_06_ch19.pdf`
  - implemented by `L6_as_ad_supply_shocks.ipynb`;
  - notebook imports `lecture_06_notebook_utils.py`.

## Topic Index

- Aggregate demand:
  - `lecture_04_ch17 (1).pdf`,
  - `L4_monetary_policy_aggregate_demand.ipynb`.
- AS-AD dynamics:
  - `lecture_06_ch19.pdf`,
  - `L6_as_ad_supply_shocks.ipynb`.
- Asset pricing:
  - `lecture_01_ch15 (1).pdf`,
  - `L1_investment_asset_prices.ipynb`,
  - `week02_investment_assetprices.pdf`.
- Business cycles and HP filtering:
  - `Ex_class_1_hold_2.pdf`,
  - `week01.pdf`,
  - `week01_task_bcstats (1).ipynb`,
  - `week01_solution_bcstats.ipynb`.
- Consumption:
  - `lecture_03_ch16 (1).pdf`,
  - `L3_consumption (1).ipynb`,
  - `week03_consumption_handin_task.pdf`.
- Data/API work:
  - FRED: `L1_investment_asset_prices.ipynb`,
    `L3_consumption (1).ipynb`,
    `L4_monetary_policy_aggregate_demand.ipynb`,
    `L6_as_ad_supply_shocks.ipynb`,
    `denmark_housing_q_data.py`,
    `lecture_06_notebook_utils.py`.
  - Eurostat: `L5_phillips_curve.ipynb`,
    `lecture_05_notebook_utils.py`.
- Housing investment:
  - `L2_business_housing_investment.ipynb`,
  - `denmark_housing_q_data.py`,
  - `week02_investment_assetprices.pdf`,
  - `week02_investment_assetprices_solutions.pdf`.
- Inflation and Phillips curve:
  - `lecture_05_ch18.pdf`,
  - `L5_phillips_curve.ipynb`.
- Investment and Tobin's q:
  - `lecture_01_ch15 (1).pdf`,
  - `L1_investment_asset_prices.ipynb`,
  - `L2_business_housing_investment.ipynb`,
  - `week02_investment_assetprices.pdf`.
- Monetary policy:
  - `lecture_04_ch17 (1).pdf`,
  - `L4_monetary_policy_aggregate_demand.ipynb`,
  - `lecture_06_ch19.pdf`.
- Mandatory hand-in:
  - `week03_consumption_handin_task.pdf`.

## Missing Or Referenced External Files

Some course materials refer to files that are not present in the current
`course_material/` folder:

- `week01_fred_gdp.xlsx`: referenced by Week 1 notebooks/PDF as optional
  fallback.
- `week01_fred_investment.xlsx`: referenced by Week 1 notebooks/PDF as optional
  fallback.
- `week03_consumption_student_start.ipynb`: referenced by the Week 3 hand-in.
- `week03_fred_consumption.csv`: referenced by the Week 3 hand-in.
- A separate Lecture 2 slide PDF is not present; the available Lecture 2
  material is the notebook `L2_business_housing_investment.ipynb`.
