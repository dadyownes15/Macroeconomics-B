# Week 3 Consumption Assignment Solution Plan

This plan is for finishing and cleaning `week_3/week_consumption_XX.ipynb`.

The goal is not to add more prose. The goal is to make the notebook run cleanly,
remove duplicated helper logic, and write short answers that state:

1. what was computed,
2. what the result is,
3. which consumption mechanism explains it.

## Target Style Agreement

Use a precise, output-driven style throughout the notebook.

### Answer Style

Each written answer should usually be 2-4 sentences.

Use this shape:

```text
I computed [object] using [equation/model]. The result is [number], so
[economic interpretation]. The mechanism is [Keynesian current-income response /
PIH wealth smoothing / intertemporal substitution / borrowing constraint /
cash-flow exposure].
```

For tasks that explicitly ask for numbers, cite the number from the notebook
output. Do not write a long conceptual essay when the task asks for a short
interpretation.

### Figure Style

Every figure should have:

- clear title,
- x-axis label,
- y-axis label,
- legend when more than one line is shown,
- brief source note in the title, caption text, or following Markdown when data
  are from FRED.

### Table Style

Use small tables for numerical comparisons. Round outputs for readability:

- rates: 3 decimals or percentage formatting,
- DKK values: 0-2 decimals,
- regression coefficients: 3 decimals,
- confidence intervals: 3 decimals.

### Sign Convention

Use one convention for Part 3 and keep it everywhere:

- Report **consumption cuts as positive numbers**.
- Do not call them deltas unless they are negative changes.

Therefore:

```python
pih_cut = pv_loss / annuity_factor(horizon, annual_real_rate)
constrained_cut = mpc * annual_payment_increase
```

If the narrative needs changes in consumption, write:

```python
pih_delta_c = -pih_cut
constrained_delta_c = -constrained_cut
```

But tables should use positive cuts.

## Source Material To Use

Primary references:

- `course_material/week03_consumption_handin_task.pdf`
- `course_material/lecture_03_ch16 (1).pdf`
- `course_material/L3_consumption (1).ipynb`

Supporting implementation references:

- `course_material/week01_solution_bcstats.ipynb` for data resampling and
  merging.
- `course_material/L4_monetary_policy_aggregate_demand.ipynb` for FRED request
  helper style.
- `week_3/course_material_assignment_map.md` for the exact source-to-assignment
  map.

Do not use housing-q code from Lecture 2 as a conceptual reference for the
mortgage cash-flow task. That code is about housing investment, not household
consumption.

## Notebook Structure After Cleanup

Keep the existing task order, but add one early helper section after imports.

Recommended top-level notebook layout:

1. Imports and global settings.
2. Shared helper functions.
3. Part 1.
4. Part 2.
5. Part 3.
6. Part 4.
7. Part 5.
8. Part 6.

The shared helper section should hold all reusable functions. Later task cells
should call those helpers instead of redefining similar logic.

## Shared Function Definitions

Create or revise one helper cell near the top of the notebook. This avoids
duplicating annuity logic, FRED parsing, OLS code, and consumption functions.

### Plotting Helpers

Keep the current `Line` dataclass if useful, but fix the mutable default issue.

Current issue:

```python
def plot(..., kwargs = {}):
```

Plan:

```python
@dataclass
class Line:
    label: str
    xx: np.ndarray
    yy: np.ndarray
    own_axis: bool = False
    color: str | None = None
    kwargs: dict = field(default_factory=dict)

def plot_lines(
    lines: list[Line],
    title: str,
    xlabel: str,
    ylabel: str,
    show_legend: bool = True,
    right_ylabel: str | None = None,
):
    ...
```

Use the helper for simple line plots. For scatter plots and regression lines,
direct matplotlib is fine.

### Keynesian Consumption Helpers

Use these for Part 1 only:

```python
def keynesian_consumption(Yd, C_bar=200.0, b=0.75):
    return C_bar + b * np.asarray(Yd)

def apc(C, Yd):
    return np.asarray(C) / np.asarray(Yd)

def mpc_keynesian(b=0.75):
    return b
```

Replace current `consumption`, `APC`, and `MPC` names with these clearer names,
or keep the old names only as thin aliases. Prefer the clearer names in new
code.

### Two-Period Model Helpers

Use these for Part 2:

