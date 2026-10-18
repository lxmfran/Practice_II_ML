# Practice II — Machine Learning (P2–P5)

Repositorio del equipo para el proyecto acumulativo de las prácticas 2 a 5.
La guía completa de qué hace cada rol está en [`docs/Guia_Roles_P2.pdf`](docs/Guia_Roles_P2.pdf).

## Estructura

Equivale a la carpeta `Proyecto/` del enunciado: los comandos que dicen "desde `Proyecto/`" se ejecutan desde la raíz de este repo.

| Carpeta | Qué hay | ¿Quién la toca? |
|---|---|---|
| `datos/cyber/`, `datos/storage/` | Datos del profe (+ `PROVENANCE.md`). Los folds oficiales se añadirán aquí cuando lleguen. | **Nadie los modifica.** R4 añade los CSV de folds. |
| `esquemas/` | Formato de las entregas. | Nadie (solo lectura). |
| `herramientas/` | `validate_submission.py`. | Nadie (solo lectura). |
| `final_test/` | Vacía hasta la P5. | Nadie. |
| `plantillas/` | Plantillas originales del profe. | Nadie: se copian, no se editan. |
| `notebooks/borradores/` | Notebook personal de cada rol (`R1_datos.ipynb`, `R2_cyber.ipynb`…). | Cada uno **solo el suyo**. |
| `notebooks/` | Los 2 notebooks de entrega (`P2_cyber.ipynb`, `P2_storage.ipynb`). | R5. |
| `entregas_prueba/` | CSV del simulacro de entrega (P2.6). | R2 (cyber), R3 (storage). |
| `docs/` | Guías internas del equipo. | — |

## Regla nº 1: no se toca el trabajo de otros

Puedes abrir y **usar** lo que haya hecho otro, pero **no cambias nada** de sus archivos.
Si ves un fallo, avisa al dueño (grupo o issue en GitHub). Si necesitas su código, lo copias a tu notebook.

## Cómo trabajar

1. Primera vez:
   ```bash
   git clone https://github.com/lxmfran/Practice_II_ML.git
   cd Practice_II_ML
   pip install -r requirements.txt
   git checkout <tu-rama>
   ```
2. Cada vez que empieces: `git pull origin main` estando en tu rama, para traerte lo último.
3. Trabajas en **tu** notebook dentro de `notebooks/borradores/`.
4. Antes de hacer commit de un borrador: **Kernel → Restart & Clear Output**.
5. `git add` + `git commit` + `git push`, y abres un **pull request a `main`**. Otro miembro lo revisa y se mergea.

Nadie hace commit directamente en `main`.

## Ramas

| Rama | Rol en P2 |
|---|---|
| `r1-datos` | R1 — Datos y preprocesado |
| `r2-cyber` | R2 — Clasificación (reto A) |
| `r3-storage` | R3 — Regresión (reto B) |
| `r4-evaluacion` | R4 — Evaluación y validación |
| `r5-informe` | R5 — Informe y reproducibilidad |

## Recordatorios

- `PROJECT_RANDOM_STATE = 2627`, impreso en la primera celda de cada notebook.
- Todo lo entregable va **en inglés**.
- Nunca entrenar con `row_id`, `feature_group`, `config_group` ni `fold_id`.
- Los datos de cyber (TON_IoT) son solo para uso académico: **el repo debe ser privado**.
