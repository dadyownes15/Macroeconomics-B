# Week 3 Assignment - Course Material Implementation Map

This document maps the code in `course_material/` to the current Week 3
assignment implementation in `week_3/week_consumption_XX.ipynb`.

Goal: make it explicit which course references should be cited or used, which
course implementations should be copied/adapted, and where the assignment
notebook currently has missing or divergent implementation.

## Files Reviewed

### Assignment-side files

- `week_3/week_consumption_XX.ipynb`
  - Active assignment notebook.
  - Partly implemented.
  - Contains the functions/classes currently being mapped.
- `week_3/week03_consumption_handin_task.pdf`
  - Assignment specification.
  - Same task family as `course_material/week03_consumption_handin_task.pdf`.
- `week_3/L3_consumption.ipynb`
  - Local copy of Lecture 3 notebook.
  - Closest direct code reference for most Week 3 tasks.
- `week_3/notes.ipynb`
  - Small local scratch notebook.
  - Contains a useful `theta_annuity(N, r)` helper.
- `week_3/week_consumption_review.md`
  - Existing review note.
  - Useful as prior diagnostic context, but this document re-checks the current
    notebook state directly.

### Course code files

The following course code files were reviewed:

- `course_material/week01_task_bcstats (1).ipynb`
- `course_material/week01_solution_bcstats.ipynb`
- `course_material/L1_investment_asset_prices.ipynb`
- `course_material/L2_business_housing_investment.ipynb`
- `course_material/L3_consumption (1).ipynb`
- `course_material/L4_monetary_policy_aggregate_demand.ipynb`
- `course_material/L5_phillips_curve.ipynb`
- `course_material/L6_as_ad_supply_shocks.ipynb`
- `course_material/denmark_housing_q_data.py`
- `course_material/lecture_05_notebook_utils.py`
- `course_material/lecture_06_notebook_utils.py`

The PDFs are not code, but the following PDFs are direct conceptual references:

- `course_material/lecture_03_ch16 (1).pdf`
- `course_material/week03_consumption_handin_task.pdf`

## High-Level Conclusion

The Week 3 assignment should draw most of its course references from Lecture 3:

- `course_material/lecture_03_ch16 (1).pdf`
- `course_material/L3_consumption (1).ipynb`
- `course_material/week03_consumption_handin_task.pdf`

Other course notebooks are secondary implementation references:

- Use `week01_solution_bcstats.ipynb` for data loading, resampling, and
  DataFrame construction patterns.
- Use `L4_monetary_policy_aggregate_demand.ipynb` and
  `lecture_06_notebook_utils.py` only for robust FRED download/fallback style.
- Use `L1_investment_asset_prices.ipynb` only for generic present-value and
  discounting intuition.
- Do not use `L2`, `L5`, or the Denmark housing q helper as substantive
  references for this assignment except as examples of plotting or helper-file
  organization.

The active assignment notebook currently has these important gaps:

- Task 3.5 is blank.
- Tasks 4.1, 4.2, and 4.3 are blank.
- Tasks 5.1, 5.2, 5.3, and 5.4 are blank.
- The Part 5 loader currently tries to read `week03_fred_consumption.csv`, but
  that file is not present in `week_3/` and `FRED_API_KEY` is empty. As written,
  the notebook will not clean-run through Part 5.
- Several written answer placeholders remain.
- Some implemented mortgage-profile calculations mix the two-period model with
  the mortgage cash-flow model. That should be corrected before using the
  results in the final narrative.

## Assignment Notebook Inventory

This section maps the current active notebook cells to their implemented objects.

| Assignment area | Current cells | Current implementation |
| --- | ---: | --- |
| Setup | code cell 3 | Imports `numpy`, `pandas`, `matplotlib.pyplot`, `requests`; sets plot style and random generator. |
| Custom plotting helper | code cell 4 | Defines `Line` dataclass and `plot(lines, title, xlabel, ylabel, show_legend, kwargs)`. |
| Task 1.1 | code cell 7 | Defines `consumption(Y_d, b=0.75, C_hat=200)`; plots `C` over `Y_d = 100,...,1200`. |
| Task 1.2 | code cell 9 | Defines `APC(C, Y_d)` and `MPC(b=0.75)`; builds table for `Y_d = 400, 600, 800, 1000`. |
| Task 1.3 | markdown cell 11 | Written answer on APC cross-section vs long-run aggregate data. |
| Task 2.1 | code cell 14 | Defines `H_1`, `C_1`, `C_2`, `thetaFunc`, and `allocation`. |
| Task 2.2 | code cell 17, markdown cell 18 | Computes baseline allocation and saving; written text currently gives a saving number that does not match the code output. |
| Task 2.3 | code cell 20, markdown cell 21 | Computes total `C1` change, fixed-wealth tilt component, and remaining wealth effect. |
| Task 2.4 | code cell 23, markdown cell 24 | Plots only two `r` points and uses `sigma = 0.1` instead of required `sigma = 1.0`; explanation placeholder remains. |
| Task 2.5 | code cells 26, 28, 29, 30, 31, 32 | Defines utility functions, Euler residual check, ternary search, and grid search. |
| Task 3.1 | code cell 36 | Defines `effective_monthly_rate(i)` and `monthly_mortgage_payment(D, M, i)`. |
| Task 3.2 | code cell 39 | Defines `annuity(N, r, start=0)` and computes PV of mortgage cash-flow loss. |
| Task 3.3 | code cell 41 | Defines `ucon_consumption_delta` and `con_consumption_delta`. |
| Task 3.4 | markdown cell 44, code cell 45, markdown cell 46 | Defines a group profile and plots profile vs baseline cuts, but current code mixes profile and baseline variables. |
| Task 3.5 | code cell 48, markdown cell 49 | Blank. |
| Task 4.1 | code cell 52 | Blank. |
| Task 4.2 | code cell 54 | Blank. |
| Task 4.3 | code cell 56 | Blank. |
| Part 5 loader | code cell 58 | Defines `fetch_fred` and `load_consumption_data`, then calls loader. This fails without CSV or API key. |
| Task 5.1 | code cell 60 | Blank. |
| Task 5.2 | code cell 62 | Blank. |
| Task 5.3 | code cell 64, markdown cell 65 | Blank plus explanation placeholder. |
| Task 5.4 | code cell 67, markdown cell 68 | Blank plus interpretation placeholder. |
| Part 6 | markdown cell 70, code cell 71 | Narrative placeholder; optional code placeholder. |

