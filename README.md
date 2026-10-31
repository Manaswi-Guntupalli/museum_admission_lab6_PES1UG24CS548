# Museum Admission - Lab 6 coverage progression

This repository organizes the completed local assignment into additive testing
milestones. Every stage was measured afresh and published as a separate commit;
commit dates are actual dates. The application code is unchanged.

## Measured progress

| Stage | Line coverage | Branch-only coverage | Combined coverage.py result |
|---|---|---|---|
| Starter | 17/36 (47.22%) | 10/28 (35.71%) | 42.19% |
| 1 | 26/36 (72.22%) | 19/28 (67.86%) | 70.31% |
| 2 | 30/36 (83.33%) | 23/28 (82.14%) | 82.81% |
| 3 | 32/36 (88.89%) | 24/28 (85.71%) | 87.50% |
| 4 | 34/36 (94.44%) | 26/28 (92.86%) | 93.75% |

Current stage: **4**, measured combined coverage **93.75%**.
The requested approximate milestones were 70%, 82%, 89%, 95%, and 100%.
Percentages are determined by real executions, with no exclusions or altered
application code. A statement contributes 1/36 to line coverage; a statement
or branch destination contributes 1/64 to the combined percentage.

## Setup and reproduce

Python 3.14, VS Code, pytest 9.2.0, and coverage 7.17.0 were verified locally.
From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r LAB6/requirements.txt
cd LAB6
..\.venv\Scripts\python -m coverage run --branch --source=museum_admission -m pytest test_museum_admission.py -q
..\.venv\Scripts\python -m coverage report -m
..\.venv\Scripts\python -m pytest -q
```

Use `.venv/Scripts/python.exe` as the VS Code interpreter. Environment activation
and PowerShell execution-policy changes are unnecessary. `pytest.ini` discovers
both the normal test filename and the handout's capitalized filenames.

## Evidence and analysis

`LAB6/results/stage_*.txt` records real commands and unedited output, and JSON
reports preserve executed/missing statements and branches for each milestone.
Reports measure only `museum_admission.py`; test code cannot inflate the result.
Baseline reports preserve the original two-test measurements. Images are added
only at stages achieving at least 90%, as required by the handout.

The PNG images are browser screenshots of saved terminal output displayed
verbatim in the accompanying HTML reports. They are not native terminal-window
captures. If the evaluator requires native terminal captures, run the saved
commands and take screenshots of the terminal before submission.

Line coverage measures executed statements; branch coverage measures decision
destinations. Coverage.py's branch-mode `Cover` column combines statements and
branch destinations. Function coverage measures functions invoked. Path coverage
measures complete combinations of decisions; 100% branch coverage does not prove
exhaustive path coverage or correctness for every possible input.

Tests grow additively across commits: tour pricing and free entry, input errors,
school/ordinary discount boundaries, and gallery wait/queue/enter decisions.
The final suite also checks all four visitor categories, ages 0/4/5, both weekend
days, adjustment order, sizes -1/0/1/7/8/9/14/15/16/19/20/21, timed slots,
90%-capacity boundaries, full-gallery priority and non-round capacities.

The final handout deliverables are the separate
`CodeCoverageTest_54_museum_admission.py` and
`BranchCoverageTest_54_museum_admission.py`, plus final result images. Assignment
identifier 54 comes from the original assigned repository. Lab 7 is outside this
handout's scope. The original assignment repository has not been rewritten.
