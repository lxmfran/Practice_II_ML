# `roles.md` — the five-phase rotation

**Team:** _(team identifier)_ · **Members:** S1 … S5 _(replace with names)_

Submit this file with **every** milestone, with the current phase's row marked.

## The five roles

| Role | Responsibility at a milestone |
|---|---|
| **R1 Data and preprocessing steward** | Loads the contract tables, verifies the schema, owns `features.md`, and ensures every fitted transformer is fitted **inside** the fold. |
| **R2 Classification lead** | Owns the Challenge A model for this milestone. |
| **R3 Regression lead** | Owns the Challenge B model for this milestone. |
| **R4 Evaluation and validation officer** | Owns the protocol: the canonical fold definitions, the grouping invariants, metric computation under the metric contract, and the running comparison table. **Has an explicit veto** on any evaluation that violates the contract. |
| **R5 Reporting and reproducibility lead** | Owns the narrative, the figures, `PROJECT_RANDOM_STATE`, top-to-bottom re-execution, `AI_USAGE.md`, and the memo. |

## The rotation — fill in your five names once, then never change it

| Student | P2 | P3 | P4 | P5 | Final Integration & Defence |
|---|---|---|---|---|---|
| S1 = ______ | R1 | R2 | R3 | R4 | **R5** |
| S2 = ______ | R2 | R3 | R4 | R5 | **R1** |
| S3 = ______ | R3 | R4 | R5 | R1 | **R2** |
| S4 = ______ | R4 | R5 | R1 | R2 | **R3** |
| S5 = ______ | R5 | R1 | R2 | R3 | **R4** |

Four properties of this table are what make it a rotation rather than a rota:

1. in each of the five phases the five roles are held by five **different** students;
2. **no student repeats a role** across the five phases;
3. each student therefore serves **exactly once** as primary owner of each of the five
   responsibility domains;
4. the role a student did **not** hold during P2–P5 is precisely the role they lead during
   **Final Integration & Defence** — so the fifth rotation is determined by the first four
   rather than chosen.

Property 4 is the design's answer to "five people, four modelling milestones": the domain you
never executed during modelling is the one you own when the project is integrated and
defended. Every member therefore has to understand a part of the pipeline they did not
personally build.

## What primary ownership does not mean

**It does not restrict questioning.** At the defence any student may be asked about **any**
part of either predictive system, independently of every role they have held. Each student is
guaranteed at least one question inside the domain they led during Final Integration &
Defence, and at least one outside it.

A team of four or six is remapped by the professor; the instrument is the table, not the
arithmetic.

## This milestone

| Field | Value |
|---|---|
| Milestone | _(P2 / P3 / P4 / P5 / Final Integration & Defence)_ |
| R1 | |
| R2 | |
| R3 | |
| R4 | |
| R5 | |
| Anything the team reallocated, and why | |