## Course Code Relevance Matrix

| Course code file | Main implemented code | Relevance to Week 3 assignment | Look at specifically |
| --- | --- | --- | --- |
| `L3_consumption (1).ipynb` | Keynesian benchmark, APC, FRED data, two-period closed form, grid verification, PIH temporary/permanent shocks, borrowing constraint, precautionary saving. | Primary code reference. Most assignment tasks come from this notebook. | Cells 4, 6, 12, 13, 15, 20, 21, 26, 27, 33, 34, 39, 40. |
| `week01_solution_bcstats.ipynb` | Reads fallback data, resamples monthly data to quarterly, concatenates series, computes log changes/statistics. | Useful for Part 5 data handling. | Cell 7 for `pd.read_excel`, `.resample(...)`, `pd.concat(...).dropna()`; cell 9 for summary table pattern. |
| `L4_monetary_policy_aggregate_demand.ipynb` | FRED downloader returning clean `DATE` plus series column; policy-rate plots. | Useful only for robust Part 5 FRED loading and plot style. | Cell 35 `download_fred_csv(series_id)`. |
| `lecture_06_notebook_utils.py` | `fetch_fred_series`, `annual_percentage_change`, `fallback_monthly_series`, AS-AD simulation helpers. | Useful for robust fallback pattern, not for consumption theory. | `fetch_fred_series(...)` and `fallback_monthly_series(...)`. |
| `L1_investment_asset_prices.ipynb` | FRED request parsing, present value plots, bond pricing, Gordon formula. | Useful for generic present-value/discounting intuition in mortgage PV and annuity sections. | Cell 11 present value; cell 13 bond discounting; cell 4 FRED parsing style. |
| `week01_task_bcstats (1).ipynb` | Starter TODO version of Week 1 data workflow. | Low value because solution notebook has the completed pattern. | Use only if checking assignment-style TODO structure. |
| `L2_business_housing_investment.ipynb` | q-theory investment, capital dynamics, housing q, Denmark housing data. | Not substantively relevant to Week 3 consumption assignment. | Do not cite for consumption mechanisms. |
| `denmark_housing_q_data.py` | FRED fetch with cache fallback for Denmark housing q. | Not substantively relevant; useful only as helper architecture example. | Cache/fallback structure if building a robust data helper. |
| `L5_phillips_curve.ipynb` | Eurostat fetch, Phillips curve, AS simulation. | Not relevant to Week 3 assignment. | Do not use as a core reference. |
| `lecture_05_notebook_utils.py` | Eurostat downloader and AS expectation simulation. | Not relevant to Week 3 assignment. | Do not use. |
| `L6_as_ad_supply_shocks.ipynb` | AS-AD shock simulations and FRED energy data. | Not substantively relevant; fallback data pattern may be useful. | Cell 16 for fallback data construction pattern only. |

## PDF Reference Map

Use these PDF sections as conceptual references in written answers.

### Lecture 3 PDF: `course_material/lecture_03_ch16 (1).pdf`

Relevant slide/page headings:

- Page 7: Keynesian Consumption Function.
- Page 8: Two Contradictory Patterns.
- Page 9: Empirical Puzzle.
- Page 10: Two-Period Setup.
- Page 11: From Period Budgets to the Lifetime Budget.
- Page 12: Intertemporal Budget Constraint.
- Page 14: Preferences: Lifetime Utility.
- Page 15: From the IBC to the Optimal Consumption Choice.
- Page 16: Deriving the Keynes-Ramsey Rule Step by Step.
- Page 17: Economic Meaning of the Keynes-Ramsey Rule.
- Page 19: Closed-Form Consumption Function with CRRA Utility.
- Page 20: Solving for Current Consumption.
- Page 21: What Drives Current Consumption.
- Page 24: Permanent Income Hypothesis.
- Page 25: From Lifetime Wealth to an Annuity Rule.
- Page 26: Evaluating the Annuity Factor.
- Page 27: Temporary Versus Permanent Income: Step by Step.
- Page 34: Borrowing Constraints.
- Page 35: Precautionary Saving.
- Page 37: Back to the Opening Question: Why Adjustable-Rate Borrowers Cut More.
- Page 38: Notebook: L3 consumption.ipynb.
- Page 39: Takeaways.

### Week 3 hand-in PDF: `course_material/week03_consumption_handin_task.pdf`

Relevant pages:

- Page 1: Purpose, exam qualification, passing requirements.
- Page 2: Parts 1 and 2.
- Page 3: Parts 3, 4, and 5.
- Page 4: Part 6 final economic take-away.

Use the hand-in PDF as the assignment authority. Use Lecture 3 slides and
notebook as the theory/code authority.

## Task-by-Task Mapping

### Part 1 - Current Income and Keynesian Benchmark

Assignment tasks:

- 1.1 Plot `C = C_bar + bY_d`.
- 1.2 Compute MPC and APC at selected income levels.
- 1.3 Explain cross-section usefulness and long-run aggregate problem.

Current assignment implementation:

- `consumption(Y_d, b=0.75, C_hat=200)` in code cell 7.
- `APC(C, Y_d)` and `MPC(b=0.75)` in code cell 9.
- Written explanation in markdown cell 11.

Primary course references:

- `lecture_03_ch16 (1).pdf`, pages 7-9.
- `L3_consumption (1).ipynb`, cell 4:
  - Implements `C = a + bYd`.
  - Plots consumption and the 45-degree line.
- `L3_consumption (1).ipynb`, cell 6:
  - Implements `APC = C / Yd`.
  - Plots APC against disposable income.
- `week03_consumption_handin_task.pdf`, Part 1.

Implementation mapping:

| Assignment object | Course analogue | Status |
| --- | --- | --- |
| `consumption(Y_d, b=0.75, C_hat=200)` | `C = par['a'] + par['b'] * Yd` in L3 cell 4 | Correct adaptation with assignment parameters. |
| `APC(C, Y_d)` | `APC = C / Yd` in L3 cell 6 | Correct. |
| `MPC(b=0.75)` | Lecture formula: MPC is `b` | Correct. |
| Plot of `C` against `Y_d` | L3 cell 4 plot | Good, though the course plot also includes the 45-degree line. |

Recommended references to draw:

