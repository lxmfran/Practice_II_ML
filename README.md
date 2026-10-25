# Practice II - Machine Learning (P2-P5)

Team repository for the cumulative Machine Learning project, Practices 2 to 5.
The internal role guide is available in [`docs/Guia_Roles_P2.pdf`](docs/Guia_Roles_P2.pdf).
The course assignment remains the authoritative specification.

## Repository structure

This repository corresponds to the `Proyecto/` directory in the assignment.
Commands described as running from `Proyecto/` must run from the repository root.

| Location | Contents | Responsibility |
|---|---|---|
| `datos/cyber/`, `datos/storage/` | Course data, provenance, grouping metadata and the canonical fold CSV files, which are already available | Preserve course-provided files unchanged |
| `esquemas/` | Submission schemas | Read-only reference |
| `herramientas/` | Course submission-format validator | Read-only reference |
| `final_test/` | Course README; final-test features are released only after the P5 model lock | No P2 notebook reads or checks final-test files |
| `plantillas/` | Existing course document files, completed in place for this team | Feature register, AI disclosure, roles and protocol memo |
| `notebooks/R1_data.ipynb`, `R2_cyber.ipynb`, `R3_storage.ipynb`, `R4_evaluacion.ipynb` | Source notebooks for the four role contributions | Team source material |
| `notebooks/P2_cyber.ipynb`, `notebooks/P2_storage.ipynb` | Integrated P2 notebooks, one per challenge | R5 integration and team review |
| `entregas_prueba/` | Development-only dry-run predictions and corresponding feature subsets | R2 and R3; integration checked by R5 |
| Repository root | Cumulative `comparativa.csv`; the document files remain in `plantillas/` | R4 owns the comparison table; R5 checks delivery completeness |

## Source and final notebooks

Use `notebooks/R1_data.ipynb` as the complete R1 source. The team moved and renamed
the source notebooks; there is no longer a separate `borradores/` directory.

R5 has assembled the supplied P2 outlines using the following team sections:

- Cyber: R1 data checks and preprocessing, R4 protocol and evaluation, R2 classification and probability analysis, and the P2.6 explanations and dry run.
- Storage: R1 data checks and preprocessing, R4 protocol and evaluation, R3 target-representation analysis and regression, and the P2.6 explanations and dry run.

Run these notebooks with `notebooks/` as the working directory. Their relative data
paths start with `../datos`, and their document paths with `../plantillas`. The final
notebooks run independently from beginning to end. Interpretations belong in Markdown
cells; copied cells include source notebook and cell identifiers in their metadata.

Coordinate substantive model or interpretation changes with the relevant role. Integration
may adjust paths and separate mixed-challenge cells while preserving the model configurations.

## Working with Git

Clone the repository and install the project dependencies:

```bash
git clone https://github.com/lxmfran/Practice_II_ML.git
cd Practice_II_ML
pip install -r requirements.txt
```

Work on the branch assigned to your role. Before integrating others' work, fetch the
remote state and merge `origin/main` into your branch. Preserve uncommitted changes
before switching branches or resolving conflicts. Another team member reviews the
pull request before it is merged into `main`.

| Branch | P2 role |
|---|---|
| `r1-datos` | R1 - Data and preprocessing |
| `r2-cyber` | R2 - Classification |
| `r3-storage` | R3 - Regression |
| `r4-evaluacion` | R4 - Evaluation and validation |
| `r5-informe` | R5 - Reporting and reproducibility |

Draft outputs may be cleared to reduce merge conflicts. This does not apply to the
two final delivery notebooks: restart their kernels, execute all cells, and save outputs.

## P2 checks before delivery

- Print `PROJECT_RANDOM_STATE = 2627` in the first cell of each final notebook. Pass it only to operations that consume randomness; do not search over seeds.
- Never use `row_id`, `feature_group`, `config_group` or `fold_id` as estimator inputs. Never reintroduce excluded predictors such as `iops`.
- Fit learned preprocessing only on each fold's training portion, inside a pipeline.
- After the explicit P2.2 protocol demonstration, use the course canonical fold assignments for scored development results.
- Model storage latency as `z = log10(latency_ns)` after P2.3. Invert predictions with `10 ** z_hat` before computing physical errors or writing submission latencies.
- Include the completed cumulative registers, comparison rows, the OneR explanation and the two-page protocol memo.
- Keep all assessed material in English, including comments, Markdown interpretations, figure labels and captions. The Spanish role guide is internal team documentation.
- Record the actual Python and library versions used for the final run; minimum versions in `requirements.txt` do not pin a complete environment.
- Document AI assistance in `AI_USAGE.md`, including purpose, affected sections and verification. No generative AI is allowed during individual defence questioning.
- Follow the data attribution and use requirements recorded in both `PROVENANCE.md` files. The team's internal guide requires a private repository for the course data.

## Submission-format dry runs

Run these commands from the repository root, using the same Python environment as the notebooks:

```bash
python herramientas/validate_submission.py cyber entregas_prueba/cyber_dry_run.csv entregas_prueba/cyber_dry_run_features.csv datos/cyber/cyber_class_codes.json
python herramientas/validate_submission.py storage entregas_prueba/storage_dry_run.csv entregas_prueba/storage_dry_run_features.csv
```

The validator checks format and identifiers, not predictive performance. For storage,
verify the conversion to nanoseconds and the output magnitude as well: a file containing
positive log-scale predictions can pass the format checks while still being incorrect.

## Verified P2 execution

On 2026-10-25, both integrated notebooks were run from beginning to end in fresh
Jupyter kernels, with outputs saved and no error outputs. The verification environment
was Python 3.12.14, NumPy 2.5.4, pandas 3.0.1, scikit-learn 1.9.1 and matplotlib 3.11.2.
The original setup comment in `requirements.txt` refers to Python 3.14; that specific
environment was not the one used for this verification. Both dry-run validators returned
`valid`. Notebook metadata also records the environment and the source-cell mapping.

Numerical tie handling and floating-point differences can affect a small number of KNN
outputs across environments. Report the results actually obtained in the recorded
environment, and retain the grouped canonical protocol, grids and frozen seed.
