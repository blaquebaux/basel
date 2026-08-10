#!/usr/bin/python3
# =============================================================================
# basel_3_tradeable.py — BLAQUE BAUX BASEL #3 (the null, mirror of Bio).
#
# Two ways to try to trade the bank factor, both fail:
#   (a) STOCK-PICKING within banks — with only ~1.5 independent bets there is almost
#       nothing to pick; momentum and reversal are flat. This is the mirror of Bio's
#       null: Bio has dispersion but it is idiosyncratic; Basel has no dispersion at all.
#   (b) TIMING the factor — trend-following KBE loses, and "long only when rates are
#       rising" underperforms simply holding. The rate sensitivity is a RISK trait, not
#       an easy timing edge.
#
# RESULTS AS TESTED (2016-2026):
#   (a) 12-1 momentum-neutral vs KBE  Sharpe -0.07  alpha +0.4%/yr
#       1-day reversal (long losers)  Sharpe +0.07  alpha +0.5%/yr
#   (b) KBE 60d trend-follow          Sharpe -0.35
#       long KBE when rates rising    Sharpe +0.13  (vs KBE buy&hold +0.47)
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _basel_common import US_BANKS, bars, rets, stats, beta_alpha

uB, dB, RB = rets(US_BANKS); T, N = RB.shape
kb = bars("KBE"); kbe = np.array([kb[d]["c"] if d in kb else np.nan for d in dB], float); kber = kbe[1:] / kbe[:-1] - 1
def lme(score, frac=0.2):
    kk = max(1, int(N * frac)); out = []
    for t in range(T - 1):
        s = score[t]; m = np.isfinite(s)
        if m.sum() < kk: out.append(np.nan); continue
        o = np.argsort(np.where(m, s, np.nan)); fwd = RB[t + 1]
        out.append(np.nanmean(fwd[o[-kk:]]) - np.nanmean(fwd[m]))
    return np.array(out)
def rep(name, pnl):
    st = stats(pnl); b, a = beta_alpha(pnl, kber[1:])
    print(f"  {name:<32} Sharpe {st['sh']:+.2f}  beta-KBE {b:+.2f}  alpha {a*100:+.1f}%/yr")

print("=" * 72, "\nBASEL #3 — is the factor tradeable? (stock-picking + timing)\n" + "=" * 72)
print("(a) stock-picking within banks, KBE-neutral:")
mom = np.full((T, N), np.nan)
for t in range(252, T): mom[t] = np.prod(1 + RB[t - 252:t - 21], axis=0) - 1
rep("  12-1 momentum-neutral", lme(mom))
rev = np.vstack([np.full(N, np.nan), RB[:-1]])[:T]; rep("  1-day reversal (long losers)", -lme(rev))
print("\n(b) timing the bank factor:")
u3, d3, R3 = rets(["KBE", "TLT"]); k = {s: u3.index(s) for s in u3}; kb3 = R3[:, k["KBE"]]; tlt3 = R3[:, k["TLT"]]
lvl = np.cumprod(1 + kb3); mom60 = np.full(len(kb3), np.nan)
for t in range(60, len(kb3)): mom60[t] = lvl[t] / lvl[t - 60] - 1
print(f"  KBE 60d trend-follow           Sharpe {stats(np.sign(mom60)[:-1]*kb3[1:])['sh']:+.2f}")
tl = np.cumprod(1 + tlt3); tt = np.full(len(tlt3), np.nan)
for t in range(60, len(tlt3)): tt[t] = tl[t] / tl[t - 60] - 1
ov = (tt < 0).astype(float)[:-1] * kb3[1:]
print(f"  long KBE when rates RISING     Sharpe {stats(ov)['sh']:+.2f}  (vs KBE buy&hold {stats(kb3)['sh']:+.2f})")
print("\nVERDICT: null on both. One factor => nothing to stock-pick (the mirror of Bio);")
print("naive timing does not beat holding. Basel is a coherent MACRO sleeve (a curve/rates")
print("expression), not a source of systematic price alpha.")