```python
def human_wealth(Y1d, Y2d, r):
    return Y1d + Y2d / (1 + r)

def theta_crra(r, phi, sigma):
    return 1 / ((1 + (1 + phi) ** (-sigma) * (1 + r) ** (sigma - 1)))

def c2_from_budget(C1, W, r):
    return (1 + r) * (W - C1)

def two_period_allocation(V1, Y1d, Y2d, r, phi, sigma, fixed_wealth=None):
    H1 = human_wealth(Y1d, Y2d, r)
    W = V1 + H1 if fixed_wealth is None else fixed_wealth
    theta = theta_crra(r, phi, sigma)
    C1 = theta * W
    C2 = c2_from_budget(C1, W, r)
    S1 = V1 + Y1d - C1
    return {
        "H1": H1,
        "W": W,
        "theta": theta,
        "C1": C1,
        "C2": C2,
        "S1": S1,
    }
```

Reason:

- One function returns all required quantities.
- The fixed-wealth decomposition becomes unambiguous:
  `fixed_wealth=baseline["W"]`.
- Avoids separate `H_1`, `C_1`, `C_2`, and `allocation` calls scattered across
  cells.

### Utility And Numerical Verification Helpers

Use these for Task 2.5:

```python
def crra_utility(C, sigma):
    C = np.asarray(C, dtype=float)
    if np.isclose(sigma, 1.0):
        return np.log(C)
    return C ** (1 - 1 / sigma) / (1 - 1 / sigma)

def lifetime_utility(C1, W, r, phi, sigma):
    C2 = c2_from_budget(C1, W, r)
    valid = (C1 > 0) & (C2 > 0)
    out = np.full_like(np.asarray(C1, dtype=float), -np.inf)
    out[valid] = (
        crra_utility(np.asarray(C1)[valid], sigma)
        + (1 / (1 + phi)) * crra_utility(C2[valid], sigma)
    )
    return out

def grid_search_c1(W, r, phi, sigma, grid_size=20_000):
    C1_grid = np.linspace(1e-8, W - 1e-8, grid_size)
    U_grid = lifetime_utility(C1_grid, W, r, phi, sigma)
    i_star = np.argmax(U_grid)
    return C1_grid[i_star], U_grid[i_star], C1_grid, U_grid
```

Do not rely on the ternary search in the final answer. It is extra and not the
course implementation. The assignment asks for a fine-grid check, so report the
grid-search result.

### Annuity And PIH Helpers

Use one annuity function for Part 3 and Part 4.

```python
def annuity_factor(N, r):
    periods = np.arange(N)
    return np.sum((1 + r) ** (-periods))

def theta_annuity(N, r):
    return 1 / annuity_factor(N, r)

def pih_cut_from_pv_loss(pv_loss, horizon, annual_real_rate=0.03):
    return pv_loss / annuity_factor(horizon, annual_real_rate)

def constrained_cut(annual_cashflow_loss, mpc):
    return mpc * annual_cashflow_loss
```

This replaces:

- `annuity(N, r, start=0)`,
- `ucon_consumption_delta`,
- `con_consumption_delta`.

Reason:

- The names say what the functions do.
- The same `annuity_factor` is used in mortgage PV, PIH spreading, and Part 4.
- No hardcoded 30-year horizon inside the helper.

### Mortgage Helpers

Use these for Part 3:

