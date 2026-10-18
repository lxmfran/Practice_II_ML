# `Proyecto/final_test/` — the one canonical post-lock release location

This directory is **the single place** where the final-test **feature** tables are released:

| File | Released |
|---|---|
| `cyber_final_test_features.csv` | after the Practice 5 model lock is frozen |
| `storage_final_test_features.csv` | after the Practice 5 model lock is frozen |

**Right now this directory contains only this note.** That is not an error. Before the lock
there is no student-visible final-test file anywhere in the course tree, under any name, in
any other directory — and no milestone before Practice 5 depends on one.

## Why the features arrive late, and the targets never arrive

The **targets** are never distributed, at any point, in any form. Only the features are
released, and only after the lock, so that the single hidden-final score measures a model
that was chosen without reference to the final partition.

Practice 2's submission-format dry run therefore uses a **development subset** you choose
yourself in place of the final feature table. The schema is identical, which is the whole
point of the dry run: the format is settled three milestones before it matters.

## What you may and may not do with the released features once they arrive

You may: read them, build the design matrix your **already-locked** pipeline expects,
predict, and write the submission.

You may not: refit, retune, re-select, threshold, calibrate, or change anything at all in the
pipeline after the lock. The model lock in `model_lock.md` is the commitment, and any
post-lock change to the model or pipeline before the single submission is an automatic method
penalty.

There is **one** submission. Check its format first with
`herramientas/validate_submission.py` — that validator reads no target file and returns no
score, so run it as often as you like.