- Cite the Keynesian consumption function from Lecture 3 slides page 7.
- Cite the APC empirical puzzle from Lecture 3 slides pages 8-9.
- In code comments or written answer, refer to L3 notebook cells 4 and 6 as the
  direct implementation pattern.

Current issues to fix before submission:

- Markdown cell 11 has several typos. The economic content is basically right:
  richer households tend to have lower APC in cross-section, while long-run
  aggregate data do not show a steadily falling APC as income grows.

### Part 2 - Two-Period Consumption and the Real Interest Rate

Assignment tasks:

- 2.1 Implement human wealth, `theta`, and allocation.
- 2.2 Compute baseline `C1`, `C2`, total wealth, and saving.
- 2.3 Increase `r` from 0.03 to 0.07 and decompose the `C1` change.
- 2.4 Plot `C1` over `r in [0, 0.10]` for `sigma = 0.5, 1.0, 1.5`.
- 2.5 Verify closed-form `C1` numerically using lifetime utility.

Current assignment implementation:

- Code cell 14:
  - `H_1(Y_1_d, Y_2_d, r)`.
  - `C_1(V_1, H_1, Theta)`.
  - `C_2(C1, r, V1, H1)`.
  - `thetaFunc(r, phi, sigma)`.
  - `allocation(...)`.
- Code cell 17:
  - Baseline computation.
- Code cell 20:
  - Interest-rate increase and decomposition.
- Code cell 23:
  - Plot for different `sigma`, currently with wrong grid and wrong sigma list.
- Code cells 26, 28, 29, 30, 31, 32:
  - Utility, marginal utility, Euler residual, ternary search, grid search.

Primary course references:

- `lecture_03_ch16 (1).pdf`, pages 10-21.
- `L3_consumption (1).ipynb`, cell 20:
  - Implements total wealth:
    - `W1 = V1 + Y1d + Y2d / (1 + r)`.
  - Implements closed-form share:
    - `theta = 1 / (1 + (1 + phi)**(-sigma) * (1 + r)**(sigma - 1))`.
  - Computes:
    - `C1_closed = theta * W1`.
    - `C2_closed = (1 + r) * (W1 - C1_closed)`.
  - Implements grid-search verification:
    - candidate `C1_grid`,
    - implied `C2_grid`,
    - utility `U_grid`,
    - `np.argmax(U_grid)`.
- `L3_consumption (1).ipynb`, cell 21:
  - Plots lifetime utility and marks closed-form vs numeric optimum.
- `week03_consumption_handin_task.pdf`, Part 2.

Implementation mapping:

| Assignment object | Course analogue | Status |
| --- | --- | --- |
| `H_1(Y_1_d, Y_2_d, r)` | `Y1d + Y2d / (1 + r)` inside `W1` in L3 cell 20 | Correct. |
| `thetaFunc(r, phi, sigma)` | `theta = 1 / (1 + (1 + phi)**(-sigma) * (1 + r)**(sigma - 1))` in L3 cell 20 | Correct formula. |
| `C_1(V_1, H_1, theta)` | `C1_closed = theta * W1` in L3 cell 20 | Correct if `W1 = V1 + H1`. |
| `C_2(C1, r, V1, H1)` | `C2_closed = (1 + r) * (W1 - C1_closed)` in L3 cell 20 | Correct. |
| `allocation(...)` | L3 cell 20 code folded into a reusable function | Good abstraction for assignment. |
| fixed-wealth decomposition | No exact function in course notebook; derived from Lecture 3 page 21 | Good idea; must describe as fixed total wealth, not fixed human wealth. |
| `u`, `U`, `grid_search` | L3 cell 20 grid-search utility verification | Mostly aligned. |
| `tenerary_search` | No course analogue | Extra. Not needed for assignment; keep only if it does not distract. |

Specific course implementation to look at:

```python
# course_material/L3_consumption (1).ipynb, cell 20
W1 = par['V1'] + par['Y1d'] + par['Y2d'] / (1.0 + par['r'])
theta = 1.0 / (
    1.0
    + (1.0 + par['phi'])**(-par['sigma'])
    * (1.0 + par['r'])**(par['sigma'] - 1.0)
)
C1_closed = theta * W1
C2_closed = (1.0 + par['r']) * (W1 - C1_closed)
```

Recommended references to draw:

- For the formula and intuition: Lecture 3 pages 10-21.
- For numeric verification: L3 notebook cells 20-21.
- For assignment requirements: Week 3 hand-in PDF Part 2.

Current issues to fix before submission:

- Task 2.2 written answer says saving is `-88.1842`, but the current formula
  with the assignment parameters gives period-1 saving around `-24.63`.
  Update the text to match the code output.
- Task 2.3 explanation should use:
  - "real interest rate", not "rental rate";
  - "current consumption `C1`", not "total consumption";
  - "holding total wealth `W = V1 + H1` fixed", not "holding the change in
    human wealth fixed".
- Task 2.4 currently uses:
  - `r_l = [0, 0.1]`, only two points;
  - `sigma_l = [0.5, 0.1, 1.5]`, but assignment asks for `0.5, 1.0, 1.5`.
  It should use a fine grid:
  - `r_l = np.linspace(0, 0.10, 100)` or similar.
- Task 2.4 written explanation is still a placeholder.
- For Task 2.5, the grid-search method should be the main reported method
  because it directly matches the assignment prompt and L3 notebook cell 20.
  The ternary search is extra; it is not wrong in principle, but it is not the
  course implementation to cite.

### Part 3 - Cash-Flow Exposure and Borrowing Constraints

Assignment tasks:

- 3.1 Compute annuity mortgage payment before and after a rate increase.
- 3.2 Compute PV of the 3-year cash-flow loss.
- 3.3 Compare PIH household and constrained household.
- 3.4 Create a group-specific household profile.
- 3.5 Find break-even constrained MPC.

Current assignment implementation:

- Code cell 36:
  - `effective_monthly_rate(i)`.
  - `monthly_mortgage_payment(D, M, i)`.
- Code cell 39:
  - `annuity(N, r, start=0)`.
  - PV of mortgage cash-flow loss.
- Code cell 41:
  - `ucon_consumption_delta(W_delta, V_delta)`.
  - `con_consumption_delta(MPC, annual_cost)`.
- Code cell 45:
  - Group-specific profile.
