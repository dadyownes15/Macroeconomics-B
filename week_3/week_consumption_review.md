# Week 3 Consumption Notebook Review

This is a review of `week_consumption_XX.ipynb` as it currently stands. The most important issues are clean-run blockers, unit/sign mistakes in the mortgage section, and a few conceptual misunderstandings in section 2.

## Clean-Run Blockers

- The notebook still contains empty tasks from Task 3.5 onward. These need to be completed before submission.
- The notebook currently fails in section 5 because `week03_fred_consumption.csv` is not present in `week_3/`, and `FRED_API_KEY` is empty. A submitted notebook must run from a clean kernel without errors.
- Several markdown cells still contain placeholders such as `_Write your explanation here._`.

## Task-Specific Issues

### Task 2.2

Your code output says:

```text
S1 = -24.6305
```

but your written answer says:

```text
S1 = -88.1842
```

The conclusion is correct: since `S1 < 0`, the household borrows in period 1. The number in the text should be updated to match the code output.

### Task 2.3

Your numerical decomposition is mostly fine:

```text
Total change in C1:          -4.8092
Fixed-wealth tilt component:  1.1059
Remaining wealth effect:     -5.9150
```

The wording should be tightened:

- Use **real interest rate**, not "rental rate".
- Say **current consumption C1**, not "total consumption".
- "Holding wealth fixed" means keeping total wealth `W = V1 + H1` fixed at the baseline value. It does not mean holding the "change in human wealth" fixed.

### Task 2.4

The plot is not doing what the task asks.

Current issue:

```python
r_l = [0, 0.1]
sigma_l = [0.5, 0.1, 1.5]
```

Problems:

- `r_l` only has two points, so the plot is just a straight line between `r = 0` and `r = 0.1`.
- The assignment asks for `sigma = 0.5, 1.0, 1.5`, not `0.5, 0.1, 1.5`.

Use something like:

```python
r_l = np.linspace(0, 0.10, 100)
sigma_l = [0.5, 1.0, 1.5]
```

Conceptually, `sigma` is the intertemporal elasticity of substitution in this assignment. A larger `sigma` means the household is more willing to move consumption between periods when the interest rate changes.

### Task 3.1

The monthly payment calculation is fine under your effective-monthly-rate convention, but the task asks for both the monthly and annual payment increase.

You have the monthly increase:

```text
Monthly increase = 4029.44 DKK
```

You should also report:

```text
Annual increase = 12 * 4029.44 = 48353.25 DKK
```

Also use "mortgage payment", not "downpayment". A down payment is the initial payment made when buying a house.

### Task 3.2

The PDF is shorter here, but the notebook is the more precise coding specification. Since Task 3.1 first computes a monthly mortgage payment increase, the most precise interpretation is to value 36 monthly cash-flow losses and discount them with the monthly real rate implied by 3 percent annually.

You currently write:

```python
ann = annuity(35, effective_monthly_rate(i=0.03), start=1)
```

This does not represent three years of monthly payments. Three years is `36` monthly payments.

Given the assignment's annuity formula:

```text
A(N, r) = sum_{j=0}^{N-1} (1+r)^(-j)
```

the direct implementation should be:

```python
ann = annuity(36, effective_monthly_rate(0.03))
pv_total_loss = ann * monthly_loss
```

With your payment numbers, this gives roughly:

```text
PV loss = 138985.06 DKK
```

not `131259.02`.

An annual approximation would use `annual_payment_increase * annuity(3, 0.03)`, which gives a similar but not identical number. For this notebook, use the monthly version because it is more precise and matches the monthly mortgage-payment calculation.

### Task 3.3

Your logic is mostly right, but the signs should be made clearer.

There are two clean conventions:

1. Report **consumption cuts as positive numbers**.
2. Report **changes in consumption as negative numbers**.

Do not mix the two.

If reporting cuts as positive numbers:

```python
pih_cut = pv_total_loss / annuity(30, 0.03)
constrained_cut = 0.9 * annual_payment_increase
```

If reporting changes in consumption:

```python
pih_delta_c = -pv_total_loss / annuity(30, 0.03)
constrained_delta_c = -0.9 * annual_payment_increase
```

The economic explanation should be: the constrained household cuts current consumption almost one-for-one with the current annual cash-flow loss, while the PIH household spreads the present-value loss over the remaining horizon.

