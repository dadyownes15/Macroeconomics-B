# Week 6 Hand-in Overview: Open Economy, Exchange Rates, and the Peg

*Welcome to Week 6! This guide combines the pedagogical intuition of open-economy macroeconomics with the full mathematical rigor required to actually solve the model and your Python notebook. We will explore how a small open economy (like Denmark) behaves when it pegs its currency to a large neighbor (the Euro).*

## Step 1: Capital Mobility and Uncovered Interest Parity (UIP)

### The Economic Intuition
If investors can freely move capital across borders, they will seek the highest return. If the Danish interest rate is higher than the European one, capital flows into Denmark. This drives up the value of the Krone today until investors *expect* it to depreciate in the future, exactly offsetting the higher interest rate. 

### The Math
Let's start from the exact no-arbitrage condition. An investor compares the payoff of investing 1 unit of domestic currency at home vs. abroad:
1. **Domestic bond payoff**: $1 + i_t$
2. **Foreign bond payoff**: Convert to foreign currency ($\frac{1}{E_t}$), earn foreign interest ($1+i_t^f$), and convert back at the expected future exchange rate ($E_{t+1}^e$).

Equating these gives the **Exact UIP**:
$$1 + i_t = (1 + i_t^f)\frac{E_{t+1}^e}{E_t}$$

To make this easier to work with, we take the natural log of both sides:
$$\ln(1 + i_t) = \ln(1 + i_t^f) + \ln E_{t+1}^e - \ln E_t$$

Using the approximation $\ln(1 + x) \approx x$ for small $x$, and defining $e_t \equiv \ln E_t$, we get the **Log-Linear UIP**:
$$i_t \approx i_t^f + \Delta e_{t+1}^e$$
*(Where $\Delta e_{t+1}^e \equiv e_{t+1}^e - e_t$ is the expected nominal depreciation).*

### The Trilemma and Credible Pegs
A country cannot simultaneously have Free Capital Mobility, a Fixed Exchange Rate, and Independent Monetary Policy. 

**What is a Credible Peg?**
A **credible peg** is a fixed exchange rate regime where financial markets fully believe the central bank will maintain the peg indefinitely. 
Because the peg is 100% credible, markets expect no future devaluation, meaning the expected future exchange rate equals the current pegged rate ($e^e_{t+1} = e_t$). Thus, the expected nominal depreciation is exactly zero:
$$\Delta e_{t+1}^e = 0$$

Plugging this into our log-linear UIP condition:
$$i_t \approx i_t^f + 0 \implies i_t = i_t^f$$
**Mathematical consequence**: Under a perfectly credible peg, the domestic interest rate must precisely match the foreign interest rate. The central bank completely surrenders its monetary policy autonomy. Denmark must set its interest rate equal to the ECB's rate.

**What happens if a Peg is NOT Credible? (Speculative Pressure)**
If markets doubt the peg (e.g., they expect a devaluation because the domestic economy is weak), they expect the currency to depreciate:
$$\Delta e^e_{t+1} > 0$$
To defend the peg and prevent capital outflows, UIP tells us the central bank must hike the domestic interest rate:
$$i_t \approx i_t^f + \Delta e^e_{t+1} > i_t^f$$
This difference ($i_t - i_t^f > 0$) is the exchange rate risk premium. High interest rates depress the domestic economy further, which can force the central bank to abandon the peg, making the speculation a self-fulfilling prophecy.

---

## Step 2: Real Exchange Rates and Competitiveness

### The Economic Intuition
Because Denmark cannot change its nominal exchange rate ($e_t$) to boost its economy, it must rely on the **real exchange rate**. The real exchange rate measures whether our goods are cheap or expensive compared to foreign goods. A higher real exchange rate means foreign goods are more expensive, so we gain price competitiveness.

### The Math
The real exchange rate in levels compares foreign prices in domestic currency to domestic prices:
$$E^r_t = \frac{E_t P_t^f}{P_t}$$

Take logs to get the working definition:
$$e^r_t = e_t + p_t^f - p_t$$

Now, take the first difference (subtracting the lagged equation) to see how it evolves over time:
$$\Delta e^r_t = \Delta e_t + \pi_t^f - \pi_t$$

Under a fixed exchange rate, the nominal rate doesn't change ($\Delta e_t = 0$). Therefore:
$$\Delta e^r_t = \pi_t^f - \pi_t$$
**Mathematical consequence**: Competitiveness ($\Delta e^r_t$) can only improve if domestic inflation ($\pi_t$) is lower than foreign inflation ($\pi_t^f$).

---

