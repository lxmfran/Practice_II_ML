# `features.md` — the typed feature register

**Team:** _(team identifier)_ · **Cumulative:** add to this file at every milestone and
**date each addition**. Never delete an earlier entry.

This is a **typed register, not a free list**. Every entry carries its definition, its
motivation, the milestone at which it was introduced, its **kind** and its **route**.

## The three kinds

| Kind | Meaning |
|---|---|
| **source feature** | a column distributed by the course, used as it is |
| **representation transformation** | scaling, encoding, or a **monotone** change of an existing numeric predictor — preprocessing, adding **no new predictive information** |
| **derived predictive feature** | a genuinely **new** predictor built from two or more source columns, or from one in a non-monotone way |

## The two routes

| Route | Meaning |
|---|---|
| **primary** | uses only the predictive-information basis frozen at the end of Practice 2. Only `primary` rows may be read as a model-family comparison. |
| **extension** | an engineering extension. Welcome, reported in its own comparison rows, and never a family comparison. |

**Nothing may be derived from a column that is not distributed, and nothing may be derived
from `row_id`.**

## What the frozen basis is

| Challenge | Frozen predictive-information basis | Frozen representation |
|---|---|---|
| A — cyber | the **eleven** distributed source predictors | `log1p` on the eight numeric predictors, declared as a representation transformation |
| B — storage | the **nine** distributed source predictors | none beyond method-required scaling; the **target** representation `z = log10(latency_ns)` is frozen in P2.3 |

Method-required transformations — scaling where the method needs it, categorical encoding,
the `log10` target — remain family-specific, and the evidence is then reported as a
**pipeline comparison**.

## Register

| Date | Milestone | Challenge | Feature | Definition | Motivation | Kind | Route |
|---|---|---|---|---|---|---|---|
| | P2 | cyber | `proto` | distributed transport protocol | source column | source feature | primary |
| | P2 | cyber | … | | | | |
| | P2 | storage | `block_size` | distributed I/O block size | source column | source feature | primary |
| | P2 | storage | … | | | | |
| | P2 | cyber | `log1p(...)` on the eight numeric predictors | monotone transform of existing predictors | brings nine orders of magnitude into a range a distance can see | representation transformation | primary |
| | P2 | storage | `z = log10(latency_ns)` | target representation | positive target over four-plus orders of magnitude, relative rather than absolute error currency, raw skew removed; see the P2.3 justification and the grouped raw-versus-log demonstration | representation transformation (target) | primary |

## If you want a derived predictive feature in your final deployment candidate

You must do **exactly one** of these two things, and say which:

1. **rerun the relevant earlier comparison models on the same new feature basis**, so the
   families are again compared on equal information; or
2. **state explicitly**, in the notebook and in the model lock, that the resulting score is
   **not** an isolated model-family comparison.

Neither option is penalised. Silently doing neither is.