```python
def effective_monthly_rate(annual_rate):
    return (1 + annual_rate) ** (1 / 12) - 1

def monthly_mortgage_payment(debt, maturity_years, annual_rate):
    monthly_rate = effective_monthly_rate(annual_rate)
    months = maturity_years * 12
    return debt * monthly_rate / (1 - (1 + monthly_rate) ** (-months))

def mortgage_payment_shock(debt, maturity_years, initial_rate, new_rate):
    old_payment = monthly_mortgage_payment(debt, maturity_years, initial_rate)
    new_payment = monthly_mortgage_payment(debt, maturity_years, new_rate)
    monthly_increase = new_payment - old_payment
    annual_increase = 12 * monthly_increase
    return {
        "old_payment": old_payment,
        "new_payment": new_payment,
        "monthly_increase": monthly_increase,
        "annual_increase": annual_increase,
    }

def pv_monthly_cashflow_loss(monthly_loss, years, annual_real_rate=0.03):
    monthly_real_rate = effective_monthly_rate(annual_real_rate)
    months = years * 12
    return monthly_loss * annuity_factor(months, monthly_real_rate)

def mortgage_consumption_cuts(
    debt,
    maturity_years,
    initial_rate,
    new_rate,
    loss_years=3,
    pih_horizon=30,
    constrained_mpc=0.9,
    annual_real_rate=0.03,
):
    shock = mortgage_payment_shock(debt, maturity_years, initial_rate, new_rate)
    pv_loss = pv_monthly_cashflow_loss(
        shock["monthly_increase"],
        loss_years,
        annual_real_rate,
    )
    pih_cut = pih_cut_from_pv_loss(pv_loss, pih_horizon, annual_real_rate)
    constrained = constrained_cut(shock["annual_increase"], constrained_mpc)
    return {
        **shock,
        "pv_loss": pv_loss,
        "pih_cut": pih_cut,
        "constrained_cut": constrained,
    }
```

Reason:

- Baseline and profile can call the same function.
- No accidental reuse of `monthly_loss` from the baseline in the profile.
- No mixing of the two-period `allocation(...)` model with mortgage cash-flow
  results.

### Break-Even MPC Helper

Use this for Task 3.5:

```python
def break_even_mpc(pih_cut, annual_cashflow_loss, grid_size=1001):
    mpc_grid = np.linspace(0, 1, grid_size)
    constrained_cuts = mpc_grid * annual_cashflow_loss
    idx = np.argmin(np.abs(constrained_cuts - pih_cut))
    return mpc_grid[idx], constrained_cuts[idx]
```

If the exact ratio is desired:

```python
m_star_exact = pih_cut / annual_cashflow_loss
```

But the task hints that a fine grid is enough, so report the grid result to
three decimals.

### Data Helpers

Use these for Part 5:

```python
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

def fetch_fred_series(series_id, api_key, frequency=None):
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
    }
    if frequency is not None:
        params["frequency"] = frequency
    response = requests.get(FRED_BASE, params=params, timeout=20)
    response.raise_for_status()
    obs = response.json()["observations"]
    dates = pd.to_datetime([o["date"] for o in obs])
    values = pd.to_numeric([o["value"] for o in obs], errors="coerce")
    return pd.Series(values, index=dates, name=series_id).dropna()

def load_consumption_data(api_key="", fallback_path="week03_fred_consumption.csv"):
    if api_key.strip():
        dpi = fetch_fred_series("DPIC96", api_key).rename("dpi")
        pce = fetch_fred_series("PCEC96", api_key).rename("pce")
        saving = fetch_fred_series("PSAVERT", api_key).rename("saving_rate")
        data = pd.concat([dpi, pce, saving], axis=1).resample("QE").mean()
    else:
        data = pd.read_csv(fallback_path, parse_dates=["DATE"]).set_index("DATE")
    data = data.sort_index().dropna()
    data.index = data.index.to_period("Q")
    return data

def index_to_base(series, base_period):
    return 100 * series / series.loc[base_period]

def quarterly_log_changes(data):
    return pd.DataFrame({
        "dlog_c": np.log(data["pce"]).diff(),
        "dlog_y": np.log(data["dpi"]).diff(),
    }).dropna()
```

Clean-run decision:

- Best option: make sure `week_3/week03_fred_consumption.csv` exists before
  submission.
- Second option: use a FRED API key.
- Avoid leaving the notebook dependent on a missing CSV and empty API key.

### OLS Helpers

Use one OLS implementation for Task 5.2 and Task 5.3.

```python
def ols_numpy(y, x):
    y = np.asarray(y, dtype=float)
    x = np.asarray(x, dtype=float)
    X = np.column_stack([np.ones(len(x)), x])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    resid = y - X @ beta
    n, k = X.shape
    sigma2 = resid @ resid / (n - k)
    cov = sigma2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    return beta, se, resid

def consumption_income_regression(reg_data):
    beta, se, resid = ols_numpy(reg_data["dlog_c"], reg_data["dlog_y"])
    beta_hat = beta[1]
    beta_se = se[1]
    ci_low = beta_hat - 1.96 * beta_se
    ci_high = beta_hat + 1.96 * beta_se
    return {
        "alpha": beta[0],
        "beta": beta_hat,
        "beta_se": beta_se,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "resid": resid,
    }

def exclude_covid_window(reg_data):
    return reg_data.loc[
        ~((reg_data.index >= "2020Q1") & (reg_data.index <= "2021Q4"))
    ]
```

