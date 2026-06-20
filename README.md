# DS_Bootcamp

> Data Science and Python programming exercises, solutions, and study notes

A structured collection of hands-on exercises and solutions from a Data Science bootcamp, covering Python fundamentals through data analysis techniques. Each exercise includes the problem statement, sample data, and a working solution.

---

## Skills Demonstrated

`Python` `Data Analysis` `Pandas` `CSV` `Data Cleaning` `Automation` `Problem Solving` `Python OOP` `File I/O`

---

## Contents

```
DS_Bootcamp/
├── Notes_And_Solutions/
│   ├── notes/
│   │   ├── notes_FPB.txt         # Functional programming basics
│   │   ├── oop_theory.docx       # Object-oriented programming notes
│   │   ├── python_book.docx      # Core Python reference notes
│   │   └── python_guide.html     # Python quick-reference guide
│   └── solutions/
│       ├── ex00-0/               # Exercise: hello world / env setup
│       ├── ex00-1/               # Exercise: file reading and parsing
│       ├── ex00-2/               # Exercise: data types and operations
│       ├── ex00-3/               # Exercise: control flow
│       ├── ex00-4/               # Exercise: functions
│       ├── ex00-5/ ...           # Exercise: collections / iteration
│       └── ds.csv                # Sample dataset used across exercises
└── roadmap/                      # Study roadmap and topic checklist
```

Each `solutions/exNN-N/` folder contains:
- `problem.txt` — original exercise description
- `solution.py` — working Python solution
- `data.txt` or `.csv` — sample input data (where applicable)

---

## Topics Covered

| Area | Topics |
|---|---|
| Python Fundamentals | Variables, types, control flow, functions, comprehensions |
| OOP | Classes, inheritance, encapsulation, magic methods |
| File I/O | Reading/writing CSV, TXT; `pathlib` |
| Data Analysis | Parsing structured data, aggregation, filtering |
| Functional Python | `map`, `filter`, `reduce`, lambda, generators |
| Automation | Script-based batch processing |

---

## Sample Exercise Pattern

**Problem** (`problem.txt`):
```
Read ds.csv. Print the total count of rows, unique values in column 'category',
and the average value in column 'score'. Output as formatted table.
```

**Solution** (`solution.py`):
```python
import csv
from collections import Counter

with open("ds.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

categories = Counter(r["category"] for r in rows)
avg_score = sum(float(r["score"]) for r in rows) / len(rows)

print(f"Total rows       : {len(rows)}")
print(f"Unique categories: {len(categories)}")
print(f"Average score    : {avg_score:.2f}")
```

---

## How to Run Solutions

```bash
git clone https://github.com/makino-p/DS_Bootcamp.git
cd DS_Bootcamp
# No dependencies beyond Python stdlib for most exercises
python "Notes_And_Solutions/solutions/ex00-1/solution.py"
```

Some later exercises use `pandas` — install with:
```bash
pip install pandas
```

---

## Relation to Other Projects

Skills developed here feed directly into production projects:

| Bootcamp Topic | Applied In |
|---|---|
| CSV parsing, file I/O | [etl-pipeline](https://github.com/makino-p/etl-pipeline) |
| Data cleaning and transformation | [etl-pipeline](https://github.com/makino-p/etl-pipeline) |
| HTTP requests and JSON parsing | [quotes-scraper](https://github.com/makino-p/quotes-scraper) |
| API integration | [studybot](https://github.com/makino-p/studybot), [ielts-mentor](https://github.com/makino-p/ielts-mentor) |

---

## License

MIT
