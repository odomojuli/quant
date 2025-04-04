# Black-Scholes Option Pricing Model

This repository contains Python code that implements the Black-Scholes Option Pricing model, which is widely used in finance to calculate the theoretical price of European call and put options. It also includes calculations for various "Greeks" that measure sensitivity to different factors like volatility, time decay, and interest rates.

## Functions Overview

### 1. **normal_pdf(x: float) -> float**
   - This function calculates the probability density function (PDF) of the standard normal distribution.
   - It is used to evaluate the likelihood of the stock price under a normal distribution.

### 2. **normal_cdf(x: float) -> float**
   - This function calculates the cumulative distribution function (CDF) of the standard normal distribution.
   - It returns the probability that a random variable from the normal distribution is less than or equal to `x`.

### 3. **d(j: int, S: float, K: float, r: float, v: float, T: float) -> float**
   - This helper function calculates the intermediate `d1` and `d2` terms used in the Black-Scholes formula for options pricing.
   - Parameters:
     - `j`: An integer (1 or 2) that determines whether we are calculating `d1` or `d2`.
     - `S`: Stock price.
     - `K`: Strike price.
     - `r`: Risk-free rate.
     - `v`: Volatility of the underlying asset.
     - `T`: Time to maturity (in years).
   
### 4. **Option Pricing Functions**
   These functions calculate the Black-Scholes price for various types of options and their associated Greeks.

   - **bs_call_option_delta(S, K, r, v, T) -> float**
     - Calculates the Delta for a European call option, which measures the rate of change of the option price with respect to changes in the underlying asset price.

   - **bs_put_option_delta(S, K, r, v, T) -> float**
     - Calculates the Delta for a European put option.

   - **bs_call_option_gamma(S, K, r, v, T) -> float**
     - Calculates the Gamma for a European call option, which measures the rate of change in Delta with respect to changes in the underlying asset price.

   - **bs_put_option_gamma(S, K, r, v, T) -> float**
     - Calculates the Gamma for a European put option.

   - **bs_call_option_vega(S, K, r, v, T) -> float**
     - Calculates the Vega for a European call option, which measures the sensitivity of the option price to changes in volatility.

   - **bs_put_option_vega(S, K, r, v, T) -> float**
     - Calculates the Vega for a European put option.

   - **bs_call_option_theta(S, K, r, v, T) -> float**
     - Calculates the Theta for a European call option, which measures the sensitivity of the option price to changes in time to expiration (time decay).

   - **bs_put_option_theta(S, K, r, v, T) -> float**
     - Calculates the Theta for a European put option.

   - **bs_call_option_rho(S, K, r, v, T) -> float**
     - Calculates the Rho for a European call option, which measures the sensitivity of the option price to changes in the risk-free interest rate.

   - **bs_put_option_rho(S, K, r, v, T) -> float**
     - Calculates the Rho for a European put option.

## Code Explanation

- **Parameters:**
  - `S`: Underlying asset price.
  - `K`: Strike price of the option.
  - `r`: Risk-free interest rate (annualized).
  - `v`: Volatility of the underlying asset (annualized).
  - `T`: Time to maturity of the option (in years).

- **Option Greeks Calculations:**
  - The Greek values are derived from the Black-Scholes formula. These values help in managing the risk of options portfolios and can give insights into the potential changes in the option price as factors change.

- **Output:**
  The script prints out the values of the Greeks (Delta, Gamma, Vega, Theta, and Rho) for both call and put options.

## Example Output

For the following inputs:
- Stock Price (`S`) = 100.0
- Strike Price (`K`) = 100.0
- Risk-Free Rate (`r`) = 0.05
- Volatility (`v`) = 0.2
- Time to Maturity (`T`) = 1.0

The output would be:

```
Underlying: 100.0
Strike: 100.0
Risk-Free Rate: 0.05
Volatility: 0.2
Maturity: 1.0

— CALL —
Delta: 0.539827837277027
Gamma: 0.018199351557815265
Vega: 39.84162407907291
Theta: -5.308953211970983
Rho: 7.719163289474353

— PUT —
Delta: -0.460172162722973
Gamma: 0.018199351557815265
Vega: 39.84162407907291
Theta: -5.308953211970983
Rho: -7.719163289474353
```

## Requirements

- Python 3.x
- `scipy` library (for `norm.cdf`)

You can install the required libraries using:

```
pip install scipy
```

## How to Run the Code

1. Clone this repository or copy the code into a Python file.
2. Install the required dependencies using `pip`.
3. Run the script.

```bash
python black_scholes.py
```

This `README.md` file should provide a clear explanation of the code and its functionalities. Let me know if you need any changes.