## Step 3: Trade Dynamics — The Marshall-Lerner Condition & J-Curve

### The Economic Intuition: The Tug-of-War
Imagine the real exchange rate depreciates (our goods become cheaper). This creates a tug-of-war on our trade balance (Net Exports):
1. **The Price Effect (Bad news first):** The imports we *already* buy suddenly cost more in our own currency. If we still import the same amount of oil, our import bill goes up. This hurts Net Exports.
2. **The Volume Effect (Good news later):** Because our goods are cheaper, foreigners will eventually buy *more* of our exports, and we will buy *fewer* foreign imports, switching to domestic goods instead. This helps Net Exports.

The **Marshall-Lerner Condition** is the mathematical rule that tells us when the good news (Volume Effect) is strong enough to beat the bad news (Price Effect).

### The Math (Derivation)
Write Net Exports (NX) measured in domestic goods:
$$NX = X(E^r) - E^r M(E^r)$$

Differentiate with respect to $E^r$:
$$\frac{\partial NX}{\partial E^r} = X'(E^r) - M(E^r) - E^r M'(E^r)$$

Assume we start from balanced trade, where $X_0 = E_0^r M_0$.
Define the absolute price elasticities (how sensitive volumes are to price changes) of exports and imports:
$$\varepsilon_X \equiv \frac{E_0^r X'(E_0^r)}{X_0} > 0, \quad \varepsilon_M \equiv -\frac{E_0^r M'(E_0^r)}{M_0} > 0$$

Multiply the derivative equation by $\frac{E_0^r}{X_0}$ and substitute the elasticities:
$$\frac{E_0^r}{X_0} \frac{\partial NX}{\partial E^r} = \varepsilon_X + \varepsilon_M - 1$$

**Mathematical consequence (Marshall-Lerner Condition)**: For a real depreciation to actually improve the trade balance ($\frac{\partial NX}{\partial E^r} > 0$), the elasticities must be large enough:
$$\varepsilon_X + \varepsilon_M > 1$$

### The J-Curve Explained
The **J-Curve** describes *how* the trade balance reacts over time, forming the shape of a "J":
* **The Short Run (The dip of the 'J')**: Right after our goods become cheaper, trade volumes are "sticky". People are locked into long-term import contracts, and it takes time for foreigners to discover our cheaper exports. Because volumes barely change initially ($\varepsilon_X \approx 0, \varepsilon_M \approx 0$), the bad **Price Effect** dominates. The trade balance initially *worsens* ($\varepsilon_X + \varepsilon_M - 1 < 0$).
* **The Long Run (The upward swing of the 'J')**: After a few quarters, contracts expire and habits change. Foreigners start buying our exports, and we stop buying expensive imports. The elasticities grow ($\varepsilon_X + \varepsilon_M > 1$), the good **Volume Effect** takes over, and the trade balance sharply *improves*, ending up much higher than where it started.

---

## Step 4: The Fixed-Rate AS-AD Model (Explained)

Before diving into the equations, let's define what **AS** and **AD** actually mean:
* **AD (Aggregate Demand)**: This curve describes the relationship between inflation and the total amount of goods people want to buy. In a fixed-exchange-rate open economy, if our inflation is high, our goods become relatively expensive to foreigners. We lose competitiveness, exports fall, and total demand drops.
* **AS (Aggregate Supply)**: This curve describes how producers set their prices based on how much they are producing. If demand is high and the economy is booming, it is hard to find workers, wages go up, and businesses are forced to raise prices, leading to higher inflation.

**Crucially, AD and AS work together.** You cannot determine prices from AS alone, nor output from AD alone. Instead, they form a simultaneous system. Their *intersection* jointly determines both the equilibrium output gap ($\widehat{y}_t$) and the inflation gap ($\widehat{\pi}_t$) for the economy.

Let's assemble the full model using gaps. We define the output gap as $\widehat{y}_t = y_t - \bar{y}$ and the inflation gap as $\widehat{\pi}_t = \pi_t - \pi_t^f$ (how much higher our inflation is compared to foreign inflation).

### 1. Aggregate Demand (AD)
*Intuition*: In a fixed exchange rate economy, our central bank can't lower interest rates to boost demand. Therefore, demand is driven primarily by **competitiveness** (the real exchange rate, $e_t^r$). If our goods are cheap relative to foreign goods, our exports boom, and demand goes up.
We start with the preliminary open-economy AD equation:
$$\widehat{y}_t = \beta_1 e_t^r - \beta_2(r_t - \bar{r}^f) + \tilde{z}_t$$
Substitute the real exchange rate identity ($e^r_t = e^r_{t-1} + \Delta e_t + \pi_t^f - \pi_t$) and impose the peg ($\Delta e_t = 0$ and $r_t \approx r_t^f$):
**Final AD**: $$\widehat{y}_t = \beta_1(e_{t-1}^r - \widehat{\pi}_t) + z_t$$
*(Where $z_t$ represents a demand shock, like a sudden increase in government spending).*

