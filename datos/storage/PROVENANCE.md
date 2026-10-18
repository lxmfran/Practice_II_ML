# Challenge B — storage latency prediction: provenance and terms

## Source and attribution

| Field | Value |
|---|---|
| Dataset | **Data Storage System Performance** |
| Authority | **HSE-LAMBDA**, `digital-twin` repository |
| Citation | *Performance Modeling of Data Storage Systems Using Generative Models*, **IEEE Access 13:49643–49658, 2025**, doi **`10.1109/ACCESS.2025.3552409`** |
| Licence | **Apache-2.0** |
| File used | `dataset.tar.gz` from the authors' `master` branch |

**The course did not generate this data and does not claim to have generated it.** What is
course-specific is the construction: the exclusion of a shortcut variable, the replicate
retention, the group-aware split, the target convention and the hidden final partition.

| File | Bytes | SHA-256 |
|---|---:|---|
| `dataset.tar.gz` (source, **not distributed**) | 6,775,657 | `e86467c1f92f595672d3c000a049bffba774ff1eef90c078439b5e747f29d3b1` |

Shape: 366,444 rows × 13 columns, in four subsets — `cache`, `hdd_sequential`, `ssd_random`,
`ssd_sequential`.

## The construction, as accepted under DEC-077 §B

1. **The unit of generalisation is a configuration, not a row.** Only **3,048 distinct
   configuration vectors** exist across the 366,444 measurements; each was measured 60–180
   times. A model evaluated on a random split of *rows* is asked to predict configurations it
   has already seen, which is not the engineering question.
2. **`iops` is excluded and is not distributed at all.** It is a second measured output of the
   same run, algebraically tied to latency through the queueing relation between concurrency
   and throughput; a model given it solves the task without learning anything about the
   configuration.
3. **`offset` is excluded** — it is constant across every row — and **`id` is excluded**: it is
   a run/configuration-associated identifier, it plays **no** part in grouping, and it is not
   needed to build the course grouping.
4. **70 rows with `lat == 0`** are dropped: no I/O completed, so there is no latency to predict.
5. **Grouping is defined by the visible nine-variable configuration vector** —
   `block_size`, `n_jobs`, `iodepth`, `read_fraction`, `load_type`, `io_type`, `raid`,
   `n_disks`, `device_type` — from which the course key `config_group` is built.
6. **Five replicates per configuration** are retained. Scores are flat from five upward, so
   keeping more buys runtime and nothing else.
7. **The development/hidden split is grouped on the configuration**, following the dataset
   authors' own train/test construction. Shared configurations between the two partitions: **0**.
8. **The distributed target is the raw `latency_ns`.** The modelling representation is not
   distributed: you discover and justify it in Practice 2, and from that point it is frozen
   for the rest of the project.
9. **Grouping metadata is shipped separately**, in `storage_groups.csv`, and is **never an
   estimator input**.

### Derived course files

| File | Columns | Bytes | SHA-256 |
|---|---|---:|---|
| `storage_development.csv` | `row_id`, 9 configuration/workload features, `latency_ns` | 663,916 | `f8954ad6874b0d6b8a888413bc0b1497a9b6285694eaf724a74e5e05bc487d10` |
| `storage_groups.csv` | `row_id`, `config_group` | 141,960 | `13e72acd28e60b8ff806b8bb2527ea661865044badf0f3b172939e6a3325bdd8` |
| `storage_submission_template.csv` | `row_id`, `latency_ns` — **the header line and nothing else** | 18 | `b5f9b356f482cd50620f66603cb113272ff01ae10f87f26a172d225334042f75` |

Development partition: **12,190 rows = 2,438 configurations × exactly 5 replicates**.

### The nine distributed features

| Feature | Kind | Domain in the development table |
|---|---|---|
| `block_size` | numeric | 9 values, 4 … 1024 |
| `n_jobs` | numeric | 42 values, 1 … 64 |
| `iodepth` | numeric | 32 values, 1 … 32 |
| `read_fraction` | numeric | 101 values, 0 … 100 |
| `n_disks` | numeric | 15 values, 3 … 24 |
| `load_type` | **nominal** | `random`, `sequential` |
| `io_type` | **nominal** | `read`, `write` |
| `raid` | **nominal** | `1+1`, `2+1`, `2+2`, `4+1`, `4+2`, `8+2` |
| `device_type` | **nominal** | `hdd`, `nvme` |

`raid` looks numeric and is not: `4+2` is a redundancy scheme, not a quantity. Treating it as
a number asserts an order and a spacing the data do not have.

Measured `latency_ns` in the development partition spans roughly **1.2 × 10⁵** to
**2.5 × 10⁹** nanoseconds — more than four orders of magnitude, and strongly right-skewed.
That observation is the starting point of the Practice 2 target-representation exercise; the
conclusion is yours to argue, not ours to assert here.

## What is not here

A hidden final test partition exists and its targets are **never** distributed. The final-test
*features* are released only after your model lock is frozen (Practice 5), at the one
canonical location `Proyecto/final_test/` and nowhere else.

**No benchmark or feasibility score is published here.** Scores obtained during the course's
own design study are not targets for you, are not expected values, and are deliberately absent
from all student material.

## Not a storage-engineering claim

This is a **teaching benchmark** built from a published measurement campaign on specific
hardware. Nothing computed in Practices 2–5 is a claim about storage systems in general.
