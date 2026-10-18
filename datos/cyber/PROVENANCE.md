# Challenge A — network intrusion classification: provenance and terms

## Source and attribution

| Field | Value |
|---|---|
| Dataset | **TON_IoT Network dataset** |
| Authority | **UNSW Canberra at ADFA**, Cyber Range and IoT Labs |
| Principal investigator | **Dr Nour Moustafa** |
| Project page | <https://research.unsw.edu.au/projects/toniot-datasets> |
| Terms | Free use for **academic research in perpetuity**; commercial use requires the authors' permission; **users must cite all eight papers referenced by the project page** |
| Subset used | `Train_Test_Network` (`train_test_network.csv`) |

**The course did not generate this data and does not claim to have generated it.** The
challenge is course-specific in its *construction* — feature selection, removal of leakage
shortcuts, deterministic sampling, group-aware splitting, target convention and hidden final
partition — and in nothing else.

## Citation obligation — the eight required references

The TON_IoT terms of use, as stated on the official project page
<https://research.unsw.edu.au/projects/toniot-datasets>, are:

> *"Free use of the TON_IoT datasets for academic research purposes is hereby granted in
> perpetuity. Use for commercial purposes is allowable after asking the author, Dr Nour
> Moustafa."*

and, on the same page:

> *"For the academic/public use of these datasets, the authors have to cities the following
> papers"*

**Source of the list below: the official UNSW TON_IoT project page named above.** The eight
references were transcribed from that page, not reconstructed from memory. Any work that uses
these data — including every Practice 2–5 deliverable that reports a result on Challenge A —
must cite all eight.

1. Moustafa, Nour. "A new distributed architecture for evaluating AI-based security systems
   at the edge: Network TON_IoT datasets." *Sustainable Cities and Society* (2021): 102994.
2. Booij, Tim M., Irina Chiscop, Erik Meeuwissen, Nour Moustafa, and Frank T. H. den Hartog.
   "ToN IoT — The role of heterogeneity and the need for standardization of features and
   attack types in IoT network intrusion datasets." *IEEE Internet of Things Journal* (2021).
3. Alsaedi, Abdullah, Nour Moustafa, Zahir Tari, Abdun Mahmood, and Adnan Anwar. "TON_IoT
   telemetry dataset: a new generation dataset of IoT and IIoT for data-driven Intrusion
   Detection Systems." *IEEE Access* 8 (2020): 165130–165150.
4. Moustafa, Nour, M. Keshk, E. Debie and H. Janicke. "Federated TON_IoT Windows Datasets for
   Evaluating AI-Based Security Applications." *2020 IEEE 19th International Conference on
   Trust, Security and Privacy in Computing and Communications (TrustCom)*, 2020,
   pp. 848–855, doi: 10.1109/TrustCom50675.2020.00114.
5. Moustafa, Nour, M. Ahmed and S. Ahmed. "Data Analytics-Enabled Intrusion Detection:
   Evaluations of ToN_IoT Linux Datasets." *2020 IEEE 19th International Conference on Trust,
   Security and Privacy in Computing and Communications (TrustCom)*, 2020, pp. 727–735,
   doi: 10.1109/TrustCom50675.2020.00100.
6. Moustafa, Nour. "New Generations of Internet of Things Datasets for Cybersecurity
   Applications based Machine Learning: TON_IoT Datasets." *Proceedings of the eResearch
   Australasia Conference, Brisbane, Australia*. 2019.
7. Moustafa, Nour. "A systemic IoT-Fog-Cloud architecture for big-data analytics and cyber
   security systems: a review of fog computing." *arXiv preprint* arXiv:1906.01055 (2019).
8. Ashraf, Javed, Marwa Keshk, Nour Moustafa, Mohamed Abdel-Basset, Hasnat Khurshid,
   Asim D. Bakhshi, and Reham R. Mostafa. "IoTBoT-IDS: A Novel Statistical Learning-enabled
   Botnet Detection Framework for Protecting Networks of Smart Cities." *Sustainable Cities
   and Society* (2021): 103041.

## How the course files were derived

The original was **supplied by the professor** as a mirror of the UNSW `Train_Test_Network`
subset. **Nothing was downloaded, nothing was reconstructed and no substitute dataset was
used.** The distribution used has no `ts` column.

