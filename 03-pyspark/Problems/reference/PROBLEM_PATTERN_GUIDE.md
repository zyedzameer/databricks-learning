"""
REFERENCE DOCUMENT: PySpark Problem Module Pattern Guide

This document defines the standardized pattern for creating new PySpark problem
modules in 03-pyspark/Problems/. Use this when adding new problems.

================================================================================
PATTERN RECOGNITION CHECKLIST
================================================================================

When user says "create a problem module" or "add problem XXX", look for:
1. Problem question/description
2. Dataset information (schema + sample data)
3. Solution approach (SQL -> PySpark translation)

================================================================================
MODULE STRUCTURE
================================================================================

Filename Convention:
  - Format: 00X_<problem_title>.py
  - Example: 001_famous_percentage.py, 002_month_over_month_revenue.py
  - X = sequential problem number

File Location:
  - All modules go in: 03-pyspark/Problems/

=================================================================================
CONTENT PATTERN
================================================================================

[1] DOCSTRING (Top of file only)
    - Problem question/description
    - Dataset location reference
    - Approach/explanation (translate from SQL to PySpark if applicable)
    - NO function definitions

Example:
    ""\"
    Question: <problem description>
    
    Dataset: <filename>.csv located in data/ folder with columns (<col_list>)
    
    Approach:
    1. <step 1>
    2. <step 2>
    ...
    \"\"

[2] IMPORTS
    from pyspark.sql import functions as F
    from pyspark.sql.window import Window  # if needed
    from spark_config import spark         # ALWAYS import from spark_config
    
[3] LOGIC (REPL-style, inline, NO functions)
    - Read CSV: spark.read.csv("data/<file>.csv", header=True, inferSchema=True)
    - Transform data using DataFrame API
    - Print results using .show()
    - Direct execution, no wrapping in functions
    
Example:
    df = spark.read.csv("data/mydata.csv", header=True, inferSchema=True)
    
    result = (
        df
        .withColumn("new_col", F.col("existing_col") * 2)
        .groupBy("some_col")
        .agg(F.sum("values").alias("total"))
    )
    
    print("Results:")
    result.show(truncate=False)

[4] NO spark.stop()
    - Global spark instance managed by spark_config.py
    - Do NOT call spark.stop() in problem modules

=================================================================================
DATASET PATTERN
=================================================================================

Location: 03-pyspark/Problems/data/

Naming: <problem_name>.csv

Format: Plain CSV with header row

Creation process:
1. Extract schema and data from problem statement
2. Create CSV file with headers in first row
3. Add sample data rows
4. Place in data/ folder

Example (famous.csv):
    user_id,follower_id
    1,2
    1,3
    2,4
    ...

=================================================================================
WHEN ADDING A NEW PROBLEM - STEP BY STEP
=================================================================================

1. user says: "create problem NNN: <description> with dataset: <data>"

2. EXTRACT:
   - Problem title (for 00N_title.py filename)
   - Question/description (for docstring)
   - Dataset schema (column names and types)
   - Sample data (all values)
   - SQL/Scala reference code if provided
   - Approach explanation

3. CREATE DATASET:
   - File: data/<problem_name>.csv
   - Header row + data rows
   - Use PowerShell or create_file tool

4. CREATE PROBLEM MODULE:
   - File: 00N_<problem_title>.py
   - Add docstring (question + approach)
   - Add imports (F, spark from spark_config, Window if needed)
   - Add inline logic (REPL-style)
   - Add print() statements for output
   - NO functions, NO spark.stop()

5. VALIDATION:
   - Check for syntax errors using get_errors
   - Verify dataset file has content
   - Provide instructions on how to run

=================================================================================
CODE STYLE GUIDELINES
================================================================================

Variable Naming:
  - Use descriptive names: monthly_revenue, follower_count_df
  - df suffix for DataFrames: sales_df, transactions_df
  - snake_case for variables and functions

Dataframe Operations:
  - Chain operations clearly with indentation
  - One transformation per line when possible
  - Use aliases for clarity: .agg(F.sum("value").alias("total_revenue"))

Comments:
  - Only docstring at top with question/approach
  - Minimal inline comments (code should be readable)
  - No block comments in solution logic

Print Statements:
  - Print descriptive labels before .show()
  - Example: print("Results (sorted by date):"), result.show(truncate=False)
  - Use truncate=False for full visibility

=================================================================================
EXAMPLES OF CORRECT PATTERN
=================================================================================

CORRECT:
    from pyspark.sql import functions as F
    from spark_config import spark
    
    df = spark.read.csv("data/myfile.csv", header=True, inferSchema=True)
    result = df.groupBy("col").agg(F.sum("value"))
    print("Results:"); result.show()

WRONG:
    spark = SparkSession.builder...  # Don't create spark here!
    
    def solve_problem():  # Don't use functions!
        ...
    
    spark.stop()  # Don't stop spark!

=================================================================================
RECOGNITION KEYWORDS
================================================================================

When user provides:
- "Question: ..." → Extract for docstring
- "dataset:", "schema", "CREATE TABLE" → Extract for CSV
- "Scala response:", "SQL query" → Translate to PySpark
- "find", "calculate", "compute" → Main logic operation
- "rounded to X decimals" → Use F.round(..., X)
- "sorted", "order" → Use .orderBy(...)
- "%", "percentage", "ratio" → Mathematical transformation

=================================================================================
COMMON TRANSFORMATIONS REFERENCE
=================================================================================

Month-over-month calculation:
    w = Window.orderBy("year_month")
    df.withColumn("prev_value", F.lag("value").over(w))

Percentage change:
    F.round((F.col("current") - F.col("previous")) / F.col("previous") * 100, 2)

Date extraction:
    F.date_format(F.col("timestamp_col"), "yyyy-MM")

Aggregation:
    df.groupBy("col").agg(F.sum(...).alias("total"), F.count(...).alias("count"))

Union (combine like columns):
    df1.select(F.col("col1").alias("new_name")).union(df2.select(...))

Distinct count:
    df.select(...).distinct().count()

=================================================================================
"""

