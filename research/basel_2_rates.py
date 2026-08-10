#!/usr/bin/python3
# =============================================================================
# basel_2_rates.py — BLAQUE BAUX BASEL #2: what IS the bank factor?
#
# If banks are one factor (basel_1), what drives it? Answer: the ECONOMY and the
# YIELD CURVE. Banks run ~1.1x market beta AND a strongly NEGATIVE beta to long bonds
# (they fall when bonds rally / rates drop) plus a positive tie to curve steepening.
# To hold banks is to be long the economy and SHORT DURATION. That is the factor's
# identity — a risk fact, and the coherent macro use of this sleeve.
#
# RESULTS AS TESTED (2016-2026):
#   KBE  Sharpe +0.47  beta-SPY +1.18  beta-TLT -0.54  corr-steepener +0.27
#   XLF  Sharpe +0.57  beta-SPY +1.03  beta-TLT -0.41  corr-steepener +0.27
#   KRE  Sharpe +0.42  beta-SPY +1.17  beta-TLT -0.56  corr-steepener +0.26
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _basel_common import rets, stats, beta_alpha

u, d, R = rets(["KBE", "XLF", "KRE", "SPY", "TLT", "IEF", "SHY"]); j = {s: u.index(s) for s in u}
steep = R[:, j["SHY"]] - R[:, j["TLT"]]      # curve-steepening proxy (long yields up => TLT falls)
print("=" * 72, "\nBASEL #2 — rate / curve sensitivity (banks are a curve bet)\n" + "=" * 72)
for s in ["KBE", "XLF", "KRE"]:
    st = stats(R[:, j[s]]); bs, _ = beta_alpha(R[:, j[s]], R[:, j["SPY"]]); bt, _ = beta_alpha(R[:, j[s]], R[:, j["TLT"]])
    cst = np.corrcoef(R[:, j[s]], steep)[0, 1]
    print(f"  {s:<4} Sharpe {st['sh']:+.2f}  CAGR {st['cagr']*100:+.1f}%  beta-SPY {bs:+.2f}  beta-TLT {bt:+.2f}  corr-steepener {cst:+.2f}")
print("\nVERDICT: the bank factor = leveraged economy + short duration. beta-TLT ~ -0.5")
print("means banks fall when bonds rally (rates drop); the curve tie is positive. Holding")
print("banks is an equity expression of 'rates up / curve steeper' — the sleeve's real use.")