- Code cell 48:
  - Blank break-even MPC task.

Primary course references:

- `lecture_03_ch16 (1).pdf`, pages 5-6:
  - Fixed-rate vs adjustable-rate mortgages.
  - Motivation for cash-flow exposure after monetary tightening.
- `lecture_03_ch16 (1).pdf`, pages 24-27:
  - PIH and annuity logic.
- `lecture_03_ch16 (1).pdf`, page 34:
  - Borrowing constraints.
- `lecture_03_ch16 (1).pdf`, page 37:
  - Adjustable-rate borrowers can cut consumption more because cash-flow
    constraints bind.
- `L3_consumption (1).ipynb`, cells 26-27:
  - Temporary/permanent income and annuity logic.
- `L3_consumption (1).ipynb`, cells 33-34:
  - Borrowing constraint implementation using `min(C1_uncon, resources_today)`.
- `week03_consumption_handin_task.pdf`, Part 3.

Important note:

- There is no exact mortgage-payment function in the course code.
- The mortgage annuity formula must be implemented from the assignment prompt
  and standard annuity-payment math.
- The relevant course implementation is the PIH annuity/spreading logic, not a
  mortgage-payment function.

Implementation mapping:

| Assignment object | Course analogue | Status |
| --- | --- | --- |
| `effective_monthly_rate(i)` | No exact course code | Acceptable assumption if stated clearly. |
| `monthly_mortgage_payment(D, M, i)` | No exact course code | Correct direction, but ensure annual and monthly conventions are clear. |
| `annuity(N, r, start=0)` | L3 cell 26 annuity share `theta_N`; Week 3 PDF Part 4 annuity formula | Good reusable helper. |
| `ucon_consumption_delta(W_delta, V_delta)` | PIH annuity rule from Lecture 3 pages 24-27 | Conceptually right if sign convention is clear. |
| `con_consumption_delta(MPC, annual_cost)` | Borrowing constraint/current-income exposure from Lecture 3 pages 34 and 37 | Conceptually right if sign convention is clear. |
| Group profile code | No exact course code | Should be built consistently from mortgage helper and PIH annuity helper. |
| Break-even MPC grid | L3 cell 20 grid-search pattern; L3 cell 39 risk-grid search pattern | Currently missing. |

Specific implementation patterns to look at:

- For PIH spreading:

```python
# course_material/L3_consumption (1).ipynb, cell 26
theta_N = (r / (1 + r)) / (1 - (1 + r)**(-N))
```

- For constrained household intuition:

```python
# course_material/L3_consumption (1).ipynb, cell 33
C1_con[i] = min(C1_uncon[i], resources_today)
```

- For grid-search style:

```python
# course_material/L3_consumption (1).ipynb, cell 20
i_star = np.argmax(U_grid)
C1_numeric = C1_grid[i_star]
```

Recommended references to draw:

- For mortgage motivation: Lecture 3 pages 5-6 and page 37.
- For PIH spreading of losses: Lecture 3 pages 24-27 and L3 notebook cell 26.
- For constrained household behavior: Lecture 3 page 34 and L3 notebook cells
  33-34.
- For the assignment-specific mortgage formula: Week 3 hand-in PDF Part 3.

Current issues to fix before submission:

- Task 3.1 table should report both monthly and annual payment increase.
- The code uses effective monthly rate:
  - `r_m = (1 + i)**(1/12) - 1`.
  State this assumption clearly.
  If the course expects nominal monthly compounding, use `i / 12` instead, but
  keep one convention consistently.
- Task 3.2 currently uses `annuity(35, monthly_rate, start=1)`.
  Three years of monthly losses should normally be `36` monthly payments. If
  using the assignment formula `sum_{j=0}^{N-1}`, the clean monthly version is:
  - `annuity(36, effective_monthly_rate(0.03)) * monthly_loss`.
  An annual approximation would be:
  - `annuity(3, 0.03) * annual_payment_increase`.
  Do not silently mix the two.
- Task 3.3 should use one sign convention:
  - consumption cuts as positive numbers, or
  - consumption changes as negative numbers.
  The final narrative should not mix "cut" and "delta" signs.
- Task 3.4 currently uses the profile rates in markdown and code, but the
  profile PIH calculation still reuses `monthly_loss` from the baseline instead
  of `monthly_cost_change` from the profile.
- Task 3.4 currently calculates one baseline PIH comparison using:
  - `allocation(r=0.04)[0] - allocation(r=0.045)[0]`.
  That is the two-period model from Part 2, not the mortgage cash-flow model
  from Part 3. The baseline comparison should instead use the baseline mortgage
  payment increase, baseline PV loss, and the same PIH annuity-spreading rule.
- Task 3.4 currently uses `u_prime(c1)` as if it were an MPC. This is not an
  MPC; it is marginal utility. Use `MPC = 0.9` for the baseline constrained
  household unless the task asks for another value.
- Task 3.5 is blank. It should use a fine grid over `m in [0, 1]` and find the
  `m` where:
  - constrained annual cut `m * annual_payment_increase_profile`
  - equals PIH annual cut `pv_loss_profile / A(horizon, 0.03)`.

### Part 4 - Temporary Versus Permanent Income Shocks

Assignment tasks:

- 4.1 Implement `A(N, r)` and `theta_N = 1 / A(N, r)`; plot `theta_N` for
  `N = 1,...,60`; add long-horizon limit `r / (1 + r)`.
- 4.2 Compare temporary and permanent DKK 5,000 income increases for
  `N = 5, 30, 60`.
- 4.3 Compute aggregate response when 35 percent are constrained with MPC 0.9
  and the rest follow PIH.

Current assignment implementation:

- Code cells 52, 54, and 56 are blank.
- Existing `annuity(N, r, start=0)` from code cell 39 can be reused.

Primary course references:

- `lecture_03_ch16 (1).pdf`, pages 24-28.
- `L3_consumption (1).ipynb`, cell 26:
  - Implements temporary vs permanent MPC table.
- `L3_consumption (1).ipynb`, cell 27:
  - Plots temporary and permanent response paths.
- `week_3/notes.ipynb`, cell 4:
  - `theta_annuity(N, r)`.
- `week_3/notes.ipynb`, cell 5:
  - `consumption(T, N, R)`.
- `week03_consumption_handin_task.pdf`, Part 4.

Implementation mapping:

| Assignment object | Course analogue | Status |
| --- | --- | --- |
| `annuity(N, r)` | Week 3 PDF Part 4 formula; L3 cell 26 closed-form `theta_N` | Already available from Task 3.2; reuse it. |
| `theta_N = 1 / annuity(N, r)` | L3 cell 26 `theta_N` formula | Missing in Part 4 cells. |
| Temporary response to DKK 5,000 | L3 cell 26 `temp_response[t] = theta_N` | Missing. |
| Permanent response to DKK 5,000 | L3 cell 26 `perm_response[t] = 1.0` | Missing. |
| Aggregate response | No exact course implementation | Compute weighted average using PIH and constrained groups. |

Specific course implementation to look at:

```python
# course_material/L3_consumption (1).ipynb, cell 26
theta_N = (par['r'] / (1.0 + par['r'])) / (
    1.0 - (1.0 + par['r'])**(-par['N'])
)
temp_response[t] = theta_N
perm_response[t] = 1.0
```

The assignment uses `theta_N = 1 / A(N, r)`, where:

```python
A(N, r) = sum((1 + r)**(-j) for j in range(N))
```

These are equivalent for the standard finite annuity factor.

Recommended references to draw:

- For theory: Lecture 3 pages 24-28.
- For implementation: L3 notebook cells 26-27.
- For exact assignment specification: Week 3 hand-in PDF Part 4.

Implementation plan:

- Reuse `annuity(N, r)` from code cell 39.
- Define:
  - `theta_N(N, r) = 1 / annuity(N, r)`.
- Build:
  - `N_grid = np.arange(1, 61)`.
  - `theta_values = np.array([theta_N(N, 0.03) for N in N_grid])`.
- Plot `theta_values`.
- Add horizontal line at:
  - `0.03 / 1.03`.
- For `N in [5, 30, 60]`:
  - temporary response = `5000 * theta_N(N, 0.03)`;
  - permanent response = `5000`;
  - aggregate temporary response =
    `0.35 * 0.9 * 5000 + 0.65 * temporary_response`.

### Part 5 - Real Data: Consumption, Income, and Saving

Assignment tasks:

- 5.1 Plot DPI and PCE as indices with 2015Q1 = 100; plot APC and saving rate.
- 5.2 Compute quarterly log changes and estimate
  `Delta log C_t = alpha + beta Delta log Y_t^d + error_t` using NumPy.
- 5.3 Repeat excluding 2020Q1 to 2021Q4.
- 5.4 Scatter plot with fitted regression line.

Current assignment implementation:

- Code cell 58:
  - Defines `fetch_fred(series_id, api_key, frequency=None)`.
  - Defines `load_consumption_data(api_key='', fallback_path=DATA_FILE)`.
  - Uses:
    - `DPIC96` for real disposable personal income,
    - `PCEC96` for real consumption,
    - `PSAVERT` for saving rate.
  - Calls `load_consumption_data(FRED_API_KEY, DATA_FILE)`.
- Code cells 60, 62, 64, and 67 are blank.
- `DATA_FILE = 'week03_fred_consumption.csv'`.
- `FRED_API_KEY = ''`.
- The CSV is not present in `week_3/`, so Part 5 currently fails on a clean run.

Primary course references:

- `week03_consumption_handin_task.pdf`, Part 5.
- `L3_consumption (1).ipynb`, cell 12:
  - FRED request helper.
  - Fallback embedded CSV strings.
  - Data merge.
  - Consumption/income indices.
  - APC proxy.
- `L3_consumption (1).ipynb`, cell 13:
  - Plots consumption and income indices.
- `L3_consumption (1).ipynb`, cell 15:
  - Plots APC proxy.
- `week01_solution_bcstats.ipynb`, cell 7:
  - Reads fallback data, resamples monthly consumption to quarterly, concatenates
    series, and drops missing rows.
- `L4_monetary_policy_aggregate_demand.ipynb`, cell 35:
  - Cleaner FRED download helper returning a DataFrame.

Important distinction:

- Lecture 3 notebook cell 12 uses `DSPIC96` and annual January observations for
  an illustrative lecture plot.
- The Week 3 assignment asks for quarterly data with:
  - `DPIC96`,
  - `PCEC96`,
  - `PSAVERT`.
- Therefore, use the Lecture 3 data code as a pattern, but follow the Week 3
  assignment series names and frequency requirements.

Implementation mapping:

| Assignment object | Course analogue | Status |
| --- | --- | --- |
| `fetch_fred(series_id, api_key, frequency=None)` | L3 cell 12 `fetch_fred`; L4 cell 35 `download_fred_csv` | Good pattern. |
| `load_consumption_data(...)` | L3 cell 12 try/fallback block; Week 1 cell 7 resampling | Partly good, but fails without CSV/API key. |
| indexed DPI/PCE plot | L3 cell 13 | Missing. |
| APC plot | L3 cell 15 | Missing; assignment also needs saving rate. |
| quarterly log changes | No exact L3 implementation; standard `np.log(...).diff()` | Missing. |
| OLS using NumPy | No exact course implementation | Missing. |
| excluding 2020Q1-2021Q4 | Week 1 cell 17 has sample restriction pattern | Missing. |
| scatter with fitted line | No exact course implementation; use standard matplotlib and OLS output | Missing. |

Specific course implementation to look at:

```python
# course_material/L3_consumption (1).ipynb, cell 12
params = {'series_id': series_id, 'api_key': api_key, 'file_type': 'json'}
r = requests.get(FRED_BASE, params=params, timeout=10)
obs = r.json()['observations']
dates = pd.to_datetime([o['date'] for o in obs])
values = pd.to_numeric([o['value'] for o in obs], errors='coerce')
s = pd.Series(values, index=dates, name=series_id)
```

```python
# course_material/week01_solution_bcstats.ipynb, cell 7
cons_q = cons.resample('QS').mean()
df = pd.concat([gdp, cons_q, inv], axis=1).dropna()
```

Recommended references to draw:

- For assignment data requirements: Week 3 hand-in PDF Part 5.
- For FRED helper and APC/index plot structure: L3 notebook cells 12, 13, 15.
- For quarterly resampling and clean `pd.concat(...).dropna()` workflow:
  Week 1 solution notebook cell 7.
- For the regression equation: Week 3 hand-in PDF Part 5.

Current issues to fix before submission:

