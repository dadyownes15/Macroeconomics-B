# Week 6 Hand-in: Course Material Mapping

This document maps the specific tasks from the Week 6 hand-in assignment (`week06_open_economy_handin_task.pdf`) to the relevant sections and code snippets in the teacher's course materials. The goal is to base your solutions closely on the teacher's provided examples.

## Part 1: UIP, Credibility, and the Trilemma

**Assignment Task:** Derive the log-linear UIP equation, compute domestic nominal interest rates using exact and log-linear formulas under different devaluation scenarios, and explain the trilemma and devaluation premiums.

**Course Material References:**
- **File:** [L10_fixed_exchange_rates_practice.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L10_fixed_exchange_rates_practice.ipynb)
  - **Section:** `3. UIP and credibility`
  - **Code:** The `uip_rate(i_f, expected_depreciation)` function calculates the log-linear UIP.
  - **Code:** Look for the code block that constructs the `uip_table` using `pd.DataFrame`. This is the exact template needed for Part 4's Python simulation of the UIP table.
  - **Code:** Look for the plotting code using `ax.plot(100 * dep_grid, 100 * uip_rate(...))` for the expected depreciation plot.
  - **Theory:** The markdown text explains the anticipation effect of expected devaluation (how expectations of devaluation raise the domestic interest rate before the parity change), which directly answers the conceptual questions in Part 1.4.
- **File:** [L9_open_economy_exchange_rates_trade.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L9_open_economy_exchange_rates_trade.ipynb)
  - **Section:** `2. Uncovered interest parity` and `3. The trilemma: peg versus float`
  - **Code:** Contains a slightly different `uip_rate` helper function and simulations for floating vs. pegged regimes.

## Part 2: Real Exchange Rates, Competitiveness, and Marshall-Lerner

**Assignment Task:** Show the relationship for $\Delta e^r_t$, compute real exchange rate changes under a fixed nominal rate for different inflation scenarios, and compute the effect of real depreciation on net exports using the Marshall-Lerner condition and J-curve.

**Course Material References:**
- **File:** [L9_open_economy_exchange_rates_trade.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L9_open_economy_exchange_rates_trade.ipynb)
  - **Section:** `4. Real exchange rates and Danish inflation differentials`
  - **Theory:** Explains the identity $\Delta e^r_t = \Delta e_t + \pi^f_t - \pi_t$ and how inflation differentials drive real depreciation under a peg.
  - **Section:** `5. Marshall-Lerner and the J-curve`
  - **Theory:** Provides the formula $\varepsilon_X + \varepsilon_M > 1$ and the exact approximation $\frac{\Delta NX}{E^r M} \approx (\varepsilon_X + \varepsilon_M - 1) \frac{\Delta E^r}{E^r}$ used in the assignment.
  - **Code:** The `simulate_j_curve` function is the direct template for computing the short-run vs. long-run elasticity effects. It shows how the price effect is immediate but quantity response takes time.

## Part 3: The Fixed-Rate AS-AD Model

**Assignment Task:** Solve the AD and AS equations for deviations from long-run equilibrium, show stability conditions (convergence root), and analyze a temporary fiscal expansion and adverse supply shock.

**Course Material References:**
- **File:** [L9_open_economy_exchange_rates_trade.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L9_open_economy_exchange_rates_trade.ipynb)
  - **Section:** `6. Open-economy AD adjustment under a peg`
  - **Code:** The `simulate_fixed_rate_adjustment(T, beta1, gamma, z0)` function implements the exact system of equations (AD, AS, RER) given in Part 3.
    - $y_t = (\beta_1 e^r_{t-1} + z_t) / (1 + \beta_1 \gamma)$
    - $\pi_t = \gamma y_t$
    - $e^r_t = e^r_{t-1} - \pi_t$
  - **Theory:** The markdown cells explain the mechanism: a recession leads to lower inflation relative to foreign ($\pi < \pi^f$), causing a real depreciation ($e^r \uparrow$), which raises net exports and shifts AD right to recover. This logic is crucial for explaining the temporary fiscal expansion.
