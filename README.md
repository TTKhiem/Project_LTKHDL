# PhishGuardVN — Programming for Data Science Final Project

PhishGuardVN explores a Vietnamese URL phishing dataset. Notebooks 01 and 02 cover source and data-quality review, exploratory analysis, and research questions Q1–Q5. Notebook 03 contains the separate Q6 machine-learning work.

## Repository structure

```text
README.md
environment.yml
LLM_USAGE.md
data/
  raw/                  # local source CSVs; ignored by Git
  processed/            # optional group-created intermediate data
notebooks/
  01_collection_exploration.ipynb
  02_analysis_q1_q2.ipynb
  02_analysis_q3_q4.ipynb
  02_analysis_q5.ipynb
  03_ml_question.ipynb  # Q6; separate from the Q1–Q5 EDA work
src/
  data_io.py
  url_utils.py
```

## Members and ownership

| Member | Student ID | Primary ownership |
|---|---:|---|
| Tiết Trọng Khiêm | 24127058 | Data source/Data Card; Q1–Q2 |
| Lê Kiến Quốc | 24127115 | Data quality/preprocessing; Q3–Q4 |
| Trịnh Tấn Phát | 24127485 | Auxiliary-data audit; Q5 and Q6 (ML) |

Each member owns two questions across the project. Ownership does not remove the expectation that every member can explain the repository and analysis.

## Datasets

The source is [PhishVN, Mendeley Data, version 4](https://data.mendeley.com/datasets/b97hxbxtpd/4), DOI `10.17632/b97hxbxtpd.4`, contributed by Thai Nguyen Vu (University of Transport and Communications — Ho Chi Minh City Campus). The release is licensed under CC BY 4.0; cite and attribute the dataset and its upstream sources when reusing it. The version 4 record describes a documentation-only update, with data files unchanged from version 3.

| Role | Local file | Observation grain |
|---|---|---|
| Main | `data/raw/vn_compphish.csv` | One URL per row; phishing/benign label and collection metadata |
| Auxiliary | `data/raw/abuse_type.csv` | One URL per row; rule-derived abuse type and rule text |

Download the open archive `PhishVN_v3.1.0_open.zip` from the Mendeley record and place only `vn_compphish.csv` and `abuse_type.csv` in `data/raw/`. The notebooks read raw files without modifying them. Keep the archive local; archive patterns and raw CSVs are ignored by Git. Do not use the separate results bundle for these EDA notebooks. The auxiliary value `unknown` is intentional and must remain a category, not be treated as a missing label.

The observed main CSV has 28 columns, while the source description summarizes 21 lexical features plus labels/split information. The notebook reports the actual header and does not force the file to match the shorter description. `is_https` is documented as a collection artifact; Q2 treats it as an observed association and does not make a causal claim.

### Existing public work

The companion article is Vu (2026), [*PhishVN: A time-stamped Vietnamese URL phishing dataset with impersonation-scenario labels and confidence tiers*](https://doi.org/10.1016/j.dib.2026.113195). The dataset author also maintains a [public PhishVN repository](https://github.com/vuthainguyen1602/phishvn) with dataset documentation, processing code, baselines, subsequent audits/benchmarks, and a [notebooks directory](https://github.com/vuthainguyen1602/phishvn/tree/master/notebooks). Q1–Q5 in this project focus on course-specific EDA questions about URL complexity, HTTPS/TLD/length associations, repeated-host patterns, and the auxiliary abuse-type table; they do not reproduce the repository's model benchmark workflow. This is an initial related-work review, not an exhaustive search. Before submission, the group should search for additional public analyses and state how Q6 differs from existing baselines.

## Environment and run order

From the repository root, create and activate the declared Python 3.11 environment:

```bash
conda env create -f environment.yml
conda activate phishguard-vn
python -m jupyter lab
```

Run notebooks in this order so that source checks and preprocessing assumptions are reviewed before analysis:

1. `notebooks/01_collection_exploration.ipynb`
2. `notebooks/02_analysis_q1_q2.ipynb`
3. `notebooks/02_analysis_q3_q4.ipynb`
4. `notebooks/02_analysis_q5.ipynb`
5. `notebooks/03_ml_question.ipynb` for Q6, after the group reviews its ML design.

The notebooks locate the repository root using `environment.yml` and load CSVs from `data/raw/`. `src/data_io.py` and `src/url_utils.py` contain small shared helpers used by multiple notebooks; analysis choices, tables, plots, and interpretations remain visible in the notebooks.

## EDA snapshot and remaining group work

The main file contains 53,116 URL rows: 36,706 phishing and 16,410 benign. The auxiliary file contains 36,706 URL rows and six observed `abuse_type` values, including the intentional `unknown` category. The EDA notebooks show counts before and after joins, compare URL-key and hostname grains, and report uncertainty/robustness where required. Inspect their executed tables and figures for the detailed Q1–Q5 evidence.

### Group findings — complete before submission

1. `[Finding supported by notebook evidence; explain its practical meaning.]`
2. `[Finding supported by notebook evidence; explain its practical meaning.]`
3. `[Finding supported by notebook evidence; explain its practical meaning.]`
4. `[Most surprising finding or an apparent conflict between analyses.]`
5. `[Shared limitation and a concrete next step.]`

Each question notebook retains a group-authored section for method choices, interpretation, limitations, and final answers. The group must complete those sections, confirm dataset approval and related-work status, and record actual LLM assistance in `LLM_USAGE.md` before submission. The computed outputs are evidence for students to review and explain, not a substitute for their own conclusions or reflections.

## Research questions

| ID | Question | Owner |
|---|---|---|
| Q1 | Does URL-structure complexity differ between phishing and benign URLs within comparable URL-length groups? | Tiết Trọng Khiêm |
| Q2 | How is HTTPS associated with phishing labels after accounting for TLD and URL length? | Tiết Trọng Khiêm |
| Q3 | Does the TLD/label relationship change when rare TLDs are pooled and URL length is considered? | Lê Kiến Quốc |
| Q4 | Do repeated hostnames have a different phishing share from singleton hostnames, and how does this vary by TLD? | Lê Kiến Quốc |
| Q5 | How consistent is the auxiliary abuse metadata with main labels under URL and hostname matching rules? | Trịnh Tấn Phát |
| Q6 | Can a URL be classified as phishing or benign at prediction time using available features? | Trịnh Tấn Phát |

Q6 remains in notebook 03 and is outside the scope of the Q1–Q5 EDA change.

## Team workflow

- Keep source CSVs unchanged and out of version control.
- Review `git diff` and rerun the notebooks affected by each change.
- Each member records their own contributions and verifies that they can explain the code and findings.
- Do not commit credentials, tokens, personal data, or large source archives.