- Add `week03_fred_consumption.csv` to `week_3/`, or supply a valid FRED API key,
  or embed a fallback CSV like L3 notebook cell 12. Without this, the notebook
  cannot run from a clean kernel.
- Complete Task 5.1:
  - create `dpi_index = 100 * dpi / dpi.loc['2015Q1']`,
  - create `pce_index = 100 * pce / pce.loc['2015Q1']`,
  - plot both,
  - compute `APC = pce / dpi`,
  - plot APC and saving rate, likely with twin y-axis.
- Complete Task 5.2:
  - compute log changes:
    - `dlog_c = np.log(data['pce']).diff()`,
    - `dlog_y = np.log(data['dpi']).diff()`.
  - drop missing rows.
  - estimate by NumPy:
    - `X = np.column_stack([np.ones(n), dlog_y])`,
    - `beta_hat = np.linalg.lstsq(X, dlog_c, rcond=None)[0]`,
    - residual variance and standard error for confidence interval.
- Complete Task 5.3:
  - exclude `2020Q1` through `2021Q4`.
  - re-run the same OLS helper.
  - explain that COVID and stimulus/lockdown periods are special because
    income, consumption opportunities, transfers, and saving behavior moved
    abnormally.
- Complete Task 5.4:
  - scatter `Delta log Y_d` vs `Delta log C`.
  - overlay fitted line from full-sample OLS.
  - explain descriptive comovement, not structural MPC causality.

### Part 6 - Economic Take-Away

Assignment task:

- Write 250-400 words.
- Must mention:
  - one two-period model number,
  - one mortgage cash-flow result from group profile,
  - one data-section `beta_hat`,
  - one limitation.

Current assignment implementation:

- Markdown cell 70 is a placeholder.
- Code cell 71 is a placeholder.

Primary course references:

- `week03_consumption_handin_task.pdf`, Part 6.
- Use the actual outputs from assignment Parts 2, 3, and 5.

Implementation mapping:

| Required narrative component | Source in assignment notebook | Course reference |
| --- | --- | --- |
| Two-period model number | Task 2.2 or 2.3 output | Lecture 3 pages 10-21; L3 cell 20 |
| Mortgage cash-flow result | Task 3.4 output after correction | Lecture 3 pages 5-6, 24-27, 34, 37 |
| Data-section `beta_hat` | Task 5.2 or 5.3 output after implementation | Week 3 PDF Part 5; L3 cells 12-15 for data |
| Limitation | Own interpretation | Lecture 3 pages 34-36 for frictions; Week 3 PDF Part 6 |

Current issue:

- Do not write Part 6 until Parts 3 and 5 are corrected. Otherwise the narrative
  will cite numbers that are either missing or based on inconsistent code.

## Function-by-Function Map

### `Line` and `plot`

Current assignment:

- `Line` dataclass and `plot(...)` are defined in code cell 4.

Course analogue:

- No exact course helper.
- Course notebooks use direct `fig = plt.figure(...)`, `ax = fig.add_subplot(...)`,
  `ax.plot(...)`, labels, legends, and `plt.show()`.

Recommendation:

- Keep the helper if it makes plots shorter.
- Do not cite it as course implementation.
- For twin-axis plots, compare with:
  - `L2_business_housing_investment.ipynb`, cell 13,
  - `L6_as_ad_supply_shocks.ipynb`, cell 17,
  but those are plotting patterns, not consumption references.

### `consumption`

Current assignment:

```python
def consumption(Y_d, b=0.75, C_hat=200):
    return Y_d * b + C_hat
```

Course analogue:

- `L3_consumption (1).ipynb`, cell 4:
  - `C = par['a'] + par['b'] * Yd`.

Recommendation:

- Good implementation.
- In the written answer, refer to the function as the Keynesian consumption
  function and connect it to APC:
  - `APC = C / Y_d = b + C_bar / Y_d`.

### `APC` and `MPC`

Current assignment:

```python
def APC(C, Y_d):
    return C / Y_d

def MPC(b=0.75):
    return b
```

Course analogue:

- `L3_consumption (1).ipynb`, cell 6:
  - `APC = C / Yd`.
- Lecture 3 page 7:
  - MPC is `b`.

Recommendation:

- Correct.
- If producing table output, include reasonable rounding for readability.

### `H_1`

Current assignment:

```python
def H_1(Y_1_d, Y_2_d, r=R_B):
    return Y_1_d + Y_2_d / (1 + r)
```

Course analogue:

- `L3_consumption (1).ipynb`, cell 20:
  - human wealth appears inside total wealth.
- Lecture 3 pages 11-12:
  - period budgets and intertemporal budget constraint.

Recommendation:

- Correct.
- In prose, distinguish:
  - human wealth `H1`,
  - total wealth `W = V1 + H1`.

### `thetaFunc`

Current assignment:

```python
def thetaFunc(r=R_B, phi=PHI_B, sigma=SIGMA_B):
    return 1 / (1 + (1 + phi)**(-sigma) * (1 + r)**(sigma - 1))
```

Course analogue:

- `L3_consumption (1).ipynb`, cell 20.
- Lecture 3 pages 19-20.

Recommendation:

- Correct formula.
- For Task 2.4, `thetaFunc` can handle `sigma = 1.0`; only the utility
  function `u` has the log-utility special case issue.

### `allocation`

Current assignment:

- Returns `c1`, `c2`, `w`, and `s1`.
- Supports `w_fixed` for Task 2.3 decomposition.

Course analogue:

- No named function, but L3 notebook cell 20 has the full calculation.

Recommendation:

- Good abstraction.
- For `w_fixed`, the code correctly sets `h1 = w_fixed - V_1`, so
  `C1 = theta * w_fixed`.
- Ensure the written explanation says fixed total wealth.

### `u`, `u_prime`, `U`

Current assignment:

- Implements CRRA utility and lifetime utility.
- Raises an error for `sigma = 1` in `u`.

Course analogue:

- `L3_consumption (1).ipynb`, cell 20:
  - uses `power = (sigma - 1) / sigma`,
  - computes `U_grid`.

Recommendation:

- Good for baseline `sigma = 0.8`.
- If ever evaluating `sigma = 1`, use log utility. Task 2.5 baseline uses
  `sigma = 0.8`, so this is not a blocker.
- Report the grid-search result as the assignment asks.

### `tenerary_search`