### Task 3.4

There are several hard mistakes here.

Your written profile says:

```text
Initial rate = 1.5%
New rate     = 5.0%
```

but the code uses:

```python
R_init = 0.04
R_n = 0.045
```

The code and table must match.

You also compute the profile PIH loss using the old baseline variable:

```python
pv_total_loss = ann * monthly_loss
```

This should use the profile's own monthly cost change:

```python
pv_total_loss_profile = ann * monthly_cost_change
```

The sign is also reversed here:

```python
delta_c_ucon = ucon_consumption_delta(W_delta=pv_total_loss, V_delta=0)
```

If `pv_total_loss` is a loss, the wealth change is negative:

```python
delta_c_ucon = -pv_total_loss_profile / annuity(horizon, 0.03)
```

The baseline comparison is also not valid:

```python
delta_c_ucon_b = allocation(r=0.04)[0] - allocation(r=0.045)[0]
```

This uses the two-period model from section 2, not the mortgage cash-flow model from section 3.

Finally, this is not an MPC:

```python
u_prime(np.array(c1))
```

`u_prime(c1)` is marginal utility, not marginal propensity to consume. For the baseline constrained household, use `MPC = 0.9`.

## Potential Conceptual Misconceptions

### 1. Saving in the Two-Period Model

`S1` is period-1 saving:

```text
S1 = V1 + Y1d - C1
```

It is not total lifetime saving. If `S1 < 0`, the household borrows in period 1. This can happen even though lifetime resources are sufficient, because the household wants to smooth consumption across periods.

### 2. Human Wealth Versus Total Wealth

Human wealth is:

```text
H1 = Y1d + Y2d / (1+r)
```

Total wealth is:

```text
W = V1 + H1
```

When `r` rises, the present value of future income `Y2d / (1+r)` falls, so human wealth falls. That is the negative wealth effect.

### 3. Fixed-Wealth Decomposition

In Task 2.3, the fixed-wealth calculation is not asking "what happens when human wealth is unchanged". It asks: what happens to `C1` when the interest rate changes but total wealth `W` is artificially held fixed?

That isolates the intertemporal tilt part of the response. The remaining difference is the wealth effect.

### 4. Why the Tilt Component Can Be Positive

The Euler equation implies:

```text
C2 / C1 = ((1+r) / (1+phi))^sigma
```

When `r` changes, the household changes the relative allocation between current and future consumption. With `sigma = 0.8`, the fixed-wealth component in your calculation is positive: `C1` rises by about `1.1059`.

So do not explain this only as "the marginal utility of consumption increases". The sign depends on the intertemporal elasticity of substitution. In this case, the positive fixed-wealth effect is smaller than the negative wealth effect, so total `C1` falls.

### 5. Mortgage Cash-Flow Loss Is a Stream, Not One Period

In Task 3.2, the payment increase lasts for three years. That means you need the present value of a stream of monthly losses, not just one annual loss.

The structure is:

```text
monthly payment increase
-> present value of 36 monthly increases
-> annual consumption cut spread over 30 years for PIH household
```

### 6. PIH Household Versus Constrained Household

The PIH household reacts to the present value of the loss:

```text
annual PIH cut = PV loss / A(30, 0.03)
```

The constrained household reacts to the current cash-flow hit:

```text
annual constrained cut = MPC * annual payment increase
```

This is why the constrained response is much larger. It is not because the cost is "multiplied by the MPC" in a deep sense; it is because constrained households cannot smooth the shock over the full horizon.

### 7. Marginal Utility Is Not MPC

`u_prime(C)` measures marginal utility:

```text
u'(C) = C^(-1/sigma)
```

MPC measures the consumption response to extra income:

```text
MPC = Delta C / Delta income
```

These are different objects. Do not use `u_prime(c1)` where the assignment asks for an MPC.

## Suggested Priority Order

1. Fix the clean-run error in section 5 or obtain the CSV.
2. Finish empty tasks from 3.5 onward.
3. Correct Task 2.2's written saving number.
4. Redo Task 2.4 with a real `r` grid and the correct `sigma` values.
5. Redo Task 3.2-3.4 with consistent monthly/annual units and consistent signs.
6. Rewrite the explanations in Task 2.3 and Task 3.3 using the concepts above.