| File | Bytes | SHA-256 |
|---|---:|---|
| `train_test_network.csv` (source, **not distributed**) | 29,902,775 | `26ddc513552de36de6428b2e578efaed2b57504c716dfba847cc0109a64e1974` |

Shape: 211,043 rows × 44 columns.

### The construction, as accepted under DEC-077 §A

1. **Eleven behavioural predictors only** are retained:
   `proto`, `service`, `conn_state`, `duration`, `src_bytes`, `dst_bytes`, `missed_bytes`,
   `src_pkts`, `src_ip_bytes`, `dst_pkts`, `dst_ip_bytes`.
2. **`label` is removed.** It is a deterministic function of the class and would hand the
   answer to any model that saw it.
3. **`src_ip`, `dst_ip`, `src_port` and `dst_port` are removed.** Acquisition identity is not
   behaviour: in this capture most address values map to exactly one class, so a model given
   them learns the testbed rather than the attack. Twenty-seven near-constant `ssl_*`,
   `http_*`, `weird_*` and DNS testbed artefacts are removed for the same reason — they carry
   the capture, not the traffic.
4. **De-duplication on the exact selected `(X, y)`** (DEC-077 §A, question C-1).
5. **A cap of 6,000 rows per class** where the class has that many, applied with the course
   seed **2627**. No synthesis, no oversampling, no class dropped.
6. **All ten classes are retained**, including the deliberately rare `ransomware`
   (DEC-077 §A, question C-2). Its small support is a property of the problem.
7. **The development/hidden split is exact-feature-group aware and class-stratified**, so that
   no exact feature vector appears on both sides. Measured exact `X` overlap between the two
   partitions: **0**.
8. **One target only: the integer `attack_code`.** The semantic names live in
   `cyber_class_codes.json`, never beside the code in the modelling table.
9. **Grouping metadata is shipped separately**, in `cyber_groups.csv`, and is **never an
   estimator input**.

### Derived course files

| File | Columns | Bytes | SHA-256 |
|---|---|---:|---|
| `cyber_development.csv` | `row_id`, 11 predictors, `attack_code` | 1,709,660 | `248353ae798d91a9670cf53d403dc4aaa7cd22c92811fcdd88edc062744b54a5` |
| `cyber_groups.csv` | `row_id`, `feature_group` | 445,175 | `31fb2ee76859c16e55bb54ca92bd7f46d7fd3ce607522f3c08a490db6366f05b` |
| `cyber_class_codes.json` | code → semantic name | 175 | `43742cdaabee865fbdefbfe535f91bf46488b4863d68b9af1ba149b0fbcf36ef` |
| `cyber_submission_template.csv` | `row_id`, `attack_code` — **the header line and nothing else** | 19 | `6e5837416d6d61107f0bf0c5608e43af975593f735f67f66c4cb7bfbd1fe9e76` |

Development partition: **34,928 rows**, 34,883 distinct feature groups.

### Class support in the development partition

| `attack_code` | class | support |
|---:|---|---:|
| 0 | `backdoor` | 1,573 |
| 1 | `ddos` | 4,800 |
| 2 | `dos` | 4,800 |
| 3 | `injection` | 4,800 |
| 4 | `mitm` | 805 |
| 5 | `normal` | 4,800 |
| 6 | `password` | 4,800 |
| 7 | **`ransomware`** | **208** |
| 8 | `scanning` | 3,542 |
| 9 | `xss` | 4,800 |

`ransomware` is the rare class the project is honest about. **Every per-class figure you
report for it must be reported beside its support.**

## What is not here

A hidden final test partition exists and its targets are **never** distributed. The final-test
*features* are released only after your model lock is frozen (Practice 5), at the one
canonical location `Proyecto/final_test/` and nowhere else. Nothing in this
directory reveals either.

**No benchmark or feasibility score is published here.** Scores obtained during the course's
own design study are not targets for you, are not expected values, and are deliberately absent
from all student material.

## Not a security claim

This is a **teaching benchmark** built from a research testbed capture. Nothing computed in
Practices 2–5 is a claim about real-world intrusion detection, and no model built here should
be deployed against live traffic.
