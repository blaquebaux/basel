# Blaque Baux Basel — research

First-pass Path-A research on the regulated-bank sleeve — the deliberate mirror of
[Bio](https://github.com/blaquebaux/bio). All sketches read Alpaca SIP daily
bars, are read-only, and print their own results. 2016–2026, on the base study's bank tier
ladder.

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
python research/basel_1_structure.py   # the one-factor confirmation
python research/basel_2_rates.py       # what the bank factor actually is
```

## Scorecard

| # | Question | Result | Verdict |
|---|----------|--------|---------|
| 1 | Are banks really one factor? | avg corr **0.80**, **1.5** eff-bets/17, 81% one factor | ✅ confirmed (flagship) |
| 2 | What *is* the bank factor? | beta-SPY +1.1, **beta-TLT −0.5**, +curve | ✅ economy + short duration |
| 3a | Does stock-picking within banks pay? | momentum −0.07, reversal +0.07 | ❌ null (nothing to pick) |
| 3b | Does timing the factor pay? | trend −0.35; rate-overlay +0.13 < B&H +0.47 | ❌ null |

## The synthesis — and the completed Bio↔Basel pair

- **#1 is the flagship.** 17 US banks collapse to **~1.5 independent bets** (avg correlation
  0.80, 81% one factor, dispersion 0.80%/day). Every tier is ~one factor internally and
  ~0.9 correlated to the GSIBs; only global ADRs (0.62 internal) and extreme-small community
  banks (0.63 market beta) are mildly distinct. Prudential (Basel) regulation forces every
  bank into the same capital/liquidity box — it *homogenizes*. Basel is the anti-Bio.

- **#2 is the insight.** The bank factor is not mysterious: it is the **economy and the yield
  curve.** Banks run ~1.1× market beta and a strongly negative beta to long bonds (−0.5:
  they fall when bonds rally / rates drop), with a positive tie to curve steepening. To hold
  banks is to be **long the economy and short duration** — an equity expression of "rates up,
  curve steeper." That is the coherent use of this sleeve.

- **#3 is the null, and it completes the pair.** Neither stock-picking (one factor → nothing
  to pick) nor naive timing (trend loses; the rate-overlay underperforms holding) produces
  systematic price alpha.

**The Bio↔Basel lesson.** Together they map exactly when cross-sectional alpha is possible —
and it *isn't*, at either pole:

| | dispersion | why stock-picking fails |
|---|---|---|
| **Bio** (FDA, idiosyncratic) | very HIGH (2.07%/d, 6.3 bets) | dispersion is real but **unpredictable** (binary events, not price) |
| **Basel** (prudential, homogenized) | very LOW (0.80%/d, 1.5 bets) | there is **nothing to pick** — one factor |

Systematic cross-sectional alpha needs dispersion that is both *high* **and** *price-predictable*.
Biotech has the first without the second; banks have neither. That is the durable law this pair
contributes to the family.

**Where this leaves Basel:** no price-alpha keeper (correctly), but unlike Bio it has a clear,
coherent identity — a **macro sleeve**: banks as an equity curve/rates expression, the natural
diversifier to duration-sensitive books. Not prototype-grade as alpha; useful as a known-beta
building block.

## Files
- `_basel_common.py` — shared helpers + the bank tier ladder.
- `basel_1_structure.py` — the one-factor / tier-ladder confirmation.
- `basel_2_rates.py` — the factor's identity (economy + yield curve).
- `basel_3_tradeable.py` — the stock-picking and timing nulls.
