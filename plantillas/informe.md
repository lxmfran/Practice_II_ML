# Protocol memo — Practice 2 *(two pages, English)*

**Team:** _(team identifier)_ · **Date:** _(date)_

This memo is written once, at Practice 2, and is carried **verbatim** into the defence pack.
It has to be defensible twelve weeks after you write it, so write it for a reader who was not
in the room.

---

## 1. The protocol we built

| Field | Challenge A — cyber | Challenge B — storage |
|---|---|---|
| Procedure and parameters | | |
| Grouping key | | |
| Whether randomness was consumed, and what seed | | |
| Fold sizes | | |

## 2. The invariants we verified

State what you checked, **what the check printed**, and what would have been evidence of
failure.

| Invariant | How it was checked | Result |
|---|---|---|
| No group in both portions of any fold (cyber) | | |
| No configuration split across folds (storage) | | |
| Every class present in every validation portion (cyber) | | |

## 3. What the split-protocol comparison measured

The course-fixed pipeline was used, identical under both schemes, with **only the splitting
protocol varying**.

| Challenge | Grouped | Ungrouped / row-wise | Difference |
|---|---|---|---|
| A — macro F1 | | | |
| B — MAE(z) | | | |

**The mechanism**, in your own words — what the ungrouped protocol lets the model see, and
what the score therefore stops estimating:

> _(two or three sentences)_

**Why grouping is right whatever the number was.** The argument must be about **what the
score is meant to estimate**, not about the size or sign of the gap:

> _(two or three sentences)_

## 4. The `log10` decision

The full justification, in prose. Not "it scored better" — the argument must be about the
**scale** of the target, the **currency of the loss**, and the **structure** of the problem.

> _(one or two paragraphs)_

**The log-to-physical rule, as we apply it:** log-scale metrics come from `z` and `ẑ`
directly; a physical metric is obtained by first inverting with `10 ** ẑ`; and
`10 ** MAE(z)` is a **multiplicative factor**, never a nanosecond error.

## 5. The metric contract

| Challenge | Primary metric | Why it fits the engineering problem | Our secondary operational concern |
|---|---|---|---|
| A | macro F1 | | |
| B | MAE(z) | | |

## 6. The declaration that closes the primary comparison basis

| Challenge | Frozen predictive-information basis | Frozen representation | What is method-specific and therefore family-specific |
|---|---|---|---|
| A | | | |
| B | | | |

**What this licenses:** every row of our comparison table on the `primary` route is a
**pipeline comparison** unless we explicitly hold the representation constant or rerun an
earlier family, in which case we will say so and claim an isolated family comparison.

## 7. What we adopted, and when

- our own fold construction was frozen at: _(cell / timestamp)_
- the canonical sidecars were read at: _(cell)_
- the discrepancy between our construction and the canonical assignment was: _(describe, or
  "none")_
- from that point, every scored development result uses the canonical assignment.