Current assignment:

- Recursive search over `C1`.

Course analogue:

- None.

Recommendation:

- This is extra and misspelled; it can stay, but it should not replace the
  grid-search answer because the prompt specifically asks for a fine grid.
- If keeping it, call it "ternary search" in comments/output.

### `grid_search`

Current assignment:

```python
def grid_search(max_c, min_c=1e-8, eps=0.05):
    grid_c1 = np.arange(min_c, max_c, eps)
    return grid_c1[np.argmax(U(grid_c1))]
```

Course analogue:

- `L3_consumption (1).ipynb`, cell 20:
  - `C1_grid = np.linspace(...)`,
  - `np.argmax(U_grid)`.

Recommendation:

- Good match to course implementation.
- `np.linspace` gives more direct control over endpoint inclusion; `np.arange`
  is acceptable if the error is within 0.05.

### `effective_monthly_rate`

Current assignment:

```python
def effective_monthly_rate(i):
    return (1 + i)**(1/12) - 1
```

Course analogue:

- None.

Recommendation:

- Acceptable if the stated assumption is effective annual rate.
- Keep the convention consistent in the mortgage payment, PV loss, and written
  explanation.

### `monthly_mortgage_payment`

Current assignment:

```python
def monthly_mortgage_payment(D, M, i):
    r = effective_monthly_rate(i)
    N = M * 12
    return D * r / (1 - (1 + r)**(-N))
```

Course analogue:

- None.

Recommendation:

- Correct annuity-payment structure.
- Report both monthly and annual payment increases.
- Use the profile's own `D`, `M`, `initial rate`, and `new rate` in Task 3.4.

### `annuity`

Current assignment:

```python
def annuity(N, r, start=0):
    i = np.arange(N)
    pv_list = ((1 / (1 + r))**i)
    return np.sum(pv_list[start:])
```

Course analogue:

- Week 3 PDF Part 4:
  - `A(N, r) = sum_{j=0}^{N-1} (1+r)^(-j)`.
- `L3_consumption (1).ipynb`, cell 26:
  - closed-form `theta_N`.

Recommendation:

- Good reusable helper.
- For assignment Part 4, use `theta_N = 1 / annuity(N, r)`.
- For Task 3.2, use `N = 36` if discounting monthly cash-flow losses over 3
  years.

### `ucon_consumption_delta`

Current assignment:

```python
def ucon_consumption_delta(W_delta, V_delta):
    return (W_delta + V_delta) / annuity(30, 0.03)
```

Course analogue:

- PIH annuity rule in Lecture 3 pages 24-27 and L3 cell 26.

Recommendation:

- Rename conceptually to PIH/unconstrained annual consumption change.
- If `W_delta` is negative, output is negative change. If reporting a cut as a
  positive number, use `-W_delta / annuity(...)`.
- Add horizon and rate as parameters instead of hardcoding `30` and `0.03`,
  because Task 3.4 changes horizon.

### `con_consumption_delta`

Current assignment:

```python
def con_consumption_delta(MPC, annual_cost):
    return MPC * annual_cost
```

Course analogue:

- Borrowing-constraint/current-income dependence in Lecture 3 pages 34 and 37.

Recommendation:

- Good, but sign convention must be explicit.
- If `annual_cost` is a positive payment increase and cuts are positive:
  `constrained_cut = MPC * annual_cost`.
- If `annual_cost` is negative change in disposable cash flow:
  `delta_C = MPC * annual_cost`.

### `fetch_fred`

Current assignment:

- Defined in code cell 58.
- Similar to L3 notebook cell 12.

Course analogue:

- `L3_consumption (1).ipynb`, cell 12.
- `L4_monetary_policy_aggregate_demand.ipynb`, cell 35.
- `lecture_06_notebook_utils.py`, `fetch_fred_series(...)`.

Recommendation:

- Good base implementation.
- Add fallback that actually exists locally, or supply API key.
- Drop missing values after combining series.
- For quarterly data, use one consistent quarterly index convention.

### `load_consumption_data`

Current assignment:

- Reads local CSV if API key is empty.
- Fetches FRED otherwise.
- Converts monthly data to quarterly by `.resample('QE').mean().dropna()`.

Course analogue:

- L3 cell 12 fallback structure.
- Week 1 solution cell 7 quarterly resampling.

Recommendation:

- The shape is good.
- The fallback file is missing.
- If using `.resample('QE')`, ensure the resulting index works with the
  2015Q1 base lookup and the 2020Q1-2021Q4 exclusion.
- If using pandas PeriodIndex, convert to quarters explicitly:
  - `data.index = data.index.to_period('Q')`
  - then reference `'2015Q1'`, `'2020Q1'`, etc.

## Exact References To Use By Assignment Part

Use this as a short checklist while writing explanations.

| Assignment part | Cite/use these course references | Avoid citing |
| --- | --- | --- |
| Part 1 | Lecture 3 PDF pages 7-9; L3 notebook cells 4 and 6; Week 3 PDF Part 1 | L1/L2 investment material |
| Part 2 | Lecture 3 PDF pages 10-21; L3 notebook cells 20-21; Week 3 PDF Part 2 | Mortgage sections for the closed-form CRRA model |
| Part 3 | Lecture 3 PDF pages 5-6, 24-27, 34, 37; L3 notebook cells 26-27 and 33-34; Week 3 PDF Part 3 | L2 housing q code; it is about housing investment, not household mortgage cash-flow consumption |
| Part 4 | Lecture 3 PDF pages 24-28; L3 notebook cells 26-27; Week 3 PDF Part 4; `week_3/notes.ipynb` cells 4-5 | AS-AD or monetary policy notebooks |
| Part 5 | Week 3 PDF Part 5; L3 notebook cells 12, 13, 15; Week 1 solution cell 7; L4 notebook cell 35 | HP-filter code unless discussing Week 1 only |
| Part 6 | Week 3 PDF Part 6; actual outputs from Parts 2, 3, and 5 | Any result not produced by the final clean-run notebook |

## What To Copy Or Adapt

### Strong candidates to adapt directly

- From `L3_consumption (1).ipynb`, cell 20:
  - closed-form wealth/theta/consumption calculation;
  - grid-search verification pattern.
- From `L3_consumption (1).ipynb`, cell 26:
  - annuity/temporary-vs-permanent response structure.
