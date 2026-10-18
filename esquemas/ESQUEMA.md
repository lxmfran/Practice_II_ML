# Submission schemas

Two files in this directory define the submission format for the two project challenges.
Each contains **the header line and nothing else**: the schema, no data.

| File | Header |
|---|---|
| `cyber_submission_template.csv` | `row_id,attack_code` |
| `storage_submission_template.csv` | `row_id,latency_ns` |

The same two files are mirrored in `Proyecto/datos/cyber/` and `Proyecto/datos/storage/`.

## Why they are empty

A template with rows in it would tell you two things you are not supposed to know before the
model lock: **which `row_id` values are in the hidden final partition**, and **how many rows
that partition has**. Neither is part of the format, and neither is released early. So the
templates carry the format and nothing more.

The `row_id` column is filled from the **released final-test feature table** — which arrives
only after the Practice 5 model lock is frozen, at the single canonical location
`Proyecto/final_test/` — or, for the Practice 2 dry run, from a development subset you choose
yourself. See `Proyecto/final_test/README.md`.

## What a well-formed file looks like

The `row_id` values below are **illustrative placeholders**, not real identifiers from any
partition of this course's data.

```
row_id,attack_code
<row_id_1>,5
<row_id_2>,0
<row_id_3>,8
```

```
row_id,latency_ns
<row_id_1>,1183157.35
<row_id_2>,49966427.5
<row_id_3>,204811.0
```

## The rules the validator enforces

Both challenges:

* the header is exactly as tabulated above, columns in that order;
* the `row_id` set is **exactly** the `row_id` set of the released feature table, each value
  appearing once — no missing value, no duplicate, no extra;
* the prediction column is numeric, finite, and not `NaN`.

Challenge A (cybersecurity):

* `attack_code` is an integer **in the ten declared class codes**, which are read from
  `cyber_class_codes.json`. That file is a **required argument** to the validator: it is not
  guessed from whichever directory the feature table happens to sit in, and a cybersecurity
  call made without it is **refused**, never passed.

Challenge B (storage):

* `latency_ns` is the prediction **on the physical scale, in nanoseconds**, strictly
  positive. A file carrying the modelling representation `z = log10(latency_ns)` is a *wrong*
  submission, not a rescaled one — and because every plausible `z` is a small positive finite
  number, the validator **cannot** catch that mistake for you. Check the magnitude yourself.

## Checking a file

After the Practice 5 lock, from `Proyecto/`:

```
python3 herramientas/validate_submission.py cyber   my_cyber_submission.csv \
        final_test/cyber_final_test_features.csv   datos/cyber/cyber_class_codes.json
python3 herramientas/validate_submission.py storage my_storage_submission.csv \
        final_test/storage_final_test_features.csv
```

For the Practice 2 dry run the feature table is a development subset you build yourself, so
the second argument is that file instead; the class-code file is the same one either way.
Note that the feature table and the class-code file live in **different directories**: the
class codes are therefore passed explicitly, always.

The validator **reads no target file and returns no score**, so it conveys nothing about the
hidden partition and there is no limit on how often you run it.