Reason:

- The same regression code is reused for the full sample and no-COVID sample.
- Avoids duplicate NumPy OLS blocks.

## Task-by-Task Plan

### Task 1.1

Current state:

- Mostly solved.

Fix:

- Rename helper or keep alias.
- Use `keynesian_consumption`.
- Keep the plot.
- Optional: add 45-degree line only if it helps; not required by assignment.

Output:

- Figure of `C` against `Yd`.

Short answer:

- None required beyond plot.

### Task 1.2

Current state:

- Mostly solved.

Fix:

- Use `Yd_values = np.array([400, 600, 800, 1000])`, not `np.arange(400,1200,200)`
  if clarity is preferred.
- Add rounded table.

Output:

- Table with `Yd`, `C`, `MPC`, `APC`.

### Task 1.3

Current state:

- Written answer exists but should be tightened.

Replacement style:

```text
The APC calculation shows that APC falls as disposable income rises because
the fixed term C_bar is spread over a larger income base. That matches the
cross-section fact that richer households often spend a smaller share of
income. It is problematic for long-run aggregate data because aggregate
consumption and income tend to grow together, so the aggregate APC is much
more stable than the simple Keynesian function predicts.
```

Mechanism:

- Keynesian current-income rule with fixed autonomous consumption.

### Task 2.1

Current state:

- Solved, but function names are inconsistent and split across several helpers.

Fix:

- Replace with `human_wealth`, `theta_crra`, `c2_from_budget`,
  `two_period_allocation`.
- Keep baseline constants:
  - `V1 = 20`,
  - `Y1d = 250`,
  - `Y2d = 320`,
  - `r = 0.03`,
  - `phi = 0.03`,
  - `sigma = 0.8`.

Output:

- No output required except helper definitions.

### Task 2.2

Current state:

- Code output and written number disagree.

Fix:

- Compute baseline once:

```python
baseline = two_period_allocation(...)
```

- Print a table with:
  - `H1`,
  - `W`,
  - `theta`,
  - `C1`,
  - `C2`,
  - `S1`.

Short answer style:

```text
I computed the two-period allocation using the closed-form CRRA consumption
share. The household consumes C1 = [number] and saves S1 = [number]. Since
S1 is negative, it borrows in period 1; the mechanism is consumption
smoothing across the two periods.
```

Mechanism:

- PIH/lifetime wealth smoothing.

### Task 2.3

Current state:

- Computation mostly correct; text should be tightened.

Fix:

- Compute:

```python
high_r = two_period_allocation(..., r=0.07)
fixed_w = two_period_allocation(..., r=0.07, fixed_wealth=baseline["W"])
total_change = high_r["C1"] - baseline["C1"]
tilt_component = fixed_w["C1"] - baseline["C1"]
wealth_effect = total_change - tilt_component
```

Output:

- Table with baseline `C1`, high-rate `C1`, total change, fixed-wealth tilt
  component, and wealth effect.

Short answer style:

```text
Raising r from 3% to 7% changes C1 by [number]. Holding total wealth fixed,
the tilt component is [number], because the higher real interest rate makes
future consumption relatively cheaper and encourages more current saving or
less current consumption depending on sigma and parameters. The remaining
wealth effect is [number], because the present value of future income falls
when r rises.
```

Check sign carefully after running the corrected code. If the tilt component is
positive, write:

```text
With wealth fixed, C1 rises by [number] because under the assignment's
parameters the intertemporal substitution effect dominates in the direction
of consuming more today.
```

Mechanisms:

- intertemporal substitution,
- wealth effect through discounted future income.

### Task 2.4

Current state:

- Wrong `r` grid.
- Wrong sigma list.
- Explanation placeholder.

Fix:

```python
r_grid = np.linspace(0, 0.10, 100)
sigma_values = [0.5, 1.0, 1.5]
```

Plot `C1` for each sigma.

Short answer style:

