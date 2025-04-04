import math
from scipy.stats import norm

def normal_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)

def normal_cdf(x: float) -> float:
    return norm.cdf(x)

def d(j: int, S: float, K: float, r: float, v: float, T: float) -> float:
    sqrt_T = math.sqrt(T)
    log_term = math.log(S / K)
    modifier = (r + (-1) ** (j - 1) * 0.5 * v * v)
    return (log_term + modifier * T) / (v * sqrt_T)

def bs_call_option_delta(S: float, K: float, r: float, v: float, T: float) -> float:
    return normal_cdf(d(1, S, K, r, v, T))

def bs_put_option_delta(S: float, K: float, r: float, v: float, T: float) -> float:
    return normal_cdf(d(1, S, K, r, v, T)) - 1

def bs_call_option_gamma(S: float, K: float, r: float, v: float, T: float) -> float:
    return normal_pdf(d(1, S, K, r, v, T)) / (S * v * math.sqrt(T))

bs_put_option_gamma = bs_call_option_gamma

def bs_call_option_vega(S: float, K: float, r: float, v: float, T: float) -> float:
    return S * normal_pdf(d(1, S, K, r, v, T)) * math.sqrt(T)

bs_put_option_vega = bs_call_option_vega

def bs_call_option_theta(S: float, K: float, r: float, v: float, T: float) -> float:
    d1 = d(1, S, K, r, v, T)
    d2 = d(2, S, K, r, v, T)
    term1 = -S * normal_pdf(d1) * v / (2 * math.sqrt(T))
    term2 = -r * K * math.exp(-r * T) * normal_cdf(d2)
    return term1 + term2

def bs_put_option_theta(S: float, K: float, r: float, v: float, T: float) -> float:
    d1 = d(1, S, K, r, v, T)
    d2 = d(2, S, K, r, v, T)
    term1 = -S * normal_pdf(d1) * v / (2 * math.sqrt(T))
    term2 = r * K * math.exp(-r * T) * normal_cdf(-d2)
    return term1 + term2

def bs_call_option_rho(S: float, K: float, r: float, v: float, T: float) -> float:
    return K * T * math.exp(-r * T) * normal_cdf(d(2, S, K, r, v, T))

def bs_put_option_rho(S: float, K: float, r: float, v: float, T: float) -> float:
    return -K * T * math.exp(-r * T) * normal_cdf(-d(2, S, K, r, v, T))

if __name__ == "__main__":
    S, K, r, v, T = 100.0, 100.0, 0.05, 0.2, 1.0

    print(f"Underlying: {S}\nStrike: {K}\nRisk-Free Rate: {r}\nVolatility: {v}\nMaturity: {T}\n")

    print("--- CALL ---")
    print(f"Delta: {bs_call_option_delta(S, K, r, v, T)}")
    print(f"Gamma: {bs_call_option_gamma(S, K, r, v, T)}")
    print(f"Vega: {bs_call_option_vega(S, K, r, v, T)}")
    print(f"Theta: {bs_call_option_theta(S, K, r, v, T)}")
    print(f"Rho: {bs_call_option_rho(S, K, r, v, T)}\n")

    print("--- PUT ---")
    print(f"Delta: {bs_put_option_delta(S, K, r, v, T)}")
    print(f"Gamma: {bs_put_option_gamma(S, K, r, v, T)}")
    print(f"Vega: {bs_put_option_vega(S, K, r, v, T)}")
    print(f"Theta: {bs_put_option_theta(S, K, r, v, T)}")
    print(f"Rho: {bs_put_option_rho(S, K, r, v, T)}")