- **File:** [lecture_10_ch24.pdf](file:///Users/mikkeldahl/study/MacroB/course_material/lecture_10_ch24.pdf) (and [lecture_09_ch23.pdf](file:///Users/mikkeldahl/study/MacroB/course_material/lecture_09_ch23.pdf))
  - **Theory:** The lecture slides provide the analytical steps to solve the AD and AS equations and derive the stability condition $1/(1+\beta_1\gamma)$.

## Part 4: Python Simulation

**Assignment Task:** Complete the starter notebook (`week06_open_economy_student_start.ipynb`) to output the UIP table, Marshall-Lerner table, plot Danish/euro-area inflation differential and real-exchange-rate index, simulate AS-AD, compare convergence roots, and compare fixed-peg with closed-economy AS-AD.

**Course Material References:**
- **UIP Table & Plot:** Use the DataFrame and plotting logic from [L10_fixed_exchange_rates_practice.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L10_fixed_exchange_rates_practice.ipynb) (Section 3).
- **Marshall-Lerner & J-Curve:** Use the `simulate_j_curve` logic and tables from [L9_open_economy_exchange_rates_trade.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L9_open_economy_exchange_rates_trade.ipynb) (Section 5).
- **Inflation & Real Exchange Rate Plot:** Look at [L9_open_economy_exchange_rates_trade.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L9_open_economy_exchange_rates_trade.ipynb) (Section 4). It has helpers to calculate `yoy_inflation` and compute the real exchange rate accumulation.
- **AS-AD Simulation & Convergence:** Use `simulate_fixed_rate_adjustment` from [L9_open_economy_exchange_rates_trade.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L9_open_economy_exchange_rates_trade.ipynb) (Section 6). The formula for the convergence root $1/(1+\beta_1\gamma)$ is embedded in how the lag $e^r_{t-1}$ propagates. 
- **Closed-Economy Comparison:** Refer back to the earlier [L6_as_ad_supply_shocks.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L6_as_ad_supply_shocks.ipynb) (and `lecture_06_notebook_utils.py`) which implements the closed-economy AS-AD model `simulate_as_ad(T, a, gamma, ...)` to contrast the adjustment speeds.

## Part 5: Policy Memo

**Assignment Task:** Write a 250-350 word memo advising whether Denmark should use fiscal expansion, wait for relative-price adjustment, or devalue during a domestic recession. Must mention UIP/trilemma, real-exchange-rate adjustment, "competitiveness hangover", and why anticipated devaluation is contractionary.

**Course Material References:**
- **UIP and Trilemma:** [L9_open_economy_exchange_rates_trade.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L9_open_economy_exchange_rates_trade.ipynb) (Section 3) and [L10_fixed_exchange_rates_practice.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L10_fixed_exchange_rates_practice.ipynb) (Section 3).
- **Real-exchange-rate adjustment:** [L9_open_economy_exchange_rates_trade.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L9_open_economy_exchange_rates_trade.ipynb) (Section 8 Summary): Explains the key mechanism under a peg (recession $\to$ low inflation $\to$ real depreciation $\to$ recovery).
- **"Competitiveness hangover":** This refers to the aftermath of a fiscal stimulus under a peg. The stimulus raises inflation above the foreign rate, causing a real appreciation (loss of competitiveness). When the stimulus ends, the accumulated real appreciation acts as a drag on net exports, causing output to fall below potential. This exact mechanism can be observed by running the `simulate_fixed_rate_adjustment` function in [L9_open_economy_exchange_rates_trade.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L9_open_economy_exchange_rates_trade.ipynb) with a positive demand shock ($z_1 = 1$).
- **Anticipated devaluation is contractionary:** [L10_fixed_exchange_rates_practice.ipynb](file:///Users/mikkeldahl/study/MacroB/course_material/L10_fixed_exchange_rates_practice.ipynb) explains the "anticipation effect." Expecting a devaluation forces the central bank to raise domestic interest rates immediately (due to UIP and the trilemma) to defend the peg. Higher interest rates depress domestic demand before any devaluation even occurs.
