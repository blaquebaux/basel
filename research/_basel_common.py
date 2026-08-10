#!/usr/bin/python3
# =============================================================================
# _basel_common.py — shared helpers for the Blaque Baux Basel (regulated banks) sketches.
# Alpaca SIP daily bars; reads ALPACA_KEY_ID / ALPACA_SECRET_KEY from env. Read-only.
# =============================================================================
import os, json, urllib.request, math
import numpy as np

H = {"APCA-API-KEY-ID": os.environ["ALPACA_KEY_ID"], "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
START, END = "2016-01-01", "2026-08-01"
_cache = {}

# The Basel tier ladder (from the base correlation study).
TIERS = {
    "T1 US GSIB":   ["JPM", "BAC", "C", "WFC", "GS", "MS"],
    "T1 Global":    ["UBS", "HSBC", "DB", "BCS", "RY", "TD"],
    "T2 super-reg": ["USB", "PNC", "TFC", "COF", "BK"],
    "T3 regional":  ["RF", "KEY", "CFG", "FITB", "HBAN", "MTB"],
    "T4 community": ["TCBI", "WSFS", "FFIN", "AUB", "CATY", "COLB", "UCBI", "INDB"],
}
US_BANKS = TIERS["T1 US GSIB"] + TIERS["T2 super-reg"] + TIERS["T3 regional"]

def bars(s):
    if s in _cache: return _cache[s]
    u = (f"https://data.alpaca.markets/v2/stocks/bars?symbols={s}&timeframe=1Day"
         f"&start={START}&end={END}&adjustment=all&feed=sip&limit=10000")
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=40))
        _cache[s] = {b["t"][:10]: b for b in d.get("bars", {}).get(s, [])}
    except Exception:
        _cache[s] = {}
    return _cache[s]

def rets(syms):
    D = {s: bars(s) for s in syms}; D = {s: v for s, v in D.items() if len(v) > 500}
    u = list(D); dates = sorted(set.intersection(*[set(D[s]) for s in u]))
    M = np.array([[D[s][d]["c"] for s in u] for d in dates], float)
    return u, dates, M[1:] / M[:-1] - 1

def stats(r):
    r = np.asarray(r, float); r = r[np.isfinite(r)]
    if len(r) < 30 or r.std() == 0: return dict(sh=float('nan'), cagr=float('nan'), dd=float('nan'))
    cum = np.cumprod(1 + r)
    return dict(sh=r.mean() / r.std() * math.sqrt(252), cagr=cum[-1] ** (252 / len(r)) - 1,
                dd=(cum / np.maximum.accumulate(cum) - 1).min())

def beta_alpha(y, x):
    y = np.asarray(y, float); x = np.asarray(x, float)
    m = np.isfinite(y) & np.isfinite(x); y, x = y[m], x[m]
    if len(y) < 30 or np.var(x) == 0: return float('nan'), float('nan')
    b = np.cov(y, x)[0, 1] / np.var(x)
    return b, (y.mean() - b * x.mean()) * 252

def eff_bets(Rm):
    C = np.corrcoef(Rm.T); lam = np.linalg.eigvalsh(C)
    return C[np.triu_indices(len(C), 1)].mean(), (lam.sum() ** 2) / (lam ** 2).sum(), 100 * lam.max() / lam.sum()