```text
I plotted C1 over real interest rates for sigma = 0.5, 1.0, and 1.5.
The curves show that [larger/smaller] sigma makes C1 [more/less] sensitive
to r. The mechanism is the intertemporal elasticity of substitution: higher
sigma means the household is more willing to move consumption across periods
when the real interest rate changes.
```

Fill the bracketed direction after inspecting the final plot.

Mechanism:

- intertemporal elasticity of substitution.

### Task 2.5

Current state:

- Utility/grid code exists.
- Ternary search is extra.

Fix:

- Use `grid_search_c1`.
- Report:
  - closed-form `C1`,
  - grid-search `C1`,
  - absolute difference.
- Plot utility if useful, but the prompt only requires reporting values.

Short answer style:

```text
The closed-form value is C1 = [number], and the grid-search maximizer is
C1 = [number]. The absolute difference is [number], which is below 0.05.
If these did not agree, the likely error would be in the budget-implied C2,
the CRRA utility formula, or the theta formula.
```

Mechanism:

- verification of closed-form intertemporal optimization.

### Task 3.1

Current state:

- Monthly payment function exists.
- Annual increase should be reported.

Fix:

- Use `mortgage_payment_shock(2_000_000, 25, 0.01, 0.05)`.
- Print table:
  - old monthly payment,
  - new monthly payment,
  - monthly increase,
  - annual increase.

Short answer:

- None required beyond table, unless adding one sentence.

Mechanism:

- cash-flow exposure from rate reset.

### Task 3.2

Current state:

- Uses 35 payments and `start=1`.

Fix:

- Use 36 monthly payments for 3 years:

```python
pv_loss = pv_monthly_cashflow_loss(monthly_increase, years=3, annual_real_rate=0.03)
```

Output:

- Monthly loss, annual loss, PV loss.

Short answer style:

```text
I valued 36 monthly payment increases using the monthly real rate implied
by a 3% annual real rate. The present value of the cash-flow loss is
[number] DKK. The mechanism is that the adjustable-rate household faces an
immediate cash-flow loss when the mortgage rate resets.
```

### Task 3.3

Current state:

- Logic exists but sign convention should be cleaned.

Fix:

- Use positive cuts:

```python
pih_cut = pih_cut_from_pv_loss(pv_loss, horizon=30)
constrained_cut_09 = constrained_cut(annual_increase, 0.9)
```

Output:

- Table with PIH cut, constrained cut, and difference.

Short answer style:

```text
The PIH household cuts annual consumption by [number] DKK, while the
constrained household cuts by [number] DKK. The gap is large because the PIH
household spreads the present-value loss over a 30-year horizon, while the
constrained household responds strongly to the current annual cash-flow loss.
```

Mechanisms:

- PIH wealth smoothing,
- borrowing/cash-flow constraint.

### Task 3.4

Current state:

- Profile exists.
- Code mixes baseline variables, profile variables, two-period allocation, and
  marginal utility.

Fix:

- Define profile constants once:

```python
profile = {
    "debt": 3_000_000,
    "maturity_years": 30,
    "initial_rate": 0.015,
    "new_rate": 0.05,
    "pih_horizon": 30,
    "constrained_mpc": 0.50,
}
```

- Compute baseline and profile with the same function:

```python
baseline_mortgage = mortgage_consumption_cuts(
    debt=2_000_000,
    maturity_years=25,
    initial_rate=0.01,
    new_rate=0.05,
    pih_horizon=30,
    constrained_mpc=0.9,
)

profile_mortgage = mortgage_consumption_cuts(**profile)
```

Need to align keyword names exactly when implementing.

Output:

- Table with:
  - baseline PIH cut,
  - baseline constrained cut,
  - profile PIH cut,
  - profile constrained cut.
- Bar plot is better than current one-point line plot.

Short answer style:

```text
The profile uses debt of 3,000,000 DKK, 30-year maturity, a rate increase
from 1.5% to 5.0%, and constrained MPC of 0.50. The PIH cut is [number] DKK
and the constrained cut is [number] DKK. This is plausible for a young
high-income first-time buyer with a large mortgage, because the mortgage
payment shock is large but the lower MPC reflects some liquidity buffer.
```

Mechanisms:

- larger debt raises cash-flow exposure,
- lower constrained MPC dampens current cut,
- PIH spreads PV loss over horizon.

### Task 3.5

Current state:

- Blank.

Fix:

- Use profile results:

```python
m_star, matched_cut = break_even_mpc(
    pih_cut=profile_mortgage["pih_cut"],
    annual_cashflow_loss=profile_mortgage["annual_increase"],
)
```

Output:

- `m_star` to three decimals.
- Table with PIH cut and matched constrained cut.

Short answer style:

```text
The break-even constrained MPC is m* = [number]. This is [low/high] relative
to typical constrained-household MPC values, which means that identifying
constrained households from annual consumption cuts is [easy/hard] in this
profile because [reason based on the number].
```

Mechanism:

- constrained household cut scales with current cash-flow loss and MPC.

### Task 4.1

Current state:

- Blank.

Fix:

- Use:

```python
N_grid = np.arange(1, 61)
theta_values = np.array([theta_annuity(N, 0.03) for N in N_grid])
long_limit = 0.03 / 1.03
```

- Plot `theta_values`.
- Add horizontal line at `long_limit`.

Short answer:

- One sentence if needed:

```text
The temporary MPC falls with the horizon because the same one-off income gain
is spread over more future periods under the PIH.
```

Mechanism:

- PIH annuity smoothing.

### Task 4.2

Current state:

- Blank.

Fix:

- For horizons `[5, 30, 60]` and income increase `5000`:

```python
temporary_response = 5000 * theta_annuity(N, 0.03)
permanent_response = 5000
```

Output:

- Table with `N`, `theta_N`, temporary response, permanent response.

Short answer style:

```text
A temporary 5,000 DKK income gain raises current consumption by [numbers]
depending on the horizon, while a permanent gain raises it by 5,000 DKK in
each case. The mechanism is that temporary income is annuitized over the
remaining horizon, but permanent income raises lifetime resources every
period.
```

### Task 4.3

Current state:

- Blank.

Fix:

```python
constrained_share = 0.35
constrained_mpc = 0.9
pih_share = 1 - constrained_share
aggregate_response = (
    constrained_share * constrained_mpc * 5000
    + pih_share * temporary_response
)
```

Output:

- Add aggregate temporary response column to Task 4.2 table.

Short answer style:

```text
The aggregate response is larger than the pure PIH response because 35% of
households are constrained and consume 90% of the temporary income gain. The
mechanism is MPC heterogeneity: constrained households link consumption more
closely to current income.
```

### Task 5 Data Loading

Current state:

- Loader exists but fails without CSV or API key.

Fix:

- Choose one clean-run strategy:
  - preferred: add `week03_fred_consumption.csv` to `week_3`;
  - acceptable: use valid FRED key;
  - robust: embed a fallback dataset in the notebook.

Plan recommendation:

- Prefer adding the CSV if available.
- If CSV is not available, use a valid FRED key once to generate it, then save
  it so the submitted notebook can run offline from the CSV.

Required data columns:

- `dpi`: real disposable personal income, FRED `DPIC96`.
- `pce`: real personal consumption expenditure, FRED `PCEC96`.
- `saving_rate`: personal saving rate, FRED `PSAVERT`.

Implementation:

- After loading, convert to quarterly `PeriodIndex`:

```python
data.index = data.index.to_period("Q")
```

Reason:

- Easier base lookup with `"2015Q1"`.
- Easier COVID exclusion with `"2020Q1"` to `"2021Q4"`.

### Task 5.1

Current state:

- Blank.

Fix:

- Create:

```python
data["dpi_index"] = index_to_base(data["dpi"], "2015Q1")
data["pce_index"] = index_to_base(data["pce"], "2015Q1")
data["apc"] = data["pce"] / data["dpi"]
```

- Plot:
  - DPI and PCE index together.
  - APC and saving rate, twin axis is fine.

Short answer:

```text
I indexed real DPI and PCE to 2015Q1 = 100 and computed APC as PCE/DPI.
The figure shows [brief observation from plot]. The mechanism is that
aggregate consumption follows income over time, but saving-rate movements
create short-run deviations.
```

### Task 5.2

Current state:

- Blank.

Fix:

- Build regression data:

```python
reg_data = quarterly_log_changes(data)
full_reg = consumption_income_regression(reg_data)
```

- Print:
  - alpha,
  - beta,
  - 95% CI.

Short answer style:

