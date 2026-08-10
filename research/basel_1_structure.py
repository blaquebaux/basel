#!/usr/bin/python3
# =============================================================================
# basel_1_structure.py — BLAQUE BAUX BASEL #1 (the flagship: one factor).
#
# The mirror of Bio. Prudential (Basel) regulation forces every bank into the same
# capital/liquidity/risk box, so they move as ONE factor — the opposite of biotech's
# FDA-driven idiosyncrasy. Confirmed across the tier ladder, and the only mildly-
# distinct pockets are global ADRs and extreme-small community banks.
#
# RESULTS AS TESTED (2016-2026, daily):
#   tier            within  eff-bets  ->T1US  ->SPY
#   T1 US GSIB       0.82    1.4/6     1.00    0.76
#   T1 Global        0.62    2.0/6     0.83    0.70   <- the global pocket (most distinct)
#   T2 super-reg     0.78    1.5/5     0.92    0.73
#   T3 regional      0.87    1.3/6     0.89    0.66
#   T4 community     0.78    1.5/8     0.82    0.63   <- lowest market beta
#   US banks (17): avg corr 0.80 | eff-bets 1.5/17 | 1-factor 81% | dispersion 0.80%/d
#   (Bio contrast: corr 0.32, eff-bets 6.3/18, dispersion 2.07%/d)
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _basel_common import TIERS, US_BANKS, rets, eff_bets

allb = [s for v in TIERS.values() for s in v] + ["SPY"]
u, dts, R = rets(allb); i = {s: u.index(s) for s in u}
t1 = R[:, [i[s] for s in TIERS["T1 US GSIB"] if s in i]].mean(1); spy = R[:, i["SPY"]]
print("=" * 72, "\nBASEL #1 — the tier ladder (one factor?)\n" + "=" * 72)
print(f"  {'tier':<14}{'within':>8}{'eff-bets':>10}{'->T1US':>8}{'->SPY':>7}")
for t, syms in TIERS.items():
    idx = [i[s] for s in syms if s in i]
    if len(idx) < 2: continue
    c, e, f = eff_bets(R[:, idx]); bk = R[:, idx].mean(1)
    print(f"  {t:<14}{c:>8.2f}{e:>7.1f}/{len(idx)}{np.corrcoef(bk,t1)[0,1]:>8.2f}{np.corrcoef(bk,spy)[0,1]:>7.2f}")
idx = [i[s] for s in US_BANKS if s in i]
c, e, f = eff_bets(R[:, idx]); disp = np.nanmean(np.nanstd(R[:, idx], axis=1))
print(f"\n  US banks ({len(idx)} names): avg corr {c:.2f}  eff-bets {e:.1f}/{len(idx)}  1-factor {f:.0f}%  dispersion {disp*100:.2f}%/d")
print(f"  Bio for contrast: corr 0.32, eff-bets 6.3/18, dispersion 2.07%/d")
print("\nVERDICT: confirmed — 17 US banks are ~1.5 independent bets (one factor, 81%).")
print("Basel homogenizes; the FDA does not (Bio). Global ADRs and community banks are")
print("the only mildly-distinct pockets. Basel is the anti-Bio.")
