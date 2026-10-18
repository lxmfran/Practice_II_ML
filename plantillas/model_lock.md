# `model_lock.md` — the final model lock

**Team:** _(team identifier)_ · **Frozen on:** _(date and time)_

> **This file is written and submitted BEFORE the final-test features are released.** Once it
> is frozen, nothing about the model, the pipeline or the configuration may change before the
> single submission. A post-lock change is an automatic method penalty, and so is a post-hoc
> explanation of the hidden result that amounts to retuning after seeing it.

Complete one block per challenge.

---

## Challenge A — cybersecurity

| Field | Entry |
|---|---|
| **Chosen model family** | |
| **Why this family, and not the one with the next-best mean** | |
| **Complete preprocessing pipeline** — in enough detail to be re-executed | |
| **Feature definitions** — by reference to `features.md` | |
| **Route of every feature in the locked pipeline** — `primary` or `extension` | |
| **If any derived predictive feature is included:** did you rerun the earlier families on the same basis, or are you stating that this is not an isolated family comparison? | |
| **Hyperparameters, in full** | |
| **Stopping parameters** *(if an MLP is locked)* — `solver`, `early_stopping`, `tol`, `n_iter_no_change`, `max_iter`, `learning_rate`, `momentum`, `nesterovs_momentum` | |

### Predicted performance — descriptive, not inferential

| Field | Entry |
|---|---|
| Primary metric | macro F1 |
| **Canonical-CV mean** | |
| **The five individual fold values** | |
| **Simple spread** — the range, or the standard deviation of those five values | |

> *"We expect hidden-test performance to be broadly consistent with the variation observed
> across the five canonical development folds, but this is **not a confidence interval** and
> **not a probability guarantee**."*

**The lock must not contain** a confidence interval, a p-value, a hypothesis test, or a
claimed probability that the hidden score falls in any interval. This course teaches none of
them, and the hidden test is not marked on numerical closeness.

---

## Challenge B — storage

| Field | Entry |
|---|---|
| **Chosen model family** | |
| **Why this family** | |
| **Complete preprocessing pipeline** | |
| **Feature definitions** — by reference to `features.md` | |
| **Route of every feature** | |
| **Derived-feature statement**, if applicable | |
| **Hyperparameters, in full** | |
| **Stopping parameters** *(if an MLP is locked)* | |
| **Target representation and the inverse transform** | modelling target `z = log10(latency_ns)`; the submitted column is `latency_ns = 10 ** ẑ`, on the physical scale |

### Predicted performance — descriptive, not inferential

| Field | Entry |
|---|---|
| Primary metric | `MAE(z)` |
| **Canonical-CV mean** | |
| **The five individual fold values** | |
| **Simple spread** | |

> *"We expect hidden-test performance to be broadly consistent with the variation observed
> across the five canonical development folds, but this is **not a confidence interval** and
> **not a probability guarantee**."*

---

## After the lock

1. The final-test features are released.
2. The frozen pipeline is **refitted on the whole development table**, with every
   preprocessing object refitted on that same table.
3. The final-test features are **transformed, never refitted on**.
4. Challenge B predictions are **inverse-transformed to physical `latency_ns`**.
5. Both files are checked with `validate_submission.py`, which reads no target file and
   returns no score.
6. **One** submission is made per challenge. There is no leaderboard.

## At the defence

The team compares the actual hidden-test result against the descriptive expectation above and
**explains any gap** — an explanation, not a test. The six things assessed are: that the lock
was genuinely frozen first and is complete; that the submission involved no post-lock change
and no contact with any hidden target; that the comparison is honest, including when the
result is worse; that the gap is described as small or large **relative to your own fold
evidence**; that plausible methodological or data-related reasons are offered without post-hoc
tuning; and that conclusions, limitations and the deployment recommendation are revised
appropriately.

**No marks are awarded or withheld because the hidden score happened to be numerically close
to, or far from, the CV mean.**