- From `L3_consumption (1).ipynb`, cells 33-34:
  - constrained vs unconstrained consumption intuition.
- From `L3_consumption (1).ipynb`, cells 12-15:
  - FRED fetch and index/APC plotting style.
- From `week01_solution_bcstats.ipynb`, cell 7:
  - data resampling and merging pattern.
- From `L4_monetary_policy_aggregate_demand.ipynb`, cell 35:
  - clean FRED downloader structure.

### Things to use only as conceptual reference

- `L1_investment_asset_prices.ipynb`, cell 11:
  - present value declines with horizon and interest rate.
  - Useful for explaining mortgage cash-flow PV, but not direct assignment code.
- Lecture 3 PDF pages 5-6:
  - mortgage contract motivation.
  - No code to copy.

### Things not to use for this assignment

- `L2_business_housing_investment.ipynb`:
  - Housing q and construction are not the same as household mortgage cash-flow
    exposure.
- `denmark_housing_q_data.py`:
  - The FRED caching pattern is fine, but the data and economics are not Part 3
    consumption references.
- `L5_phillips_curve.ipynb` and `lecture_05_notebook_utils.py`:
  - Phillips curve/Eurostat code is unrelated.
- `L6_as_ad_supply_shocks.ipynb` AS-AD simulations:
  - Not relevant except for fallback data style.

## Clean-Run Risks

Before submission, these are the risks most likely to break grading:

1. Missing `week03_fred_consumption.csv`.
   - Current Part 5 loader expects it when `FRED_API_KEY = ''`.
   - The file is not present in `week_3/`.
2. Blank code cells from Task 3.5 onward.
   - Blank cells do not always crash, but missing outputs and placeholder text
     fail the assignment requirements.
3. Task 2.4 wrong plot grid and wrong sigma value.
4. Task 3.4 inconsistent mortgage-profile calculations.
5. Part 6 cannot be valid until Part 5 produces a `beta_hat`.

## Suggested Implementation Order

Follow this order to make the notebook coherent:

1. Fix Task 2.2 text and Task 2.4 code/explanation.
2. Fix Task 3.2 payment-count convention and define a clear sign convention.
3. Refactor Part 3 helpers so they return either positive cuts or negative
   consumption changes consistently.
4. Fix Task 3.4 to use the profile's own monthly payment increase and PV loss.
5. Implement Task 3.5 with a grid over constrained MPC.
6. Implement Part 4 using the existing `annuity` function and L3 cell 26 logic.
7. Make Part 5 data loading clean-run:
   - add the CSV,
   - or use a FRED key,
   - or embed a fallback dataset.
8. Implement Part 5 plotting, OLS, COVID exclusion, and scatter plot.
9. Write Part 6 only after all numbers are final.

## Minimal Implementation Blueprints

These are not full replacements for the notebook, but they show how to align
with the course implementation.

### Part 2.4 blueprint

```python
r_grid = np.linspace(0.0, 0.10, 100)
sigma_values = [0.5, 1.0, 1.5]

lines = []
for sigma in sigma_values:
    c1_values = np.array([allocation(r=r, sigma=sigma)[0] for r in r_grid])
    lines.append(Line(label=f"sigma = {sigma}", xx=r_grid, yy=c1_values))

plot(
    lines,
    "Current consumption as a function of the real interest rate",
    "Real interest rate r",
    "Current consumption C1",
    show_legend=True,
)
```

### Part 3.5 blueprint

Use positive cuts:

```python
mpc_grid = np.linspace(0.0, 1.0, 1001)
pih_cut = pv_loss_profile / annuity(horizon_profile, 0.03)
constrained_cuts = mpc_grid * annual_payment_increase_profile
m_star = mpc_grid[np.argmin(np.abs(constrained_cuts - pih_cut))]
```

### Part 4 blueprint

```python
def theta_N(N, r):
    return 1 / annuity(N, r)

N_grid = np.arange(1, 61)
theta_values = np.array([theta_N(N, 0.03) for N in N_grid])
long_limit = 0.03 / 1.03

horizons = [5, 30, 60]
shock = 5000
rows = []
for N in horizons:
    temp = shock * theta_N(N, 0.03)
    perm = shock
    agg = 0.35 * 0.9 * shock + 0.65 * temp
    rows.append({
        "N": N,
        "temporary_response": temp,
        "permanent_response": perm,
        "aggregate_temporary_response": agg,
    })
pd.DataFrame(rows)
```

### Part 5 OLS blueprint

```python
reg = pd.DataFrame({
    "dlog_c": np.log(data["pce"]).diff(),
    "dlog_y": np.log(data["dpi"]).diff(),
}).dropna()

def ols_numpy(frame):
    y = frame["dlog_c"].to_numpy()
    x = frame["dlog_y"].to_numpy()
    X = np.column_stack([np.ones(len(x)), x])
    coef = np.linalg.lstsq(X, y, rcond=None)[0]
    resid = y - X @ coef
    n, k = X.shape
    sigma2 = (resid @ resid) / (n - k)
    cov = sigma2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    beta = coef[1]
    beta_se = se[1]
    ci = (beta - 1.96 * beta_se, beta + 1.96 * beta_se)
    return coef, se, ci
```

For the COVID exclusion:

```python
reg_no_covid = reg.loc[
    ~((reg.index >= "2020Q1") & (reg.index <= "2021Q4"))
]
```

This requires `reg.index` to be a quarterly `PeriodIndex`. If it is a
DatetimeIndex, use date bounds such as:

```python
reg_no_covid = reg.loc[
    ~((reg.index >= "2020-01-01") & (reg.index <= "2021-12-31"))
]
```

## Final Reference Hierarchy

When deciding what to mention in explanations, use this hierarchy:

1. Assignment specification:
   - `week03_consumption_handin_task.pdf`.
2. Lecture 3 theory slides:
   - `lecture_03_ch16 (1).pdf`.
3. Lecture 3 implementation:
   - `L3_consumption (1).ipynb`.
4. Supporting data-code patterns:
   - `week01_solution_bcstats.ipynb`,
   - `L4_monetary_policy_aggregate_demand.ipynb`,
   - `lecture_06_notebook_utils.py`.
5. General discounting intuition:
   - `L1_investment_asset_prices.ipynb`.

Everything else in `course_material/` is either outside the Week 3 assignment
scope or useful only as a general coding example.