```text
I estimated quarterly consumption-growth comovement with disposable-income
growth using NumPy OLS. The estimate is beta_hat = [number], with 95% CI
[low, high]. This is descriptive comovement, not a structural MPC, because
income and consumption are jointly affected by shocks and policy.
```

Mechanism:

- empirical comovement of consumption and income.

### Task 5.3

Current state:

- Blank.

Fix:

```python
reg_no_covid = exclude_covid_window(reg_data)
no_covid_reg = consumption_income_regression(reg_no_covid)
```

Output:

- Table comparing full-sample and excluding-2020Q1-2021Q4 beta and CI.

Short answer:

```text
Excluding 2020Q1-2021Q4 changes beta_hat from [full] to [no-COVID].
That period is special because lockdowns, transfers, forced saving, and
reopening changed consumption and disposable income in unusually large and
asynchronous ways.
```

Mechanism:

- pandemic shock and policy transfers distort normal consumption-income
  comovement.

### Task 5.4

Current state:

- Blank.

Fix:

- Scatter:

```python
ax.scatter(reg_data["dlog_y"], reg_data["dlog_c"])
x_grid = np.linspace(reg_data["dlog_y"].min(), reg_data["dlog_y"].max(), 100)
y_fit = full_reg["alpha"] + full_reg["beta"] * x_grid
ax.plot(x_grid, y_fit)
```

Short answer:

```text
The scatter plot shows a positive relationship between income growth and
consumption growth, consistent with beta_hat = [number]. It cannot prove a
structural MPC because causality may run through common shocks, expectations,
credit constraints, and policy transfers. The regression is useful as a
descriptive check, not as a full consumption model.
```

### Part 6 Narrative

Current state:

- Blank.

Fix only after all numbers are final.

Use this exact structure:

```text
The two-period model shows that [number from Task 2], which means [mechanism].
In the mortgage experiment, my profile gives [number from Task 3], because
[mechanism]. In the data section, beta_hat is [number], so [interpretation].
A limitation is [specific limitation].
```

Target length:

- 250-400 words, but closer to 250 is fine if every required number is cited.

Do not introduce new theory in Part 6. Summarize the notebook's own outputs.

## Streamlining Rules

Apply these while editing the notebook:

1. Define `annuity_factor` once and use it everywhere.
2. Define `theta_annuity` once and use it in Part 4.
3. Define mortgage shock/cut helpers once and use them for both baseline and
   profile.
4. Define one OLS helper and use it for full sample and no-COVID sample.
5. Avoid hardcoded horizons inside helpers. Pass `horizon` as an argument.
6. Do not reuse variables named `payments`, `monthly_loss`, or `pv_total_loss`
   across baseline and profile without clear prefixes.
7. Use names like:
   - `baseline_mortgage`,
   - `profile_mortgage`,
   - `monthly_increase`,
   - `annual_increase`,
   - `pv_loss`,
   - `pih_cut`,
   - `constrained_cut`.
8. Do not use `u_prime` as an MPC.
9. Do not use Part 2 `allocation(...)` to compute mortgage cuts.
10. Keep all generated numbers in variables that Part 6 can reuse.

## Final Verification Checklist

Before submission:

- [ ] Clean kernel run completes without errors.
- [ ] No code cells contain only `# write your code here`.
- [ ] No markdown placeholders remain.
- [ ] Task 2.2 written saving number matches code output.
- [ ] Task 2.4 uses `sigma = 0.5, 1.0, 1.5` and a real grid over `r`.
- [ ] Task 3 reports cuts as positive numbers.
- [ ] Task 3.2 uses 36 monthly losses or clearly justified annual approximation.
- [ ] Task 3.4 profile code uses profile variables only.
- [ ] Task 3.5 reports `m*` to three decimals.
- [ ] Part 4 table includes `N = 5, 30, 60`.
- [ ] Part 5 data loads without internet dependency or with a valid key.
- [ ] Part 5 reports full-sample beta and no-COVID beta.
- [ ] Part 6 cites one number from Part 2, one from Part 3, one beta from Part 5,
      and one limitation.

## Implementation Priority

1. Shared helper cell.
2. Part 2 corrections.
3. Part 3 corrections and missing Task 3.5.
4. Part 4 implementation.
5. Part 5 data strategy and implementation.
6. Part 6 narrative.
7. Clean-run verification.

