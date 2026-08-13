# Blaque Baux Basel

**Banks under the Basel regime — one regulated factor.**

Basel is a member of the Blaque Baux family. The [core repo](https://github.com/blaque-baux/base)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Basel points that engine in its own
direction and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/blaque-baux/basel.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

The base correlation study found US banks are ~0.8-0.95 one factor across every tier, because prudential (Basel) regulation homogenizes them: correlation is proportional to shared forced exposure. Basel makes that its subject — trade the regulated-bank factor, knowing that 'diversifying' across banks is an illusion. It is the deliberate opposite of Bio.

## Research plan (Path A — not yet built)

- The bank factor — confirm the one-factor structure across GSIBs; size to the real bet count, not the name count.
- Rate/curve sensitivity — banks' dominant macro driver; measure and optionally hedge it.
- Cross-tier / global — the mildly-distinct pockets (global ADRs, community banks) the base identified.

## Research — first pass done

Full detail in [`research/README.md`](research/README.md). The scorecard:

| # | Question | Verdict |
|---|----------|---------|
| 1 | Are banks really one factor? | ✅ **confirmed** — 17 banks = 1.5 eff-bets, corr 0.80, 81% one factor |
| 2 | What *is* the bank factor? | ✅ economy + short duration (beta-SPY +1.1, beta-TLT −0.5, +curve) |
| 3a | Stock-picking within banks? | ❌ null — nothing to pick |
| 3b | Timing the factor? | ❌ null — trend loses, rate-overlay < buy&hold |

**The synthesis (and the completed Bio↔Basel pair):** prudential regulation homogenizes banks
into one factor — the exact mirror of biotech's FDA-driven idiosyncrasy — and that factor is
the economy plus the yield curve (banks = long economy, short duration). Neither stock-picking
nor naive timing yields systematic alpha. Together, **Bio and Basel bound when cross-sectional
alpha is possible**: it needs dispersion that is both high *and* price-predictable — biotech has
the first without the second, banks have neither. Basel's value is as a coherent **macro sleeve**
(an equity curve/rates expression), not a price-alpha source.

## Status
**Research: first pass complete** (`research/`). No price-alpha keeper (correctly); a coherent
macro/known-beta sleeve. No live driver; nothing validated to the spine's bar.

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/blaque-baux/base) is the
base/blueprint and holds the [full family roster](https://github.com/blaque-baux/base#the-blaque-baux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> blaque-baux/base)
research/   three Path-A sketches (one-factor structure, rate/curve identity, tradeability null) + scorecard
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
