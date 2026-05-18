# PySpark Problems

This folder contains practice problems and solutions using PySpark.

## Directory Structure

```
Problems/
├── reference/                        # Reference guides (read these first!)
│   ├── PROBLEM_PATTERN_GUIDE.md     # Complete pattern guide for creating new problems
│   └── COPILOT_PROMPT.txt           # One-liner prompt for the agent when adding problems
├── data/                            # CSV datasets for all problems
│   ├── famous.csv
│   └── sf_transactions.csv
├── spark_config.py                  # Global Spark configuration (import this!)
├── 001_famous_percentage.py         # Problem 1: Calculate user famous percentage
├── 002_month_over_month_revenue.py  # Problem 2: Month-over-month revenue change
└── README.md                        # This file
```

## How to Use

### Running a Problem

```bash
cd 03-pyspark/Problems/
python 001_famous_percentage.py
python 002_month_over_month_revenue.py
```

### Adding a New Problem

1. **Read the guide**: See `reference/PROBLEM_PATTERN_GUIDE.md` for complete patterns
2. **Use the prompt**: Copy the prompt from `reference/COPILOT_PROMPT.txt`
3. **Follow the pattern**:
   - Create CSV dataset in `data/` folder
   - Create python file `00N_<problem_title>.py` in this folder
   - Use imports from `spark_config`
   - Write inline REPL-style logic
   - No functions, no spark.stop()

## Quick Reference

### Import Pattern
```python
from pyspark.sql import functions as F
from pyspark.sql.window import Window  # if needed
from spark_config import spark
```

### Read Data
```python
df = spark.read.csv("data/<filename>.csv", header=True, inferSchema=True)
```

### Show Results
```python
print("Description:")
df.show(truncate=False)
```

## Global Spark Configuration

All problems use a shared Spark session from `spark_config.py`:
- ✅ Single initialization
- ✅ Consistent configuration
- ✅ Auto-shutdown on program exit
- ❌ Do NOT create your own SparkSession
- ❌ Do NOT call spark.stop()

## Problem Guidelines

- **Docstring only**: Use docstring at top for question + approach description
- **No functions**: Write inline REPL-style logic
- **Readable code**: Use descriptive variable names and clear transformations
- **DataFrame suffix**: Name DataFrames with `_df` suffix (e.g., `sales_df`)
- **Print output**: Use print() statements with descriptive labels
- **CSV datasets**: Keep datasets in `data/` folder for easy modification and retry

## File Naming

- `00N_<descriptive_title>.py` where N is the problem number
- Keep titles lowercase, replace spaces with underscores
- Examples: `001_famous_percentage.py`, `002_month_over_month_revenue.py`