### 2. Aggregate Supply (AS)
*Intuition*: This is often called the Phillips Curve. It says that if our economy is running too hot ($\widehat{y}_t > 0$), our inflation will rise above the foreign inflation rate. 
Because we are pegged, long-run inflation expectations are anchored to foreign expectations ($\pi_t^e = \pi_t^f$). 
**Final AS**: $$\widehat{\pi}_t = \gamma \widehat{y}_t + s_t$$
*(Where $\gamma$ tells us how sensitive inflation is to an economic boom, and $s_t$ is a supply shock, like an oil price spike).*

### 3. State Variable Update (RER)
**RER Update**: $$e^r_t = e^r_{t-1} - \widehat{\pi}_t$$
*(Note: the lecture uses $q$ for the real exchange rate gap, so $q_t = q_{t-1} - \widehat{\pi}_t$. Both notations mean the same thing).*

---

## Step 5: Solving the Model (Crucial for the Python Notebook)

To simulate the model in a `for` loop, you need to solve the AD and AS equations algebraically for $\widehat{y}_t$ and $\widehat{\pi}_t$ within a single period, given the inherited state $e_{t-1}^r$.

**1. Substitute AS into AD:**
$$\widehat{y}_t = \beta_1 e_{t-1}^r - \beta_1(\gamma \widehat{y}_t + s_t) + z_t$$

**2. Collect terms for $\widehat{y}_t$:**
$$(1 + \beta_1\gamma)\widehat{y}_t = \beta_1 e_{t-1}^r + z_t - \beta_1 s_t$$

**3. The Within-Period Solutions:**
These are the formulas you will code into the notebook:
$$\widehat{y}_t = \frac{\beta_1 e_{t-1}^r + z_t - \beta_1 s_t}{1 + \beta_1\gamma}$$
$$\widehat{\pi}_t = \frac{\gamma\beta_1 e_{t-1}^r + \gamma z_t + s_t}{1 + \beta_1\gamma}$$

### Stability and Convergence Root
Why does the economy naturally return to equilibrium? Look at the RER update equation without shocks ($z_t = s_t = 0$):
$$e^r_t = e^r_{t-1} - \widehat{\pi}_t = e^r_{t-1} - \frac{\gamma\beta_1}{1+\beta_1\gamma} e^r_{t-1}$$
$$e^r_t = \left( \frac{1}{1+\beta_1\gamma} \right) e^r_{t-1}$$
Because $\beta_1 > 0$ and $\gamma > 0$, the root $\frac{1}{1+\beta_1\gamma}$ is strictly between 0 and 1. The gap shrinks every period.

---

## Step 6: The "Competitiveness Hangover" (Fiscal Policy)

If the government enacts a temporary fiscal stimulus ($z_1 = 1$, then $z_t = 0$ for $t \ge 2$), what happens mathematically?
- **Period 1**: Output spikes ($\widehat{y}_1 > 0$), driving inflation up ($\widehat{\pi}_1 > 0$).
- **RER Update**: $e^r_1 = 0 - \widehat{\pi}_1 < 0$. The real exchange rate appreciates.
- **Period 2**: The stimulus ends ($z_2 = 0$). But we enter the period with $e^r_1 < 0$.
- **Result**: $\widehat{y}_2 = \frac{\beta_1 e^r_1}{1 + \beta_1\gamma} < 0$. 

The math proves that a temporary fiscal stimulus *must* result in a subsequent recession because the induced inflation permanently eroded competitiveness, shifting the AD curve to the left until a period of low inflation can repair it.

---

## Final Policy Memo Tip
When you write your 250-350 word memo, use the economic intuition to explain the mathematical outcomes:
- **UIP/Trilemma**: Why $i_t = i_t^f$ means no independent monetary policy.
- **RER Channel**: Why waiting out a recession relies on $\pi_t < \pi_t^f$ to gradually increase $e_t^r$.
- **Hangover**: Why fiscal stimulus ($z_t$) feels good today but drives $e_t^r$ down, causing pain tomorrow.
- **Speculative Attacks**: Why $\Delta e_{t+1}^e > 0$ forces $i_t$ up, hurting $\widehat{y}_t$ before a devaluation even occurs.
