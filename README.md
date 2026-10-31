# Lab 6 - Museum Admission

**Manaswi Guntupalli | Assignment 54**

In this lab, I tested the museum admission program using pytest and coverage.
I checked the starting results, added more tests, and measured line and branch
coverage. The final result is **100% line coverage and 100% branch coverage**.
The application code has not been changed.

## Reports and screenshots

| Part | Report | Test file | Actual terminal screenshot |
|---|---|---|---|
| Code coverage | [Code report](LAB6/CODE_COVERAGE_REPORT.md) | [16 cases](LAB6/CodeCoverageTest_54_museum_admission.py) | [100% code coverage](LAB6/results/code_coverage_terminal.png) |
| Branch coverage | [Branch report](LAB6/BRANCH_COVERAGE_REPORT.md) | [64 cases](LAB6/BranchCoverageTest_54_museum_admission.py) | [100% branch coverage](LAB6/results/branch_coverage_terminal.png) |

The reports explain the starting coverage, missing cases, tests added, commands,
final results, and what the results mean. The two screenshots above are from
my VS Code terminal. Earlier HTML reports and browser images are kept as
supporting stage records. The actual terminal screenshots are the final evidence.
Only results above 90% have screenshots, as asked in the handout.

## Coverage progress and commits

The completed local solution was arranged into smaller, additive test stages.
Each stage was run again, committed, and pushed separately. These percentages
are measured results; the application was not changed to increase them.

| Stage | Line coverage | Branch-only coverage | Combined coverage | Commit |
|---|---:|---:|---:|---|
| Original two tests | 47.22% | 35.71% | 42.19% | Starting reports in `LAB6/results/initial_*` |
| 1 | 72.22% | 67.86% | 70.31% | [4f15f82](https://github.com/Manaswi-Guntupalli/museum_admission_lsb6_PES1UG24CS548/commit/4f15f82) |
| 2 | 83.33% | 82.14% | 82.81% | [6569cfc](https://github.com/Manaswi-Guntupalli/museum_admission_lsb6_PES1UG24CS548/commit/6569cfc) |
| 3 | 88.89% | 85.71% | 87.50% | [5c7ecb1](https://github.com/Manaswi-Guntupalli/museum_admission_lsb6_PES1UG24CS548/commit/5c7ecb1) |
| 4 | 94.44% | 92.86% | 93.75% | [56438f2](https://github.com/Manaswi-Guntupalli/museum_admission_lsb6_PES1UG24CS548/commit/56438f2) |
| 5 | 100% | 100% | 100% | [49bc6cd](https://github.com/Manaswi-Guntupalli/museum_admission_lsb6_PES1UG24CS548/commit/49bc6cd) |

In branch mode, coverage.py's `Cover` column combines statements and branch
destinations. It is different from the branch-only percentage. The reports
explain the calculation using the saved counts.

The history includes separate commits for the code coverage tests and the
branch coverage tests, followed by the reports and actual terminal screenshots.
The full history is [available here](https://github.com/Manaswi-Guntupalli/museum_admission_lsb6_PES1UG24CS548/commits/main).

## Run the lab

I used Python 3.14.0, pytest 9.2.0, coverage 7.17.0, and VS Code.
From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r LAB6/requirements.txt
cd LAB6
```

Run code coverage:

```powershell
..\.venv\Scripts\python -m coverage run --data-file=.coverage_terminal_code --source=museum_admission -m pytest -p no:cacheprovider CodeCoverageTest_54_museum_admission.py -q
..\.venv\Scripts\python -m coverage report --data-file=.coverage_terminal_code -m
```

Expected result: **16 passed**, 36 statements, 0 missing, **100%**.

Run branch coverage:

```powershell
..\.venv\Scripts\python -m coverage run --branch --data-file=.coverage_terminal_branch --source=museum_admission -m pytest -p no:cacheprovider BranchCoverageTest_54_museum_admission.py -q
..\.venv\Scripts\python -m coverage report --data-file=.coverage_terminal_branch -m
```

Expected result: **64 passed**, 36 statements, 28 branches, 0 partial branches,
**100%**.

Run all tests:

```powershell
..\.venv\Scripts\python -m pytest -p no:cacheprovider -q
```

Expected result: **95 passed**. This includes 15 tests in the growing original
test file, 16 code coverage cases, and 64 branch coverage cases. Some cases
overlap because the two submission files also need to run independently.

The commands use separate data files so line and branch runs do not get mixed.
The cache option avoids a temporary pytest cache warning on this computer.
The tests and coverage checks still run normally. Environment activation is
not required. In VS Code, select `.venv/Scripts/python.exe` as the interpreter.

## Submission checklist

| Handout requirement | Where it is included |
|---|---|
| Initial code and branch measurements | `LAB6/results/initial_line.*` and `initial_branch.*` |
| Code coverage analysis and report - 2 marks | `LAB6/CODE_COVERAGE_REPORT.md` and actual code screenshot |
| Branch coverage analysis and report - 2 marks | `LAB6/BRANCH_COVERAGE_REPORT.md` and actual branch screenshot |
| Test cases above 90% and commits - 6 marks | Both separate test files reach 100%; staged commits are linked above |
| Required code test filename | `LAB6/CodeCoverageTest_54_museum_admission.py` |
| Required branch test filename | `LAB6/BranchCoverageTest_54_museum_admission.py` |
| Screenshots only after reaching 90% | Final actual screenshots show 100%; stage 4 images also exceed 90% |
| At least two commits | Separate code and branch test commits, plus the other measured stages |

The handout uses `xxxx` as a placeholder in its filenames. I used `54`, the
assignment number in the assigned repository name. All Lab 6 work is in `LAB6`.
This is the separate repository for the requested staged history; the original
assigned repository has been left intact. Lab 7 is not part of this handout.
